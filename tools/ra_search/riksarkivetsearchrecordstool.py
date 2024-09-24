import requests
from transformers import Tool

class RiksarkivetSearchRecordsTool(Tool):
    name = "search_records"
    description = """
    Searches the Riksarkivet records using the provided parameters.

    Args:
        text (str): General free text search.
        name (str): Free text search on name.
        place (str): Free text search on referenced place name.
        year_min (int): Earliest year.
        year_max (int): Latest year.
        offset (int): Start position in the total search result.
        max_results (int): Max number of hits in the result list.

    Returns:
        str: A summary of the search results. in the format: caption , date , referenceCode
    """

    inputs = {
        "text": {
            "type": "string",
            "description": "General free text search.",
            "default": ""
        },
        "name": {
            "type": "string",
            "description": "Free text search on name.",
            "default": ""
        },
        "place": {
            "type": "string",
            "description": "Free text search on referenced place name.",
            "default": ""
        },
        "year_min": {
            "type": "int",
            "description": "Earliest year.",
            "default": None
        },
        "year_max": {
            "type": "int",
            "description": "Latest year.",
            "default": None
        },
        "offset": {
            "type": "int",
            "description": "Start position in the total search result.",
            "default": 0
        },
        "max_results": {
            "type": "int",
            "description": "Max number of hits in the result list.",
            "default": 100
        },
    }
    output_type = "string"

    def forward(self, text="", name="", place="", year_min=None, year_max=None, offset=0, max_results=100):
        base_url = "https://data.riksarkivet.se/api/records"
        params = {
            "text": text,
            "name": name,
            "place": place,
            "offset": offset,
            "max": max_results,
        }
        if year_min is not None:
            params["year_min"] = year_min
        if year_max is not None:
            params["year_max"] = year_max

        # Remove empty parameters
        params = {k: v for k, v in params.items() if v}

        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()

        # Process the data to create a summary
        total_hits = data.get("totalHits", 0)
        hits = data.get("hits", 0)
        offset = data.get("offset", 0)
        items = data.get("items", [])

        # Create a simple summary
        summaries = []
        for item in items[:10]:  # Limit to first 10 items for brevity
            caption = item.get("caption", "No Title")
            date = item.get("metadata", {}).get("date", "No Date")
            reference_code = item.get("metadata", {}).get("referenceCode", "No Reference Code")
            summaries.append(f"- {caption} ({date}, Ref: {reference_code})")

        result_summary = f"Total Hits: {total_hits}\nShowing {hits} results starting from offset {offset}:\n"
        result_summary += "\n".join(summaries)

        return result_summary