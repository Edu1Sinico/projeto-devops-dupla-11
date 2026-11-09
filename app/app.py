import os

from flask import Flask, jsonify

# ===== VARIAÇÃO DA DUPLA ====

NOME_DUPLA = "dupla-11"
MENSAGEM = "Ola, bem-vindo(a) a API da dupla 11!"
PORTA = 5000

# ==================================================
VERSAO = os.environ.get("APP_VERSION", "v1")

app = Flask(__name__)

@app.route("/saude")
def saude():
    return jsonify(status="ok", versao=VERSAO)

@app.route("/aluno")
def aluno():
    return jsonify(dupla=NOME_DUPLA, mensagem=MENSAGEM)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORTA)