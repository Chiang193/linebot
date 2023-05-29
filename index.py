from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('USazBFzGGm3vtogwZwobys6ta5d2Y/bBlX3UOIcPW3WTw8lX4AhE8/l42EI49x4gJeIURmDoEvHzDgo+AGVuBmJo3A2crx+Ac0eOxXavmrbXEBVZeVK2p4dGlqhHzC4rtRtRYw7aKSkKP2GVB/b/ewdB04t89/1O/w1cDnyilFU=')
handler1 = WebhookHandler('10d4565fcf83e198a9500628eaaecb91')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler1.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler1.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()
