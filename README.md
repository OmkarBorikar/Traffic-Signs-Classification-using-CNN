# Traffic-Signs-Classification-using-CNN

* **Overview of Project**

Goal of this project is to identify the traffic sign and display what the uploaded traffic sign is about. The Convolution Neural Network model used  is 
trained on 31367 number of images containing 43 different types of traffic signes.

* **About Dataset Used**

Dataset used for this project can be found here - [German Traffic Sign Recognition Benchmark](https://www.kaggle.com/meowmeowmeowmeowmeow/gtsrb-german-traffic-sign)
Train folder contains 43 different folders (numberd from 0 to 42) and in each folder there are images of traffic sign belonging to that class. There are almost 39200 images in Training 
folder.
Test folder contains 12600 images without any label for them for testing purpose.
As mentioned earlier , Training folder contains 43 folder and each folder belongs to one label and labels are as followed - 

            0:'Speed limit (20km/h)'
            1:'Speed limit (30km/h)'
            2:'Speed limit (50km/h)'
            3:'Speed limit (60km/h)'
            4:'Speed limit (70km/h)'
            5:'Speed limit (80km/h)'
            6:'End of speed limit (80km/h)'
            7:'Speed limit (100km/h)'
            8:'Speed limit (120km/h)'
            9:'No passing'
            10:'No passing veh over 3.5 tons'
            11:'Right-of-way at intersection'
            12:'Priority road'
            13:'Yield'
            14:'Stop'
            15:'No vehicles'
            16:'Vehicle > 3.5 tons prohibited'
            17:'No entry'
            18:'General caution'
            19:'Dangerous curve left'
            20:'Dangerous curve right'
            21:'Double curve'
            22:'Bumpy road'
            23:'Slippery road'
            24:'Road narrows on the right'
            25:'Road work'
            26:'Traffic signals'
            27:'Pedestrians'
            28:'Children crossing'
            29:'Bicycles crossing'
            30:'Beware of ice/snow'
            31:'Wild animals crossing'
            32:'End speed + passing limits'
            33:'Turn right ahead'
            34:'Turn left ahead'
            35:'Ahead only'
            36:'Go straight or right'
            37:'Go straight or left'
            38:'Keep right'
            39:'Keep left'
            40:'Roundabout mandatory',
            41:'End of no passing'
            42:'End no passing vehicle > 3.5 tons'
            
* **Overview of Web app**

This web app is deployed on streamlit share and can be accessed here - [Traffic Signs Identifier](https://share.streamlit.io/omkarborikar/traffic-signs-classification-using-cnn/main/app.py)

After opening the web app below page will load - 

![image](https://user-images.githubusercontent.com/82905366/144586157-4cdc69a8-33e2-44ab-a1a5-978518b09a49.png)

On side bar list of traffic signs is displayed from which this app can identify signs.

Upload traffic sign by clicking on Browse Files. For now user need to upload image which contains only traffic sign and no other objects. If image contains any other object then app may give incorrect output.

After uploading image click on Identify traffic sign - uploaded image will be displayed with its description as shown below.

