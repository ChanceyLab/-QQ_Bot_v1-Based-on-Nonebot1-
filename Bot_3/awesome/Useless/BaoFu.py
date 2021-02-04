#from nonebot import on_command, CommandSession
#from nonebot import on_natural_language, NLPSession, IntentCommand
#from jieba import posseg
#from nonebot import get_bot
#from pypinyin import lazy_pinyin
#from Bot_3 import TRUST
#import re
#import random
#import urllib.request
#import io
#import sys
#import requests
#import pypinyin

#url = 'https://nmsl.shadiao.app/api.php?level=min'


#@on_command('Zuan',only_to_me = False)
#async def Zuan(session: CommandSession):

#    Msg_Text = session.ctx["message"][0]["data"]["text"]
#    首字母
#    Head_Msg_Text = pypinyin.pinyin(Msg_Text,style = pypinyin.FIRST_LETTER)
#    Long_Head_Msg_Text = len(Head_Msg_Text)
#    Result_Head_PinYin = ''
#    i_H = 0
#    for i_H in range(Long_Head_Msg_Text):
#        Result_Head_PinYin = Result_Head_PinYin + Head_Msg_Text[i_H][0]
#    全拼
#    PinYin_Msg_Text = lazy_pinyin(Msg_Text)
#    Long_Msg_Text= len(PinYin_Msg_Text)
#    Result_PinYin = ''
#    i_M = 0
#    for i_M in range(Long_Msg_Text):
#        Result_PinYin = Result_PinYin + PinYin_Msg_Text[i_M]
#    混合检测
#    if  re.search('wocao',Result_PinYin,  re.I) or \
#        re.search('baba',Result_PinYin,  re.I) or \
#        re.search('sil',Result_PinYin,  re.I) or \
#        re.search('fuck',Result_PinYin,  re.I) or \
#        re.search('laji',Result_PinYin,  re.I) or \
#        re.search('naocan',Result_PinYin,  re.I) or \
#        re.search('cnm',Result_PinYin,  re.I) or \
#        re.search('gun', Result_PinYin, re.I) or \
#        re.search('jb',Result_Head_PinYin, re.I) or\
#        re.search('nm',Result_Head_PinYin, re.I) or\
#        re.search('sb',Result_Head_PinYin, re.I) or\
#        re.search('wg',Result_Head_PinYin, re.I) or\
#        re.search('bb',Result_Head_PinYin, re.I) or\
#        re.search('fw',Result_Head_PinYin, re.I) :

#        response = requests.get(url)
#        s = re.findall(r'.*',response.text)

#        a = random.randint(1,30)

#        if a == 1:
#            await session.send(s[0],at_sender = True)
#        elif a == 2:
#            await session.send('开学干死你！',at_sender = True)
#        elif a == 3:
#            await session.send('cnm！我要顺着网线去你家打爆你的狗头！',at_sender = True)
#        elif a == 4:
#            await session.send(s[0],at_sender = True)
#        elif a == 5:
#            await session.send('别人问我有多强，我在祖安有爹娘',at_sender = True)
#        elif a == 6:
#            await session.send('傻逼，你再骂一句？',at_sender = True)
#        elif a == 7:
#            await session.send('几个🐎呀？说话这么嚣张！',at_sender = True)
#        elif a == 8:
#            await session.send(s[0],at_sender = True)
#        elif a == 9:
#            await session.send('你🐎逼里开小坦克！嘻嘻！',at_sender = True)
#        elif a == 10:
#            await session.send('刚才火葬场打电话来了，说你🐎粘锅啦！快去看看啊！',at_sender = True)
#        elif a == 11:
#            await session.send('如果你🐎不是批量生产，那我劝你少惹我！',at_sender = True)
#        elif a == 12:
#            await session.send(s[0],at_sender = True)
#        elif a == 13:
#            await session.send('你就像青青草原上那个美羊羊，三千多集找不着娘！',at_sender = True)
#        elif a == 14:
#            await session.send('我看你嘴挺能说的，能帮我暖暖脚么？',at_sender = True)
#        elif a == 15:
#            await session.send('我给你娘大卸八块摁在马桶一顿踹，老子给你腿打瘸，骨灰都被老子拌饭喂路边傻狗了！',at_sender = True)
#        elif a == 16:
#            await session.send(s[0],at_sender = True)
#        elif a == 17:
#            await session.send('老子的五句话禁言，保住了你这个废物的臭🐎。',at_sender = True)
#        elif a == 18:
#            await session.send('我透你爸爸个嘴儿！你爸坟头草五丈高！',at_sender = True)
#        elif a == 19:
#            await session.send('尘归尘，土归土，把你骨灰扬了都不配做PM2.5！',at_sender = True)
#        elif a == 20:
#            await session.send(s[0],at_sender = True)
#        elif a == 21:
#            await session.send('我真想送你妈一朵花。对不起开个玩笑！我哪来的花？你哪来的妈？',at_sender = True)
#        elif a == 22:
#            await session.send('还怪你爹呢？不就是当初给你妈上坟没带上你吗？',at_sender = True)
#        elif a == 23:
#            await session.send('是泰坦尼克号在你🐎臭批里沉了给你自信了？',at_sender = True)
#        elif a == 24:
#            await session.send('傻逼！你等着！',at_sender = True)
#        elif a == 25:
#            await session.send('你是那青青草原懒羊羊，三千多集顶着翔！',at_sender = True)
#        elif a == 26:
#            await session.send('火葬场打电话问你🐎几分熟？',at_sender = True)
#        elif a == 27:
#            await session.send('狗再叫！狗别怂！',at_sender = True)
#        elif a == 28:
#            await session.send(s[0],at_sender = True)
#        elif a == 29:
#            await session.send('多出去晒晒太阳就没人说你是白痴了！',at_sender = True)
#        elif a == 30:
#            await session.send('去拼多多拼个🐎再来跟我说话！',at_sender = True)





# on_natural_language 装饰器将函数声明为一个自然语言处理器
# keywords 表示需要响应的关键词，类型为任意可迭代对象，元素类型为 str
# 如果不传入 keywords，则响应所有没有被当作命令处理的消息
#@on_natural_language(only_to_me = True)
#async def _(session: NLPSession):
#     去掉消息首尾的空白符
#    stripped_msg = session.msg_text.strip()
#     返回意图命令，前两个参数必填，分别表示置信度和意图命令名
#    return IntentCommand(TRUST, 'Zuan')




