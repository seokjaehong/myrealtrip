import os

from django.conf import settings
from django.core.files.storage import default_storage
from django.db import models

# Create your models here.
from django.db.models.signals import post_delete
from django.dispatch import receiver

from config.settings.dev import DATABASES


class Photo(models.Model):
    file = models.ImageField(upload_to='photo', blank=True)


# photo모델이 삭제되는 시점의 signal을 이용해서
# 인스턴스가 삭제될 때 file필드의 파일도 삭제하도록 구현

# 데코레이터로 연결해준다.
# instance에는 시그널이 발생한 모델의 객체가 전달된다.
@receiver(post_delete, sender=Photo)
def photo_post_delete(sender, instance, **kwargs):
    # path = os.path.join(settings.MEDIA_ROOT, instance.file.name)
    # os.remove(path)
    # default_storage.delete()
    instance.file.delete(save=False)
