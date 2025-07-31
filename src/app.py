from flask import Flask, render_template, request, redirect, url_for, flash,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, logout_user, login_required
import random
import datetime

from config import config

#Models
from models.ModelUser import ModelUser
from models.ModelEjercicio import ModelEjercicio
from models.ModelUserRutina import ModelUserRutina

#Entities
from models.entities import User, Ejercicio


app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://neondb_owner:npg_RsXCf5J7Ltmn@ep-lingering-salad-a2ump1k5-pooler.eu-central-1.aws.neon.tech/neondb?sslmode=require"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

login_manager_app = LoginManager(app)

@login_manager_app.user_loader
def load_user(id):
    return ModelUser.get_by_id(db,id)

@app.route('/')
def index():
    return redirect(url_for('Login'))

@app.route('/Login', methods=['GET','POST'])
def Login():
    if request.method=='POST':

        user = User.User(None, None,None,request.form['username'], request.form['password'],None,None,None)
        logged_user = ModelUser.login(db, user)

        if logged_user != None:
            if logged_user.password:
                print(logged_user.password)
                login_user(logged_user)
                return redirect(url_for('home'))
            else:
                flash("Invalid password...")
                return render_template('auth/login.html')
        else:
            flash("User not found...")
            return render_template('auth/login.html')

    else:
        return render_template('auth/login.html')
    
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('Login'))

@app.route('/supervisar')
def supervisar():
    graficaPorDia = ModelUserRutina.get_dia(db)
    #ejerciciosArr = ModelEjercicio.get_all(db)
    #ejerciciosArr = ModelEjercicio.get_musculo(db)
    por_semana = []
    por_mes = []
    
    return render_template('supervisar2.html',ejercicios=graficaPorDia,por_semana=por_semana, por_mes=por_mes)

@app.route('/home')
@login_required
def home():
    return render_template('home.html')

@app.route('/ejercicio/', defaults={'tipo': None, 'rutina': None})
@app.route('/ejercicio/<tipo>/', defaults={'rutina': None})
@app.route('/ejercicio/<tipo>/<rutina>')
@login_required
def ejercicio(tipo,rutina):
    ejerciciosArr= [] 
    if rutina:
        if tipo == '1':
            ejerciciosArr = ModelEjercicio.get_dificultad(db)
        elif tipo == '2':
            ejerciciosArr = ModelEjercicio.get_all(db)
            ejerciciosArr = ModelEjercicio.get_musculo(db, rutina)
    else:
        ejerciciosArr = ModelEjercicio.get_all(db)
    random.shuffle(ejerciciosArr)
    
    return render_template('ejercicio.html',ejercicios=ejerciciosArr, tipo=tipo, rutina=rutina)

@app.route('/ejercicioPorDificultad')
@login_required
def ejercicioPorDificultad():
   
    return render_template('ejercicioPorDificultad.html')

@app.route('/ejercicioPorMusculo')
@login_required
def ejercicioPorMusculo():
    
    return render_template('ejercicioPorMusculo.html')

@app.route('/ejercicioPorMusculo/<rutina>')
@login_required
def ejercicioPorMusculoEspecifico(rutina):
    ejerciciosArr= [] 
    ejerciciosArr= ModelEjercicio.get_musculo(db,rutina)
    random.shuffle(ejerciciosArr)
    
    return render_template('ejercicioPorMusculo.html',ejercicios=ejerciciosArr)

@app.route('/rutinaCompletada/<id_user>')
@login_required
def rutinaCompletada(id_user):
    ModelUserRutina.guardarProgreso(db,id_user)
    return render_template('rutinaCompletada.html')




if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run()