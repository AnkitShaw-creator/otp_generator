import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from string import Template

s = smtplib.SMTP("smtp.gmail.com", 587)
s.starttls()
s.login('ankitshaw667@gmail.com', 'pfbcqizwzpcwehua')


def read_template(filename):
    with open(filename, 'r', encoding='utf-8') as templateFile:
        template_file_content = templateFile.read()
        return Template(template_file_content)


res = input("Hello! Do you want to receive an OTP on screen?[Y/N]")
message_template = read_template('message.txt')

if res == 'Y':
    r = random.randint(100000, 1000000)
    msg = MIMEMultipart()
    message = message_template.substitute(PERSON_NAME="ALLEN", otp=r)
    msg['From'] = 'ankitshaw667@gmail.com'
    msg['To'] = 'alcemedis987654@gmail.com'
    msg['Subject'] = 'OTP generator'
    msg.attach(MIMEText(message, 'plain'))
    s.send_message(msg)
    del msg
    print(r)
else:
    print("Okay no problem")
