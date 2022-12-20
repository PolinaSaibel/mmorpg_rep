
#from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
# from django.utils.encoding import force_bytes
# from django.utils.http import urlsafe_base64_encode
# from django.contrib.auth.tokens import default_token_generator as \
#     token_generator
import random

def send_email_for_verify(request, user):
    user = user
    print("utils", user)
    user.code = random.randint(1000, 9999)
    user.save()
    context = {
        'user': user,
        'code': user.code,
        'user_id': user.id,
    }
    message = render_to_string(
        'registration/verify_email.html',
        context=context,
    )
    email = EmailMessage(
        'Veryfi email',
        message,
        to=[user.email],
    )
    email.send()