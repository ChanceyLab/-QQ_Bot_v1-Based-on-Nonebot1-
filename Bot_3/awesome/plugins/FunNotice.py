#-*- coding:utf-8 -*-
from typing import Optional
from aiocqhttp.message import escape
from nonebot.helpers import context_id, render_expression
from nonebot import on_command, CommandSession
from nonebot import on_notice, NoticeSession
from nonebot import on_request, RequestSession
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
import requests, json, time, re, os, sys, time, io, csv
import bs4
import pandas as pd#引入pandas方便数据可视化
import serial#安装
import nonebot
import xlwt#安装
import xlrd#安装

bot = nonebot.get_bot()

#WelcomeNew
@on_notice('group_increase')
async def WelcomeNew(session: NoticeSession):
    GroupID = session.ctx['group_id']
    UserID = session.ctx['user_id']
    await bot.send_group_msg(group_id  = GroupID,message = '来人啊！快欢迎新朋友进群~[CQ:face,id=144][CQ:face,id=144][CQ:face,id=144][CQ:at,qq = %d]'%UserID)

#SomeoneLeave
@on_notice('group_decrease')
async def SomeoneLeave(session: NoticeSession):
    GroupID = session.ctx['group_id']
    UserID = session.ctx['user_id']
    OwnerID = session.ctx['operator_id']
    if OwnerID == UserID:
        await bot.send_group_msg(group_id  = GroupID,message = '成员%d主动退出本群[CQ:face,id=107]希望大家珍惜这来之不易的缘分[CQ:face,id=176]我们有缘再见！'%UserID)
    else:
        await bot.send_group_msg(group_id  = GroupID,message = '成员%d被管理员%d踢出本群[CQ:face,id=32]虽然不知道什么原因[CQ:face,id=30]但还是希望大家引以为戒，争做优秀群成员！！'%(UserID,OwnerID))

#GroupBan
@on_notice('group_ban')
async def GroupBan(session: NoticeSession):
    GroupID = session.ctx['group_id']
    UserID = session.ctx['user_id']
    OwnerID = session.ctx['operator_id']
    Seconds = session.ctx['duration']
    if session.ctx['sub_type'] == 'lift_ban':
        await bot.send_group_msg(group_id  = GroupID,message = '你已被解除禁言，下次说话注意啊~[CQ:face,id=178][CQ:at,qq = %d]'%UserID)
    else:
        await bot.send_group_msg(group_id  = GroupID,message = '成员%d被管理员%d禁言%d秒！'%(UserID,OwnerID,Seconds))

#NewFriends
@on_request('friend')
async def NewFriends(session: NoticeSession):
    UserID = session.ctx['user_id']
    Msg = session.ctx['comment']
    await bot.send_group_msg(group_id = 774261838,message = '%d请求加baby为好友，主人去看一下嘛~[CQ:at,qq = 1258691091]'%UserID)
    await bot.send_group_msg(group_id = 637399227,message = '%d请求加我为好友。\n验证消息：%s\n去看看~[CQ:at,qq = 1258691091]'%(UserID,Msg))
