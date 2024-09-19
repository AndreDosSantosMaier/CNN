from flask import Flask, render_template, request

def Guia():
    if request.method == 'GET':
        return render_template('guia.html')
    else:
        return {
            'status': 405,
            'message': "Método não aceito"
        }, 405
