from operator import sub
from django.shortcuts import render
from django.core.mail import EmailMessage, send_mail
from email.message import EmailMessage
import ssl
import smtplib


def Home(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['body']
        
        email_sender = 'akinolabahubali@gmail.com'
        email_password = 'stfsiwgsyozphcid'
        email_receiver = 'akinolabahubali@gmail.com'

        subject = subject
        body = name + ": " +message + '\nFrom '+ email
        em = EmailMessage()
        em['From'] = email
        em['To'] = email_receiver
        em['subject'] = subject
        em.set_content(body)

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_receiver, em.as_string())
        
    return render(request, 'portfolio/index.html')