'''
#微信调用网易的播放音乐端口，在微信上控制电脑播放歌曲


#coding=utf=8
import os
import itchat
from NetEaseMusicApi import interact_select_song
with open("stop.mp3","w") as f:
    pass
def close_music():
    os.startfile("stop.mp3")
@itchat.msg_register(itchat.content.TEXT)
def music_player(msg):
    #print(msg["Text"])
    #if msg["ToUserName"] =="fielhelper":
    if msg["Text"]==u"关闭":
        close_music()
        itchat.send(u"音乐已关闭","filehelper")
    elif msg["Text"]==u'帮助':
        itchat.send(u'帮助信息','filehelper')
    else:
        itchat.send(interact_select_song(msg['Text']),'filehelper')
                            
                        
        
    


#itchat.send(HELP_MSG,'filehelper')
itchat.auto_login(hotReload=True)
itchat.run()
'''
'''
#给所有的好友发微信消息：祝幻雪之神新年快乐，发给幻雪之神
#coding=utf8
import itchat, time

itchat.auto_login(True)

SINCERE_WISH = u'祝%s新年快乐！'

friendList = itchat.get_friends(update=True)[1:]
for friend in friendList:
    # 如果是演示目的，把下面的方法改为print即可
    itchat.send(SINCERE_WISH % (friend['DisplayName']
        or friend['NickName']), friend['UserName'])
    time.sleep(.5)

#给群内的所有人发消息
#coding=utf8
import itchat, time

itchat.auto_login(True)

REAL_SINCERE_WISH = u'祝%s新年快乐！！'

chatroomName='wishgroup'
itchat.get_chatrooms(update=True)
chatrooms = itchat.search_chatrooms(name=chatroomName)
if chatrooms is None:
    print(u'没有找到群聊：' + chatroomName)
else:
    chatroom = itchat.update_chatroom(chatrooms[0]['UserName'])
    for friend in chatroom['MemberList']:
        friend = itchat.search_friends(userName=friend['UserName'])
        # 如果是演示目的，把下面的方法改为print即可
        itchat.send(REAL_SINCERE_WISH % (friend['DisplayName']
            or friend['NickName']), friend['UserName'])
        time.sleep(.5)

'''




#好友删除检测







    
