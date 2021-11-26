import pandas as pd
import streamlit as st
from keras.models import load_model
from PIL import Image,ImageOps
import numpy as np
import matplotlib.pyplot as plt
import cv2
from streamlit.proto.RootContainer_pb2 import SIDEBAR

st.title("Traffic Signs Identifier")

uploaded_file = st.file_uploader("Upload the traffic sign", type="png")



classes = { 0:'Speed limit (20km/h)',
            1:'Speed limit (30km/h)',
            2:'Speed limit (50km/h)',
            3:'Speed limit (60km/h)',
            4:'Speed limit (70km/h)',
            5:'Speed limit (80km/h)',
            6:'End of speed limit (80km/h)',
            7:'Speed limit (100km/h)',
            8:'Speed limit (120km/h)',
            9:'No passing',
            10:'No passing veh over 3.5 tons',
            11:'Right-of-way at intersection',
            12:'Priority road',
            13:'Yield',
            14:'Stop',
            15:'No vehicles',
            16:'Vehicle > 3.5 tons prohibited',
            17:'No entry',
            18:'General caution',
            19:'Dangerous curve left',
            20:'Dangerous curve right',
            21:'Double curve',
            22:'Bumpy road',
            23:'Slippery road',
            24:'Road narrows on the right',
            25:'Road work',
            26:'Traffic signals',
            27:'Pedestrians',
            28:'Children crossing',
            29:'Bicycles crossing',
            30:'Beware of ice/snow',
            31:'Wild animals crossing',
            32:'End speed + passing limits',
            33:'Turn right ahead',
            34:'Turn left ahead',
            35:'Ahead only',
            36:'Go straight or right',
            37:'Go straight or left',
            38:'Keep right',
            39:'Keep left',
            40:'Roundabout mandatory',
            41:'End of no passing',
            42:'End no passing vehicle > 3.5 tons' }

class_values = classes.values()

st.sidebar.header("This app is trained on below list of traffic signs.")
st.sidebar.selectbox(' ',options = class_values)

if st.button("Identify traffic sign"):

    def image_processing(img):
        model = load_model('archive/training/TSR.h5')
        data=[]
        image_og = Image.open(uploaded_file)
        # image_og = cv2.imread('image_og.png')
        # img_array = cv2.imread('/home/omkar/CNN proj/images.png',0)  # convert to array
        img_array = ImageOps.grayscale(image_og)
        img_array = np.array(img_array)
        new_array = cv2.resize(img_array, (30, 30))
        new_array = new_array.reshape(-1,30,30,1)
        Y_pred = model.predict(new_array)

        return image_og,Y_pred


    st.header("Uploaded image is :")
    plot,res = image_processing(uploaded_file)
    final_plot = plot.resize((1920,1080))
    st.image(final_plot)

    final_res = np.argmax(res,axis=1)
    st.write(classes[final_res[0]])