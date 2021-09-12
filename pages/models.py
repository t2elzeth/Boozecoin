from django.db import models
from solo.models import SingletonModel
from ckeditor.fields import RichTextField


class PagesContent(SingletonModel):
    # guide = models.TextField(default="")
    guide = RichTextField()
    what_is_boozecoin = RichTextField(default="")
    booz_it_up = RichTextField(default="")
    faq = RichTextField(default="")
    about = RichTextField(default="")

    def __str__(self):
        return "Pages"

    class Meta:
        verbose_name = "Pages content"
