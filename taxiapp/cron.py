from .models        import Driver, Working_day
import datetime 
import time
import requests
import json
from decimal import Decimal

import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def creating_working_days():

    drivers = Driver.objects.filter(active=True)

    for driver in drivers:

        today = datetime.datetime.weekday(datetime.datetime.today())

        if today == 0:
            if driver.monday == True:
                dr_rate = driver.rate
            else:
                dr_rate = 0

        elif today == 1:
            if driver.tuesday == True:
                dr_rate = driver.rate
            else:
                dr_rate = 0

        elif today == 2:
            if driver.wednesday == True:
                dr_rate = driver.rate
            else:
                dr_rate = 0

        elif today == 3:
            if driver.thursday == True:
                dr_rate = driver.rate
            else:
                dr_rate = 0

        elif today == 4:
            if driver.friday == True:
                dr_rate = driver.rate
            else:
                dr_rate = 0

        elif today == 5:
            if driver.saturday == True:
                dr_rate = driver.rate
            else:
                dr_rate = 0

        elif today == 6:
            if driver.sunday == True:
                dr_rate = driver.rate
            else:
                dr_rate = 0

        else:
            dr_rate = 0       


        new_working_day = Working_day(
            driver=driver,
            date=datetime.datetime.today(),
            rate=dr_rate,
            fuel=0,
            penalties=0,
            cash=0,
            cash_card=0,
            cashless=0,
            )

        new_working_day.save()


def yandex_transactions():

    driver_url = 'https://fleet-api.taxi.yandex.net/v1/parks/driver-profiles/list'
    dr_headers = {'Accept-Language': 'ru',
               'X-Client-ID': 'taxi/park/d720a2f94349461ab80d9c613b8e801c',
               'X-API-Key': 'rrAqtFLKUQzNQTNPkh+WyCGzWfPbIvCxCUt+Iy'}

    driver_data = {
                "fields": {

                    "account": [],
                    "car": [],
                    "park": []
                },
                "query": {
                      "park": {
                        "id": 'd720a2f94349461ab80d9c613b8e801c'
                      },
                },

    } 

    answer = requests.post(driver_url, headers=dr_headers, data=json.dumps(driver_data),)
    response = answer.json()
    profiles = response.get('driver_profiles')

    missing_drivers = []

    for p in profiles:
        driver = (p.get('driver_profile'))
        dr_license = driver.get('driver_license')

        n = datetime.datetime.now()
        n = n.replace(hour=0, minute=1)
        y = n - datetime.timedelta(days=1)
        y = y.replace(hour=0,minute=1)

        now         =   n.isoformat() + '+00:00'
        yesterday   =   y.isoformat() + '+00:00'

        url = 'https://fleet-api.taxi.yandex.net/v2/parks/driver-profiles/transactions/list'
        headers = {'Accept-Language': 'ru',
                   'X-Client-ID': 'taxi/park/d720a2f94349461ab80d9c613b8e801c',
                   'X-API-Key': 'rrAqtFLKUQzNQTNPkh+WyCGzWfPbIvCxCUt+Iy'}

        data = {
                    "query": {
                            "park": {
                                    "driver_profile": {
                                    "id": driver['id']
                                    },
                                  "id": "d720a2f94349461ab80d9c613b8e801c",
                                  "transaction": {
                                        "category_ids": ['partner_service_manual',],
                                        "event_at": {
                                          "from": yesterday,
                                          "to": now
                                        }
                                  }
                            }
                    }

        } 

        time.sleep(2)
        answer = requests.post(url, headers=headers, data=json.dumps(data),)
        response = answer.json()
        transactions = response.get('transactions')

        for key in transactions:
            day_before_today = datetime.datetime.now() - datetime.timedelta(days=1)
            taxidriver = Driver.objects.filter(driver_license=dr_license['number']).first()
            if taxidriver:
                working_day = Working_day.objects.filter(driver=taxidriver, date=day_before_today).first()
                if working_day:
                    working_day.cashless = working_day.cashless + Decimal(abs(float(key['amount'])))
                    working_day.save()
                else:
                    working_day = Working_day.objects.filter(driver=taxidriver).last()
                    working_day.cashless = working_day.cashless + Decimal(abs(float(key['amount'])))
                    working_day.save()
            else:
                missing_drivers.append([dr_license['number'], driver.get('last_name'), driver.get('first_name'), driver.get('middle_name'),])

    if missing_drivers:
            send_mail(missing_drivers, day_before_today)    
            


def send_mail(missing_drivers, day_before_today):

    HOST = "smtp.mail.ru"
    sender_email = "info@annasoft.ru"
    receiver_email = ['info@annasoft.ru', 'm.pekshev@annasoft.ru']
    password = "M@sterkey$302"
     
    message = MIMEMultipart("alternative")
    message["Subject"] = "Отчет по загрузке из Яндекс Такси"
    message["From"] = sender_email
    message["To"] = ','.join(receiver_email)
    
    test_text = ""

    for item in missing_drivers:
        test_text += "<p>{} {} {} {} </p>".format(item[0], item[1], item[2], item[3],)

    text = """\
    {}""".format(test_text)
     
    html = """\
    <html>
      <body>
        <H3>Список водителей, которые не найдены в базе данных: </H3>
           {}
        <p>Данные по транзакциям этих водителей за {} необходимо загрузить вручную!</p>
      </body>
    </html>
    """.format(test_text, day_before_today.strftime("%Y-%m-%d"))
     
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")
     
    message.attach(part1)
    message.attach(part2)
    
    context = ssl.create_default_context()
    server = smtplib.SMTP(HOST, 587)
    server.starttls()
    server.login(sender_email, password)
    server.sendmail(
        sender_email, receiver_email , message.as_string()
    )
    server.quit()