from flask import Flask, request, jsonify, render_template
import sqlite3

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

def salvar_contato(nome, email, mensagem):
    conn = sqlite3.connect("bemfarma.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO contato (nome, email, mensagem)
        VALUES (?, ?, ?)
    """, (nome, email, mensagem))

    conn.commit()
    conn.close()

@app.post("/contato")
def receber_contato():
    dados = request.get_json()
    salvar_contato(dados["nome"], dados["email"], dados["mensagem"])
    return jsonify({"status": "sucesso", "mensagem": "Contato enviado!"})

if __name__ == "__main__":
    app.run(debug=True)
