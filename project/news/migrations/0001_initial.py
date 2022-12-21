# Generated by Django 4.1.4 on 2022-12-21 05:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.CharField(blank=True, max_length=100, null=True)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='images/profile/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('image', models.FileField(blank=True, null=True, upload_to='files/')),
                ('image2', models.FileField(blank=True, null=True, upload_to='files/')),
                ('image3', models.FileField(blank=True, null=True, upload_to='files/')),
                ('time_creation', models.DateTimeField(auto_now_add=True)),
                ('category', models.CharField(choices=[('tanks', 'Танки'), ('healers', 'Хилы'), ('damage_dealers', 'ДД'), ('dealers', 'Торговцы'), ('gildmasters', 'Гилдмастеры'), ('quest_givers', 'Квестгиверы'), ('blacksmiths', 'Кузнецы'), ('tanners', 'Кожевники'), ('potion_makers', 'Зельевары'), ('spell_masters', 'Мастера заклинаний')], default='tanks', max_length=50, verbose_name='Категории')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.author')),
            ],
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('time_creation', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.post')),
            ],
        ),
    ]