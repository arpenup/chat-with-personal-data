class Config:
    PROJECT_NAME="chat-with-personal-data" # project name
    VERSION="0.0.1-demo" # project version

    DEBUG = True
    HOST = "127.0.0.1"
    PORT = 5001

    LOCAL_PATH = "app/resources/file_md" # local files path

    # LLM configurations
    PROVIDER = "openai" # provider for llm, available value: 
    MODEL = "gpt-4o-mini"
