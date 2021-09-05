from django.urls import path

from . import views

urlpatterns = [
    path("", views.HomepageView.as_view(), name='homepage'),
    path("guide/", views.GuideView.as_view(), name='guide'),
    path("faq/", views.FAQView.as_view(), name='faq'),
    path("get-booze/", views.GetBoozeView.as_view(), name='get-booze'),
    path("booz-it-up/", views.BoozItUpView.as_view(), name='booz-it-up'),
    path("what-is-boozecoin/", views.WhatIsBoozecoinView.as_view(), name='what-is-boozecoin'),
    path("about/", views.AboutView.as_view(), name='about')
]
