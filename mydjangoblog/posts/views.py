from django.shortcuts import render

# Create your views here.

# https://docs.djangoproject.com/en/1.11/ref/class-based-views/generic-display/

#def lista_post(request):
#    return render(request, "lista_post.html")

#def post_unico(request):
#    return render(request, "post_unico.html")

def contato(request):
    return render(request, "contato.html")