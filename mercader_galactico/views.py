from django.shortcuts import render
from mercader_galactico.mercader_app import app

# Create your views here.
def index(request):
    return render(request, 'index.html',{})

def pregunta(request):

    if request.method == 'POST':
        aprendizaje = request.POST['aprendizaje']
        pregunta = request.POST['pregunta']
        texto_completo = aprendizaje + pregunta
        response = app.aprender_y_responder(texto_completo.splitlines())
        context = {'pregunta':pregunta.splitlines(), 'response':response}
        return render(request, 'pregunta.html',context)
    else:
        return render(request, "error_404.html", {})