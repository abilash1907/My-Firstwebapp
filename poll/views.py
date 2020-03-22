from django.shortcuts import render
from django.http import HttpResponse
from . import count
def Index(request):
    return render(request,"index.html")
def Result(request):
    art=request.GET["article"]
    var,word_count=count.counter(art)
    return render(request,"result.html",{"key":art,"count":word_count,"var_count":var})
