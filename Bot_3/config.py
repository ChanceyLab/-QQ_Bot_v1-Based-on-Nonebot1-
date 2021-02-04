import re
from nonebot.default_config import *
from datetime import timedelta

#https://nonebot.cqp.moe/api.html#access-token

API_ROOT = 'http://127.0.0.1:5050'

HOST = '0.0.0.0'

PORT = 5050

SUPERUSERS = {}

COMMAND_START = {''}
#COMMAND_START = ['', re.compile(r'[/!]+')]#

TULING_API_KEY = '#此处放图灵机器人key'

SHORT_MESSAGE_MAX_LENGTH = 2000

DEBUG = False

SESSION_RUN_TIMEOUT = timedelta(seconds = 5)

#SESSION_RUNNING_EXPRESSION = '我在处理命令呢！别说话！'#运行中回复

#DEFAULT_VALIDATION_FAILURE_EXPRESSION = '发送内容格式不太对呢，问问管理员在特么发送哦～'#设置更亲切的默认错误提示