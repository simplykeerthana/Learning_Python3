# sending emaiks with python
# there are built in libraries to send emails in python. 

#for example mailchimp is a subscription based software 

import smtplib #simple mail transfer protocol library, to create a server

#gmail, hotmail use the smptlib

from email.message import EmailMessage

email = EmailMessage()

email['from'] = 'Keerthana Madhavan'
email['to'] = 'mkeerthanarockz@gmail.com'
email['subject'] = 'Prepare yourself to become a software engineer this 2020'

 email.set_content('I will be a python Master!')
 
 #use the smtp server to login to our gmail and send it 
 #smpt is customed to whatever email you use
 
 with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
     smtp.ehlo()
     smtp.starttls() #encryption methods
     smtp.login('somthing@gmail.com', 'password')
     
     