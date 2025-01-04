from django.shortcuts import render
from .models import Auto,Reservas,ReservaForm

def index(request):
    context = {
        'title': 'Austral Rent a Car - Inicio',
    }
    return render(request, 'index.html', context)

def admin2(request):
    context = {
        'title': 'Austral Rent a Car - Administración',
    }
    return render(request, 'html/admin.html', context)

def vehiculos(request):
    context = {
        'title': 'Austral Rent a Car - Vehículos',
    }
    return render(request, 'vehiculos.html', context)

def detalle_vehiculo(request, tipo):
    # Diccionario con los detalles de cada tipo de vehículo
    vehiculos = {
        'sedan': {
            'nombre': 'Kia Rio 4',
            'descripcion': 'Este vehículo cuenta con un diseño elegante, eficiencia de combustible y tecnología avanzada. Ideal para viajes largos o traslados urbanos.',
            'precio': '$35.000/día',
            'imagenes': ['imagenes/sedan6.jpg', 'imagenes/sedan kia 4.webp', 'imagenes/sedan.webp']
        },
        'suv': {
            'nombre': 'Chery Tiggo 4',
            'descripcion': 'Un SUV potente y espacioso, perfecto para explorar destinos fuera de la carretera.',
            'precio': '$45.000/día',
            'imagenes': ['imagenes/suv4.jpg', 'imagenes/suv2.jpg', 'imagenes/suv.jpg']
        },
        'minivan': {
            'nombre': 'Kia Sedona',
            'descripcion': 'Viaja cómodo y con espacio con nuestras minivans',
            'precio': '$50.000/día',
            'imagenes': ['imagenes/minivan3.webp', 'imagenes/minivan2.jpg', 'imagenes/minivan.jpg']
        },
        'camioneta': {
            'nombre': 'Toyota Hilux',
            'descripcion': 'Disfruta de la emoción de la carretera con nuestras camionetas',
            'precio': '$45.000/día',
            'imagenes': ['imagenes/camioneta2.png', 'imagenes/camioneta.jpeg', 'imagenes/camioneta3.avif']
        },
        
    }

    vehiculo = vehiculos.get(tipo, None)

    if vehiculo is None:
        return render(request, '404.html')  # Redirige a una página de error si el tipo no existe

    return render(request, 'detalle_vehiculo.html', {'vehiculo': vehiculo})

def sedan(request):
    return render(request, 'sedan.html')

def reservas(request, tipo_vehiculo):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            # Aquí puedes guardar los datos en la base de datos o realizar otras acciones
            form.save()  # Guarda los datos si usas un modelo o similar
            return('reservas_exito')  # Redirige a una página de éxito
        else:
            return ("Formulario inválido")  # Muestra un mensaje si el formulario no es válido
    else:
        form = ReservaForm()

    context = {
        'tipo_vehiculo': tipo_vehiculo,
        'form': form,
    }
    return render(request, 'reservas.html', context)

def reservas_exito(request):
    return render(request, 'reservas_exito.html')

def suv(request):
    return render(request, 'suv.html')

def minivan(request):
    return render(request, 'minivan.html')

def camioneta(request):
    return render(request, 'camioneta.html')

def nosotros(request):
    context = {
        'title': 'Austral Rent a Car - Nosotros',
    }
    return render(request, 'nosotros.html', context)

def login(request):
    contexto = {}
    return render(request,'login.html',contexto);

def menu(request):
    request.session["usuaio"]="barby"
    usuario=request.session["usuario"]
    context={'usuario':usuario}
    return render(request, 'html/admin.html', context)

def admin(request):
    Auto=Auto.objects.all()
    context={'auto':Auto}
    return render(request,'html/vehiculo.html',context)

def agregar(request):
    if request.method !="POST":
        Auto=Auto.objects.all();
        context={'idauto':Auto}
        return render(request,'html/agregar.html',context)
    else:
        #Es un POST,por lo tanto se recuperan los datos del formulario
        id_auto =request.POST["idAuto"]
        nombre=request.POST["nombre"]
        annio=request.POST["fecha"]
        activo="1"
    
    
        obj=Auto.objects.create(id_auto=id_auto,
                                   nombre=nombre,
                                   annio=annio,
                                   activo=1)
        obj.save()
        context={'mensaje':'OK, datos guardados con éxito'}
        return render(request,'html/agregar.html',context)

def encontrar(request, pk):
    context = {}
    try:
        auto = Auto.objects.get(id_auto=pk)
        marca = marca.objects.all()  
        context = {'auto': auto}
        return render(request, 'html/modificar.html', context)
    except Auto.DoesNotExist:
        context = {'mensaje': 'Error, id auto no existe'}
        return render(request, 'html/admin.html', context)

def modificar(request):
    if request.method == "POST":
        idauto = request.POST["idauto"]
        nombre = request.POST["nombre"]
        annio = request.POST["fecha"]
        marca = request.POST["marca"]
        color = request.POST["color"]
        cant_pasajeros = request.POST["cant_pasajeros"]
        activo = "1"

        try:
            auto = Auto.objects.get(id_auto=idauto)
            auto.nombre = nombre
            auto.annio = annio
            auto.marca = marca
            auto.color = color
            auto.cant_pasajeros = cant_pasajeros
            auto.activo = activo
            auto.save()
            autos = Auto.objects.all()
            context = {'mensaje': 'OK, datos actualizados con éxito', 'autos': autos}
            return render(request, 'html/modificar.html', context)
        except Auto.DoesNotExist:
            autos = Auto.objects.all()
            context = {'autos': autos, 'mensaje': 'Error, auto no encontrado'}
            return render(request, 'html/admin.html', context)
    else:
        autos = Auto.objects.all()
        context = {'autos': autos}
        return render(request, 'html/admin.html', context)


def eliminar(request, pk):
    try:
        auto = Auto.objects.get(id_auto=pk)
        auto.delete()
        mensaje = "Ok, Datos eliminados satisfactoriamente"
    except Auto.DoesNotExist:
        mensaje = "Error, id auto no existe"

    autos = Auto.objects.all()
    context = {'autos': autos, 'mensaje': mensaje}
    return render(request, 'html/admin.html', context)

