'''
演示如何再python中发送邮件
'''

from smtplib import SMTP
from email.header import Header
from email.mime.text import MIMEText

def main():
	sender = '914932027@qq.com'
	receivers = 'chenjiahuan268@163.com'

	message = MIMEText('用Python发送邮件的示例代码.', 'plain', 'utf-8')

	message['From'] = Header('陈嘉欢', 'utf-8')
	message['To'] = Header('陈嘉欢', 'utf-8')

	message['Subject'] = Header('示例代码邮件', 'utf-8')

	smtper = SMTP('smtp.qq.com')

	smtper.login(sender, 'cjhjyhappy1211')
	smtper.sendmail(sender, receivers, message.as_string())
	print('邮件发送完成!')

if __name__ == '__main__':
    main()
