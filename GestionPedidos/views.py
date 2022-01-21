
from django.shortcuts import render
from django.http import HttpResponse
from GestionPedidos.models import articulos
from django.conf import settings
from django.core.mail import send_mail
from GestionPedidos.forms import formulario_contacto

# Create your views here.
def busqueda_producto(request):
    return render(request, 'busqueda_productos.html')
#esto se debe registrar en las urls


def button_buscar(request):
    if request.GET["prod"]:
        producto=request.GET["prod"]# obtiene lo que viene del cuadro de texto
        articulo=articulos.objects.filter(nombre__icontains=producto)
        return render(request, "resultados_busqueda.html",{"articulos":articulo, "query":producto})# estos datos se usan en el html (lo que esta entre comillas)
    # mensaje="articulo buscado: %r" % request.GET["prod"]
    else:
        mensaje="no has introducido nada"
    return HttpResponse(mensaje)

#primera forma de enviar el corrreo con el forms
def contacto(request):
    if request.method == "POST":
        miFormulario= formulario_contacto(request.POST)
        if miFormulario.is_valid():#vemos si el formualrio a pasado las validaciones
            infoFormulario=miFormulario.cleaned_data#obtenemos la informacion desde el formlario
            
            send_mail(infoFormulario['asunto'], infoFormulario['mensaje'],
                      infoFormulario.get('email',''),[infoFormulario['email']],)# el ultimo parametro es para el correo del destinantario
            return render(request, "gracias.html")
    else:
        miFormulario= formulario_contacto()  
    return render(request, "fromulario_contacto.html", {"form": miFormulario}) #se le espesifica el formulario que debe renderisar 
            
            


#segunda foram de enviar un correo sin el forms
""" 
def contacto(request):
    if request.method == "POST":
        #ENVIAR UN CORREO LO OTRO ESTA EN EL ARCHIVO SETTINGS
        subject=request.POST["asunto"]#tomamos los datos que obtuvimos de la vista (lo que el usuario ingresa)
        message=request.POST["mensaje"]+" "+request.POST["email"] #el mensaje en este caso mas el correo
        correo_destino=request.POST["email"]#el correo a donde se envia
        email_from=settings.EMAIL_HOST_USER# desde que correo es enviado
        recipient_list=[correo_destino]# hacia que correo ser enviado
        send_mail(subject, message, email_from,recipient_list)
        
        return render(request, "gracias.html")
        
    return render(request, "contactos.html")
    """