import datetime


def home():
    
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
    print (misterio)
    print(diasemana)

home()
