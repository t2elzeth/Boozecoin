from django.db import models
from solo.models import SingletonModel


class PagesContent(SingletonModel):
    guide = models.TextField(default="")
    what_is_boozecoin = models.TextField(default="")
    booz_it_up = models.TextField(default="")
    faq = models.TextField(default="")
    about = models.TextField(default="")

    def __str__(self):
        return "Pages"

    class Meta:
        verbose_name = "Pages content"
