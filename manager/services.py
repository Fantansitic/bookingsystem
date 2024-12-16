from smtplib import SMTP_SSL
from email.header import Header
from manager import constants as mc
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def create_server_room_key() -> str:
    #TODO
    raise

def send_key_by_weichat(key:str) -> bool:
    #TODO
    raise

def send_key_by_email(email:str,key:str) -> bool:
    from project.settings import EMAIL_SECRET_KEY
    msg = MIMEMultipart()
    msg["Subject"] = Header(mc.MAIL_TITLE,'utf-8')
    msg["From"] = mc.HOST_EMAIL
    msg["To"] = Header(email,"utf-8")
    msg.attach(MIMEText(mc.MAIL_CONTENT.format(key),'html'))
    try:
        smtp = SMTP_SSL(mc.HOST_SERVER)
        smtp.set_debuglevel(1)
        smtp.ehlo(mc.HOST_SERVER)
        smtp.login(mc.HOST_EMAIL,EMAIL_SECRET_KEY)
        smtp.sendmail(mc.HOST_EMAIL,email,msg.as_string())
        smtp.quit()
        return True
    except:
        return False