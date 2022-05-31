import random
from .models import UserTask
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
from .forms import UserRegisterForm
from .models import Tusk
from django.views.generic import ListView, DetailView, CreateView
from django.contrib import messages
from django.contrib.auth.models import User
from cloudTusk.models import SubmitAnswer

class ShowTuskView(ListView):
    model = Tusk
    template_name = 'cloudTusk/allTusk.html'
    context_object_name = 'tusk'
    def get(self,request,*args,**kwargs):
        super().get(request,*args,**kwargs)
        context = self.get_context_data()
        if request.user and not request.user.is_anonymous:
            number = UserTask.objects.filter(user=request.user)
            if not number.exists():
                number = random.randint(1, Tusk.objects.count())
                UserTask.objects.create(user=request.user, number=number)
            else:
                number = number.first().number
        else:
            number = random.randint(1, Tusk.objects.count())
        context["count"] = number
        return self.render_to_response(context)
def form(request):
    if request.method == "POST":
       # form = UserRegisterForm(request.POST)
       # if form.is_valid():
           # form.save()
        user: User = request.user
        variable = user.user_tusk.number
        text = Tusk.objects.get(id=variable).text
        answer = request.POST.get('answer', None)
        SubmitAnswer.objects.create(user=user,
                                    variable=variable,
                                    text=text,
                                    answer=answer)
        messages.success(request, f'Ответ {user.username} был успешно создан!')
        return redirect('home')



class ShowVarableView(DetailView):
    model = Tusk
    template_name = 'cloudTusk/variableTusk.html'
    context_object_name = 'tusk'



class AddTuskView(CreateView):
    model = Tusk
    template_name = 'cloudTusk/add.html'

    fields = ['variable', 'text']

class ShowTuskAdminView(ListView):
    model = SubmitAnswer
    template_name = 'cloudTusk/show.html'
    context_object_name = 'answer'
    #Tusk.objects.all()[offset:limit]


