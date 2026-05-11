"""
Esse arquivo é um exemplo de controller
"""

from flask import Blueprint, request, redirect, url_for, render_template, flash, session
from werkzeug.security import check_password_hash, generate_password_hash

from database import db
from models import User

bp = Blueprint(__name__, "HomeController")

@bp.route("/") # cria uma rota
def index(): # função que gerencia rota
    """ Página inicial"""
    if '_user_id' not in session:
        return redirect(url_for("auth.login"))
    
    return render_template("dashboard/index.html") # Renderiza um template
    
@bp.route("/dashboard") # cria uma rota
def dashboard(): # função que gerencia rota
    """ Painel de Vendas """
    #remova o login

    import locale
    # Define para o padrão brasileiro
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8') 

    vendas: list = [
        {"mes":"Janeiro", "total":139519.19},
        {"mes":"Fevereiro", "total":143225.55},
        {"mes":"Marco", "total":205434.00},
        {"mes":"Abril", "total":178765.01},
        {"mes":"Maio", "total":156457.70},
        {"mes":"Junho", "total":106543.43},
        {"mes":"Julho", "total":167632.11},
        {"mes":"Agosto", "total":194436.88},
        {"mes":"Setembro", "total":118657.09},
        {"mes":"Outubro", "total":125494.50},
        {"mes":"Novembro", "total":144356.22},
        {"mes":"Dezembro", "total":208854.00},
    ] #fim lista vendas

    # if 'user' not in session:
    #     return redirect(url_for("auth.login"))
    
    return render_template("dashboard/index.html", vendas=vendas, locale=locale) # Renderiza um template
