from flask import Flask, render_template, request

def Sobre():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        return {
            'status': 405,
            'message': "Método não aceito"
        }, 405
