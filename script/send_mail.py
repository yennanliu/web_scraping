import os, smtplib 

class SendMail:

    def __init__(self):
        pass

    def send_mail(self, message, to, subject):
        # Gmail Sign In
        if not os.getenv('FLASK_ENV') == 'testing':
            gmail_sender = os.getenv("EMAIL")
            gmail_passwd = os.getenv("EMAIL_PASS")

            try:
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.ehlo()
                server.starttls()
                server.login(gmail_sender, gmail_passwd)

                BODY = '\r\n'.join(['To: %s' % to,
                                    'From: %s' % gmail_sender,
                                    'Subject: %s' % subject,
                                    '', message])

                server.sendmail(gmail_sender, [to], BODY)
                res = "sent"
            except:
                res = "fail"
            server.quit()
            return res
        return True

def main(message, to, subject):
    try:
        SendMail().send_mail(message, to, subject)
        print ('email sent!')
    except Exception as e:
        print ('email sending failed', e)

if __name__ == '__main__':
    message='this is test msg'
    to='<accept@emial.com>'
    subject='eamil from SendMail script'
    main(message, to, subject)