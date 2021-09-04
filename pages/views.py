from django.views import View
from django.shortcuts import render


class HomepageView(View):
    def get(self, request):
        return render(request, 'pages/index.html')


class GuideView(View):
    def get(self, request):
        return render(request, 'pages/guide.html')


class FAQView(View):
    def get(self, request):
        return render(request, 'pages/FAQ.html')


class GetBoozeView(View):
    def get(self, request):
        return render(request, 'pages/get_booze.html')


class BoozItUpView(View):
    def get(self, request):
        return render(request, 'pages/booz-it-up.html')


class WhatIsBoozecoinView(View):
    def get(self, request):
        return render(request, 'pages/what-is-Boozecoin.html')
