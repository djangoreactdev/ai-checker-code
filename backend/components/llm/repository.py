from components.core.settings import settings
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Qdrant
from langchain.document_loaders import JSONLoader
from components.llm import schemas as llm_schemas


class LLMService:
    def __init__(self) -> None:
        pass

    def get_answer_from_llm(self, input: str) -> llm_schemas.FAQItem:
        # file_path = (
        #     settings.current_folder + settings.project_folder + "/datasource/FAQ.json"
        # )
        # loader = JSONLoader(
        #     file_path=file_path,
        #     jq_schema=".[]",
        #     text_content=False,
        # )
        # documents = loader.load()
        # text_splitter = CharacterTextSplitter(chunk_size=100, chunk_overlap=0)
        # docs = text_splitter.split_documents(documents)

        # embeddings = OpenAIEmbeddings()

        # qdrant_document = Qdrant.from_documents(
        #     docs,
        #     embeddings,
        #     url=settings.qdrant_url,
        #     prefer_grpc=True,
        #     collection_name="my_documents",
        # )
        # found_docs = qdrant_document.similarity_search(input)
        return llm_schemas.FAQItem(**eval(found_docs[0].page_content))
