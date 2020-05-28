import sys
import smtplib

with smtplib.SMTP('smtp.gmail.com',587) as smtp:
    smtp.ehlo() #identifies ourselves to the mail server we are using
    smtp.starttls() #encrypts message
    smtp.ehlo() #identifies ourselves to the mail server we are using
    smtp.login("Sender@gmail.com","senderPassword")

    inFile = open(sys.argv[1])
    for  line in inFile:
        info = line.split()
        subject = "Email Subject Here"
        body = "Email Content Here"
        msg = 'Subject: '+subject+' \n\n'+body
        try:
            smtp.sendmail("hafethwadi@gmail.com",info[1],msg)
            print("Email to "+info[1]+" sent successfully")
        except:
            print("Email to "+info[1]+" didn't send")
    inFile.close()
