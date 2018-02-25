from django.shortcuts import render
from django.http import HttpResponse,Http404
from .models import Gallery,Category
from django.db.models.base import ObjectDoesNotExist

# Create your views here.
def welcome(request):
      photos = Gallery.objects.all()
      return render(request, 'index.html',{"photos":photos})

"""

method that selects a single image and displays it

"""
def image(request, image_id):
      try:
            image = Gallery.objects.get(id = image_id)
      except Gallery.DoesNotExist:
            raise Http404()

      return render(request,"image.html", {"image":image})

def search_results(request):
      if 'category' in request.GET and request.GET("category"):
            search_category = request.GET.get('category')
            searched_categories = Category.search_by_category(search_category)
            message = f"{search_category}"

            return render(request, 'search.html', {"message":message, "category":searched_categories})

      else:
            message = "You haven't searched for any term"

            return render(request, 'search.html',{"message":message})
