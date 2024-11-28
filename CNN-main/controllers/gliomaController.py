from flask import Flask, render_template, request

def Glioma():
    if request.method == 'GET':
        return render_template('glioma.html')
    else:
        return {
            'status': 405,
            'message': "Método não aceito"
        }, 405
