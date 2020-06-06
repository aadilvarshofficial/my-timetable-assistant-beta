import smtplib
import schedule
import time


def sunday_8_55():
	server = smtplib.SMTP_SSL("smtp.gmail.com",465)

	server.login("aadilvarshofficial@gmail.com", "dream@google")

	server.sendmail('aadilvarshofficial@gmail.com',
					'aadilvarshhtsIX@gmail.com',
					'hey,Aadil its time for your english class')

def sunday_9_55():
	server = smtplib.SMTP_SSL("smtp.gmail.com",465)

	server.login("aadilvarshofficial@gmail.com", "dream@google")

	server.sendmail('aadilvarshofficial@gmail.com',
					'aadilvarshhtsIX@gmail.com',
					'hey,Aadil its time for your chemistry class')
def sunday_10_55():
	server = smtplib.SMTP_SSL("smtp.gmail.com",465)

	server.login("aadilvarshofficial@gmail.com", "dream@google")

	server.sendmail('aadilvarshofficial@gmail.com',
					'aadilvarshhtsIX@gmail.com',
					'hey,Aadil its time for your biology class')
def sunday_11_55():
	server = smtplib.SMTP_SSL("smtp.gmail.com",465)

	server.login("aadilvarshofficial@gmail.com", "dream@google")

	server.sendmail('aadilvarshofficial@gmail.com',
					'aadilvarshhtsIX@gmail.com',
					'hey,Aadil its time for your history and economics class')
def sunday_12_55():
	server = smtplib.SMTP_SSL("smtp.gmail.com",465)

	server.login("aadilvarshofficial@gmail.com", "dream@google")

	server.sendmail('aadilvarshofficial@gmail.com',
					'aadilvarshhtsIX@gmail.com',
					'hey,Aadil its time for your geography and civics class')


schedule.every().sunday.at('8:55').do(sunday_8_55)
schedule.every().sunday.at('9:55').do(sunday_9_55)
schedule.every().sunday.at('10:55').do(sunday_10_55)
schedule.every().sunday.at('11:55').do(sunday_11_55)
schedule.every().sunday.at('12:55').do(sunday_12_55)


while 1:
	schedule.run_pending()
	time.sleep(1)
