from flask import Flask, render_template, request

def Meningioma():
    if request.method == 'GET':
        return render_template('meningioma.html')
    else:
        return {
            'status': 405,
            'message': "Método não aceito"
        }, 405
