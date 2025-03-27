from flask import Flask, request
import uuid

app = Flask(__name__)

lista = []

@app.route("/soma", methods=["POST"])
def somar():
    global dados_recebidos
    global n1
    global n2
    global resultado

    dados_recebidos =  request.get_json()
    n1 = dados_recebidos["n1"]
    n2 = dados_recebidos["n2"]
    resultado = n1 + n2
    id = str(uuid.uuid4())

    lista.append({"ID": id, "Número 1" : n1, "Número 2": n2, "Conta": str(n1)+"+"+str(n2), "Resultado": resultado})

    return {"Resultado" : resultado}

@app.route("/deletar/<id>", methods=["DELETE"])
def deletar(id):
    global lista
    lista = [d for d in lista if d.get("ID") != id]
    return {"Lista" : lista}

@app.route("/calculos", methods=["GET"])
def calculos():
    return {"Lista" : lista}

@app.route("/editar/<id>", methods=["PUT"])
def editar(id):
    global lista

    dados_recebidos =  request.get_json()
    n1 = dados_recebidos["n1"]
    n2 = dados_recebidos["n2"]

    listatemp = []

    for conta in lista:
        if conta['ID'] == id:
            resultado = n1 + n2
            listatemp.append({"ID": id, "Número 1" : n1, "Número 2": n2, "Conta": str(n1)+"+"+str(n2), "Resultado": resultado})
        else:
            listatemp.append(conta)
    lista = listatemp
                
    return {"Lista" : lista}

#.venv/Scripts/activate