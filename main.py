from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os
from dotenv import load_dotenv

load_dotenv()

llm = ChatAnthropic(model="claude-3-5-sonnet-20241022", temperature=0.3)

prompt = ChatPromptTemplate.from_messages([
    ("system", open("prompts/system_prompt.md").read()),
    ("human", "{input}")
])

chain = prompt | llm | StrOutputParser()

def handle_customer_query(query: str) -> str:
    return chain.invoke({"input": query})

if __name__ == "__main__":
    print("Customer Support AI Agent is ready!")
    user_input = input("Enter customer message: ")
    response = handle_customer_query(user_input)
    print("\nAI Response:\n", response)
