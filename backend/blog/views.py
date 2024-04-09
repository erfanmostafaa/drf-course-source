from django.views.generic import ListView , DetailView
from .models import Article
from django.shortcuts import get_object_or_404



class ArticleList(ListView):

    def get_queryset(self):
        return Article.objects.filter(status = True)
    




class ArticleDetail(DetailView):
    def get_object(self) :
        return  get_object_or_404(Article.objects.filter(status = True) , 
                                    pk = self.kwargs.get("pk")
                                    )  