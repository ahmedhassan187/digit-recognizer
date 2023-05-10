import numpy as np
import matplotlib.pyplot as plt
import cv2
import tensorflow as tf
class Model():
    def __init__(self):
        self.model = tf.keras.models.load_model('./model_weights/model.h5')
    # def import_model(self):
    #     loaded_model = 
    #     self.model = loaded_model
    def process_image(self,image):
        image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        if image.shape[0] != 28 and image.shape[1] != 28:
            image = cv2.resize(image,(28,28))
        image_norm = image/255
        return image_norm
    def reshape_im(self,image):
        reshaped_image = image.reshape(1,28,28,1)
        return reshaped_image
    def prediction(self,image):
        predictions = self.model.predict(image)
        predicted_number = np.argmax(predictions)
        return predicted_number