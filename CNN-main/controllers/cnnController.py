from flask import Flask, render_template, request, jsonify
import pybase64
import tensorflow as tf
from keras import preprocessing
from tensorflow import image
import numpy as np
import io
from PIL import Image
import os
import matplotlib.pyplot as plt
from base64 import b64encode
from json import dumps


classes = [
    "glioma",
    "meningioma",
    "notumor",
    "pituitary"
]
#lista de paths de modelos de CNN
models = ["./model/d.keras","./model/e.keras","./model/b.keras","./model/normalizado.keras","./model/3.keras","./model/32batches.keras","./model/ruim.keras"]

#função para fazer a previsão do tipo de tumor
def predict(path):
    data = request.get_json()
    image_data = pybase64.b64decode(data['foto'])
    image_file = io.BytesIO(image_data)
    img = Image.open(image_file).convert('RGB')
    img = img.resize((128, 128))

    img_array = tf.keras.utils.img_to_array(img)
    img_array = img_array / 255.0  # Normalizar a imagem
    img_array = np.expand_dims(img_array, axis=0)

    # Verifique se o modelo existe
    model_path = path
    if not os.path.exists(model_path):
        raise FileNotFoundError(
            f"Modelo não encontrado no caminho: {model_path}")

    # Carregar o modelo salvo no formato Keras
    saved_model = tf.keras.models.load_model(model_path)
    prediction = saved_model.predict(img_array)
    pred_index = np.argmax(prediction)
    return classes[pred_index] #retorna o nome do tumor
     

def cnn():

    results = []

    if request.method == 'POST':
        try:
            for i in models:
                disease_name = predict(i)
                results.append(disease_name)
            percentg = round((len(list(filter(lambda ele: ele == "glioma", results))) / len(results)) * 100) 
            percentp = round((len(list(filter(lambda ele: ele == "pituitary", results))) / len(results)) * 100)
            percentm = round((len(list(filter(lambda ele: ele == "meningioma", results))) / len(results)) * 100)
            percentn = round((len(list(filter(lambda ele: ele == "notumor", results))) / len(results)) * 100)

            #retorna a data pro index 
            return {
                'status': 200,
                'message': "Requisição funcionou",
                'prediction': results, #retorna a lista de resultados de todas as CNN's
                'glioma': percentg,  #retorna a porcentagem de chance pra cada tipo de tumor
                'pituitary': percentp,
                'meningioma': percentm,
                'notumor': percentn,
            
            
            }
        except Exception as error:
            return {
                'status': 400,
                'message': "Não foi possível enviar a imagem.",
                'error': str(error)
            }, 400
        

    elif request.method == 'GET':
        return render_template('index.html')
    else:
        return {
            'status': 405,
            'message': "Método não aceito"
        }, 405
