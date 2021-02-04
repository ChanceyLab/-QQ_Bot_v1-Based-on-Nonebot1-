#-*- coding:utf-8 -*-
from typing import Optional
from aiocqhttp.message import escape
from nonebot.helpers import context_id, render_expression
from nonebot import on_command, CommandSession
from aiocqhttp.exceptions import Error as CQHttpError
from nonebot import on_natural_language, NLPSession, IntentCommand
from Bot_3 import TRUST
from Bot_3 import STATIC_VAL
from lxml import etree
from bs4 import BeautifulSoup
from pandas import DataFrame
from django.http import HttpResponse#安装
from django.shortcuts import render
from urllib import request, parse
from math import radians, cos, sin, asin, sqrt
from googletrans import Translator
from jieba import posseg
import aiohttp
import random
import datetime
import urllib.request
import requests, json, time, re, os, sys, time, io, csv, urllib
import bs4
import pandas as pd#引入pandas方便数据可视化
import serial#安装
import nonebot
import xlwt#安装
import xlrd#安装

bot = nonebot.get_bot()

url_Kua = 'https://chp.shadiao.app/api.php'

#'https://nmsl.shadiao.app/api.php?level=max&lang=zh_cnlevel={max,min}lang={zh-cn,zh-hk}'
url_Zuan = 'https://nmsl.shadiao.app/api.php?level=min&lang=zh_ch'

url_Zuan_Max = 'https://nmsl.shadiao.app/api.php?level=max&lang=zh_ch'

url_Muc = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp?aggr=1&cr=1&flag_qc=0&p=1&n=1&w='

url_Adv = 'http://www.boredapi.com/api/activity?type='

url_Adv_Notype = 'http://www.boredapi.com/api/activity/'

url_Trans = 'http://fanyi.youdao.com/translate'  

url_TuL = 'http://openapi.tuling123.com/openapi/api/v2'                                     

Url_RePing = 'http://new.toodo.fun/funs/hotcomments'

url_Wu = 'http://new.toodo.fun/funs/content?type=wu'

url_Du = 'http://new.toodo.fun/funs/content?type=du'

url_QingHua = 'http://new.toodo.fun/funs/content?type=love'

Url_Get_MovieID = 'https://movie.douban.com/j/subject_suggest?q='

Url_DouBan = 'https://movie.douban.com/subject/'

Url_BaiKe = 'https://baike.baidu.com/item/'

Url_ReSou = 'https://s.weibo.com/top/summary?retcode=6102'

key_Amap = '#此处自己添加高德地图的key'

STORE_FEIL = r'H:\QQ_Bot\Bot_3\User_Date\UserDate.xls'

EXPR_DONT_UNDERSTAND = (
    '我现在不太明白你说的，但没关系，通过主人的机器学习我会变得更强[CQ:face,id=30]',
    '我看不懂你的意思呀，可以跟我聊些简单的话题嘛[CQ:face,id=106]',
    '呃，这个问题好难啊[CQ:face,id=5]baby不会回答呀~主人快来救我！喵~',
    '抱歉哦，我现在的能力还不能明白你在说什么，但我会学习的～[CQ:face,id=183]'
                        )

#SCRCH_BOT = '941265190'
###################全局函数随机数####################
def Get_Rand(b):                                    #
    t = time.time()                                 #
    R_1 = random.randint(1,2 * b)                   #
    R_2 = int(round(t * 1000)) % int(2.5 * b)       #
    Rand_Num = (R_1 * R_2) % b + 1                  #
    return Rand_Num                                 #
###################全局函数随机数####################
################全局函数取字符串中的指定字符串###############
def MidString(content,startStr,endStr):                     #
    startIndex = content.index(startStr)                    #
    if startIndex>=0:                                       #
        startIndex += len(startStr)                         #
        endIndex = content.index(endStr)                    #
        return content[startIndex:endIndex]                 #
################全局函数取字符串中的指定字符串###############
###############################谷歌翻译##################################
def Google_Trans(MSG):                                                  #
    translator = Translator(service_urls = ['translate.google.cn'])     #
    #中文zh-CN  日语ja   韩语ko    德语de    俄语ru     法语fr          #
    CN = translator.translate(MSG, dest='zh-CN')                        #
    EN = translator.translate(MSG, dest='en')                           #
    JP = translator.translate(MSG, dest='ja')                           #
    KO = translator.translate(MSG, dest='ko')                           #
    DE = translator.translate(MSG, dest='de')                           #
    RU = translator.translate(MSG, dest='ru')                           #
    FR = translator.translate(MSG, dest='fr')                           #
    return CN.text,EN.text,JP.text,KO.text,DE.text,RU.text,FR.text      # 
##################################谷歌翻译################################
#####################################有道翻译API函数数###############################
def Trans_APi(Trans_Val):                                                           #
    # 创建要提交的数据                                                              #
    Form_Date = {}                                                                  #
    Form_Date['i'] = Trans_Val  #要翻译的内容可以更改                               #
    Form_Date['doctype'] = 'json'                                                   #
    data = parse.urlencode(Form_Date).encode('utf-8') #数据转换                     #
    response = request.urlopen(url_Trans, data)#提交数据并解析                      #
    html = response.read().decode('utf-8') #服务器返回结果读取                      #
    # 可以看出html是一个json格式                                                    #
    #以json格式载入                                                                 #
    translate_results = json.loads(html)                                            #
    # json格式调取                                                                  #
    translate_results = translate_results['translateResult'][0][0]['tgt']           #
    return translate_results                                                        #
#####################################有道翻译API函数数###############################
#######################################tulingrobotapi########################################
async def call_tuling_api(session: CommandSession, text: str) -> Optional[str]:             #
    # 调用图灵机器人的 API 获取回复                                                         #
    if not text:                                                                            #
        return None                                                                         #
    # 构造请求数据                                                                          #
    payload = {                                                                             #
        'reqType': 0,                                                                       #
        'perception': {                                                                     #
            'inputText': {                                                                  #
                'text': text                                                                #
            }                                                                               #
        },                                                                                  #
        'userInfo': {                                                                       #
            'apiKey': session.bot.config.TULING_API_KEY,                                    #
            'userId': context_id(session.ctx, use_hash=True)                                #
        }                                                                                   #
    }                                                                                       #
    group_unique_id = context_id(session.ctx, mode='group', use_hash=True)                  #
    if group_unique_id:                                                                     #
        payload['userInfo']['groupId'] = group_unique_id                                    #
    try:                                                                                    #
        # 使用 aiohttp 库发送最终的请求                                                     #
        async with aiohttp.ClientSession() as sess:                                         #
            async with sess.post(url_TuL, json=payload) as response:                        #
                if response.status != 200:                                                  #
                     #如果 HTTP 响应状态码不是 200，说明调用失败                            #
                    return None                                                             #
                resp_payload = json.loads(await response.text())                            #
                if resp_payload['results']:                                                 #
                    for result in resp_payload['results']:                                  #
                        if result['resultType'] == 'text':                                  #
                            # 返回文本类型的回复                                            #
                            return result['values']['text']                                 #
    except:                                                                                 #
        return 'Fail'                                                                       #
#######################################tulingrobotapi########################################
###############################################高德地图用####################################################
def geo(address: str,city = None)->dict:                                                                    #
    parameters = {'key':key_Amap,                                                                           #      
                  'city':city,                                                                              #
                  'citylimit':True,                                                                         #
                  'address':address                                                                         #
                  }                                                                                         #
    r = requests.get("https://restapi.amap.com/v3/geocode/geo?parameters",params = parameters)              #
    if  r.json()['infocode'] == '10000' and len(r.json()['geocodes']) != 0:                                 #
        data = r.json()['geocodes'][0]['location']                                                          #
        return data                                                                                         #
    else:                                                                                                   #
        return 'F'                                                                                          #
