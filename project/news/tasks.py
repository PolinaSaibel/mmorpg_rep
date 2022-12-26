from celery import shared_task
from .models import *
from django.core.mail import send_mail, EmailMultiAlternatives
from project.settings import DEFAULT_FROM_EMAIL
from django.template.loader import render_to_string
import time
from datetime import datetime, timedelta
from django.utils import timezone


# celery -A project worker -l INFO

@shared_task
def notify_sub_weekly():
    # d_to = datetime.now().date()
    # d_from = d_to - timedelta(days=7)
    # posts = Post.objects.filter(time_creation__range=(d_from, d_to))
    now = timezone.now()
    posts = Post.objects.filter(time_creation__gte=now - timedelta(days=7))
    author = Author.objects.all()

    for user in author:
        
        mail = user.user.email
        html_content = render_to_string('week_mess.html',{
            'posts':posts,
    })

    msg = EmailMultiAlternatives(
        subject=f'Новости за последнюю неделю.',
        from_email=DEFAULT_FROM_EMAIL,
        to=[mail],
    )
    msg.attach_alternative(html_content, "text/html")  # добавляем html
    msg.send()  # отсылаем 

@shared_task
def respond_accept_send_email(id):
    """сообщение о принятии отклика"""
    respond = Response.objects.get(id=id) # id отклика
    mail=respond.author.email
    print('mail_respond',mail)
    post = respond.post
    post_id = post.id
    print("post_id", post)
    post_title = post.title
    print("post_title", post_title)

    html_content = render_to_string('messages/respond_accept.html',{
        'post_id': post_id,
        'post_title': post_title,
    })


    msg = EmailMultiAlternatives(
        subject=f'Ваш отклик принят!',               
        from_email=DEFAULT_FROM_EMAIL,
        to=[mail],
    )
    msg.attach_alternative(html_content, "text/html")  # добавляем html
    msg.send()  # отсылаем 


@shared_task
def respond_del_send_email(id):
    """сообщение при отклонении отклика"""
    respond = Response.objects.get(id=id) # id отклика
    mail=respond.author.email
    print('mail_respond',mail)
    post = respond.post
    post_id = post.id
    print("post_id", post)
    post_title = post.title
    print("post_title", post_title)

    html_content = render_to_string('messages/respond_del.html',{
        'post_id': post_id,
        'post_title': post_title,
    })


    msg = EmailMultiAlternatives(
        subject=f'Ваш отклик принят!',               
        from_email=DEFAULT_FROM_EMAIL,
        to=[mail],
    )
    msg.attach_alternative(html_content, "text/html")  # добавляем html
    msg.send()  # отсылаем     


@shared_task
def new_response(id):
    """сообщение новом отклике"""
    respond = Response.objects.get(id=id)# id resp
    post = respond.post 
    print(post)
    mail= post.author.user.email
    print(mail)
    post_id = post.id
    post_title = post.title
    respond_author = respond.author
    respond_text = respond.text
   

    html_content = render_to_string('messages/new_response.html',{
        'post_id': post_id,
        'post_title': post_title,
        'respond_text': respond_text,
        'respond_author': respond_author,
    })


    msg = EmailMultiAlternatives(
        subject=f'Ваш отклик принят!',               
        from_email=DEFAULT_FROM_EMAIL,
        to=[mail],
    )
    msg.attach_alternative(html_content, "text/html")  # добавляем html
    msg.send()  # отсылаем       