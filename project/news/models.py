from django.db import models
from django.urls import reverse
from users.models import User
#from django.contrib.auth.models import User

# Create your models here.
class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="author")
    bio = models.CharField(max_length=100, null=True, blank=True )
    avatar = models.ImageField(upload_to='images/profile/', null=True, blank=True)

    # def get_absolute_url(self):
    #     return reverse('author_pofile', kwargs={'pk': self.pk})

    def __str__(self):
        return str(self.user)



class Post(models.Model):
    CAT = (('tanks', 'Танки'),
    ('healers', 'Хилы'),
    ('damage_dealers', 'ДД'),
    ('dealers', 'Торговцы'),
    ('gildmasters', 'Гилдмастеры'),
    ('quest_givers', 'Квестгиверы'),
    ('blacksmiths', 'Кузнецы'),
    ('tanners', 'Кожевники'),
    ('potion_makers', 'Зельевары'),
    ('spell_masters', 'Мастера заклинаний'))

    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="post_author")
    title = models.CharField(max_length=100)
    text =models.TextField()
    image = models.FileField(upload_to='files/', null=True, blank=True)
    video = models.FileField(upload_to='files/', null=True, blank=True)
    docx = models.FileField(upload_to='files/', null=True, blank=True)
    time_creation = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=50, choices=CAT, default='tanks', verbose_name='Категории')

    def get_absolute_url(self):
        return reverse('post', args=[str(self.id)])




class Response(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="responses")
    text = models.TextField()
    time_creation = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default = False)
    