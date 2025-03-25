from flask import Flask, request

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

    lista.append(f'Número 1: {n1} / Número 2: {n2} / Conta: {n1} + {n2} / Resultado: {resultado}')

    return {"Resultado" : resultado}

@app.route("/calculos", methods=["GET"])
def calculos():
    return {"Lista" : lista}

#.venv/Scripts/activate