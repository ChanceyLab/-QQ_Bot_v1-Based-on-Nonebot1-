import json
from typing import Optional
import aiohttp
from aiocqhttp.message import escape
from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand
from nonebot.helpers import context_id, render_expression

# 定义无法获取图灵回复时的「表达（Expression）」
EXPR_DONT_UNDERSTAND = (
    '我现在不太明白你说的，但没关系，通过主人的机器学习我会变得更强[CQ:face,id=30]',
    '我看不懂你的意思呀，可以跟我聊些简单的话题嘛[CQ:face,id=106]',
    '呃，这个问题好难啊[CQ:face,id=5]baby不会回答呀~主人快来救我！喵~',
    '抱歉哦，我现在的能力还不能明白你在说什么，但我会学习的～[CQ:face,id=183]'
                        )

# 注册一个仅内部使用的命令，不需要 aliases
@on_command('tuling',only_to_me = False)
async def tuling(session: CommandSession):
    # 获取可选参数，这里如果没有 message 参数，命令不会被中断，message 变量会是 None
    message = session.state.get('message')
    #print(message)
    # 通过封装的函数获取图灵机器人的回复
    reply = await call_tuling_api(session, message)
    if reply == 'Fail':
        await session.send('唉~我都烦死了！今天回复次数用完啦！明天再来吧！')
        #add you code here!
    if reply:
        # 如果调用图灵机器人成功，得到了回复，则转义之后发送给用户
        # 转义会把消息中的某些特殊字符做转换，以避免 酷Q 将它们理解为 CQ 码
        await session.send(escape(reply))
    else:
        # 如果调用失败，或者它返回的内容我们目前处理不了，发送无法获取图灵回复时的「表达」
        # 这里的 render_expression() 函数会将一个「表达」渲染成一个字符串消息
        await session.send(render_expression(EXPR_DONT_UNDERSTAND))
    #if escape(reply) == '':
        #print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

@on_natural_language
async def _(session: NLPSession):
    # 以置信度 60.0 返回 tuling 命令
    # 确保任何消息都在且仅在其它自然语言处理器无法理解的时候使用 tuling 命令
    return IntentCommand(60.0, 'tuling', args={'message': session.msg_text})

async def call_tuling_api(session: CommandSession, text: str) -> Optional[str]:
    # 调用图灵机器人的 API 获取回复
    if not text:
        return None
    url = 'http://openapi.tuling123.com/openapi/api/v2'
    # 构造请求数据
    payload = {
        'reqType': 0,
        'perception': {
            'inputText': {
                'text': text
            }
        },
        'userInfo': {
            'apiKey': session.bot.config.TULING_API_KEY,
            'userId': context_id(session.ctx, use_hash=True)
        }
    }
    group_unique_id = context_id(session.ctx, mode='group', use_hash=True)
    if group_unique_id:
        payload['userInfo']['groupId'] = group_unique_id
    try:
        # 使用 aiohttp 库发送最终的请求
        async with aiohttp.ClientSession() as sess:
            async with sess.post(url, json=payload) as response:
                if response.status != 200:
                     #如果 HTTP 响应状态码不是 200，说明调用失败
                    return None
                resp_payload = json.loads(await response.text())
                if resp_payload['results']:
                    for result in resp_payload['results']:
                        if result['resultType'] == 'text':
                            # 返回文本类型的回复
                            #print("成功回复？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？")
                            return result['values']['text']
    except:
        #aiohttp.ClientError, json.JSONDecodeError, KeyError
        #print('调用失败！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！')
        return 'Fail'
