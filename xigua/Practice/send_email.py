# coding=utf-8
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# 发件相关参数
smtpserver = "smtp.163.com"
port = 0
sender ="huqiuyueya@163.com"
psw = "hqy945688026"
receiver ="1162714666@qq.com"
# 多个收件人时
# receiver = ['1162714666@qq.com','945688026@qq.com']

# # 编辑文字邮件内容
# subject ="这个主题是163"
# body ='<p>这是163发送的邮件</p>'
# msg = MIMEText(body,"html","utf-8")
# msg["from"] = sender
# msg["to"] = "1162714666@qq.com"
# msg["subject"] =subject

# 编辑有附件的邮件
#****读文件****
file_path = "report.html"    #先读取发送的文件内容，file_path是路径的参数名
with open(file_path,"rb") as fp:
    mail_body = fp.read()
msg=MIMEMultipart()
msg["from"] = sender
msg["to"] = receiver
# 多个收件人
# msg["to"] = ";".join(receiver)
msg["subject"] = "人生苦短，我学Python"

# ****正文****
body = MIMEText(mail_body,"html","utf-8")
msg.attach(body)

# ****附件****
att = MIMEText(mail_body,"base64","utf-8")
att.add_header('Content-Type','application/octet-stream')
att.add_header('Content-Disposition','attachment',filename="test_rport.html")  #filename是对发送的文件重新命名
msg.attach(att)

# 发送邮件
try:
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(sender,psw)
except:
    smtp = smtplib.SMTP_SSL(smtpserver,port)
    smtp.login(sender,psw)
smtp.sendmail(sender,receiver,msg.as_string())
smtp.quit()