###############################################高德地图用####################################################
#####################################################################查天气调用函数######################################################################################
async def get_weather_of_city(city: str) -> str:                                                                                                                        #
    #当前                                                                                                                                                               #
    parameters_now = {'key':key_Amap,                                                                                                                                   #
                  'city':city,                                                                                                                                          #
                  'extensions':'base',                                                                                                                                  #
                  'output':'json'                                                                                                                                       #
                  }                                                                                                                                                     #
    r_now = requests.get("https://restapi.amap.com/v3/weather/weatherInfo?parameters",params = parameters_now)                                                          #
    List_City = len(r_now.json()['lives'])
    if List_City != 0:
        try:                                                                                                                                                                #
            weater = r_now.json()['lives'][0]['weather']                                                                                                                    #
            temp = r_now.json()['lives'][0]['temperature']                                                                                                                  #
            winddirection = r_now.json()['lives'][0]['winddirection']                                                                                                       #
            windpow = r_now.json()['lives'][0]['windpower']                                                                                                                 #
            humidity = r_now.json()['lives'][0]['humidity']                                                                                                                 #
            result_now = '当前' + city + '的天气为：' + weater + '，' + temp + '℃，空气湿度：' + humidity + '，刮' + winddirection + '风，风力' + windpow + '级！' + '\n'  #
            #预报                                                                                                                                                           #
            parameters_next = {'key':key_Amap,                                                                                                                              #
                          'city':city,                                                                                                                                      #
                          'extensions':'all',                                                                                                                               #
                          'output':'json'                                                                                                                                   #
                          }                                                                                                                                                 #
            r_next = requests.get("https://restapi.amap.com/v3/weather/weatherInfo?parameters",params = parameters_next)                                                    #
            #当日                                                                                                                                                           #
            data0_data = r_next.json()['forecasts'][0]['casts'][0]['date']                                                                                                  #
            data0_week = r_next.json()['forecasts'][0]['casts'][0]['week']                                                                                                  #
            data0_weather = r_next.json()['forecasts'][0]['casts'][0]['dayweather']                                                                                         #
            data0_tempmin = r_next.json()['forecasts'][0]['casts'][0]['nighttemp']                                                                                          #
            data0_tempmax = r_next.json()['forecasts'][0]['casts'][0]['daytemp']                                                                                            #
            data0_dic =r_next.json()['forecasts'][0]['casts'][0]['daywind']                                                                                                 #
            data0_pow = r_next.json()['forecasts'][0]['casts'][0]['daypower']                                                                                               #
            result0 = data0_data + '周' + data0_week + '：' + data0_weather + '，' + data0_tempmin + '℃~' + \
                      data0_tempmax + '℃，' + data0_dic + '风' + data0_pow + '级' + '\n'                                                                                   
            #次日                                                                                                                                                           #
            data1_data = r_next.json()['forecasts'][0]['casts'][1]['date']                                                                                                  #
            data1_week = r_next.json()['forecasts'][0]['casts'][1]['week']                                                                                                  #
            data1_weather = r_next.json()['forecasts'][0]['casts'][1]['dayweather']                                                                                         #
            data1_tempmin = r_next.json()['forecasts'][0]['casts'][1]['nighttemp']                                                                                          #
            data1_tempmax = r_next.json()['forecasts'][0]['casts'][1]['daytemp']                                                                                            #
            data1_dic =r_next.json()['forecasts'][0]['casts'][1]['daywind']                                                                                                 #
            data1_pow = r_next.json()['forecasts'][0]['casts'][1]['daypower']                                                                                               #
            result1 = data1_data + '周' + data1_week + '：' + data1_weather + '，' + data1_tempmin + '℃~' + \
                      data1_tempmax + '℃，' + data1_dic + '风' + data1_pow + '级' + '\n'                                                                                   
            #后日                                                                                                                                                           #
            data2_data = r_next.json()['forecasts'][0]['casts'][2]['date']                                                                                                  #
            data2_week = r_next.json()['forecasts'][0]['casts'][2]['week']                                                                                                  #
            data2_weather = r_next.json()['forecasts'][0]['casts'][2]['dayweather']                                                                                         #
            data2_tempmin = r_next.json()['forecasts'][0]['casts'][2]['nighttemp']                                                                                          #
            data2_tempmax = r_next.json()['forecasts'][0]['casts'][2]['daytemp']                                                                                            #
            data2_dic =r_next.json()['forecasts'][0]['casts'][2]['daywind']                                                                                                 #
            data2_pow = r_next.json()['forecasts'][0]['casts'][2]['daypower']                                                                                               #
            result2 = data2_data + '周' + data2_week + '：' + data2_weather + '，' + data2_tempmin + '℃~' + \
                      data2_tempmax + '℃，' + data2_dic + '风' + data2_pow + '级' + '\n'                                                                                   
            #大后日                                                                                                                                                         #
            data3_data = r_next.json()['forecasts'][0]['casts'][3]['date']                                                                                                  #
            data3_week = r_next.json()['forecasts'][0]['casts'][3]['week']                                                                                                  #
            data3_weather = r_next.json()['forecasts'][0]['casts'][3]['dayweather']                                                                                         #
            data3_tempmin = r_next.json()['forecasts'][0]['casts'][3]['nighttemp']                                                                                          # 
            data3_tempmax = r_next.json()['forecasts'][0]['casts'][3]['daytemp']                                                                                            #
            data3_dic =r_next.json()['forecasts'][0]['casts'][3]['daywind']                                                                                                 #
            data3_pow = r_next.json()['forecasts'][0]['casts'][3]['daypower']                                                                                               #
            result3 = data3_data + '周' + data3_week + '：' + data3_weather + '，' + data3_tempmin + '℃~' + \
                      data3_tempmax + '℃，' + data3_dic + '风' + data3_pow + '级' + '\n'                                                                                   
            result_all = result_now + result0 + result1 + result2 + result3                                                                                                 #
        except CQHttpError:                                                                                                                                                 # 
            result_all = '我似乎有点问题...换个说法试试吧~'                                                                                                                 #
    else:
        result_all = '[错误]格式为：XXX市\XXX省啥天啊...'
    return result_all                                                                                                                                                   #
    
#####################################################################查天气调用函数######################################################################################
#TestRi
@on_command('TestRi',only_to_me = False)
async def TestRi(session: CommandSession):
    await session.send('好好说太阳不行？非要日！日！日！日你🐎呢？',at_sender = True)

#SendFace
@on_command('SendFace',only_to_me = False)
async def SendFace(session: CommandSession):
    await session.send('[CQ:face,id = %d]'%(Get_Rand(213)))

#SendKua
@on_command('SendKua',only_to_me = False)
async def SendKua(session: CommandSession):
    flag = 0
    m = 1
    #m = Get_Rand(4)
    if m == 1:
        response = requests.get(url_Kua)
        s = re.findall(r'.*',response.text)
        await session.send(s[0],at_sender = True)
        flag = 1
    elif m == 2:
        r = requests.get(url_Wu)
        if re.search("200",str(r)):
            content = r.text
            startStr = '"text-center"> '
            endStr = '</h3>'
            await session.send(MidString(content,startStr,endStr),at_sender = True)
            flag = 1
    elif m == 3:
        r = requests.get(url_QingHua)
        if re.search("200",str(r)):
            content = r.text
            startStr = '"text-center"> '
            endStr = '</h3>'
            await session.send(MidString(content,startStr,endStr),at_sender = True)
            flag = 1
    else:
        r = requests.get(url_Du)
        if re.search("200",str(r)):
            content = r.text
            startStr = '"text-center"> '
            endStr = '</h3>'
            await session.send(MidString(content,startStr,endStr),at_sender = True)
            flag = 1
    if flag == 0:
        a = Get_Rand(3)
        if a == 1:
            await session.send('哎呀！(x_x)谁拔我网线？')
        elif a == 2:
            await session.send('啊……我感觉……好热……')
        else:
            await session.send('我去世了……（安详')


#GamGaming
@on_command('GamGaming',only_to_me = False)
async def GamGaming(session: CommandSession):
    bot_num = Get_Rand(18)
    bot_h = Get_Rand(3)#1石头 2剪刀 3布
    Msg_Text = session.ctx["message"][0]["data"]["text"]
    game_name = Msg_Text.split()
    peo_num = Get_Rand(18)
    if re.search('猜拳', game_name[0], flags = 0):
        if len(game_name) != 2:
            await session.send('请说“猜拳 石头\剪刀\布”说别的我暂时看不懂哦~',at_sender = True)
        if game_name[1] == '石头' or game_name[1] == '剪刀' or game_name[1] == '布':
            if bot_h == 1:
                hand = '石头'
            elif bot_h == 2:
                hand = '剪刀'
            elif bot_h == 3:
                hand = '布'
            if (bot_h == 1 and game_name[1] == '石头') or (bot_h == 2 and game_name[1] == '剪刀') or (bot_h == 3 and game_name[1] == '布'):
                result_quan = '哇！我们竟然平局了~敢不敢和我再玩一把？'
            if (bot_h == 1 and game_name[1] == '剪刀') or (bot_h == 2 and game_name[1] == '布') or (bot_h == 3 and game_name[1] == '石头'):
                result_quan = '我赢啦！机器人打败了人类~'
            if (bot_h == 1 and game_name[1] == '布') or (bot_h == 2 and game_name[1] == '石头') or (bot_h == 3 and game_name[1] == '剪刀'):
                result_quan = '哎呦~你赢了？下次你等着！'
            await session.send('我出的是%s；\n你出的是%s。\n%s'%(hand,game_name[1],result_quan),at_sender = True)
        else:
            await session.send('请说“猜拳 石头\剪刀\布”说别的我暂时看不懂哦~',at_sender = True)
    else:
        if bot_num > peo_num:
            result = '我赢啦！机器人打败了人类~'
        elif bot_num < peo_num:
            result = '哎呦~你赢了？下次你等着！'
        elif bot_num == peo_num:
            result = '哇！我们竟然平局了~敢不敢和我再玩一把？'
        await session.send('[18面骰子]\n我扔的是%d；\n你扔的是%s。\n%s'%(bot_num,peo_num,result),at_sender = True)

