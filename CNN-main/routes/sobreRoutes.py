from controllers.sobreController import Sobre
from flask import Flask, render_template, request, jsonify

def sobreRoutes(app):
    app.route('/', methods=['GET'])(Sobre)
