import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr

for i in range(1, 501):
    send = "grievance.officer@teampureplay.com"
    msg = MIMEMultipart()
    msg['From'] = formataddr((str(Header('Rishabh', 'utf-8')), 'rishabhj928@gmail.com'))
    msg['To'] = formataddr((str(Header('Spammer', 'utf-8')), send))
    msg['Subject'] = 'STOP SPAMMING ME OTHERWISE I WILL SPAM YOU - ' + str(i)
    message = "I want to opt out of your SMS communications form PLUMGD, promotional sms, all other sms, and all emails. My number is 7889153525.\nI don't know what sorcery you are playing around, I have activated DND and stopped all promotions but still you are sending me sms again and again on a daily basis. I mailed you a many times but you don't care and send me sms again and again, Please STOP THIS\nPlease stop the communications ASAP and confirm."
    msg.attach(MIMEText(message))
    mailserver = smtplib.SMTP('smtp.gmail.com', 587)
    mailserver.ehlo()
    mailserver.starttls()
    mailserver.ehlo()
    mailserver.login('rishabhj928@gmail.com', 'tangeuvbbrxzpskd')
    mailserver.sendmail('rishabhj928@gmail.com', send, msg.as_string())
    mailserver.quit()