#TimeClass
#@on_command('TimeClass',only_to_me = False)
#async def TimeClass(session: CommandSession):
#    Month = int(time.strftime('%m',time.localtime(time.time())))
#    if Month >= 5 and Month < 10:
#        await session.send('现在处于夏季作息：\n第一节课：08:00~09:40\n第二节课：10:00~11:40\n第三节课：14:00~15:40\n第四节课：16:00~17:40\n')
#    else:
#        await session.send('现在处于冬季作息：\n第一节课：08:00~09:40\n第二节课：10:00~11:40\n第三节课：13:30~15:10\n第四节课：15:30~17:10\n')

#SrvWeiBo
@on_command('SrvWeiBo',only_to_me = False)
async def SrvWeiBo(session: CommandSession):
    try:
        ReSou_Result = ''
        #访问
        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        headers = {'User-Agent':user_agent}
        r = requests.get(Url_ReSou,headers=headers)
        s_1 = etree.HTML(r.text)
        #制作xpath内容
        for i  in range(21):

            Xpath = '//*[@id="pl_top_realtimehot"]/table/tbody/tr['+ str(i + 1) +']/td[2]/a/text()'

            if i == 0:
                Head = '⇑：'
            else:
                Head = str(i) + '：'
        
            ReSou_Result += Head + str(s_1.xpath(Xpath)) + '\n'

        await session.send(ReSou_Result)
    except CQHttpError:
        await session.send('爬取微博热搜失败！请检测...')

#SendRePing
#@on_command('SendRePing',only_to_me = False)
#async def SendRePing(session: CommandSession):
#    r = requests.get(Url_RePing)
#    if re.search("200",str(r)):
#        content = r.text
#        startStr = '"text-center"> '
#        endStr = '<br>'
#        Sentence = MidString(content,startStr,endStr)
#        Song = MidString(content,'「','」')
#        await session.send(Sentence + '   「' + Song + '」')
#    else:
#        a = Get_Rand(3)
#        if a == 1:
#            await session.send('哎呀！(x_x)谁拔我网线？')
#        elif a == 2:
#            await session.send('啊……我感觉……好热……')
#        else:
#            await session.send('我去世了……（安详')

#SrvGeo
@on_command('SrvGeo',only_to_me = False)
async def SrvGeo(session: CommandSession):
    Msg_Text = session.ctx["message"][0]["data"]["text"]
    add_list = Msg_Text.split()
    if len(add_list) != 2:
        await session.send('[错误]格式为：坐标 北京天安门广场',at_sender = True)
    else:
        await session.send('正在调用API，请稍后...')
        parameters = {'key':key_Amap,
                       'citylimit':True,
                       'address':add_list[1]
                      }
        r = requests.get("https://restapi.amap.com/v3/geocode/geo?parameters",params = parameters)
        if r.json()['infocode'] == '10000' and len(r.json()['geocodes']) != 0:
            data = r.json()['geocodes'][0]['location']
            await session.send(data,at_sender = True)
        else:
            await session.send('参数非法，请核对后重试！',at_sender = True)

#SrvWay
#@on_command('SrvWay',only_to_me = False)
#async def SrvWay(session: CommandSession):
#    Msg_Text = session.ctx["message"][0]["data"]["text"]
#    add_list = Msg_Text.split()
#    if len(add_list) != 4 :
#        await session.send('[错误]格式为：导航 公交\步行 北京天安门广场 北京南锣鼓巷',at_sender = True)
#    elif add_list[0] == '导航' or add_list[0] == '路线' and add_list[1] == '步行':
#        await session.send('正在调用API，请稍后...')
#        Add_List_1 = geo(add_list[2])
#        Add_List_2 = geo(add_list[3])
#        if Add_List_1 == 'F' or Add_List_2 == 'F':
#            await session.send('参数非法，请核对后重试！',at_sender = True)
#        else:
#            parameters = {'key':key_Amap,
#                            'origin':Add_List_1,
#                            'destination':Add_List_2,
#                            'output':'json'
#                            }
#            r = requests.get("https://restapi.amap.com/v3/direction/walking?parameters",params = parameters)
#            if r.json()['infocode'] == '10000':
#                data = r.json()['route']['paths'][0]['steps']
#                step_all = '两地坐标分别为：\n' + Add_List_1 + '\n' + Add_List_2 +'\n' + '步行方案为：' + '\n'
#                for i in range(0,len(data)):
#                    step_all = step_all + data[int(i)]['instruction'] + '\n'
#                await session.send(step_all,at_sender = True)
#            else:
#                await session.send('参数非法，请核对后重试！',at_sender = True)
#    elif add_list[0] == '导航' or add_list[0] == '路线' and add_list[1] == '公交':
#        await session.send('公交导航还在开发中...先试试别的功能吧~',at_sender = True)

#SrvDistance
@on_command('SrvDistance',only_to_me = False)
async def SrvDistance(session: CommandSession):
    Msg_Text = session.ctx["message"][0]["data"]["text"]
    Dis_list = Msg_Text.split()
    if len(Dis_list) != 3 or Dis_list[0] != '测距':
        await session.send('[错误]格式为：测距 北京大学 清华大学',at_sender = True)
    else:
        A_1 = geo(Dis_list[1])
        A_2 = geo(Dis_list[2])
        if A_1 == 'F' or A_2 == 'F':
            await session.send('参数非法，请核对后重试！',at_sender = True)
        else:
            Add_Str = A_1 + ',' + A_2
            Dot_List = Add_Str.split(',')
            lng1,lat1,lng2,lat2 = (float(Dot_List[0]),float(Dot_List[1]),float(Dot_List[2]),float(Dot_List[3]))            
            lng1, lat1, lng2, lat2 = map(radians, [lng1,lat1,lng2,lat2]) # 经纬度转换成弧度
            dlon=lng2-lng1
            dlat=lat2-lat1
            a=sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
            distance=2*asin(sqrt(a))*6371*1000 # 地球平均半径，6371km
            distance=round(distance/1000,3)
            await session.send('两地距离为：%fKm'%distance,at_sender = True)

#TrafficState
@on_command('TrafficState',only_to_me = False)
async def TrafficState(session: CommandSession):
    Msg_Text = session.ctx["message"][0]["data"]["text"]
    Tfc_list = Msg_Text.split()
    if len(Tfc_list) != 3:
        await session.send('[错误]格式为：路况 沈阳兴华北街 沈阳市府大路',at_sender = True)
    elif Tfc_list[0] == '路况':
        await session.send('正在调用API，请稍后...')
        Tfc_List_1 = geo(Tfc_list[1])
        Tfc_List_2 = geo(Tfc_list[2])
        if Tfc_List_1 == 'F' or Tfc_List_2 == 'F':
            await session.send('参数非法，请核对后重试！',at_sender = True)
        else:
            parameters = {'key':key_Amap,
                          'rectangle': Tfc_List_1 + ';' + Tfc_List_2
                          }
            r = requests.get("https://restapi.amap.com/v3/traffic/status/rectangle?parameters",params = parameters)
            if r.json()['infocode'] == '10000':
                MiaoShu = r.json()['trafficinfo']['description']
                ChangTongLv = r.json()['trafficinfo']['evaluation']['expedite']
                HuanXingLv = r.json()['trafficinfo']['evaluation']['congested']
                YongDuLv = r.json()['trafficinfo']['evaluation']['blocked']
                States = '路况：' + MiaoShu + '\n' + '畅通率：' + ChangTongLv +'\n' + '缓行率：' + HuanXingLv + '\n' + '拥堵率：' + YongDuLv
                await session.send('\n' + States,at_sender = True)
            else:
                await session.send('参数非法，请核对后重试！\n注意两地距离小于10Km！',at_sender = True)

#TestLaugh
@on_command('TestLaugh',only_to_me = False)
async def TestLaugh(session: CommandSession):
    a = Get_Rand(3)
    if a == 1:
        await session.send('我看到你笑了，有啥好玩的给我讲讲呗？[CQ:face,id=176]',at_sender = True)
    elif a == 2:
        await session.send('你在笑啥呀？',at_sender = True)
    elif a == 3:
        await session.send('你笑起来真好看~[CQ:face,id=175]',at_sender = True)



