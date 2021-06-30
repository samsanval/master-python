from django.shortcuts import render, HttpResponse, redirect

# Create your views here.


def index(request):
    html = """
        <h1>Inicio</h1>
        <p>Años hasta el 2050: </p>
        <ul>
    """
    year = 2021
    while year <= 2050:
        html += f"<li>{str(year)}</li>"
        year += 1
    html += "</ul>"
    return render(request, 'index.html')


def helloworld(request):
    return render(request, 'helloworld.html')


def page(request, redirection=0):
    if redirection == 1:
        return redirect('contact', name="S")
    return render(request,'page.html')


def contact(request, name=""):
    return HttpResponse(f"<h2>Contacto {name}</h2>")
