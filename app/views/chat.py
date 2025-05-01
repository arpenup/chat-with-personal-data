from flask import Blueprint, render_template, request, jsonify
from ..utils.langchain import call_llm
from flask import current_app

# 创建蓝图对象
chat_bp = Blueprint("chat", __name__, url_prefix='/chat')

@chat_bp.route("/")
def chat_interface():
    return render_template("chat.html")

@chat_bp.route('/send_message', methods=['POST'])
def send_message():
    user_message = request.form.get('message')
    if user_message:
        # LangChain 调用
        ai_reply = call_llm(user_message, current_app.config["MODEL"], current_app.config["PROVIDER"])

        return jsonify({'reply': ai_reply})
    else:
        return jsonify({'error': 'No message received'}), 400
