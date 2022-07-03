from locale import currency
import smtplib
from api import main
# import schedule


input = {
    'currency': 'USD'
}


def send_mail(text):
    EMAIL = "grinkevich.test.mail1@gmail.com"
    PASSWORD = 'gajqvhianjwykubt'
    EMAIL_TO_SEND = '375298105570@sms.mts.by'
    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpObj.starttls()
    smtpObj.login(EMAIL, PASSWORD)
    if not text == {}:
        text = str(text).replace(":", ' = ')
    smtpObj.sendmail(EMAIL, EMAIL_TO_SEND, text) 

def job():
    api = str(main(input))
    return send_mail(api)

job()

# schedule.every().day.at("9:00").do(job)

"""while True:
    schedule.run_pending()
    time.sleep(60)"""