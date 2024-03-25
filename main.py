from flask import Flask, render_template

app = Flask(__name__)

# Rota para a página inicial
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/quem_somos')
def quem_somos():
    return render_template('quem_somos.html')

# Executando a aplicação Flask
if __name__ == '__main__':
    app.run(debug=True)
