from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.text_splitter import CharacterTextSplitter
from langchain.llms import OpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.document_loaders import PyPDFLoader
from langchain.memory import ConversationBufferMemory
from langchain.chat_models import ChatOpenAI


import os

os.environ["OPENAI_API_KEY"] = "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"


class VectorStore:
    def __init__(self):
        self.vectorstore = None


vector_store = VectorStore()

memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)


def split_pdf_add_db(file) -> Chroma:
    global vectorstore

    loader = PyPDFLoader(file)
    documents = loader.load()

    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    documents = text_splitter.split_documents(documents)

    embeddings = OpenAIEmbeddings()
    vectorstore = Chroma.from_documents(documents, embeddings)

    vector_store.vectorstore = vectorstore

    return vectorstore


def answer_question(query):
    qa = ConversationalRetrievalChain.from_llm(
        OpenAI(temperature=0), vectorstore.as_retriever(), memory=memory
    )

    chat_history = [(query, "")]

    query = query["question"]
    result = qa({"question": query, "chat_history": chat_history})
    return result


'''
#!/usr/bin/env python
# coding: utf-8

from langchain.memory import ConversationBufferMemory
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.llms import OpenAI
from langchain.document_loaders import PyPDFLoader
from langchain.chains import ConversationalRetrievalChain
import panel as pn
import os

os.environ["OPENAI_API_KEY"] = "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"


pn.extension("texteditor", template="bootstrap", sizing_mode="stretch_width")
pn.state.template.param.update(
    main_max_width="690px", header_background="#F08080")


file_input = pn.widgets.FileInput(width=300)

prompt = pn.widgets.TextEditor(
    value="", placeholder="Enter your question here...", height=160, toolbar=False
)

run_button = pn.widgets.Button(name="Run!")

select_k = pn.widgets.IntSlider(
    name="Name of relevant Chunks", start=1, end=5, step=1, value=2
)

select_chain_type = pn.widgets.RadioButtonGroup(
    name="Chain Type", options=["Stuff", "Map Reduce", "Refine", "Map Rerank"]
)


widgets = pn.Row(
    pn.Column(prompt, run_button, margin=4),
    pn.Card(
        "Chain Type:",
        pn.Column(select_chain_type, select_k),
        title="Advenced Settings",
        margin=4,
    ),
    width=900,
)


memory = ConversationBufferMemory(
    memory_key="chat_history", return_messages=True)


def ConvRetQA(file, query, chain_type, k):
    loader = PyPDFLoader(file)
    documents = loader.load()

    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    texts = text_splitter.split_documents(documents)

    embeddings = OpenAIEmbeddings()

    db = Chroma.from_documents(texts, embeddings)

    retriever = db.as_retriever(
        search_type="similarity", search_kwargs={"k": 2})

    qa = ConversationalRetrievalChain.from_llm(
        OpenAI(temperature=0), db.as_retriever(), memory=memory
    )

    chat_history = []

    result = qa({"question": query, "chat_history": chat_history})
    print(result)
    return result["answer"]


convos = []  # store all panel objects in a list


def qa_result(_):
    # save pdf file to a temp file
    if file_input.value is not None:
        file_input.save("temp.pdf")

        prompt_text = prompt.value
        if prompt_text:
            result = ConvRetQA(
                file="temp.pdf",
                query=prompt_text,
                chain_type=select_chain_type.value,
                k=select_k.value,
            )
            convos.extend(
                [
                    pn.Row(pn.panel("\U0001F60A", width=10),
                           prompt_text, width=900),
                    pn.Row(
                        pn.panel("\U0001F916", width=10),
                        pn.Column(
                            result,
                            "Relevant source text:",
                            pn.pane.Markdown(
                                "\n--------------------------------------------------------------------\n".join(
                                    doc.page_content
                                    for doc in result[0]["source_documents"]
                                )
                            ),
                        ),
                    ),
                ]
            )
            # return convos
    return pn.Column(*convos, margin=15, width=575, min_height=400)


qa_interactive = pn.panel(
    pn.bind(qa_result, run_button),
    loading_indicator=True,
)


output = pn.WidgetBox(
    "*Output will show up here:*", qa_interactive, width=630, scroll=True
)


# layout
pn.Column(
    pn.pane.Markdown(
        """
    ## \U0001F60A! Question Answering with your PDF file
    
    1) Upload a PDF.  2) Type a question and click "Run".
    
    """
    ),
    pn.Row(file_input),
    widgets,
    output,
).servable()
'''
