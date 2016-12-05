from smart_qq_bot.logger import logger
from smart_qq_bot.signals import (on_all_message, on_group_message, on_discuss_message, on_private_message)
import re

@on_group_message(name="iwish[群]")
def iwish_group(msg, bot):
    """
    :type bot: smart_qq_bot.bot.QQBot
    :type msg: smart_qq_bot.messages.QMessage
    :param msg:
    :param bot:
    :return:
    """
    if msg.content == "爱是":
        reply = bot.reply_msg(msg, return_function=True)
        logger.info("INPUT: " + msg.content)
        reply("爱是最棒了！")
    elif re.match("麦客|表单组件|联系人", msg.content):
        bot.reply_msg(msg, return_function=True)("联系人组件：\n姓名-姓名\n学号-网址\n性别-称谓\n个人特长-传真\n志愿者编号-公司\n宿舍号-职位\n手机-手机\n年级-城市")
        logger.info("INPUT: " + msg.content)
    elif re.match("晓彤", msg.content):
        bot.reply_msg(msg, return_function=True)("记得上近代史😯 😯 ")
        logger.info("INPUT: " + msg.content)