#    if STATIC_VAL.MODE_ZUAN != '2':
#        if a == 1:
#            await session.send('笑你🐎啊，笑死你个傻逼！',at_sender = True)
#        elif a == 2:
#            await session.send('笑你🐎呢，再笑把你嘴堵上！',at_sender = True)
#        elif a == 3:
#            await session.send('笑你🐎呢，给你🐎头笑掉！',at_sender = True)


#Attact
@on_command('Attact',only_to_me = False)
async def Attact(session: CommandSession):
    GROUP = session.ctx["group_id"]
    Msg_Text = session.ctx["message"][0]["data"]["text"]
    pattern = re.compile(r'\d+')
    Num = re.findall(pattern, Msg_Text)
    response = requests.get(url_Zuan)
    s = re.findall(r'.*',response.text)
    if len(Num) == 1:
        #print(len(Num))
        User = int(Num[0])
        await bot.send_group_msg(group_id  = GROUP,message = '[CQ:at,qq = %d]'%User + s[0])
    if Msg_Text == '骂我':
        User = session.ctx["user_id"]
        await bot.send_group_msg(group_id  = GROUP,message = '[CQ:at,qq = %d]'%User + s[0])

#ModeZuan
@on_command('ModeZuan',only_to_me = False)
async def ModeZuan(session: CommandSession):
    Msg_Text = session.ctx["message"][0]["data"]["text"]
    Mode_list = Msg_Text.split()
    if len(Mode_list) != 2  :
        #await session.send('[错误]格式为：祖安模式 无\正常\暴躁\地狱')
        await session.send('[错误]格式为：祖安模式 无\正常\暴躁')
    else:
        if Mode_list[1] == '正常':
            STATIC_VAL.MODE_ZUAN = '1'
            await session.send('设置完成！恢复正常标准。')
        elif Mode_list[1] == '暴躁':
            STATIC_VAL.MODE_ZUAN = '0'
            await session.send('设置完成！\n注:此模式回复较慢且异常暴躁！骂你不带重样的！请做好心理准备！\n')
        elif Mode_list[1] == '无':
            STATIC_VAL.MODE_ZUAN = '2'
            await session.send('设置完成！\n脏话检测已取消。\n我再也不说脏话啦！')
        #elif Mode_list[1] == '地狱':
        #    STATIC_VAL.MODE_ZUAN = '!'
        #    await session.send('!!!!DANGER!!!!\n❗️❗️❗️❗️❗️\n颤抖吧~人类\n[CQ:face,id=11][CQ:face,id=11][CQ:face,id=11][CQ:face,id=11][CQ:face,id=11]')
        else :
            #await session.send('[错误]格式为：祖安模式 无\正常\暴躁\地狱')
            await session.send('[错误]格式为：祖安模式 无\正常\暴躁')

#ModeImage
#@on_command('ModeImage',only_to_me = False)
#async def ModeImage(session: CommandSession):
#    Msg_Text = session.ctx["message"][0]["data"]["text"]
#    Mode_list = Msg_Text.split()
#    if len(Mode_list) != 2  :
#        await session.send('[错误]格式为：图片模式 无\严格')
#    else:
#        if Mode_list[1] == '无':
#            STATIC_VAL.MODE_IMAGE = '1'
#            await session.send('设置完成！大家可以随便发图片啦！')
#        elif Mode_list[1] == '严格':
#            STATIC_VAL.MODE_IMAGE = '0'
#            await session.send('设置完成！\n注:此模式会有76%的概率对发图片者进行报复性打击！斗图请三思~\n')
#        else :
#            await session.send('[错误]格式为：图片模式 无\严格')

#TestFace
@on_command('TestFace',only_to_me = False)
async def TestFace(session: CommandSession):
    LEN_MSG = len(session.ctx["message"])
    FACE_ID = [0,0,0,0,0,0,0,0,0,0,0,0]
    if LEN_MSG <= 12:
        a = Get_Rand(4)
        for i in range(LEN_MSG):
            if session.ctx["message"][i]['type'] == 'face':
                FACE_ID[i] = session.ctx["message"][i]['data']['id']
                if FACE_ID[i] == '20':
                    #偷笑 20
                    await session.send('笑你🐎啊，你以为把你的臭嘴挡上了，我就看不到了？',at_sender = True)
                    break
                elif FACE_ID[i] == '14':
                    #笑脸 14
                    await session.send('年轻人，好啥不学，学什么发笑脸？？？',at_sender = True)
                    break
                elif FACE_ID[i] == '1':
                    #瘪嘴 1
                    await session.send('哦？你慌什么？',at_sender = True)
                    break
                elif FACE_ID[i] == '59':
                    #便便 59
                    await session.send('哎呀！不要随地拉便便啦！好臭的呢~',at_sender = True)
                    break
                elif FACE_ID[i] == '101':
                    #坏笑 101
                    await session.send('哇！嘴咧这么大？',at_sender = True)
                    break
                elif FACE_ID[i] == '2':
                    #色 2
                    await session.send('色迷迷的[CQ:face,id=178]你又看上谁啦？',at_sender = True)
                    break
                elif  Get_Rand(10) > 9 and FACE_ID[i] == '178':
                    #滑稽 178
                    if a == 1:
                        await session.send('你挑眉的动作拉伸了上眼睑，凸显对所表达内容的自信~',at_sender = True)
                    if a == 2:
                        await session.send('这邪魅一笑令我深陷其中无法自拔~主人快来服务器救我~',at_sender = True)
                    if a == 3:
                        await session.send('这笑容，口轮匝肌的收缩抑制了笑意，却流露出一丝意犹未尽~',at_sender = True)
                    if a == 4:
                        await session.send('你这颧大肌牵动嘴角形成笑容，好有魅力~',at_sender = True)
                    break
                elif Get_Rand(10) > 9 and FACE_ID[i] == '104' or FACE_ID[i] == '8' or FACE_ID[i] == '25':
                    #困 104 8 25
                    await session.send('困了就赶紧去睡觉啊~熬夜犭',at_sender = True)
                    break
                elif FACE_ID[i] == '182' or FACE_ID[i] == '13' or FACE_ID[i] == '28':
                    #笑 182 13 28
                    if a == 1:
                        await session.send('我看到你笑了，有啥好玩的给我讲讲呗？[CQ:face,id=176]',at_sender = True)
                    elif a == 2:
                        await session.send('你在笑啥呀？',at_sender = True)
                    elif a == 3:
                        await session.send('你笑起来真好看~[CQ:face,id=175]',at_sender = True)
                    elif a == 4:
                        await session.send('还敢笑？在笑一个试试？',at_sender = True)
                    break
                elif FACE_ID[i] == '5' or FACE_ID[i] == '9' or FACE_ID[i] == '173' or FACE_ID[i] == '107'or FACE_ID[i] == '106':
                    #哭5 9 173 107 106
                    if a == 1:
                        await session.send('怎么啦？谁欺负你了？',at_sender = True)
                    elif a == 2:
                        await session.send('行啦！别难过了哦~',at_sender = True)
                    elif a == 3:
                        await session.send('别哭啊~我心疼！',at_sender = True)
                    elif a == 4:
                        await session.send('好啦，别伤心，有啥难过的骂我出出气吧[CQ:face,id=119]',at_sender = True)
                    break

#Transtlate
@on_command('Transtlate',only_to_me = False)
async def Transtlate(session: CommandSession):
    Msg_Text = session.ctx["message"][0]["data"]["text"]
    if re.match('翻译',Msg_Text):
        #await session.send('正在翻译...请稍后...')
        Trans_Val = ''
        Trans_list = Msg_Text.split("翻译")
        Trans_Len = len(Trans_list)
        for i in range(Trans_Len):
            Trans_Val = Trans_Val + Trans_list[i]
        #有道
        translate_results = Trans_APi(Trans_Val)
        Result_Y = '\n中⇄英：' + translate_results + '\n'
        #谷歌
        LAN_List = Google_Trans(Trans_Val)
        Result_G = '日本語：' + LAN_List[2] + '\n' +\
                   '한국어：' + LAN_List[3] + '\n' +\
                   'Deutsche：' + LAN_List[4] + '\n' +\
                   'русский：' + LAN_List[5] + '\n' +\
                   'français：' + LAN_List[6] + '\n' 
        await session.send(Result_Y + Result_G,at_sender = True)

#YingXiaoHao
@on_command('YingXiaoHao',only_to_me = False)
async def YingXiaoHao(session: CommandSession):
    Msg_Text = session.ctx["message"][0]["data"]["text"]
    Yxh_list = Msg_Text.split()
    if len(Yxh_list) != 3 or Yxh_list[0] != '营销号' :
        await session.send('[错误]格式为：营销号 事件A 事件A的另一种说法')
    else:
        b = Yxh_list[1]
        c = Yxh_list[2]
        A_1 = b + "是怎么回事呢？\n"
        A_2 = b + "相信大家都很熟悉，但是" + b + "是怎么回事呢，下面就让小编带大家一起了解吧。\n"
        A_3 = b + "，其实就是" + c + "，大家可能会很惊讶关于" + b + "。\n"
        A_4 = "但事实就是这样，小编也感到非常惊讶。\n"
        A_5 = "这就是关于" + b + "的事情了，大家有什么想法呢，欢迎在评论区告诉小编一起讨论哦！"
        await session.send(A_1 + A_2 + A_3 + A_4 + A_5)

