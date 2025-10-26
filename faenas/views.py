from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from .models import Faena, Predio
from .forms import FaenaForm

@login_required
def lista_faenas(request):
    
    predio_activo_id = request.session.get('predio_activo')
    
    
    if predio_activo_id:
        faenas = Faena.objects.filter(predio_id=predio_activo_id).order_by('fecha_inicio', 'estado')
        predio_activo = Predio.objects.get(id=predio_activo_id)
    else:
        faenas = Faena.objects.all().order_by('fecha_inicio', 'estado')
        predio_activo = None
    
    return render(request, 'faenas/lista_faenas.html', {
        'faenas': faenas,
        'predio_activo': predio_activo
    })

@login_required
def detalle_faena(request, pk):
    faena = get_object_or_404(Faena, pk=pk)
    return render(request, 'faenas/detalle_faenas.html', {'faena': faena})

@login_required
def crear_faena(request):
    if request.method == 'POST':
        form = FaenaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_faenas')
    else:
        form = FaenaForm()
    return render(request, 'faenas/faena_form.html', {'form': form})

@login_required
def editar_faena(request, pk):
    faena = get_object_or_404(Faena, pk=pk)
    if request.method == 'POST':
        form = FaenaForm(request.POST, instance=faena)
        if form.is_valid():
            form.save()
            return redirect('detalle_faena', pk=faena.pk)
    else:
        form = FaenaForm(instance=faena)
    return render(request, 'faenas/faena_form.html', {'form': form})

@login_required
def eliminar_faena(request, pk):
    faena = get_object_or_404(Faena, pk=pk)
    if request.method == 'POST':
        faena.delete()
        return redirect('lista_faenas')
    return render(request, 'faenas/faena_confirm_delete.html', {'faena': faena})

def user_login(request):
    if request.user.is_authenticated:
        return redirect('lista_faenas')
        
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            next_url = request.GET.get('next', 'lista_faenas')
            messages.success(request, f'Bienvenido, {user.username}!')
            return redirect(next_url)
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
    
    return render(request, 'registration/login.html')

@login_required
def user_logout(request):
    if request.method == 'POST':
        logout(request)
        messages.info(request, 'Has cerrado sesión correctamente')
        return redirect('login')
    return redirect('lista_faenas')

@login_required
@never_cache
def seleccionar_predio(request):
    if request.method == 'POST':
        predio_id = request.POST.get('predio')
        if predio_id:
            request.session['predio_activo'] = int(predio_id)
            predio = Predio.objects.get(id=predio_id)
            messages.success(request, f'Predio activo establecido: {predio.nombre}')
        else:
            request.session.pop('predio_activo', None)
            messages.info(request, 'Se ha eliminado el predio activo')
        return redirect('lista_faenas')
    
    predios = Predio.objects.all().order_by('nombre')
    predio_activo_id = request.session.get('predio_activo')
    predio_activo = None
    if predio_activo_id:
        try:
            predio_activo = Predio.objects.get(id=predio_activo_id)
        except Predio.DoesNotExist:
            request.session.pop('predio_activo', None)
    
    return render(request, 'faenas/seleccionar_predio.html', {
        'predios': predios,
        'predio_activo': predio_activo
    })
    from .models import Predio
    predios = Predio.objects.all()
    return render(request, 'faenas/seleccionar_predio.html', {'predios': predios})

def user_logout(request):
    logout(request)
    from django.shortcuts import redirect
    return redirect('/accounts/login/')
