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
                 "cognom2":"Gil",
                 "correu":"roger@itic.cat",
                 "curs":"2",
                 "mod":"M7"
                },
        'prof2':{"nom":"Juanma",
                 "cognom1":"Sànchez",
                 "cognom2":"Bel",
                 "correu":"juanma@itic.cat",
                 "curs":"2",
                 "mod":"M6"
                },
        'prof3':{"nom":"Xavi",
                 "cognom1":"Quesada",
                 "cognom2":"Puertas",
                 "correu":"xavi@itic.cat",
                 "curs":"2",
                 "mod":"M8"
                },
        'prof4':{"nom":"Oriol",
                 "cognom1":"Roca",
                 "cognom2":"Fabra",
                 "correu":"oriol@itic.cat",
                 "curs":"2",
                 "mod":"M9"
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
              },
        'al2':{"nom":"Facundo",
               "cognom1":"Calixto",
               "cognom2":"Barrios",
               "correu":"rulo@itic.cat",
               "curs":"1",
               },
        'al3':{"nom":"Angelo",
               "cognom1":"Montenegro",
               "cognom2":"Nose",
               "correu":"angelo@itic.cat",
               "curs":"2",
              },
        'al4':{"nom":"Oscar",
               "cognom1":"Perez",
               "cognom2":"Perez",
               "correu":"oscar@itic.cat",
               "curs":"2",
              },
        'al5':{"nom":"Angelo",
               "cognom1":"Montenegro",
               "cognom2":"Nose",
               "correu":"angelo@itic.cat",
               "curs":"2",
              },
        'al6':{"nom":"Adrià",
               "cognom1":"García",
               "cognom2":"Pèrez",
               "correu":"adria@itic.cat",
               "curs":"2",
              },
        'al7':{"nom":"Gemma",
               "cognom1":"Garrigosa",
               "cognom2":"Francés",
               "correu":"gemma@itic.cat",
               "curs":"2",
              },
        'al8':{"nom":"Oriana",
               "cognom1":"Saray",
               "cognom2":"Rojas",
               "correu":"oriana@itic.cat",
               "curs":"2",
              }}
    
    context = {'alm': alumnat}
    return render(request, 'index_alumnat.html', context)