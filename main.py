#-*-coding:utf-8 -*-
import itchat
# tuling plugin can be get here:
# https://github.com/littlecodersh/EasierLife/tree/master/Plugins/Tuling
# from tuling import get_response

@itchat.msg_register('Text')
def text_reply(msg):
    _FromUserName = msg['FromUserName']
    _ToUserName = msg['ToUserName']
    if _ToUserName in ['filehelper',_FromUserName]:
        itchat.send(u'[Pig]' + msg['Text'], toUserName=_ToUserName)

    print(_FromUserName + '#-->#' + _ToUserName)
    # return u'[Pig]：' + msg['Text']


@itchat.msg_register(['Picture', 'Recording', 'Attachment', 'Video'])
def atta_reply(msg):
    return ({ 'Picture': u'图片', 'Recording': u'录音',
        'Attachment': u'附件', 'Video': u'视频', }.get(msg['Type']) +
        u'[Pig]：已下载到本地') # download function is: msg['Text'](msg['FileName'])

@itchat.msg_register(['Map', 'Card', 'Note', 'Sharing'])
def mm_reply(msg):
    if msg['Type'] == 'Map':
        return u'[Pig]：收到位置分享'
    elif msg['Type'] == 'Sharing':
        return u'[Pig]：收到分享' + msg['Text']
    elif msg['Type'] == 'Note':
        return u'[Pig]：收到：' + msg['Text']
    elif msg['Type'] == 'Card':
        return u'[Pig]：收到好友信息：' + msg['Text']['Alias']

@itchat.msg_register('Text', isGroupChat = True)
def group_reply(msg):
    if msg['isAt']:
        return u'@%s\u2005%s' % (msg['ActualNickName'],
            '[Pig]：' + msg['Text'])

@itchat.msg_register('Friends')
def add_friend(msg):
    itchat.add_friend(**msg['Text'])
    itchat.send_msg(u'[Pig]：Nice to meet you!', msg['RecommendInfo']['UserName'])

# itchat.auto_login(True, enableCmdQR=True)
itchat.auto_login(True, enableCmdQR=0)
itchat.run()