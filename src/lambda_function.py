import os
import json
import boto3
import markovify
from linebot import LineBotApi
from linebot.models import (TextSendMessage)

GET_OBJECT_KEY_NAME = "learned_data.json"

s3_client = boto3.client("s3")


def lambda_handler(event, content):
    AWS_S3_BUCKET_NAME = os.environ['BUCKET_NAME']
    response = s3_client.get_object(
        Bucket=AWS_S3_BUCKET_NAME, Key=GET_OBJECT_KEY_NAME)
    body = response['Body'].read()
    learned_model = body.decode('utf-8')
    text_model = markovify.NewlineText.from_json(learned_model)
    message = "発言を生成しました\n ----------\n"
    i = 0
    while i != 3:
        sentense = text_model.make_short_sentence(140, state_size=3, trial=100)
        if not sentense is None:
            i += 1
            message += f'・{sentense.replace(" ", "")}\n'
    message += "----------"
    res = broadcast_message(message)
    return res


def broadcast_message(msg):
    LINE_ACCESS_TOKEN = os.environ["LINE_ACCESS_TOKEN"]
    line_bot_api = LineBotApi(LINE_ACCESS_TOKEN)
    return line_bot_api.broadcast(TextSendMessage(text=msg))
