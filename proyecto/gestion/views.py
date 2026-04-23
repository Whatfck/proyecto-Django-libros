from django.shortcuts import render, redirect, get_object_or_404
from .models import Autor, Libro
from .forms import AutorForm, LibroForm


def inicio(request):
    """
    Vista para la página de inicio.
    Muestra estadísticas y acceso rápido al CRUD.
    """
    autores_count = Autor.objects.count()
    libros_count = Libro.objects.count()
    context = {
        'autores_count': autores_count,
        'libros_count': libros_count,
    }
    return render(request, 'gestion/inicio.html', context)


# ============ CRUD AUTORES ============

def lista_autores(request):
    """
    Vista para listar todos los autores.
    GET: Obtiene todos los autores de la BD
    """
    autores = Autor.objects.all()
    return render(request, 'gestion/lista_autores.html', {'autores': autores})


def crear_autor(request):
    """
    Vista para crear un nuevo autor.
    GET: Muestra el formulario vacío
    POST: Guarda el autor si el formulario es válido
    """
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gestion:lista_autores')
    else:
        form = AutorForm()
    return render(request, 'gestion/autor_form.html', {'form': form})


def editar_autor(request, pk):
    """
    Vista para editar un autor existente.
    GET: Muestra el formulario con los datos del autor
    POST: Actualiza el autor si el formulario es válido
    """
    autor = get_object_or_404(Autor, pk=pk)
    if request.method == 'POST':
        form = AutorForm(request.POST, instance=autor)
        if form.is_valid():
            form.save()
            return redirect('gestion:lista_autores')
    else:
        form = AutorForm(instance=autor)
    return render(request, 'gestion/autor_form.html', {'form': form})


def eliminar_autor(request, pk):
    """
    Vista para eliminar un autor.
    GET: Muestra confirmación de eliminación
    POST: Elimina el autor de la BD
    """
    autor = get_object_or_404(Autor, pk=pk)
    if request.method == 'POST':
        autor.delete()
        return redirect('gestion:lista_autores')
    return render(request, 'gestion/autor_confirm_delete.html', {'autor': autor})


# ============ CRUD LIBROS ============

def lista_libros(request):
    """
    Vista para listar todos los libros.
    GET: Obtiene todos los libros de la BD
    """
    libros = Libro.objects.all()
    return render(request, 'gestion/lista_libros.html', {'libros': libros})


def crear_libro(request):
    """
    Vista para crear un nuevo libro.
    GET: Muestra el formulario vacío
    POST: Guarda el libro si el formulario es válido
    """
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gestion:lista_libros')
    else:
        form = LibroForm()
    return render(request, 'gestion/libro_form.html', {'form': form})


def editar_libro(request, pk):
    """
    Vista para editar un libro existente.
    GET: Muestra el formulario con los datos del libro
    POST: Actualiza el libro si el formulario es válido
    """
    libro = get_object_or_404(Libro, pk=pk)
    if request.method == 'POST':
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            form.save()
            return redirect('gestion:lista_libros')
    else:
        form = LibroForm(instance=libro)
    return render(request, 'gestion/libro_form.html', {'form': form})


def eliminar_libro(request, pk):
    """
    Vista para eliminar un libro.
    GET: Muestra confirmación de eliminación
    POST: Elimina el libro de la BD
    """
    libro = get_object_or_404(Libro, pk=pk)
    if request.method == 'POST':
        libro.delete()
        return redirect('gestion:lista_libros')
    return render(request, 'gestion/libro_confirm_delete.html', {'libro': libro})
