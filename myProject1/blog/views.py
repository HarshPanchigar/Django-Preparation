from django.shortcuts import render
from django.http import HttpResponse

def post_details(request , post_id):
    return HttpResponse(f"<h1>Details of Post {post_id}</h1>")

def users(request , username):
    return HttpResponse(f"<h1>Profile of User : {username}</h1>")

def article_by_year(request , year):
    return HttpResponse(f'<h1>Article from the year {year}</h1>')

# def article_details(request,year,month):
#     return HttpResponse(f'<h1>Article from {year} - {month}</h1>')

def article_details(request,**kwargs):
    return HttpResponse(f'<h1>Data : {kwargs}</h1>')
