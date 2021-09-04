from django.views import View
from django.shortcuts import render


class HomepageView(View):
    def get(self, request):
        return render(request, 'homepage/index.html')


class GuideView(View):
    def get(self, request):
        return render(request, 'guide/guide.html')


class FAQView(View):
    def get(self, request):
        return render(request, 'faq/FAQ.html')


class GetBoozeView(View):
    def get(self, request):
        return render(request, 'get_booze/get_booze.html')


class BoozItUpView(View):
    def get(self, request):
        return render(request, 'booz-it-up/booz-it-up.html')


class WhatIsBoozecoinView(View):
    def get(self, request):
        return render(request, 'what-is-boozecoin/what-is-Boozecoin.html')
