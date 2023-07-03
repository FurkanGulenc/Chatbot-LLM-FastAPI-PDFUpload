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



