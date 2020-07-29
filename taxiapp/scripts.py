from decouple import config

import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import datetime

from .models import Driver

 

def driver_mailing():


		HOST = "mail.hosting.reg.ru"
		sender_email = config('MAIL_USER')
		password = config('MAIL_PASSWORD')

		for driver in Driver.objects.filter(active=True):

			if driver.email:	

				receiver_email = [ driver.email ]

				message = MIMEMultipart("alternative")
				message["Subject"] = "Таксопарк ИП Дивиченко О.И. - {}".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))
				message["From"] = sender_email
				message["To"] = ','.join(receiver_email)

				text = """\
				"""

				html = """\
			    <html>
					<body>
						<div style="max-width: 610px; width:100%">
							<H4 style="margin-left: 20px;" >Уважаемый (ая) {2} {3}!</H4>
							<H4 style="margin-left: 20px;">Ваш долг на {0} составляет {1}р.</H4>
							<p style="margin-left: 20px;">* В расчете НЕ УЧТЕНО топливо сегодняшнего дня</p>
						</div>
					</body>
				</html>
			    """.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), driver.debt, driver.second_name,  driver.first_name)

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