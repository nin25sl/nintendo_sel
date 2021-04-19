from flask import Flask, request, abort
import os

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError,  LineBotApiError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

#環境変数取得
YOUR_CHANNEL_ACCESS_TOKEN = os.environ["YOUR_CHANNEL_ACCESS_TOKEN"]
YOUR_CHANNEL_SECRET = os.environ["YOUR_CHANNEL_SECRET"]
user_id = os.environ["USER_ID"]

line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(YOUR_CHANNEL_SECRET)

@app.route("/")
def hello_world():
    return "hello world!"

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = "sorry, can't responce"
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=message))

def push_mes():
    try:
        line_bot_api.push_message(user_id, TextSendMessage(text='switchが入荷しました。購入しましょう'))
        line_bot_api.push_message(user_id, TextSendMessage(text="https://store-jp.nintendo.com/customize/switch/"))
    except LineBotApiError as e:
        print("miss")

def push_secretmessage():
    try:
        line_bot_api.push_message(user_id, TextSendMessage(text='test message'))
        line_bot_api.push_message(user_id, TextSendMessage(text='1分に一回通知するようになっていましたが、毎時26分に通知するように変更しました。また、ログをみたところ今日プログラムは動いていませんでした。笑'))
    except LineBotApiError as e:
        print("miss")

if __name__ == "__main__":
#    app.run()
    port = int(os.getenv("PORT"))
    app.run(host="0.0.0.0", port=port)