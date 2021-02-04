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

url_Zuan = 'https://nmsl.shadiao.app/api.php?level=min&lang=zh_ch'


#SbAttactMe
@on_command('SbAttactMe')
async def SbAttactMe(session: CommandSession):
    response = requests.get(url_Zuan)
    s = re.findall(r'.*',response.text)
    await session.send(s[0],at_sender = True)

@on_natural_language(only_to_me = True,keywords={'sb','bb','鸡巴','艹','fuck','妈','nm','傻','逼','煞笔','屁','屎','吃shi','滚','脑残','变态','垃圾','氵衮','死','儿子','弟弟','爸','病','爹','没马','🐎'})
async def _(session: NLPSession):
    stripped_msg = session.msg_text.strip()
    return IntentCommand(TRUST, 'SbAttactMe')
