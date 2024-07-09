import os
from dotenv import load_dotenv
from langchain.chains.retrieval_qa.base import RetrievalQA
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_openai import ChatOpenAI

# Load environment variables from .env file
load_dotenv()

# Set your OpenAI API key
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY not found in environment variables")

# Load the PDF document
loader = PyPDFLoader("https://arxiv.org/pdf/2302.03803.pdf")
documents = loader.load()

# Create embeddings for the documents
def get_embedding(page_content, engine):
    pass


embeddings = [get_embedding(doc.page_content, engine="text-embedding-ada-002") for doc in documents]

# Create a FAISS vector store from the documents and embeddings
db = FAISS.from_documents(documents, embeddings)
retriever = db.as_retriever()

# Initialize the language model
llm = ChatOpenAI(model_name="gpt-3.5", openai_api_key=OPENAI_API_KEY)

# Create the RetrievalQA chain
qa = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=retriever,
    return_source_documents=True
)

# Query the model
query = "대강 무슨 내용이야?"
result = qa({"query": query})

# Print the result
print(result['result'])
