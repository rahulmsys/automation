import smtplib


class SendEmailReport:
    def __init__(self, email_address, email_password, email_server, email_port, email_subject, email_body):
        self.email_address = email_address
        self.email_password = email_password
        self.email_server = email_server
        self.email_port = email_port
        self.email_subject = email_subject
        self.email_body = email_body

    def send_email(self):
        try:
            server = smtplib.SMTP(self.email_server, self.email_port)
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login(self.email_address, self.email_password)
            message = 'Subject: {}\n\n{}'.format(self.email_subject, self.email_body)
            server.sendmail(self.email_address, self.email_address, message)
            server.quit()
            print('Email sent successfully')
        except Exception as e:
            print(e)