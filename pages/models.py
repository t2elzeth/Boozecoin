from django.db import models
from solo.models import SingletonModel


class PagesContent(SingletonModel):
    guide = models.TextField()
    what_is_boozecoin = models.TextField()
    booz_it_up = models.TextField()
    faq = models.TextField()

    def __str__(self):
        return "Pages"

    class Meta:
        verbose_name = "Pages content"
