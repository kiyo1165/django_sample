from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import SignupForm

class SignupView(CreateView):
    form_class = SignupForm
    success_url = reverse_lazy('login')
    template_name = 'registration/sigunup.html'

# ユーザー登録後に自動でログインする場合
    def from_valid(self, form):
        #self.objectにsave()されたユーザーObjectが格納される
        valid = super().form_valid(form)
        login(self.request, self.object)
        return valid