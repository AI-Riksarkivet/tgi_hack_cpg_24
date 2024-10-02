import re

from avmllib.ocr_tools.s3_getter import OcrGetter
import requests

from transformers import Tool


class OcrGetterTool(Tool):
    name = "OcrGetterTool"
    description = (
        "A tool that gets the OCR text of a document. The OCR result may be"
        "very bad, since not all documents are easily readable by the OCR engine."
        "If this is the case, the OCR text may be gibberish, and in this case it is likely"
        "to be handwritten so that the OCR model cannot handle it."
    )
    inputs = {
        "urn_id": {
            "type": "string",
            "description": "The URN ID of the document to get the OCR text for. The"
            "URN ID is formatted as \w{2}\d{14}. Any other format will not work.",
        }
    }
    output_type = "string"

    def __init__(self):
        self.ocr_getter = OcrGetter()
        super().__init__()

    def forward(self, urn_id: str = "") -> str:
        """
        Returns the OCR text of the document
        Args:
            urn_id (str): URN ID of the document to get the OCR text for

        Returns str: The OCR text of the document

        """
        if not bool(re.match(r"\w{2}\d{14}", urn_id)):
            # print('this thing is soooooo dumb I have to add a zero for it to work')
            # add a zero in the middle, ie turn db6013360000001 into db60133600000001
            urn_id = urn_id[:10] + "0" + urn_id[10:]
        res = self.ocr_getter.get_urn_id(urn_id)
        s = ""
        current_line = None
        for token in res["strings"]:
            if token["line"] != current_line:
                s += "\n"
                current_line = token["line"]
            else:
                s += token["text"] + " "

        return s


class OcrSummarizer(Tool):
    name = "OcrSummarizer"
    description = "A tool that summarizes the text of an OCR result"
    inputs = {
        "text": {"type": "string", "description": "The text document to summarize"}
    }
    output_type = "string"

    def __init__(self):
        super().__init__()

    def forward(self, text: str = "") -> str:
        """
        Returns a summary of the OCR text
        Args:
            text (str): text of the document to summarize

        Returns str: A summary of the OCR text

        """
        # text = self._get_ocr_text(urn_id)
        j = dict(
            messages=[
                {
                    "role": "system",
                    "content": "Summarize the content of the text of this document.",
                },
                {"role": "user", "content": text},
            ]
        )
        response = requests.post("http://localhost:1234/v1/chat/completions", json=j)
        return response.json()["choices"][0]["message"]["content"]


class UrnIdValidator(Tool):
    name = "UrnIdValidator"
    description = (
        "A tool that validates the URN ID of a document. A valid URN ID is formatted as \w{2}\d{14}, that is, 2 letters and 14 digits.  Any other format will not work."
    )
    inputs = {
        "urn_id": {
            "type": "string",
            "description": "The URN ID of the document to validate.",
        }
    }
    output_type = "string"

    def __init__(self):
        super().__init__()

    def forward(self, urn_id: str = "") -> str:
        """
        Returns whether the URN ID is valid
        Args:
            urn_id (str): URN ID of the document to validate

        Returns str: Whether the URN ID is valid

        """
        if bool(re.match(r"\w{2}\d{14}", urn_id)):
            return "Valid"
        else:
            return "Invalid"

class SubstringCounter(Tool):
    name = "SubstringCounter"
    description = (
        "A tool that counts the number of times a substring appears in a string."
    )
    inputs = {
        "text": {
            "type": "string",
            "description": "The text to search for the substring in.",
        },
        "substring": {
            "type": "string",
            "description": "The substring to count the number of occurrences of.",
        },
    }
    output_type = "number"

    def __init__(self):
        super().__init__()

    def forward(self, text: str = "", substring: str = "") -> int:
        """
        Returns the number of times the substring appears in the text
        Args:
            text (str): The text to search for the substring in
            substring (str): The substring to count the number of occurrences of

        Returns int: The number of times the substring appears in the text

        """
        return text.count(substring)
