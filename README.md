# potato_disease_detection
#How to Run:
1.Set up streamlit in your machine $ pip install streamlit

2.Clone the repository 'git clone https://github/S2I-D4TT0/potato_disease_detection'

3.Navigate to the repository directory.

4. Run $ streamlit main.py 
  

#Using the tool:
1)After local hosting , you can upload image by clicking upload image button or capturing image using camera can be done by clicking Take image button.

2)After uploading/capture you can preview your image before clicking predict button. Then click Predict button to get your results and rate your experience out of scale from 1 to 5.

3)If any error occurred do try refreshing the page 


#About the Prediction Model:
In this project, we have employed a detection model trained on a diverse array of potato leaf disease images sourced from the **plant_village** dataset and many other datasets combinely we acquired a dataset size of about 10000 images and hence which increases our accuracy pretty much than others.

For an in-depth exploration of the model's inner workings, including its architecture, data preprocessing methodologies, feature extraction techniques, and the model's accuracy, I encourage you to delve into the accompanying Jupyter notebook:

📘 [Explore Model Details](https://github.com/S2I-D4TT0/potato_disease_detection/blob/main/potato-disease-classifier.ipynb)

After training the model using the above techniques I got a training accuracy of 0.9932 and a validation accuracy of 0.9900

