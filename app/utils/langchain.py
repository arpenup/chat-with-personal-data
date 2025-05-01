from langchain_community.document_loaders import DirectoryLoader, TextLoader
from typing import Optional
from langchain_text_splitters import MarkdownHeaderTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import DocArrayInMemorySearch
from langchain.chat_models import init_chat_model
from langchain.chains import RetrievalQA

DB: DocArrayInMemorySearch = None

'''初始化 LangChain 矢量数据库

读取本地存储数据源，解析并生成 矢量数据库，赋值到全局变量 DB 中

Parameters
----------
path : str
    本地数据源的路径

Returns
----------

'''
def initLibrary(path: str):
    global DB  # 声明我们要使用全局变量

    # 文档加载器
    loader = DirectoryLoader(path, 
                             glob="*.md", 
                             show_progress=True,
                             loader_cls=TextLoader,
                             loader_kwargs={'encoding': 'utf-8'})
    docs = loader.load()

    # 将所有文件整合拼接
    if len(docs) < 1:
        raise ValueError("{path} 下文档列表为空，程序无法继续运行。")
    
    content = "\n\n".join([doc.page_content for doc in docs])

    # 文本分割器——markdown分割器
    headers_to_split_on = [
        ("#", "Header 1"),
        ("##", "Header 2"),
        ("###", "Header 3"),
    ]
    markdown_splitter = MarkdownHeaderTextSplitter(headers_to_split_on)
    md_header_splits = markdown_splitter.split_text(content)

    # 创建 OpenAI 的词嵌入
    embeddings = OpenAIEmbeddings()
    # 生成矢量数据库
    DB = DocArrayInMemorySearch.from_documents(
        md_header_splits, 
        embeddings
    )

'''LangChain检索器链式查询

Parameters
----------
query : str
    用户查询内容
model : str
    使用的大语言模型，默认 gpt-4o-mini
provider : str
    模型提供者，默认 openai

Returns
----------
response : any
    大预言模型生成的响应结果

'''
def call_llm(query: str, model: Optional[str] = "gpt-4o-mini", provider: Optional[str] = "openai") -> any:
    llm = init_chat_model(model, model_provider=provider)
    retriever = DB.as_retriever()

    qa_stuff = RetrievalQA.from_chain_type(
        llm=llm, 
        chain_type="stuff", 
        retriever=retriever, 
        verbose=True
    )

    response = qa_stuff.invoke(query)

    return response