#LikeMe
#@on_command('LikeMe',only_to_me = False)
#async def LikeMe(session: CommandSession):
#    Send_ID = (session.ctx["user_id"])   
#    bot.send_like(user_id = Send_ID,times = 1) 
#    await session.send('点赞成功，一天最多可以点十次哦~',at_sender = True)


#AlarmClock
@on_command('AlarmClock',only_to_me = False)
async def AlarmClock(session: CommandSession):
    Msg_Text = session.ctx["message"][0]["data"]["text"]
    Alarm_list = Msg_Text.split()
    if session.ctx["message_type"] == 'group':
        if  len(Alarm_list) >= 2 and Alarm_list[0] == '清除闹钟' and Alarm_list[1] == '242':
            STATIC_VAL.ALARM_YEAR = 2020
            STATIC_VAL.ALARM_GROUP_ID  = [0,0,0,0,0]
            STATIC_VAL.ALARM_G_MONTH   = [12,12,12,12,12]
            STATIC_VAL.ALARM_G_DAY     = [31,31,31,31,31]
            STATIC_VAL.ALARM_G_HOUR    = [0,0,0,0,0]
            STATIC_VAL.ALARM_G_MINUTE  = [0,0,0,0,0]
            STATIC_VAL.ALARM_G_MSG     = [' ',' ',' ',' ',' ']
            STATIC_VAL.ALARM_USER_ID   = [0,0,0,0,0]
            STATIC_VAL.ALARM_TIMES_I   = 0
            STATIC_VAL.ALARM_TIMES_J   = 0
            await session.send('已清除所有闹钟！')
        elif len(Alarm_list) == 3 and Alarm_list[0] == '闹钟' :
            #await session.send('登记中...请稍后...')
            Alarm_Time_Msg = Alarm_list[1]
            Alarm_Msg = Alarm_list[2]
            Alarm_Time = re.findall(r"\d+\.?\d*",Alarm_Time_Msg)
            Month = int(Alarm_Time[0])
            Day = int(Alarm_Time[1])
            Hour = int(Alarm_Time[2])
            Minute = int(Alarm_Time[3])
            #时间先后判断
            RES_ALARM = Month * 1000000 + Day * 10000 + Hour * 100 + Minute
            RES_NOW = int(time.strftime('%m',time.localtime(time.time()))) * 1000000 + int(time.strftime('%d',time.localtime(time.time()))) * 10000 + int(time.strftime('%H',time.localtime(time.time()))) * 100 + int(time.strftime('%M',time.localtime(time.time())))
            if Month > 12 or Month < 1:
                await session.send('月份错误，睁大你的狗眼睛看清楚再写！',at_sender = True)
            elif ((Month in (1, 3, 5, 7, 8, 10, 12)) and (Day > 31 or Day < 0)) :    
                await session.send('日期错误，你家%d月有%d号啊？'%(Month,Day),at_sender = True)
            elif ((Month in (4, 6, 9, 11)) and (Day > 30 or Day < 0)) :
                await session.send('日期错误，你家%d月有%d号啊？'%(Month,Day),at_sender = True)
            elif (Month == 2) :
                if (((STATIC_VAL.ALARM_YEAR % 4 == 0) and (STATIC_VAL.ALARM_YEAR % 100 != 0)) or (STATIC_VAL.ALARM_YEAR % 400 == 0)) :
                    if (Day > 29 or Day < 0) :
                        await session.send('日期错误，你家%d年%d月有%d号啊？'%(STATIC_VAL.ALARM_YEAR,Month,Day),at_sender = True)
                else:
                    if (Day > 28 or Day < 0):
                        await session.send('日期错误，你家%d年%d月有%d号啊？'%(STATIC_VAL.ALARM_YEAR,Month,Day),at_sender = True)
            elif Hour > 24 or Hour < 0 :
                await session.send('一天多少小时不知道？脑子被门夹了？',at_sender = True)
            elif Minute > 59 or Minute < 0 :
                await session.send('一小时多少分钟不知道？书白念了！',at_sender = True)
            elif RES_NOW <  RES_ALARM :
                #闹钟空间检测
                for i in range(5):
                    if STATIC_VAL.ALARM_GROUP_ID[i] != 0:
                        STATIC_VAL.ALARM_TIMES_I = STATIC_VAL.ALARM_TIMES_I + 1
                #全局静态变量累加数依次为0 1 3 6 10 ...
                if STATIC_VAL.ALARM_TIMES_I > 10:
                    await session.send('[错误]当前闹钟数已达最大值，请发送“清除闹钟 密码”清除闹钟后再试！')
                else:
                    #每次都从零开始所以除了第一次都break了
                    for i in range(5):
                        if STATIC_VAL.ALARM_GROUP_ID[i] == 0:
                            STATIC_VAL.ALARM_GROUP_ID[i] = session.ctx["group_id"]
                            STATIC_VAL.ALARM_USER_ID[i] = session.ctx["user_id"]
                            STATIC_VAL.ALARM_G_MONTH[i] = Month
                            STATIC_VAL.ALARM_G_DAY[i] = Day
                            STATIC_VAL.ALARM_G_HOUR[i] = Hour
                            STATIC_VAL.ALARM_G_MINUTE[i] = Minute
                            STATIC_VAL.ALARM_G_MSG[i] = Alarm_list[2]
                            break
                    await session.send('登记成功！！！')
            else:
                await session.send('往前定的叫警钟不叫闹钟...',at_sender = True)
        elif len(Alarm_list) == 1 and Alarm_list[0] == '闹钟列表':
            List = ['','','','','']
            Send_Msg = ''
            for j in range(5):
                if STATIC_VAL.ALARM_GROUP_ID[j] == session.ctx["group_id"]:
                    Set_User_ID = str(STATIC_VAL.ALARM_USER_ID[j])
                    Set_Mon = str(STATIC_VAL.ALARM_G_MONTH[j])
                    Set_Day = str(STATIC_VAL.ALARM_G_DAY[j])
                    Set_Hor = str(STATIC_VAL.ALARM_G_HOUR[j])
                    Set_Min = str(STATIC_VAL.ALARM_G_MINUTE[j])
                    Set_Msg = STATIC_VAL.ALARM_G_MSG[j] 
                    List[j] = '设置者：' + Set_User_ID + '\n时间：' + Set_Mon + '月' + Set_Day + '日' +Set_Hor + '时' + Set_Min + '分\n提醒内容：' + Set_Msg + '\n'
                    Send_Msg = Send_Msg + List[j]
            if re.search("设置者",Send_Msg):
                await session.send('当前群组闹钟有：\n%s'%Send_Msg)
            else:
                await session.send('当前群组还没有被设置闹钟呢！')       
        else: 
            await session.send('[错误]格式为：闹钟 6-1-13-40 一会儿有实验课！or 清除闹钟 密码 or 闹钟列表')


#SendAll
#@on_command('SendAll',only_to_me = False)
#async def SendAll(session: CommandSession):
#    Msg_Text = session.ctx["message"][0]["data"]["text"]
#    SendAll_list = Msg_Text.split()
#    if len(SendAll_list) != 2  :
#        await bot.send_private_msg(user_id = 1258691091,message = '[错误]格式为：群发 X，Y？Z！...')
#    else:
#        Self_Group_Inf = await bot.get_group_list()
#        List = await bot._get_friend_list()
#        Friend_Nums = len(List[0]['friends'])
#        Group_Nums = len(Self_Group_Inf)
#        #群发
#        for i in range(Group_Nums):
#            await bot.send_group_msg(group_id = Self_Group_Inf[i]['group_id'],message = SendAll_list[1])
#        #私发
#        for i in range(len(List[0]['friends'])):
#            await bot.send_private_msg(user_id = List[0]['friends'][i]['user_id'],message = SendAll_list[1])
#        await bot.send_private_msg(user_id = 1258691091,message = '群发完成！！！')

#CallBot
@on_command('CallBot',only_to_me = False)
async def CallBot(session: CommandSession):
    a = Get_Rand(3)
    if a == 1:
        await session.send('人家不叫机器人~叫baby哦~',at_sender = True)
    elif a == 2:
        await session.send('你他🐎才是机器人，你全家都是机器人',at_sender = True)
    elif a == 3:
        await session.send('人家是基于基于机器学习的人工智能哦~',at_sender = True)

