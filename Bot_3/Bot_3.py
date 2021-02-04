import nonebot
import config
from os import path


TRUST = 100.0


class STATIC_VAL(object):
    #0狂躁模式 1正常模式 2无 !地狱
    MODE_ZUAN       = '2'
    #0严格模式
    MODE_IMAGE      = '1'
    
    MODE_SERCH      = '关'

    SERCH_GROUP     = ''

    ALARM_GROUP_ID  = [0,0,0,0,0]
    ALARM_YEAR      = 2020
    ALARM_G_MONTH   = [12,12,12,12,12]
    ALARM_G_DAY     = [31,31,31,31,31]
    ALARM_G_HOUR    = [0,0,0,0,0]
    ALARM_G_MINUTE  = [0,0,0,0,0]
    ALARM_G_MSG     = [' ',' ',' ',' ',' ']
    ALARM_USER_ID   = [0,0,0,0,0]
    ALARM_TIMES_I   = 0
    ALARM_TIMES_J   = 0

    MSG_FEILS_TXT   = ''
    MSG_FEILS_IMG   = ''

    NETWORKFLAG     = False
    NETWORKOFFTIME  = ''
    NETWORKOFFFLAG  = True

    HEALTHYFLAG     = True

    REPEAT_FLAG     = ''
    REPEAT_VAL_NOW  = ''
    REPEAT_VAL_LAST = ''
#@on_command()加上only_to_me = False，可以实现不用@的
            #Send_Type = session.ctx["message_type"]
            #print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!' + Send_Type)
            #Group_ID = session.ctx["group_id"]
            #print(Group_ID)
            #Send_ID = session.ctx["user_id"]
            #print(Send_ID)
            #Msg_Tppe = session.ctx["message"][0]["type"]
            #print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!' + Msg_Tppe)
            #Msg_Text = session.ctx["message"][0]["data"]["text"]
            #print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!' + Msg_Text)
            #Msg_Len = session.ctx["message"]['__len__']
#on_natural_language如果不传入 keywords，则响应所有没有被当作命令处理的消息
#需要@他就在session.send()里面加上at_sender = True
#定时计划任务需要#pip install "nonebot[scheduler]"
#MongoDB服务：https://www.runoob.com/mongodb/mongodb-window-install.html
#开启方法：cmd->net start MongoDB
#如果有些消息不回复把TRUST设置小点就好了
#jieba词性https://www.cnblogs.com/adienhsuan/p/5674033.html
#群组管理https://cqhttp.cc/docs/4.15/#/API?id=api-%E5%88%97%E8%A1%A8    
#bot = nonebot.get_bot()
#await bot.set_group_ban(group_id = 774261838,user_id = 3293753447,duration = 30)
# 去掉消息首尾的空白符以及开头的XX两字
#stripped_msg = session.msg_text.strip()[2:].strip()
if __name__ == '__main__':    
    nonebot.init(config)
    #nonebot.load_builtin_plugins()  
            #nonebot.load_builtin_plugins()加载了NoneBot的内置插件，这一步不是必须的，
            #尤其在你编写了自己的插件之后，可能不再需要内置插件。
            #NoneBot 的内置插件只包含了两个命令，echo 和 say，两者的功能都是重复发送者的话                                     
    nonebot.load_plugins(path.join(path.dirname(__file__), 'awesome', 'plugins'),'awesome.plugins')    
            #这里的重点在于 nonebot.load_plugins() 函数的两个参数。
            #第一个参数是插件目录的路径，这里根据 bot.py 的所在路径和相对路径拼接得到；
            #第二个参数是导入插件模块时使用的模块名前缀，这个前缀要求必须是一个当前 Python 解释器可以导入的模块前缀，
            #NoneBot 会在它后面加上插件的模块名共同组成完整的模块名来让解释器导入，
            #因此这里我们传入 awesome.plugins，当运行 bot.py 的时候，Python 解释器就能够正确导入 awesome.plugins.weather 这个插件模块了。

    nonebot.run()
#好的源码
#https://cqp.cc/forum.php?mod=viewthread&tid=42103&highlight=python
#https://cqp.cc/forum.php?mod=viewthread&tid=40695&highlight=python
#https://cqp.cc/forum.php?mod=viewthread&tid=42509&highlight=%E7%BD%91%E6%98%93%E4%BA%91
#汉字转拼音https://blog.csdn.net/mydistance/article/details/85009791
#          https://blog.csdn.net/lihuarongaini/article/details/101298166
#正则表达式https://www.runoob.com/python/python-reg-expressions.html
#          https://www.cnblogs.com/OnlyDreams/p/7845527.html






'''
              return "我去世了……（安详"
                return "你们如果还能看到消息一定是奇迹……"
                return "啊……我感觉……好热……"
                return "谁拔我网线?!"
                return "我节点又断惹(识图、上车等部分功能会受到影响)"
            return "我似乎出了点问题……"
'''