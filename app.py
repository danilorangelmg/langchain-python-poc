import os

from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import TokenTextSplitter
from langchain.vectorstores.redis import Redis
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chat_models.openai import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain.chains import StuffDocumentsChain
from langchain.chains import LLMChain
from pdf2image import convert_from_path


def loadData():
    files = DirectoryLoader("/Users/danilorangel/Documents/Workspace/LLM/langchain-python-poc/assets").load()
    tokentextsplitter = TokenTextSplitter(
        encoding_name="cl100k_base",
        chunk_size=400,
        chunk_overlap=10
    )

    os.environ["OPENAI_API_KEY"] = "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"

    split = tokentextsplitter.split_documents(files)

    redis = Redis.from_documents(
        split, OpenAIEmbeddings(), redis_url="redis://localhost:6379", index_name="chunk"
    )
    chat = ChatOpenAI(
        temperature=0.1,
        openai_api_key=os.environ["OPENAI_API_KEY"],
        model_name="gpt-3.5-turbo"
    )

    prompt = PromptTemplate(
        template="Você Responde perguntas sobre programação." +
                 "O usuário está lendo a documentação afim de entender e implementar os conceitos de codigo." +
                 "Use o conteudo informado abaixo para responder a pergunta do usuário." +
                 "Se a resposta não for encontrada no texto, responda que voce não sabe, não invente uma resposta." +
                 "Se possivel, inclua exemplos de código. "
                 "Textos {context} "
                 "Perguntas {question}".strip(),
        input_variables=["context", "question"]
    )

    llm_chain = LLMChain(llm=chat, prompt=prompt)

    combine_documents_chain = StuffDocumentsChain(
        llm_chain=llm_chain,
        document_variable_name="context"
    )

    chain = RetrievalQA(
        combine_documents_chain=combine_documents_chain,
        retriever=redis.as_retriever(),
    ).from_llm(
        llm=chat,
        retriever=redis.as_retriever(),
        prompt=prompt,
        return_source_documents=True
    )

    # chain = RetrievalQA().from_llm(
    #     combine_documents_chain=combine_documents_chain,
    #     retriever=redis.as_retriever(),
    #     return_source_documents=True
    # )

    response = chain._call(
        {
            "query": "how to combine two prompts the using the first result with parameters in the second prompt using agents?"
        }
    )


    print(response)


# result = Redis.similarity_search_with_score(
#    redis,
#    "what is langchain?"
# )
#
# print(result)


if __name__ == "__main__":
    loadData()
    # print("finalizado...")
print("finalizado...")
