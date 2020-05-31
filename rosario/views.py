import datetime
from django.shortcuts import render

def home(request):

# 0 é segunda-feira
# 1 é terça-feira
# 2 é quarta-feira
# 3 é quinta-feira
# 4 é sexta-feira
# 5 é sábado
# 6 é domingo
    
    hoje = datetime.datetime.today()
    diasemana = hoje.weekday()

    misterio = ""
    saida = ""
    if (diasemana == 0 | diasemana == 5):
        misterio = "gozosos"        
    if (diasemana == 1 | diasemana == 4):
        misterio = "dolorosos"
    if (diasemana == 2 | diasemana == 6):
        misterio = "gloriosos"
    if (diasemana == 3):
        misterio = "luminosos"

    saida = "rosario/" + misterio + ".html"

    return render(request, saida, {'misterio': misterio})
