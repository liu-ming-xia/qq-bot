import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def health_check():
    """健康检查端点，Render需要"""
    return jsonify({"status": "online", "service": "qq-bot"})

@app.route("/qq-bot", methods=["POST"])
def handle_qq_message():
    """接收QQ机器人消息的接口"""
    try:
        data = request.get_json()
        print(f"收到消息: {data}")
        
        if not data or "post_type" not in data:
            return jsonify({"status": "error", "message": "无效的消息格式"}), 400
        
        post_type = data.get("post_type")
        
        if post_type == "message":
            message_type = data.get("message_type")
            user_id = data.get("user_id", "")
            message = data.get("message", "")
            
            print(f"消息类型: {message_type}, 用户: {user_id}, 消息内容: {message}")
            
            reply = handle_reply(message)
            
            if reply:
                print(f"回复: {reply}")
                return jsonify({"status": "success", "reply": reply})
            
        return jsonify({"status": "ok"})
    
    except Exception as e:
        print(f"处理消息时出错: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500

def handle_reply(message: str) -> str:
    """简单的自动回复逻辑"""
    if not message:
        return None
    
    message = message.strip().lower()
    
    if "你好" in message or "hello" in message:
        return "你好！我是QQ机器人，很高兴认识你！"
    elif "帮助" in message or "help" in message:
        return "我可以帮你：\n1. 回复简单对话\n2. 查看天气\n3. 更多功能开发中..."
    elif "天气" in message:
        return "天气查询功能开发中，敬请期待！"
    else:
        return f"收到你的消息：{message}"

@app.route("/webhook", methods=["POST"])
def webhook():
    """备用Webhook端点"""
    return handle_qq_message()

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8080))
    app.run(host="0.0.0.0", port=port, debug=False)
