import smtplib

def send_email(recipient,message):
    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)
    # start TLS for security
    s.starttls()
    # Authentication
    s.login("kace.yokohama@gmail.com", "ljoy zrrc hpsl bbjk ")
    # message to be sent
    
    # sending the mail
    s.sendmail(recipient, "orthodoxrabbibillclinton42@gmail.com", message)
    # terminating the session
    print("SENT EMAIL!!")
    print(message)
    s.quit()