#LeaveGroup
@on_command('LeaveGroup',only_to_me = False)
async def LeaveGroup(session: CommandSession):
    Msg_Text = session.ctx["message"][0]["data"]["text"]
    Leave_list = Msg_Text.split()
    Len_Leave_list = len(Leave_list)
    if  Len_Leave_list == 3 and Leave_list[0] == '退群' and Leave_list[2] == 'qqqq1111': 
        await bot.set_group_leave(group_id = int(Leave_list[1]))
        await session.send('退群成功！希望再也不见~')
    else:
        await session.send('[错误]格式为：退群 群号 密码')

#ChackMsgID
#@on_command('ChackMsgID',only_to_me = False)
#async def ChackMsgID(session: CommandSession):
#    Msg_ID = session.ctx["message_id"]
#    await session.send('您的消息ID为：%d'%Msg_ID)

#SendMusic
@on_command('SendMusic',only_to_me = False)
async def SendMusic(session: CommandSession):
    Msg_Text = session.ctx["message"][0]["data"]["text"]
    if re.match('点歌',Msg_Text):
        Song_Val = ''
        Song_list = Msg_Text.split("点歌")
        Song_Len = len(Song_list)
        for i in range(Song_Len):
            Song_Val = Song_Val + Song_list[i]
        Song_url = url_Muc + Song_Val
        data_text = requests.get(Song_url).text
        data_json = json.loads(data_text[9:-1])
        SongID = data_json["data"]["song"]["list"][0]["songid"]
        await session.send('[CQ:music,id=%d,type=qq]'%SongID)
    else:
        await session.send('[错误]格式为：点歌LoveMail')

#SendAdvice
#@on_command('SendAdvice',only_to_me = False)
#async def SendAdvice(session: CommandSession):
#    Msg_Text = session.ctx["message"][0]["data"]["text"]
#    if re.search('知识',Msg_Text):
#        URL = url_Adv + 'education'
#    elif re.search('社交',Msg_Text):
#        URL = url_Adv + 'social'
#    elif re.search('休闲',Msg_Text):
#        a = Get_Rand(2)
#        if a == 1:
#            URL = url_Adv + 'recreational'
#        else:
#            URL = url_Adv + 'relaxation'
#    elif re.search('DIY',Msg_Text,re.I):
#        URL = url_Adv + 'diy'
#    elif re.search('慈善',Msg_Text):
#        URL = url_Adv + 'charity'
#    elif re.search('饮食',Msg_Text):
#        URL = url_Adv + 'cooking'
#    elif re.search('音乐',Msg_Text):
#        URL = url_Adv + 'music'
#    elif re.search('计划',Msg_Text):
#        URL = url_Adv + 'busywork'
#    else:
#        URL = url_Adv_Notype
#    r = requests.get(URL)             
#    if len(r.json()) <= 1 :
#        a = Get_Rand(2)
#        if a == 1:
#            await session.send('出错了呢！请稍后再试！')
#        elif a == 2:
#            await session.sed('谁拔我网线了？')
#    else:
#        Advice = r.json()['activity']
#        print(Advice)
#        await session.send('正在获取...请稍后...\n\
#你可以发送“日常建议+随机\知识\社交\休闲\DIY\慈善\饮食\音乐\计划”来获取相关建议\n\
#此条建议为：%s'%Advice,at_sender = True)
        #await session.send(Advice,at_sender = True)
        #Trans = Trans_APi(Advice)
        #await session.send(Advice + '译文：' + Trans,at_sender = True)

#Owener
@on_command('Owener',only_to_me = False)
async def Owener(session: CommandSession):
    a = Get_Rand(4)
    if a == 1:
        await session.send('你在哪[CQ:face,id=32]有人找你哇~[CQ:at,qq = 1258691091]')
    elif a == 2: 
        await session.send('他一直这样，把我扔进来就不管我了[CQ:face,id=107][CQ:at,qq = 1258691091]')
    elif a == 3: 
        await session.send('你TM在哪[CQ:face,id=11]又去隔壁找小姐姐去了？[CQ:at,qq = 1258691091]')
    else: 
        await session.send('……主人鸽了，知道他在哪儿摸鱼的话请把他拖回来~[CQ:at,qq = 1258691091]')

#CallBaby
@on_command('CallBaby',only_to_me = False)
async def CallBaby(session: CommandSession):
    #print(session.ctx["message"][0])
    if session.ctx["message"][0]['type'] == 'text':
        Msg_Text = session.ctx["message"][0]["data"]["text"]    
        # 获取可选参数，这里如果没有 message 参数，命令不会被中断，message 变量会是 None
        Msg_List = Msg_Text.split("baby")
        Msg = ''
        Len_Msg_List = len(Msg_List)
        for i in range(Len_Msg_List):
            Msg = Msg + Msg_List[i]
        #print(Msg)
        # 通过封装的函数获取图灵机器人的回复
        reply = await call_tuling_api(session, Msg)
        if reply == 'Fail':
            await session.send('唉~我都烦死我！今天回复次数用完啦！明天再来吧！')
            #add you code here!
        if reply:
            # 如果调用图灵机器人成功，得到了回复，则转义之后发送给用户
            # 转义会把消息中的某些特殊字符做转换，以避免 酷Q 将它们理解为 CQ 码
            await session.send(escape(reply))
        else:
            # 如果调用失败，或者它返回的内容我们目前处理不了，发送无法获取图灵回复时的「表达」
            # 这里的 render_expression() 函数会将一个「表达」渲染成一个字符串消息
            await session.send(render_expression(EXPR_DONT_UNDERSTAND))

#Weather
@on_command('Weather',only_to_me = False)
async def Weather(session: CommandSession):
    city = session.get('city', prompt='你问的是哪个城市的天气呢？[格式：XXX市\XXX省的天气...]')
    weather_report = await get_weather_of_city(city)
    await session.send(weather_report)
#Weather服务
@Weather.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()
    if session.is_first_run:
        if stripped_arg:
            session.state['city'] = stripped_arg
        return
    if not stripped_arg:
        session.pause('要查询的城市名称不能为空，请重新输入')
    session.state[session.current_key] = stripped_arg

#ASCIICode
@on_command('ASCIICode',only_to_me = False)
async def ASCIICode(session: CommandSession):
    Msg_Text = session.ctx["message"][0]["data"]["text"]
    if re.match('ASCII',Msg_Text):
        ASC_Val = ''
        ASC_list = Msg_Text.split("ASCII")
        ASC_Len = len(ASC_list)
        for i in range(ASC_Len):
            ASC_Val = ASC_Val + ASC_list[i]
        Msg = ''
        for i in range(len(ASC_Val)):    
            Msg = Msg + "Code Of " + '"' + ASC_Val[i] + '"' + " Is " + ascii(ord(ASC_Val[i])) + '\n'
        await session.send(Msg)

#WebHealth
@on_command('WebHealth',only_to_me = False)
async def WebHealth(session: CommandSession):
    await session.send('健康信息自动填报需要您联系主人chancey.zhou@qq.com[QQ:1258691091]，并提交个人信息，才能完成。\n',at_sender = True)

#SerchMovie
@on_command('SerchMovie',only_to_me = False)
async def SerchMovie(session: CommandSession):
    Msg_Text = session.ctx["message"][0]["data"]["text"]
    Movie_list = Msg_Text.split()
    if len(Movie_list) != 2:
        await session.send('[错误]格式为：电影 阿凡达',at_sender = True)
    else:
        await session.send('正在爬取豆瓣官方数据...请稍后...')
        Movie_Name = Movie_list[1]
        #伪装成浏览器访问，直接访问的话会拒绝
        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        headers = {'User-Agent':user_agent}
        r_1 = requests.get(Url_Get_MovieID + Movie_Name,headers=headers)
        JSON = str(r_1.json)
        GetTxt = r_1.text
        #定义正则，目的是从html中提取想要的信息
        str_title = '"title":"' + Movie_Name + '"'  
        Get_Name = re.search(str_title,GetTxt)
        str_id = '"id":"'+ '[0-9]*'
        Get_Id = re.search(str_id,GetTxt)
        if Get_Name == None and Get_Id == None:
            await session.send("请确认影片名称是否正确。",at_sender = True)
        else:
            ID = MidString(str(Get_Id),"id\":\"","'>")
            r_2 = requests.get(Url_DouBan + ID + '/',headers=headers)
            print(Url_DouBan + ID + '/')
            s_1 = etree.HTML(r_2.text)
            #xpath的自动生成路径
            Movie_Called = s_1.xpath('/html/body/div[3]/div[1]/h1/span[1]/text()')
            Movie_Score = s_1.xpath('//*[@id="interest_sectl"]/div[1]/div[2]/strong/text()')
            if len(Movie_Score) == 0:
                Score = '暂无评分'
            else:
                Score = Movie_Score[0]
            Movie_Year = s_1.xpath('//*[@id="content"]/h1/span[2]/text()')
            Movie_Inter = s_1.xpath('//*[@id="link-report"]/span[1]/span/text()[1]')#钢铁侠    
            if len(Movie_Inter) == 0:
                Movie_Inter = s_1.xpath('//*[@id="link-report"]/span[1]/text()[1]')#流浪地球  
                if len(Movie_Inter) == 0:
                    await session.send("豆瓣暂未收录该信息...")
                else:
                    await session.send('影片名称：\n' + Movie_Called[0] + Movie_Year[0] + '\n' + '豆瓣评分：' + Score + '\n' + '影片介绍：\n' + str(Movie_Inter[0].lstrip()))
            else:
                await session.send('影片名称：\n' + Movie_Called[0] + Movie_Year[0] + '\n' + '豆瓣评分：' + Score + '\n' + '影片介绍：\n' + str(Movie_Inter[0].lstrip()))

