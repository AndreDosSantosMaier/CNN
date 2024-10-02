from controllers.guiaController import Guia
from flask import Flask, render_template, request, jsonify

def guiaRoutes(app):
    app.route('/guia', methods=['GET'])(Guia)
