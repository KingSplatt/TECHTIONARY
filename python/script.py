# Aqui voy a intentar leer un jpg a ver si lo reconoce el tensorflow, también voy a usar pillow para darle tamaño a la imagen
# Las dependencias son: 
# pip install tensorflow pillow
# pip install keras

import tensorflow as tf
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input, decode_predictions
from PIL import Image
import numpy as np

ruta_imagen = 'python\\HDMI.jpg'  


print('De hecho no se correr python en vscode')

## To do: elegir un modelo que si sirva por dios
##model = tf.saved_model.load('https://tfhub.dev/tensorflow/ssd_mobilenet_v2/fpnlite_320x320/1')

def preparar_imagen(ruta_imagen, tamanio_imagen=(224, 224)):
    img = Image.open(ruta_imagen)
    img = img.resize(tamanio_imagen)
    img_array = np.array(img)
    img_array = np.expand_dims(img_array, axis=0) 
    img_array = preprocess_input(img_array) 
    return img_array

def predict_image(ruta_imagen):
    img_array = preparar_imagen(ruta_imagen)
    predictions = model.predict(img_array)
    decoded_preds = decode_predictions(predictions, top=1)[0][0] 
    return decoded_preds[1], decoded_preds[2]  # Nombre de la clase y probabilidad




nombre, confianza = predict_image(ruta_imagen)
print(f"Predicción: {nombre}, Confianza: {confianza:.2f}")