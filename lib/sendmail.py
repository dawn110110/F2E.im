#!/usr/bin/env python
# coding=utf-8
#
# Copyright 2012 F2E.im
# Do have a faith in what you're doing.
# Make your life a story worth telling.

import smtplib
import sys
import email
from email.mime.text import MIMEText
#from lib.mylog import mylogger  # from ../
from mylog import mylogger  # from ../

__debug = True

send_mail_host = 'smtp.xx.xx'
send_mail_user = 'xxuser'
send_mail_user_name = u'PyHack 社区'
send_mail_pswd = 'xxpw'
send_mail_postfix = 'xx.xx'
get_mail_user = 'xxxx'
charset = 'utf-8'

get_mail_postfix = 'get_mail_postfix'
get_mail_host = 'get_mail_host'

def send(sub, content, reciver = get_mail_user + get_mail_postfix):
    send_mail_address = send_mail_user_name + '<' + send_mail_user + '@' + send_mail_postfix + '>'
    msg = email.mime.text.MIMEText(content,'html',charset)
    msg['Subject'] = email.Header.Header(sub,charset)
    msg['From'] = send_mail_address
    msg['to'] = to_adress = reciver
    try:
        mylogger.info('sendmail: %r' % {
            'to_adress': to_adress,
            'msg': msg.as_string(),
            })
        stp = smtplib.SMTP()
        stp.connect(send_mail_host)
        stp.login(send_mail_user,send_mail_pswd)
        stp.sendmail(send_mail_address,to_adress,msg.as_string())
        stp.close()
        return True
    except Exception,e:
        print(e)
        return False

if __name__ == "__main__":
    send('testing hello', 'this is just for testing', 'dawn110110@foxmail.com')
