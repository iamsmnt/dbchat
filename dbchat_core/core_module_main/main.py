from core_module_dbs.dbs import DBInterface
from core_module_llm_engines.engines import LlmEngine
from core_module_llm_models.llm_models import LlmModel
from core_module_prompts.sql_prompt import (SQL_PROMPT)
from langchain_community.chat_models import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.llms import Ollama
# import ollama

embeddings = (
    OllamaEmbeddings()
)

llm = Ollama(
    model="llama2",
    system="you are a funny bot, you answer with sarcasm!"
)
llm.invoke("Tell me an awful joke")

llm = Ollama(model="sqlcoder",stop=["###Resonse"])
prompt = ChatPromptTemplate.from_template(SQL_PROMPT)
chain = prompt | llm | StrOutputParser()
resp = chain.invoke({"question": "which products generate the most sales."})
print(resp)




text = "This is a test document."

query_result = embeddings.embed_query(text)
query_result[:5]

class MainChatModule(DBInterface,LlmEngine,LlmModel):

    def __init__(self,db_params,llm_engine_params,model_params):
        self.db_params = db_params 
        self.llm_engine_params = llm_engine_params
        self.model_params = model_params


    def getPostgresDB(self, engine):
        super().getPostgresDB(engine)
        


