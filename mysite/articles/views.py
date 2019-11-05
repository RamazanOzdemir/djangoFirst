from django.shortcuts import render

# Create your views here.
def article_list(requset):
    return render(requset,'articles/article_list.html')
