# coding: utf-8
from random import randint
from smart_qq_bot.logger import logger
import requests
import hashlib

from smart_qq_bot.signals import (
    on_all_message,
    on_discuss_message,
    on_group_message
)
from smart_qq_bot.messages import GROUP_MSG;
import datetime

# 使用前请先前往 http://www.tuling123.com/register/index.jhtml
# 申请 API key 谢谢
# 另外需要 requests 支持
# 修改成调用图灵官方接口
url = 'http://www.tuling123.com/openapi/api'
apikey = '8124ed4f28874af6ac759fc48f4fff99'


@on_all_message
def turing_robot(msg, bot):
    """
    :type bot: smart_qq_bot.bot.QQBot
    :type msg: smart_qq_bot.messages.QMessage
    """
    if datetime.datetime.now().minute % 2 == 0:
        try:
            querystring = {
                "key": apikey,
                "info": msg.content,
                "userid": msg.src_sender_id
            }
            response = requests.request("GET", url, params=querystring)
            response_json = response.json()
            bot.reply_msg(msg, response_json.get('text'))
            try:
                bot.reply_msg(msg, response_json.get('url'))
            except AttributeError:
                logger.info("No URL!")
        except NotImplementedError:
            querystring = {
                "key": apikey,
                "info": msg.content
            }
            response = requests.get(url, params=querystring);
            response_json = response.json()
            bot.reply_msg(msg, response_json.get('text'))
            try:
                bot.reply_msg(msg, response_json.get('url'))
            except AttributeError:
                logger.info("No URL!")
