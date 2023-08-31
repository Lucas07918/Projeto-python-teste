from flask import Flask, render_template, redirect, request, flash, send_from_directory
import json
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = 'LALA'

@app.route('/')
def entrada():
     return render_template('botao.html')

@app.route('/gerarTodos')
def gerarTodos():
    with open('foundationDld.json', 'r') as comidasTemp:
        comidas = json.load(comidasTemp)
    descricoes_unicas = set()
    comidas_sem_duplicatas = []
    for i in comidas:
        descricao = i.get('description')
        if descricao not in descricoes_unicas:
                descricoes_unicas.add(descricao)
                comidas_sem_duplicatas.append(i)
    ramdomic = random.sample(comidas_sem_duplicatas, 3)
    cardapioNovo = []
    cardapioNovo = ramdomic    
    with open('cafeDaManha.json', 'w') as gravarTemp:
        json.dump(cardapioNovo, gravarTemp, indent=4)
    with open('foundationDld.json', 'r') as comidasTemp:
        comidas = random.sample(json.load(comidasTemp), 6)
    descricoes_unicas = set()
    comidas_sem_duplicatas = []
    for i in comidas:
        descricao = i.get('description')
        if descricao not in descricoes_unicas:
                descricoes_unicas.add(descricao)
                comidas_sem_duplicatas.append(i)
    ramdomic = random.sample(comidas_sem_duplicatas, 3)
    cardapioNovo = []
    cardapioNovo = ramdomic    
    with open('almoco.json', 'w') as gravarTemp:
        json.dump(cardapioNovo, gravarTemp, indent=4)
    return redirect('/home')

@app.route('/gerarCafeDaManha')
def gerarCafeDaManha():
    with open('foundationDld.json', 'r') as comidasTemp:
        comidas = random.sample(json.load(comidasTemp), 6)
        print(comidas)
    descricoes_unicas = set()
    comidas_sem_duplicatas = []
    for i in comidas:
        descricao = i.get('description')
        number = i.get('number')
        if descricao not in descricoes_unicas and number <= 500:
                descricoes_unicas.add(descricao)
                comidas_sem_duplicatas.append(i)
    ramdomic = random.sample(comidas_sem_duplicatas, 3)
    cardapioNovo = []
    cardapioNovo = ramdomic    
    with open('cafeDaManha.json', 'w') as gravarTemp:
        json.dump(cardapioNovo, gravarTemp, indent=4)
    return redirect('/home')

@app.route('/gerarAlmoco')
def gerarAlmoco():
    with open('foundationDld.json', 'r') as comidasTemp:
        comidas = random.sample(json.load(comidasTemp), 6)
    descricoes_unicas = set()
    comidas_sem_duplicatas = []
    for i in comidas:
        descricao = i.get('description')
        if descricao not in descricoes_unicas:
                descricoes_unicas.add(descricao)
                comidas_sem_duplicatas.append(i)
    ramdomic = random.sample(comidas_sem_duplicatas, 3)
    cardapioNovo = []
    cardapioNovo = ramdomic    
    with open('almoco.json', 'w') as gravarTemp:
        json.dump(cardapioNovo, gravarTemp, indent=4)
    return redirect('/home')

@app.route('/home')
def home():
    with open('cafeDaManha.json') as cardapioTemp:
        comida = json.load(cardapioTemp)
    with open('almoco.json') as almocoTemp:
        almoco = json.load(almocoTemp)
    return render_template('home.html', comidas = comida, almoco = almoco)

if __name__ in "__main__":
    app.run(debug=True)