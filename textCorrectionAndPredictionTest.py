from OpenAIBuilder import OpenAIBuilder

text = ""
with open('/Users/danilorangel/Documents/Workspace/LLM/langchain-python-poc/assets/mat.txt') as f:
    lines = f.readlines()
    text = text.join(lines)

    builder = OpenAIBuilder("Você é um analisador e corretor de textos em Portugues-BR " +
                            "sua função é executar uma analise por contexto pois os textos " +
                            "são extraidos de OCR e podem conter caracteres estranhos, divergentes e fora de contexto " +
                            "substitua os caracteres para que a frase em questão faça sentido dentro do texto " +
                            " e apos isso retorno o texto corrigido. Texto para analise {texto}", ["texto"])

    correctText = builder.build({
        "texto": text
    })

    builder = OpenAIBuilder(
        "Você é um analisador de documentos, sua função é extrair informações importantes " +
        "contida dentro de um texto que representa um documento em questão, o usuário irá " +
        "fornecer o texto fornecerá a resposta em um formado json, especificado abaixo " +
        "Para esta analise voce ira extrair as informações sobre o imovel " +
        "Documento a ser analisado: {texto} " +
        "formato de resposta "
        " tipoImovel: tipoImovel, descricaoImovel: descricaoImovel, metragem: metragem",
        input_variable=["texto"]
    )

    result = correctText = builder.build({
        "texto": correctText
    })

    print(result)

    builder = OpenAIBuilder(
        "Você é um analisador de documentos, sua função é extrair informações importantes " +
        "contida dentro de um texto que representa um documento em questão, o usuário irá " +
        "fornecer o texto fornecerá a resposta em um formado json, especificado abaixo " +
        "Para esta analise voce ira extrair todas as informações que julgar importante " +
        "Documento a ser analisado: {texto} ",
        input_variable=["texto"]
    )

    result = correctText = builder.build({
        "texto": correctText
    })

    print(result)