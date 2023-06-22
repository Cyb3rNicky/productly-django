from django.http import Http404, HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404

from productos.forms import ProductoForm
from .models import Producto

# Create your views here.
# def index(request):
#     productos = Producto.objects.all().values() 
#     # productos = Producto.objects.filter(puntaje__gte=6)
#     # productos = Producto.objects.filter(pk=1)
#     print(productos)
#     return JsonResponse(list(productos), safe=False)

def index(request):
    productos = Producto.objects.all()
    return render(
        request,
        'index.html',
        context={'productos': productos}
    )

def detalle(request, producto_id):
    # try:
    producto = get_object_or_404(Producto, id=producto_id)
    # producto = Producto.objects.get(id=producto_id)
    return render(
        request, 
        'detalle.html',
        context={'producto': producto })
    # except Producto.DoesNotExist:
    #     raise Http404()

def formulario(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/productos')
    else:
        form = ProductoForm()


    return render(
        request,
        'producto_form.html',
        {'form': form}
    )