from django.shortcuts import render
# HttpResponse, redirect
import datetime

from products.models import Product


# Create your views here.

def main_view(request):
    if request.method == 'GET':
        return render(request, 'layouts/index.html')


def products_view(request):
    if request.method == 'GET':
        products = Product.objects.all()

        context_data = {
            'products': products
        }
        return render(request, 'products/products.html', context=context_data)

# def hello_view(request):
#     if request.method == 'GET':
#         return HttpResponse("Hello! It's my project")
#
#
# def redirect_to_youtube_view(request):
#     if request.method == 'GET':
#         return redirect("https://youtube.com")
#
#
# def now_date_view(request):
#     if request.method == 'GET':
#         now = datetime.datetime.now()
#     return HttpResponse(now)
#
#
# def goodbye_view(request):
#     if request.method == 'GET':
#         return HttpResponse("Goodbye user!")
