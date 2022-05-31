from django.shortcuts import render
from .models import News
from django.views.generic import ListView, DetailView, CreateView
# Create your views here.

class ShowNewsView(ListView):
    model = News
    template_name = 'blog/home.html'
    context_object_name = 'news'
    ordering =['-date']

    def get_context_data(self, **kwargs):
        ctx = super(ShowNewsView, self).get_context_data(**kwargs)

        ctx['title'] = 'Главная страница сайта'

        return ctx

class NewDetailView(DetailView):
    model = News

    def get_context_data(self, **kwargs):
        ctx = super(NewDetailView, self).get_context_data(**kwargs)
        ctx['title'] = News.objects.get(pk=self.kwargs['pk'])

        return ctx

    template_name = 'blog/news_detail.html'



class CreateNewView(CreateView):
    model = News
    template_name = 'blog/create_news.html'

    fields = ['title', 'text']

    def form_valid(self, form):
        form.instance.avtor = self.request.user
        return super().form_valid(form)

def contakti(request):
        return render(request, 'blog/сontakti.html', {'title': 'Страница контакты!'})