
#一、监控消息
#coding=utf8
import itchat
#1、不带具体对象注册，当a发送消息x给b时,b显示收到消息内容为x，a显示发送成功x。
@itchat.msg_register(itchat.content.TEXT)
def simple_reply(msg):
    #itchat.send_msg("收到消息内容为%s"%msg["Text"],toUserName="filehelper")
    #return "发送成功:%s" %msg["Text"]
    for i in msg:
        print(i,    msg[i])
itchat.auto_login(hotReload=True)

#itchat.send("dierci","filehelper")
   
itchat.run()



#2、带具体对象注册

#coding=utf8
import itchat
@itchat.msg_register(itchat.content.TEXT,isFriendChat=True,isGroupChat=True,isMpChat=True)
def text_reply(msg):
    msg.user.send("%s : %s" % (msg.type, msg.text))#user是接收方，fromuser是发送方
itchat.auto_login(hotReload=True)

itchat.run()
#806892233
#mali0913..
