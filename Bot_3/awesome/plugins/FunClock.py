from datetime import datetime
from aiocqhttp.exceptions import Error as CQHttpError
from nonebot import get_bot
from Bot_3 import STATIC_VAL
from selenium import webdriver
from lxml import html,etree
from PIL import Image
from selenium.webdriver.support.select import Select
import urllib.request
import io
import requests
import sys
import time
import nonebot
import pytz
import json
import socket
import re
import urllib
import os
import socket

now = datetime.now(pytz.timezone('Asia/Shanghai'))

url_Adv_Notype = 'http://www.boredapi.com/api/activity/'

url_Zuan = 'https://nmsl.shadiao.app/api.php?level=min&lang=zh_ch'

Url_ReSou = 'https://s.weibo.com/top/summary?retcode=6102'

def isNetOK(testserver):
    s = socket.socket()
    s.settimeout(3)
    try:
        status = s.connect_ex(testserver)
        if status == 0:
            s.close()
            return True
        else:
            return False
    except Exception as e:
        return False

#定期任务-20min
@nonebot.scheduler.scheduled_job('interval', minutes = 20)
async def _1():
    bot = nonebot.get_bot()
    isOK = isNetOK(('www.baidu.com',443))
    if isOK:
        #心跳包
        try:
            await bot.send_group_msg(group_id = 637399227,message = 'The Network Status:%s'%isOK)
        except CQHttpError:
            await bot._set_restart()
            print("心跳包未发送！已为您重启酷Q-AIR。")

##定期任务-6h
##@nonebot.scheduler.scheduled_job('interval', hour = 6).
#async def _1():
#    bot = nonebot.get_bot()
#    isOK = isNetOK(('www.baidu.com',443))
#    if isOK:
#        #微博热搜
#        try:
#            ReSou_Result = ''
#            #访问
#            user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
#            headers = {'User-Agent':user_agent}
#            r = requests.get(Url_ReSou,headers=headers)
#            s_1 = etree.HTML(r.text)
#            #制作xpath内容
#            for i  in range(21):

#                Xpath = '//*[@id="pl_top_realtimehot"]/table/tbody/tr['+ str(i + 1) +']/td[2]/a/text()'

#                if i == 0:
#                    Head = '⇑：'
#                else:
#                    Head = str(i) + '：'
        
#                ReSou_Result += Head + str(s_1.xpath(Xpath)) + '\n'

#            await bot.send_group_msg(group_id = 774261838,message = ReSou_Result)
#        except CQHttpError:
#            await bot.send_group_msg(group_id = 774261838,message = '爬取微博热搜失败！请检测...')

#每分钟检测任务
@nonebot.scheduler.scheduled_job('cron', minute = '*')#minute 
async def _2():
    bot = nonebot.get_bot()
    isOK = isNetOK(('www.baidu.com',443))
    #获取字符串形式的时间表
    Mth_Now = int(time.strftime('%m',time.localtime(time.time())))
    Day_Now = int(time.strftime('%d',time.localtime(time.time())))
    Hor_Now = int(time.strftime('%H',time.localtime(time.time())))
    Min_Now = int(time.strftime('%M',time.localtime(time.time())))
    #网络
    #if  not isOK and STATIC_VAL.NETWORKOFFFLAG:
    #    STATIC_VAL.NETWORKOFFTIME = str(Hor_Now) + ':' + str(Min_Now)
    #    STATIC_VAL.NETWORKFLAG = True
    #    STATIC_VAL.NETWORKOFFFLAG = False
    #if  STATIC_VAL.NETWORKFLAG and isOK:
    #    await bot.send_group_msg(group_id = 774261838,message = '哎妈呀~我网不好[CQ:face,id=107]\n%s断网的，现在可算是连上了！都吓死我了！'%STATIC_VAL.NETWORKOFFTIME)
    #    STATIC_VAL.NETWORKFLAG = False
    #    STATIC_VAL.NETWORKOFFFLAG = True
    #闹钟
    try:
        #闹钟提醒
        for i in range(4):
            if  STATIC_VAL.ALARM_G_MONTH[i] == Mth_Now and \
                STATIC_VAL.ALARM_G_DAY[i] == Day_Now and \
                STATIC_VAL.ALARM_G_HOUR[i] == Hor_Now and \
                STATIC_VAL.ALARM_G_MINUTE[i] == Min_Now :
                await bot.send_group_msg(group_id = STATIC_VAL.ALARM_GROUP_ID[i],
                                            message = STATIC_VAL.ALARM_G_MSG[i] + '[CQ:at,qq = %d]'%STATIC_VAL.ALARM_USER_ID[i])
    except CQHttpError:
        pass

#定时任务-健康信息\清理垃圾
#@nonebot.scheduler.scheduled_job('cron', hour = 21,minute = 11)
@nonebot.scheduler.scheduled_job('cron', hour = 0,minute = 4)
async def _3():
    bot = nonebot.get_bot()
    isOK = isNetOK(('www.baidu.com',443))
    #健康信息
    #需要加断网判断，如果一直断网，等到联网后再填报！！！
    while(STATIC_VAL.HEALTHYFLAG):
        if  isOK and \
            os.system('H:\VS_Py\Proj_Boswer\Boswer\Boswer\Heal_hsn_New.py') == 0 and \
            os.system('H:\VS_Py\Proj_Boswer\Boswer\Boswer\Heal_zcq.py') == 0 \
            :

            await bot.send_group_msg(group_id = 774261838,message = '健康信息打卡已自动帮您填写完成！[CQ:at,qq = 1258691091]')
            
            await bot.send_group_msg(group_id = 662080134,message = '健康信息打卡已自动帮您填写完成！[CQ:at,qq = 1018743169]')
            
            STATIC_VAL.HEALTHYFLAG = False

        else:
            await bot.send_group_msg(group_id = 662080134,message = '健康信息打卡有些问题，正在重试中...')
            STATIC_VAL.HEALTHYFLAG = True            
    #清理垃圾
    await bot.clean_data_dir(data_dir = 'image') 
    await bot.clean_data_dir(data_dir = 'record') 
    await bot.clean_data_dir(data_dir = 'show') 
    await bot.clean_data_dir(data_dir = 'bface') 
    await bot.clean_plugin_log()
    await bot.send_group_msg(group_id = 774261838,message = '定时清理缓存任务点已完成！')
    STATIC_VAL.HEALTHYFLAG = True


#每秒检测任务
#@nonebot.scheduler.scheduled_job('cron', second = '*')
#async def _4():
#    bot = nonebot.get_bot()
#    response = requests.get(url_Zuan)
#    s = re.findall(r'.*',response.text)
#    await bot.send_group_msg(group_id = 774261838,message = '[CQ:at,qq = 2435870276] %s'%s[0])
