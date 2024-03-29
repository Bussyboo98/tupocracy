import imp
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from tupo_app.models import *
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.shortcuts import render
from .models import *
from .forms import *
from django.urls import reverse_lazy
from django.views.generic import(
    ListView, DetailView, 
    )

# Create your views here.

def home(request):
    about = AboutUsModel.objects.first()
    credit = CreditModel.objects.all()
    comm = Community.objects.all()[:4]
    context = {'about': about ,
    'credit': credit , 'community': comm 
    }
    return render(request, 'public/index.html', context)


def about(request):
    about = AboutUsModel.objects.all()
    credit = CreditModel.objects.all()
    context = {'about': about ,
    'credit': credit  
    }
    return render(request, 'public/about.html', context)

def emytology(request):
    emytology = Emytology.objects.all()
   
    context = {'emytology': emytology , }
    return render(request, 'public/emytology.html', context)
def credit(request):
   
    credit = CreditModel.objects.all()
    context = {
    'credit': credit  
    }
    return render(request, 'public/credit.html', context)


class Comm(ListView):
    model = Community
    template_name = 'public/community.html'
    context_object_name = 'community'
    paginate_by = 2


class Comm_Article(ListView):
    model = CommunityArticle
    template_name = 'public/comm-article.html'
    context_object_name = 'community_art'
    paginate_by = 2

    def get_queryset(self):
        return CommunityArticle.objects.order_by('-created_at')
    
class Comm_ArticleDetail(DetailView):
    model = CommunityArticle
    template_name = 'public/comm-article-details.html'
    context_object_name = 'comm_det'
    success_url = reverse_lazy('tupo_app:single_comm')
   

    def get_object(self):
        obj = super().get_object()
        return obj

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        var_slug = self.get_object()
        get_slug = var_slug.slug
        
        return context

   


def award(request):
    award= Award.objects.all()
    form = NominationForm()
    if request.method == 'POST':
        form = NominationForm(request.POST)
        if form.is_valid():
            form = form.save()
            messages.success(request, 'Your form have been submited, Thanks for choosing Transtura')
        else :
            form = NominationForm()
    
    p_form = PrincipalForm()
    if request.method == 'POST':
        p_form = PrincipalForm(request.POST)
        if p_form.is_valid():
            p_form = p_form.save()
            messages.success(request, 'Your form have been submited, Thanks for choosing Transtura')
        else:
            p_form = PrincipalForm()
    return render(request, 'public/award.html', {'form': form, 'p_form': p_form, 'award':award})
    