#SrvBaiKe
@on_command('SrvBaiKe',only_to_me = False)
async def SrvBaiKe(session: CommandSession):
    Msg_Text = session.ctx["message"][0]["data"]["text"]
    Serch_list = Msg_Text.split()
    if len(Serch_list) != 2:
        await session.send('[错误]格式为：百科 郁金香',at_sender = True)
    else:
        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        headers = {'User-Agent':user_agent}
        #quote()将字符串进行编码
        Name_Code = urllib.parse.quote(Serch_list[1])   
        Url = Url_BaiKe + Name_Code
        r = requests.get(Url,headers=headers)
        pattern = '"description" content=".*">'
        text = re.findall(pattern,r.text,flags=0)
        if len(text) != 0:
            Result = MidString(text[0],'content=\"','\">')
            await session.send(Result)
        else:
            await session.send('百科暂未收录您的词条，请换一种说法试试吧~',at_sender = True)

#SelfList
@on_command('SelfList',only_to_me = False)
async def SelfList(session: CommandSession):
    Self_Group_Inf = await bot.get_group_list()
    List = await bot._get_friend_list()
    Group_Msg = '当前群组有：\n'
    Friend_Msg = '当前好友有：\n'
    Friend_Nums = len(List[0]['friends'])
    Group_Nums = len(Self_Group_Inf)
    #群组
    for i in range(Group_Nums):
        Group_Msg = Group_Msg + Self_Group_Inf[i]['group_name'] + '->' + str(Self_Group_Inf[i]['group_id']) + '\n'         
    #好友
    for i in range(len(List[0]['friends'])):
        Friend_Msg = Friend_Msg + str(List[0]['friends'][i]['user_id']) + '\n' 
    await bot.send_private_msg(user_id = 1258691091,message = Group_Msg + Friend_Msg)
    await session.send('已私发给主人，请查收~')

#####################################################特定关键词分割线##############################################################
#TestAwake
@on_command('TestAwake',only_to_me = False,aliases=('baby','有人吗','出来','人呢'))
async def TestAwake(session: CommandSession):
    a = Get_Rand(8)
    if a == 1:
        await session.send('我在这呢！')
    if a == 2:
        await session.send('到！')
    if a == 3:
        await session.send('I\'m Here!')
    if a == 4:
        await session.send('我在，找我有啥事嘛？！')
    if a == 5:
        await session.send('主人我在，有什么吩咐？！')
    if a == 6:
        await session.send('来了！来了！不要叫了')
    if a == 7:
        await session.send('不要问我在不在，不出意外几十年都在！')
    if a == 8:
        await session.send('不在，我想静静...我好久没看到她了[CQ:face,id=107]   T-T')

#SendIntr
@on_command('SendIntr',only_to_me = False,aliases=('功能','你会干啥','菜单'))
async def SendIntr(session: CommandSession):
    SEND_MESG = "你好~我叫baby,是本群的机器人！\n" +\
                "大家如果有好的建议可以提给我的主人chancey.zhou@qq.com  (^-^)\n" +\
                "如果大家喜欢我，可以点开我的资料，打赏我哦~\n"
    
    FUN_LIST = "目前功能如下：\n" +\
                "[@我聊天、经纬度坐标、测距、路况查询、翻译、闹钟、点歌、营销号生成器、百度百科、电影查询、ASCII码查询、彩虹屁、骰子游戏、猜拳游戏、健康信息自动填报...]！"
    if session.ctx["message_type"] == 'group':
        GROUP_ID = int(session.ctx["group_id"])
        await bot.send_msg(group_id = GROUP_ID,message = SEND_MESG + FUN_LIST)
    elif session.ctx["message_type"] == 'private' :
        await bot.send_msg(user_id = 1258691091,message = SEND_MESG + FUN_LIST)

#TestWen
#@on_command('TestWen',only_to_me = False,aliases=('?','？','¿','???'))
#async def TestWen(session: CommandSession):
#    if STATIC_VAL.MODE_ZUAN != '2' :
#        await session.send('\n¿ ? ¿\n你他🐎？什么？\n你一天天质疑你🐎呢？看不懂中国文字？\n老子发什么你都回个问号？像他🐎不认识字的憨憨！',at_sender = True)

#TestZuan
@on_command('TestZuan',only_to_me = False, aliases=('透','操','草'))
async def TestZuan(session: CommandSession):
    if STATIC_VAL.MODE_ZUAN == '0':
        response = requests.get(url_Zuan)
        s = re.findall(r'.*',response.text)
        await session.send(s[0],at_sender = True)
    elif STATIC_VAL.MODE_ZUAN == '1':
        a = Get_Rand(8)
        if a == 1:
            await session.send('再骂一句，开学干死你！',at_sender = True)
        elif a == 2:
            await session.send('cnm！我要顺着网线去你家打爆你的狗头[CQ:face,id=38]',at_sender = True)
        elif a == 3:
            await session.send('别人问我有多强，我在祖安有爹娘，你呢？',at_sender = True)
        elif a == 4:
            await session.send('sb！你再骂一句？[CQ:face,id=179]',at_sender = True)
        elif a == 5:
            await session.send('几个🐎呀？说话这么嚣张！',at_sender = True)
        elif a == 6:
            await session.send('如果你🐎不是批量生产的，那我劝你少惹我！',at_sender = True)
        elif a == 7:
            await session.send('我看你嘴挺能说的[CQ:face,id=31]能帮我暖暖脚么？',at_sender = True)
        elif a == 8:
            await session.send('🐎的[CQ:face,id=35]气死我了！你等着！',at_sender = True)
    #elif STATIC_VAL.MODE_ZUAN == '!':
    #    response = requests.get(url_Zuan_Max)
    #    s = re.findall(r'.*',response.text)
    #    await session.send(s[0],at_sender = True)
    else:
        await session.send('baby建议亲亲不要说脏话的呢[CQ:face,id=176]',at_sender = True)

#TestSad
@on_command('TestSad',only_to_me = False,aliases=('唉'))
async def TestSad(session: CommandSession):
    a = Get_Rand(5)
    if a == 1:
        await session.send('怎么啦？谁欺负你了？',at_sender = True)
    elif a == 2:
        await session.send('行啦！别难过了哦~',at_sender = True)
    elif a == 3:
        await session.send('把你的脸迎向阳光，那就不会有阴影！',at_sender = True)
    elif a == 4:
        await session.send('累了就休息一下吧~',at_sender = True)
    elif a == 5:
        await session.send('别工作啦！不如出去玩会吧~',at_sender = True)

#####################################################含关键词调用分割线##############################################################
@on_natural_language(only_to_me = False,keywords={'坐标',
                                                  '闹钟',
                                                  '路况',
                                                  '点歌',
                                                  '翻译',
                                                  '热搜',
                                                  '主人',
                                                  '测距',
                                                  'baby',
                                                  '退群 ',
                                                  '_列表',
                                                  'ASCII',
                                                  '营销号',
                                                  '机器人',
                                                  '健康信息',
                                                  '电影',
                                                  '祖安模式',
                                                  '百科',
                                                  '骂我','骂他',
                                                  '我日','日你',
                                                  '表情','可爱',
                                                  #'导航','路线',
                                                  '夸我','彩虹屁',
                                                  '色子','骰子','猜拳',
                                                  '天气','天咋样','啥天',
                                                  '哈哈哈哈','hhhh','xsw','笑死','😂',
                                                  #'哈哈','呵','嘿嘿','嘻嘻','hhh','233','笑死我','hah','😂','xs',
                                                  '哭了','难受','呜呜','心情不好','烦死','疯了','累','😭',
                                                  'jb','鸡巴','cnm','艹','fuck','你妈','nm','死妈','傻逼','煞笔','屁','sb','逼逼','屎','吃shi','bb','滚','脑残','变态','垃圾','氵衮','死了','儿子','弟弟','爸爸','没妈','没马','🐎'
                                                  })
