# -*- coding: UTF-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.header import Header
 
# 第三方 SMTP 服务
mail_host="smtp.siterubix.com"  #设置服务器
mail_user="digital-evaluation.com"    #用户名
mail_pass='3Kx89kRsop'  #口令 
 
 
sender = 'support@digital-evaluation.com'
receivers = 'sxcccya@outlook.com'  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

mail_msg = """
<p>Python 邮件发送测试...</p>
<p><a href="http://www.runoob.com">这是一个链接</a></p>
"""
subject = 'Python SMTP test'
message = MIMEText(mail_msg, 'html', 'utf-8')
message['Subject'] = Header(subject, 'utf-8')
message['From'] = 'tyouki<support@digital-evaluation.com>'
message['To'] =  receivers
 

 
 
#try:
smtpObj = smtplib.SMTP(mail_host, 25) 
smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
smtpObj.ehlo()
#smtpObj.starttls()
smtpObj.ehlo()
smtpObj.login(mail_user,mail_pass)
smtpObj.sendmail(sender, receivers, message.as_string())
smtpObj.quit()
print ("邮件发送成功")
#except smtplib.SMTPException:
#    print ("Error: 无法发送邮件")
#    print (smtplib.SMTPException)

#server = smtplib.SMTP('smtp.example.com', 25)
#server.connect("smtp.example.com",465)
#server.ehlo()
#server.starttls()
#server.ehlo()
#server.login(fromaddr, "password")
#text = msg.as_string()
#server.sendmail(fromaddr, toaddr, text)
#server.quit()

#smtpObj = smtplib.SMTP( [host [, port [, local_hostname]]] )
#SMTP.sendmail(from_addr, to_addrs, msg[, mail_options, rcpt_options])

