from ntpath import join

from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")

# RESETEO DE MARCAS INGRESADAS
def nuevo_ingreso():
    marcas_ingresadas["marcas"]=[]
    marcas_ingresadas["marcas_cantidad"]=" "

# FORMATEO DE MARCAS INGRESADAS 
def formato():
    palabra = ""

    for i in marcas_ingresadas["marcas"]:
        palabra = palabra + i + " " 

    return palabra

marcas_ingresadas = {
    "marcas": [],
    "marcas_cantidad": " "
}




@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    nuevo_ingreso()
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "marcas": formato(),
            "marcas_cantidad": f"Usted ingreso {len(marcas_ingresadas['marcas'])} marcas"
        if len(marcas_ingresadas["marcas"]) > 0
        else "Usted no ingreso ninguna marca"
    }
    )
    
@app.post("/", response_class=HTMLResponse)
def enviar(
    request: Request,
    letra: str = Form(...)
):
    marcas_ingresadas["marcas"].append(letra)
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "marcas": formato(),
            "marcas_cantidad": len(marcas_ingresadas["marcas"]) 
        }
    )
