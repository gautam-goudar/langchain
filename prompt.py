from dotenv import load_dotenv
from langchain.llms import OpenAI
from langchain import PromptTemplate, LLMChain


# Load the .env file
load_dotenv()

# Create the prompt object
template = """Question: {question}

Answer: """
prompt = PromptTemplate(
    template=template,
    input_variables=["question"]
)

question = "Which NFL team has won the most Super Bowls?"

# Create the OpenAI object with text-davinci-003 model
openai = OpenAI(model="text-davinci-003")

llm_chain = LLMChain(
  prompt=prompt,
  llm=openai
)

print(llm_chain.run(question))