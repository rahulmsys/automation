import os
import smtplib
from datetime import datetime
from email import encoders
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path


class SendReportEmail:
    def __init__(self, template_path, attachment_dir, report_screenshot_path, **kwargs):
        self.template_path = template_path
        self.attachment_dir = attachment_dir
        self.report_screenshot_path = report_screenshot_path
        self.start_time = kwargs.get('start_time')
        self.end_time = kwargs.get('end_time')
        self.time_elapsed = kwargs.get('time_elapsed')

    def send_gmail(self):
        sender = 'rraj@msystechnologies.com'
        receiver = 'rraj@msystechnologies.com'
        password = 'ccqzizgklceribtw'
        curr_date = datetime.now().strftime('%d-%b-%Y')
        msg = MIMEMultipart()
        msg['From'] = sender
        msg['To'] = receiver
        msg['Cc'] = "rraj@msystechnologies.com"
        msg['Subject'] = 'Test Report' + ' | ' + str(curr_date) + ' (no-reply)'
        with open(self.report_screenshot_path, 'rb') as f:
            img = MIMEImage(f.read())
            img.add_header('Content-ID', '<reportimage>')
            msg.attach(img)

        img_msg = """
        <img src="cid:reportimage"/>
        """

        with open(self.template_path, 'r') as f:
            html_template = f.read()
        # Check all variables in template and replace with values
        html_template = html_template.format(self.start_time, self.end_time, self.time_elapsed, img_msg)
        msg.attach(MIMEText(html_template, 'html'))

        attachments = [os.path.join(self.attachment_dir, f) for f in os.listdir(self.attachment_dir) if
                       os.path.isfile(os.path.join(self.attachment_dir, f)) and not f.endswith('.png')]
        for file in attachments:
            with open(file, 'rb') as f:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(open(file, 'rb').read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', 'attachment; filename="{}"'.format(os.path.basename(file)))
                msg.attach(part)
                f.close()

        text = msg.as_string()
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, receiver, text)
        server.quit()
        print("Test Report email sent successfully.")
