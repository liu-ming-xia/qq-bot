# QQ机器人

基于 Python Flask 的简单 QQ 机器人，部署在 Render 免费服务器上。

## 功能

- 自动回复简单对话
- 支持关键词回复
- Webhook 接收 QQ 消息

## 部署说明

代码已部署在 Render 平台，通过 QQ 开放平台的消息URL配置接入。

## 本地测试

```bash
pip install -r requirements.txt
python app.py
