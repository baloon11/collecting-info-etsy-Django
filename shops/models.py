# coding: utf-8
from __future__ import unicode_literals
from django.db import models
from users.models import EtsyUser
from etsy_django.settings import AUTH_USER_MODEL


class Shops(models.Model):
    etsy_user=models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='shop owner')
    name=models.CharField(verbose_name='name of the shop',max_length=200)

    class Meta:
        verbose_name = "Shop"
        verbose_name_plural = "Shops"

    def __str__(self):
        return 'shop "%s"' % self.name


class Teams(models.Model):
    shop=models.ForeignKey(Shops, verbose_name='shop')
    name=models.CharField(verbose_name='name of the team',max_length=200)

    class Meta:
        verbose_name = "Team"
        verbose_name_plural = "Teams"

    def __str__(self):
        return 'team "%s"' % self.name


class Forums(models.Model):
    team=models.ForeignKey(Teams,verbose_name='Team')
    name=models.CharField(verbose_name='name of the forum', max_length=200)
    link=models.URLField(verbose_name='forum link',max_length=200)
    update=models.DateField(auto_now=True,verbose_name='день обновления ссылок для этого форума')
    day_was_processed=models.BooleanField(default=False,\
         verbose_name='одна ссылка из этого форума сегодня уже обработана(добавлен пост)' )

    class Meta:
        verbose_name = "Forum"
        verbose_name_plural = "Forums"

    def __str__(self):
        return 'forum "%s"' % self.name