import streamlit as st
from PIL import Image
import numpy as np
from keras.models import load_model
import keras as keras
from keras.preprocessing.image import load_img ,img_to_array
import warnings
warnings.filterwarnings("ignore")

# Load the Keras model
model = load_model('model.h5')
class_names = ["EarlyBlight", "LateBlight", "Healthy"]


def predict(image):
    test_image = image.resize((256, 256))
    test = img_to_array(test_image)
    test /= 255.0
    test = np.array(test)
    prediction = model.predict(test.reshape(1, 256, 256, 3))  # Reshape for model compatibility
    predicted_class_index = np.argmax(prediction)
    predicted_class = class_names[predicted_class_index] if class_names else str(predicted_class_index)
    confidence_score = int(100 * prediction[0][predicted_class_index])
    return predicted_class, confidence_score
    
    
def upload_page():
    st.title("Upload Image")
    col1,col2,col3 = st.columns([1,3,1])
    with col1:
        if st.button("Back",key="capture_back",on_click=lambda: st.session_state.update(page="home")):
            pass
    file_uploader = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"], accept_multiple_files=False, key="upload")

    if file_uploader is not None:
        # Display the uploaded image
        uploaded_image = Image.open(file_uploader)
        st.image(uploaded_image, caption='Uploaded Image', use_column_width=True)
        
        # Preprocess the uploaded image
        #target_shape = (1, 719, 1280, 3)  # Target shape expected by the model
       
        upload_captured_button = st.button("Predict")
        if upload_captured_button:
            try:
                predicted_class,accuracy= predict(uploaded_image)
                if predicted_class == "Healthy":
                    st.write("Hurray! Your leaf is", predicted_class,"with accuracy ",accuracy)
                else:
                    st.write("Your leaf is infected with", predicted_class,"with accuracy" ,accuracy, ".")
                rating_input = st.text_input("Rate from 1 to 5 (whole numbers only):")
    
                if rating_input.strip():  # Check if the input is not empty
                    try:
                        rating = int(rating_input)
                        if 1 <= rating <= 5:
                            if rating >= 4:
                                st.write("😃 Thank you for your positive feedback!")
                            elif rating < 3:
                                st.write("😔 We're sorry to hear that. How can we help?")
                            else:
                                st.write("Please enter a valid rating between 1 and 5.")
                    except ValueError:
                        st.write("Please enter a valid integer rating between 1 and 5.")

            except Exception as e:
               st.error(f"Error occurred: {str(e)}")
               

                 
            
        
def capture_page():
    st.title("Capture Image")
    col1,col2,col3 = st.columns([1,3,1])
    with col1:
        if st.button("Back",key="capture_back",on_click=lambda: st.session_state.update(page="home")):
            pass
    captured_image = st.camera_input("", key="capture")

    if captured_image is not None:
        image = Image.open(captured_image)
        # st.image(image, caption='Captured Image', use_column_width=True)
        
        upload_captured_button = st.button("Predict")
        if upload_captured_button:
            try:
                predicted_class,accuracy = predict(captured_image)
                if predicted_class == "Healthy":
                    st.write("Hurray! Your leaf is", predicted_class,"with accuracy",accuracy)
                else:
                    st.write("Your leaf is infected with", predicted_class,"with accuracy",accuracy,".")
                    rating_input = st.text_input("Rate from 1 to 5 (whole numbers only):")
    
                if rating_input.strip():  # Check if the input is not empty
                    try:
                        rating = int(rating_input)
                        if 1 <= rating <= 5:
                            if rating >= 4:
                                st.write("😃 Thank you for your positive feedback!")
                            elif rating < 3:
                                st.write("😔 We're sorry to hear that. How can we help?")
                            else:
                                st.write("Please enter a valid rating between 1 and 5.")
                    except ValueError:
                        st.write("Please enter a valid integer rating between 1 and 5.")

            except Exception as e:
               st.error(f"Error occurred: {str(e)}")

               
def home_page():
    
    st.title("Potato leaf disease predictor")
    st.markdown(
        """
        <style>
        body {
            background-color: #ffffff;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    icon = Image.open('img.jpeg')  # Replace "path/to/your/icon.png" with the actual path to your icon image
    
    st.image(icon, use_column_width=True)
    st.write(" ")

    col1, col2,col3 = st.columns(3)
    with col1:
        if st.button("Upload File", key="upload_button", on_click=lambda: st.session_state.update(page="upload")):
            pass
    with col3:
        if st.button("Take Photo", key="capture_button", on_click=lambda: st.session_state.update(page="capture")):
            pass


def main():
    st.set_page_config(page_title="Upload or Take a Picture")

    if "page" not in st.session_state:
        st.session_state.page = "home"

    pages = {
        "home": home_page,
        "upload": upload_page,
        "capture": capture_page,
    }

    pages[st.session_state.page]()

if __name__ == "__main__":
    main()