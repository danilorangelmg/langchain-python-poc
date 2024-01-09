import os
from langchain.chat_models.openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# Configurar a chave da API da OpenAI (substitua pelo seu valor)
os.environ["OPENAI_API_KEY"] = "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"


class OpenAIBuilder:
    def __init__(self, prompt, input_variable):
        self.prompt = prompt,

        if not isinstance(input_variable, list) or not all(isinstance(item, str) for item in input_variable):
            raise ValueError("inputVariable deve ser uma lista de strings")
        self.inputVariable = input_variable

    def build(self, parameters):
        template = PromptTemplate(
            template=self.prompt[0],
            input_variables=self.inputVariable
        )
        chat = ChatOpenAI(
            model_name="gpt-3.5-turbo"
        )
        chain = LLMChain(llm=chat, prompt=template)
        result = chain.run(parameters)
        return result
