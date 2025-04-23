from flask import Flask, request
import uuid
import psycopg

# Importa Flask, uuid e psycopg

app = Flask(__name__)
conection_db = psycopg.connect("dbname=turma3f user=postgres password=3f@db host=164.90.152.205 port=80")

# Cria a aplicação flask e estabelece uma conexão ao banco de dados turma3f

@app.route('/pessoas', methods=['POST'])
def incluir_pessoa():
    dados_recebidos = request.get_json()
    id = uuid.uuid4()
    nome = dados_recebidos['nome']
    cursor = conection_db.cursor()
    cursor.execute("insert into PESSOAS (id,nome) values (%s,%s)", (id, nome))
    conection_db.commit()
    return{
        "id": id
    }

# Inclui pessoas na tabela PESSOAS, com o id sendo auto-incrementado

psycopg.connect("dbname=turma3f user=postgres password=3f@db host=164.90.152.205 port=80")

@app.route('/vendas', methods=['GET'])
def get_vendas():
    cursor = conection_db.cursor()
    cursor.execute("select * from vendas left join pessoas on vendas.id_pessoa = pessoas.id left join produtos on vendas.id_produto = produtos.id")
    lista = []
    for item in cursor:
        lista.append({
            "id": item[0],
            "pessoa": {
                "id": item[1],
                "nome" : item[4]
            },
            "produto" : {
                "id" : item[2],
                "nome" : item[6],
                "preço" : item[7]
            }
        })
    return lista

# Retorna todas as vendas com suas informações

@app.route('/vendas', methods=['POST'])
def incluir_venda():
    dados_recebidos = request.get_json()
    id = uuid.uuid4()
    id_pessoa = dados_recebidos['id_pessoa']
    id_produto = dados_recebidos['id_produto']
    cursor = conection_db.cursor()
    cursor.execute("insert into VENDAS (id, id_pessoa, id_produto) values (%s,%s,%s)", (id, id_pessoa, id_produto))
    conection_db.commit()
    return{
        "id": id
    }

#Inclui uma venda na tabela VENDAS

@app.route('/pessoas', methods=['GET'])
def get_pessoas():
    cursor = conection_db.cursor()
    cursor.execute("select id, nome from pessoas order by nome")
    lista = []
    for item in cursor:
        lista.append({
            "id": item[0],
            "nome": item[1]
        })
    return lista

# Retorna todas as pessoas em ordem A-z

@app.route('/pessoas', methods=['PUT'])
def atualizar_pessoa():
    dados_recebidos = request.get_json()
    nome = dados_recebidos['nome']

    cursor = conection_db.cursor()
    cursor.execute("update pessoas set nome = %s where id = %s", (nome, id))
    conection_db.commit()
    return {
        "id": id,
    }

# Atualiza o nome de uma pessoa por meio do seu id