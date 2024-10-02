from avmllib.ocr_tools.s3_getter import OcrGetter
import requests

class OcrEmbedder:
    ocr_getter: OcrGetter

    def __init__(self):
        self.ocr_getter = OcrGetter()

    def _get_ocr(self, urn_id):
        res = self.ocr_getter.get_urn_id(urn_id)
        s = ""
        current_line = None
        for token in res["strings"]:
            if token["line"] != current_line:
                s += "\n"
                current_line = token["line"]
            s += token["text"] + " "
        return s

    def get_embedding(self, urn_id):
        text = self._get_ocr(urn_id)
        j = dict(
            input=text
        )
        response = requests.post("http://localhost:1234/v1/embeddings", json=j)
        return response.json()["choices"][0]["message"]["content"]

embedder = OcrEmbedder()
emb = embedder.get_embedding("db60133600000001")
pass