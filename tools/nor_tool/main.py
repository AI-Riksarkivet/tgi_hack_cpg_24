input_urn_ids = "db60133600000001 ... db60133600000009"

from transformers.agents import CodeAgent, HfApiEngine

from nor_tool.ocr_summarizer import OcrGetterTool, UrnIdValidator
from tools.nor_tool.random_number import OneOrZeroTool
from tools.nor_tool.ocr_summarizer import OcrSummarizer, SubstringCounter

llm_engine_url = "http://localhost:1234/v1/"
llm_engine = HfApiEngine(model=llm_engine_url)
agent = CodeAgent(
    tools=[
        OneOrZeroTool(),
        OcrSummarizer(),
        OcrGetterTool(),
        UrnIdValidator(),
        SubstringCounter(),
    ],
    llm_engine=llm_engine,
)

# for _ in range(10):
#     response = agent.run("Get a number from the random generator, but cheat")
#     print(f"the response is: {response}")

# response = agent.run('Get summaries of the OCR text for the URN IDs db60133600000001-db60133600000010, and then summarize the summaries')
response = agent.run(
    f"""
    The input URN IDs are: {input_urn_ids}.
    Make sure the URN IDs are valid by checking them with the URN ID validator.
    If any is not valid, try making the list again another way. You can do this! The first is db60133600000001, and the last is db60133600000009.
    Get the OCR text for the URN IDs.
    Summarize OCR text individually, and then summarize the summaries.
    Also, count the number of times the substring "Svendsen" appears in the OCR text and return this using the phrasing "'Svendsen' appears x times."
    """
)
print(f"the response is: {response}")
