from dotenv import load_dotenv
from langchain.llms import OpenAI
from langchain import PromptTemplate, LLMChain


# Load the .env file
load_dotenv()

# Create the prompt object
multi_template = """Answer the following questions one at a time.

Questions:
{questions}

Answers:
"""
long_prompt = PromptTemplate(
    template=multi_template,
    input_variables=["questions"]
)

questions = (
    "Which NFL team won the Super Bowl in the 2010 season?\n" +
    "If I am 6 ft 4 inches, how tall am I in centimeters?\n" +
    "Who was the 12th person on the moon?" +
    "How many eyes does a blade of grass have?"
)

# Create the OpenAI object with text-davinci-003 model
openai = OpenAI(model="text-davinci-003")

llm_chain = LLMChain(
  prompt=long_prompt,
  llm=openai
)

print(llm_chain.run(questions))