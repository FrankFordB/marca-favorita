from ntpath import join

from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")


marcas_ingresadas = {
    "marcas": [],
    "marcas_cantidad": 0,
    }

# RESETEO DE MARCAS INGRESADAS

def nuevo_ingreso():
    marcas_ingresadas["marcas"]=[]
    marcas_ingresadas["marcas_cantidad"] = 0
    

# FORMATEO DE MARCAS INGRESADAS 
def formato():
    palabra = ""

    for i in marcas_ingresadas["marcas"]:
        palabra = palabra + i + " " 

    return palabra

# REPETICIONES DE LOS ELEMENTOS
def contar_repeticiones():
    repeticiones = {}
    for elemento in marcas_ingresadas["marcas"]:
        if elemento in repeticiones:
            repeticiones[elemento] += 1
        else:
            repeticiones[elemento] = 1
    return repeticiones

 
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    nuevo_ingreso()
    texto_cantidad = "Todavia no has ingresado ninguna marca"
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
               "marcas": formato(),            
               "marcas_cantidad": texto_cantidad,
               "repeticiones": formato(),
    }
    )

@app.post("/", response_class=HTMLResponse)
def enviar(
    request: Request,
    letra: str = Form(...)
):  
    letra = letra.capitalize()
    marcas_ingresadas["marcas"].append(letra)
    marcas_ingresadas["marcas_cantidad"] = len(marcas_ingresadas["marcas"])

    cantidad = marcas_ingresadas["marcas_cantidad"]

    if cantidad == 1:
        texto_cantidad = "Usted ingresó 1 marca"
    else:
        texto_cantidad = f"Usted ingresó {cantidad} marcas"

    repeticiones = contar_repeticiones()

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "marcas": formato(),
            "marcas_cantidad":  texto_cantidad,
            "repeticiones": repeticiones,
        }
    )