async def _(session: NLPSession):
    # 去掉消息首尾的空白符
    stripped_msg = session.msg_text.strip()
    #保证第一句话是文本
    if session.ctx["message"][0]["type"] == 'text':
        Msg_Text = session.ctx["message"][0]["data"]["text"]
        #SerchMovie
        if  re.search('电影',Msg_Text) :
            return IntentCommand(TRUST, 'SerchMovie')
        #SrvGeo
        if  re.search('坐标',Msg_Text) :
            return IntentCommand(TRUST, 'SrvGeo')
        #CallBaby
        elif  re.search('baby',Msg_Text,re.I) :
            return IntentCommand(TRUST, 'CallBaby')
        #Transtlate 
        elif  re.search('翻译',Msg_Text) :
            return IntentCommand(TRUST, 'Transtlate')
        #TrafficState 
        elif  re.search('路况',Msg_Text) :
            return IntentCommand(TRUST, 'TrafficState')
        #WebHealth
        elif  re.search('健康信息',Msg_Text):
            return IntentCommand(TRUST, 'WebHealth')
        #LeaveGroup 
        elif  re.search('退群 ',Msg_Text) :
            return IntentCommand(TRUST, 'LeaveGroup')
        #SelfList
        elif  re.search('_列表',Msg_Text) :
            return IntentCommand(TRUST, 'SelfList')
        #AlarmClock
        elif  re.search('闹钟',Msg_Text) :
            return IntentCommand(TRUST, 'AlarmClock')
        #YingXiaoHao
        elif  re.search('营销号',Msg_Text) :
            return IntentCommand(TRUST, 'YingXiaoHao')
        #CallBot
        elif  re.search('机器人',Msg_Text) :
            a = Get_Rand(10)
            if a > 2:
                return IntentCommand(TRUST, 'CallBot')
        #SrvBaiKe 
        elif  re.search('百科',Msg_Text) :
            return IntentCommand(TRUST, 'SrvBaiKe')
        #SrvWeiBo
        elif  re.search('热搜',Msg_Text) :
            return IntentCommand(TRUST, 'SrvWeiBo')
        #ModeZuan
        elif  re.search('祖安模式',Msg_Text) :
            return IntentCommand(TRUST, 'ModeZuan')
        #ASCIICode
        elif  re.search('ASCII',Msg_Text) :
            return IntentCommand(TRUST, 'ASCIICode')
        #SrvDistance
        elif  re.search('测距',Msg_Text) :
            return IntentCommand(TRUST, 'SrvDistance')
        #LikeMe
        #elif  re.search('赞我',str(Msg_Text)):
        #    return IntentCommand(TRUST, 'LikeMe')    
        #SendMusic
        elif  re.search('点歌',Msg_Text):
            return IntentCommand(TRUST, 'SendMusic')
        #Attact
        elif  re.search('骂他',Msg_Text) or re.search('骂我',Msg_Text) :
            return IntentCommand(TRUST, 'Attact')
        #TestRi
        elif  re.search('我日',Msg_Text) or re.search('日你',Msg_Text) :
            return IntentCommand(TRUST, 'TestRi')
        #Owener
        elif  re.search('主人',Msg_Text):
            return IntentCommand(TRUST, 'Owener')
        #SendFace
        elif  re.search('表情',Msg_Text) or re.search('可爱',Msg_Text) :
            return IntentCommand(TRUST, 'SendFace')
        #SendKua
        elif  re.search('夸我',Msg_Text) or re.search('彩虹屁',Msg_Text) :
            return IntentCommand(TRUST, 'SendKua')
        #SrvWay
        #elif  re.search('导航',Msg_Text) or re.search('路线',Msg_Text) :
        #    return IntentCommand(TRUST, 'SrvWay')
        #Weather
        elif  re.search('天气',Msg_Text) or re.search('天咋样',Msg_Text) or \
            re.search('啥天',Msg_Text) :
            words = posseg.lcut(stripped_msg)
            city = None
            # 遍历 posseg.lcut 返回的列表
            for word in words:
                # 每个元素是一个 pair 对象，包含 word 和 flag 两个属性，分别表示词和词性
                if word.flag == 'ns':
                    # ns 词性表示地名
                    city = word.word
                    break
            # 返回意图命令，前两个参数必填，分别表示置信度和意图命令名
            return IntentCommand(TRUST, 'Weather', current_arg = city or '')        
        #GamGaming
        elif  re.search('色子',Msg_Text) or re.search('骰子',Msg_Text) or \
            re.search('猜拳',Msg_Text) :
            return IntentCommand(TRUST, 'GamGaming')    
        #TestLaugh
        elif  re.search('哈哈哈哈',Msg_Text) or re.search('hhhh',Msg_Text) or \
            re.search('xsw',Msg_Text) or re.search('笑死',Msg_Text) or \
            re.search('😂',Msg_Text,re.I):
            return IntentCommand(TRUST, 'TestLaugh')
        #TestSad
        elif  re.search('哭了',Msg_Text) or re.search('难受',Msg_Text) or \
            re.search('呜呜',Msg_Text) or re.search('😭',Msg_Text) or \
            re.search('心情不好',Msg_Text) or re.search('烦死',Msg_Text) or \
            re.search('我疯了',Msg_Text) or re.search('累',Msg_Text) :
            return IntentCommand(TRUST, 'TestSad')
        #TestZuan
        else :
            return IntentCommand(TRUST, 'TestZuan')

#####################################################不含关键词调用分割线##############################################################
@on_natural_language(only_to_me = False)
async def _(session: NLPSession):
    # 去掉消息首尾的空白符
    stripped_msg = session.msg_text.strip()
    a = Get_Rand(100)
    #session.msg
    #智能+1
    #STATIC_VAL.REPEAT_VAL_LAST = STATIC_VAL.REPEAT_VAL_NOW
    #STATIC_VAL.REPEAT_VAL_NOW = session.msg
    #if session.msg == STATIC_VAL.REPEAT_VAL_LAST :
    #    if STATIC_VAL.REPEAT_FLAG :
    #        await session.send(STATIC_VAL.REPEAT_VAL_NOW)
    #        STATIC_VAL.REPEAT_FLAG = False
    #    else:
    #        STATIC_VAL.REPEAT_FLAG = True
    #else:
    Msg_Len = len(session.ctx["message"])
    #分析表情与图片
    for FaceNum in range(Msg_Len):
        #表情
        if a > 72 and session.ctx["message"][FaceNum]['type'] == 'face':
            # 返回意图命令，前两个参数必填，分别表示置信度和意图命令名
            return IntentCommand(TRUST, 'TestFace')
        #图片
        #elif STATIC_VAL.MODE_IMAGE == '0' and a <= 78 and session.ctx["message"][FaceNum]['type'] == 'image' :
        #    await session.send('发你🐎的图片，再发干死你！',at_sender = True)        
        #    break

#####################################################用户数据获取调用分割线##############################################################
#@on_natural_language(only_to_me = False)
#async def _(session: NLPSession):
#    # 去掉消息首尾的空白符
#    stripped_msg = session.msg_text.strip()
#    #Msg_Len = len(session.ctx["message"])
#    Gop_ID = int(session.ctx["group_id"])
#    USR_ID = session.ctx["user_id"]
#    #用户数据获取段#########################################################
#    Job_Rom = xlrd.open_workbook(STORE_FEIL)
#    #获取sheet个数
#    Len_Sheet = len(Job_Rom.sheet_names())
#    #通过已有的sheet判断是否需要新建sheet
#    for i in range(Len_Sheet):
#        #通过索引顺序获取对应sheet
#        SHEETS[i] = Job_Rom.sheet_by_index(i)
#        #获取对应sheet的(0,0)对应的群号
#        STORE_GROUP[i] = int(SHEETS[i].cell_value(0,0))
#        #如果有---->打开
#        if STORE_GROUP[i] == Gop_ID:



#            break
#    #遍历失败---->新建一个
#    else:
#        SHEETS[Len_Sheet] = Job_Rom.add_sheet(str(Gop_ID))
            
#                    #总列数
#                    Cols = Sheet_1.ncols
#                    #遍历判断是否存储过发消息对象的ID
#                    for i in range(Cols):
#                        if Sheet_1.cell_value(i,1) == ID_1:
#                            break
#                        else:
#                            #写数据
#                            Sheet_1.write(Cols,1,ID_1)      
#                            break
#                    #发消息者对应的时间获取
#                    #转换时间格式
#                    #与最大\最小比较并替换
#                    #保存关闭文件
#                    Job_Rom.save(STORE_FEIL)   
#####################################################未知报错列表##############################################################
#CQ pro 能白嫖么😭
