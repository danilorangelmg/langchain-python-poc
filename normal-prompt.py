import os
from langchain.chat_models.openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.tools import

# Configurar a chave da API da OpenAI (substitua pelo seu valor)
os.environ["OPENAI_API_KEY"] = "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"


class OpenAIBuilder:
    def __init__(self, prompt, inputVariable):
        self.marca =

template = PromptTemplate(
    template="What is the sum of {number1} and {number2}?",
    input_variables=["number1", "number2"]
)

chat = ChatOpenAI(
    model_name="gpt-3.5-turbo"
)

chain = LLMChain(llm=chat, prompt=template)
result = chain.run({
    "number1": 3,
    "number2": 10
})
print(result)


