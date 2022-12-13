import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import os
"""发送带附件的邮件"""
def sendReport(file_path):
    # with open(file_path,"r",encoding="utf-8") as f:
    #     mail_body = f.read()
    sendfile = open(file_path,"rb").read()

    #第三方SMTP服务
    mail_host = "smtp.qq.com"   #设置smtp服务器
    mail_user = "309331666@qq.com"
    mail_pwd = "enxsxlqisoewcbdc"   #邮箱授权码
    sender = "309331666@qq.com"
    receivers = ["309331666@qq.com"]
    message = MIMEMultipart()
    message['From'] = Header('自动化测试组',"utf-8")
    message['To'] = Header('项目组','utf-8')
    subject = '测试报告邮件'
    message['Subject'] = Header(subject,'utf-8')
    #邮件正文内容
    message.attach(MIMEText("测试报告邮件","plain","utf-8"))
    att1 = MIMEText(sendfile,"base64","utf-8")
    att1["Content-Type"] = 'application/octet-stream'
    #filename可以任意写
    att1["Content-Disposition"] = 'attachment; filename="result.html"'
    message.attach(att1)
    try:
        smtpobj = smtplib.SMTP()
        smtpobj.connect(mail_host,25)   #25为smtp端口号
        smtpobj.login(mail_user,mail_pwd)
        smtpobj.sendmail(sender,receivers,message.as_string())
        print("邮件发送成功")
    except smtplib.SMTPException:
        print("邮件发送失败")

def newReport(testReport):
    lists = os.listdir(testReport)  #返回测试报告下所在目录下的所有文件夹
    lists2 = sorted(lists)  #获得升序排列后的测试报告列表
    #获得最新一条测试报告的地址
    file_new = os.path.join(testReport,lists2[-1])
    #print(file_new)
    return file_new


#测试代码，架构设计完毕真正运行时需要注释掉
if __name__ == "__main__":
    test_report='C:/Users/Administrator/PycharmProjects/AutoUiTestFrame/Report/TestReport'  #测试报告所在目录
    new_report = newReport(test_report)     #获取最新的测试报告
    print(new_report)
    sendReport(new_report)      #发送测试报告