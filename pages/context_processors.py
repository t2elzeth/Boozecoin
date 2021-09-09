from pages.models import PagesContent


def pages_content(*args, **kwargs):
    return {
        'content': PagesContent.objects.get()
    }
