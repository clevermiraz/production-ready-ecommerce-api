# from django.core.mail import send_mail, mail_admins, BadHeaderError
from django.shortcuts import render

from .tasks import notify_customers


def say_hello(request):
    # try:
    #     mail_admins('subject', 'messages', html_message='message', )
    #     # send_mail('Test', 'Hi smtp', 'info@mail.com', ['none@test.com'])
    # except BadHeaderError:
    #     pass

    notify_customers.delay('Hello')
    return render(request, 'hello.html', {'name': 'Mosh'})
