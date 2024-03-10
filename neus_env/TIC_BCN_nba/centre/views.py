from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, Context


# Create your views here.

def index(request):
    return render(request, 'index_centre.html')

def index_profes(request):
    professors = {
        'prof1':{"nom":"Roger",
                 "cognom1":"Sobrino",
                 "cognom2":"Sobrino",
                 "correu":"roger@itic.cat",
                 "curs":"2",
                 "tutor":"no",
                 "mod":"M7"
                },
        'prof2':{"nom":"Moises",
                 "cognom1":"Gómez",
                 "cognom2":"Gómez",
                 "correu":"moi@itic.cat",
                 "curs":"1",
                 "tutor":"sí",
                 "mod":"M3"
                },
        'prof3':{"nom":"Xavi",
                 "cognom1":"Quesada",
                 "cognom2":"Quesada",
                 "correu":"xavi@itic.cat",
                 "curs":"2",
                 "tutor":"no",
                 "mod":"M8"
                }}
    context = {'prf': professors}
    return render(request, 'index_professorat.html', context)

    # template = loader.get_template('index_centre.html')
    # dades = template.render({'nombre:':professor["name"], 'surname':professor["surname"], 'age':professor["age"]})
    # return HttpResponse(dades)

def index_alumnat(request):
    alumnat = {
        'al1':{"nom":"Neus",
               "cognom1":"Bravo",
               "cognom2":"Arias",
               "correu":"neus@itic.cat",
               "curs":"2",
               "mod":"M7"
              },
        'al2':{"nom":"Facundo",
               "cognom1":"Calixto",
               "cognom2":"Barrios",
               "correu":"rulo@itic.cat",
               "curs":"1",
               "mod":"M3"
               },
        'al3':{"nom":"Angelo",
               "cognom1":"Montenegro",
               "cognom2":"Nose",
               "correu":"angelo@itic.cat",
               "curs":"2",
               "mod":"M8"
              }}
    context = {'alm': alumnat}
    return render(request, 'index_alumnat.html', context)