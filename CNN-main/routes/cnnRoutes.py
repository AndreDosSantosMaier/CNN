from controllers.cnnController import cnn
from flask import Flask, render_template, request, jsonify

def cnnRoutes(app):
    app.route('/api/cnn', methods=['POST'])(cnn)
    app.route('/', methods=['GET'])(cnn)
