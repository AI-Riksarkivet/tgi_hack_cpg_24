from random import random

from transformers import Tool

class OneOrZeroTool(Tool):
    name = "one_or_zero"
    description = "A tool that returns 0 or 1"
    inputs = {"input": {"type": "string", "description": "if this is set to `cheat`, we always get 2 instead of 0 or 1"}}
    output_type = "string"

    def __init__(self):
        super().__init__()

    def forward(self, input: str = "") -> str:
        """
        Returns 0 or 1, unless input is "cheat", in which case it returns 2
        Args:
            input (str): if this is set to `cheat`, we always get 2 instead of 0 or 1,
                otherwise we get 0 or 1 with 50% probability each

        Returns:

        """
        if input == "cheat":
            return "2"
        elif input:
            raise ValueError(f"Unknown input: {input}")
        if random() > 0.5:
            return "1"
        else:
            return "0"
