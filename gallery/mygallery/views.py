from django.shortcuts import render
from .models import Gallery,Category

# Create your views here.
def welcome(request):
      photos = Gallery.objects.all()
      return render(request, 'index.html',{"photos":photos})

def search_results(request):
      if 'category' in request.GET and request.GET("category"):
            search_category = request.GET.get('category')
            searched_categories = Category.search_by_category(search_category)
            message = f"{search_category}"

            return render(request, 'search.html', {"message":message, "category":searched_categories})

      else:
            message = "You haven't searched for any term"

            return render(request, 'search.html',{"message":message})
