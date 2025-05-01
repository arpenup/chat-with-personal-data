import getpass
import os
from flask import Flask, render_template
from .views import chat
from .utils import langchain

'''检测/加载 API Key

检测是否存在 Key
若不存在则从 api_key.txt 文件加载
若文件不存在则设置用户输入
'''
def init_env():
    FILE_PATH = "api_key.txt"
    NAME = "OPENAI_API_KEY"
    if NAME not in os.environ:
        if FILE_PATH and os.path.exists(FILE_PATH):
            try:
                with open(FILE_PATH, 'r', encoding='utf-8') as f:
                    for line in f:
                        line = line.strip()
                        if line and '=' in line:
                            name, val = line.split('=', 1)
                            if name.strip() == NAME:
                                value = val.strip()
                                os.environ[name] = value
                                print(f"成功从文件 {FILE_PATH} 读取到: {NAME}={value}")
                                return
                    print(f"在文件 {FILE_PATH} 中未找到环境变量: {NAME}")
            except Exception as e:
                print(f"读取文件 {FILE_PATH} 时发生错误: {e}")
        else:
            os.environ[NAME] = getpass.getpass("请输入你的 OpenAI API key: ")
    else:
        print(f"已从系统检测环境变量: {NAME}")

'''创建 Flask 应用实例

Returns
app : Flask
    应用实例对象
'''
def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # 注册蓝图
    app.register_blueprint(chat.chat_bp)

    print(app.config['LOCAL_PATH'])
    langchain.initLibrary(app.config['LOCAL_PATH'])

    # 默认路由
    @app.route('/')
    def default_route():
        project_name = app.config['PROJECT_NAME']
        return render_template('home.html', project_name=project_name)

    return app
