import streamlit as st
import pandas as pd
import joblib

# Define a dictionary to map pet types to integers
pet_mapping = {
    'Dog': 0,
    'Cat': 1,
    'Rabbit': 2,
    'Turtle': 3,
    'Lizard': 4,
    'Chameleon': 4,
    'Crocodile': 5,
    'Frog': 6,
    'Gecko': 7,
    'Iguana': 8,
    'Salamander': 9,
    'Snake': 10,
    'Toad': 11,
    'Tortoise': 12,
    'Bird':13
}
size_mapping = {
    'Small': 0,
    'Medium': 1,
    'Large': 2
}
gender_mapping = {
    'Male': 0,
    'Female': 1,
}

vaccination_mapping = {'Vaccinated': 0, 'Not Vaccinated': 1}
spaying_mapping = {'Spayed/Neutered': 0, 'Not Spayed/Neutered': 1}
behavior_mapping = {'Friendly': 0, 'Shy': 1, 'Energetic': 2,'Aggressive':3}
medical_history_mapping = {'Healthy': 0, 'Minor Health Issues': 1, 'Chronic Condition': 2}
location_mapping = {'Shelter': 0, 'Rescue Organization': 1}
color_mapping = {'Brown': 0, 'Black': 1, 'White': 2, 'Spotted': 3, 'Mixed': 4}
specialcharecter_mapping = {'Playful': 0, 'Calm': 1, 'Loyal': 2, 'Affectionate': 3, 'Active': 4,'Aggressive':5}
diet_mapping = {'Dry food': 0, 'Canned food': 1, 'Mixed diet': 2}
training_mapping = {'Basic': 0, 'Advanced': 1, 'None': 2}

# Streamlit setup
st.title('Pet Adoption Prediction App')

pet = st.selectbox('Pet Type', list(pet_mapping.keys()))
age = st.slider('Age', 1, 20, 1)
weight = st.slider('Weight (kg)', 1, 20, 1)
size = st.selectbox('Size', list(size_mapping.keys()))
gender = st.selectbox('Gender', list(gender_mapping.keys()))
vaccinating = st.selectbox('Vaccination Status', list(vaccination_mapping.keys()))
spaying = st.selectbox("Spaying/Neutering Status", list(spaying_mapping.keys()))
behavior = st.selectbox("Behavior", list(behavior_mapping.keys()))
medical_history = st.selectbox("Medical History", list(medical_history_mapping.keys()))
location = st.selectbox("Location", list(location_mapping.keys()))
color = st.selectbox("Color", list(color_mapping.keys()))
specialcharecter = st.selectbox("Special Characteristics", list(specialcharecter_mapping.keys()))
previousowner = st.slider('Previous Owners', 1, 3, 1)
diet = st.selectbox("Diet", list(diet_mapping.keys()))
training = st.selectbox("Training Level", list(training_mapping.keys()))

# Create input data as a dictionary
input_data = {
    'Pet Type': [pet_mapping[pet]],
    'Age': [age],
    'Size': [size_mapping[size]],
    'Gender': [gender_mapping[gender]],
    'Vaccination Status': [vaccination_mapping[vaccinating]],
    'Spaying/Neutering Status': [spaying_mapping[spaying]],
    'Behavior': [behavior_mapping[behavior]],
    'Medical History': [medical_history_mapping[medical_history]],
    'Location': [location_mapping[location]],
    'Color': [color_mapping[color]],
    'Weight (kg)': [weight],
    'Special Characteristics': [specialcharecter_mapping[specialcharecter]],
    'Previous Owners': [previousowner],
    'Diet': [diet_mapping[diet]],
    'Training Level': [training_mapping[training]]
}

# Create a DataFrame for the test data
test_df = pd.DataFrame(input_data)

# Define model names
model_names = ['Logistic Regression']

# Load the Logistic Regression model
loaded_logistic_reg_model = joblib.load('logistic_regression_model.pkl')

# Create a button to make predictions
if st.button('Predict Adoption'):
    # Predict with the Logistic Regression model
    logistic_reg_prediction = loaded_logistic_reg_model.predict(test_df)

    # Display the Logistic Regression prediction
    if logistic_reg_prediction[0] == 0:
        st.write('Logistic Regression Model Prediction: Not Adoptable')
    else:
        st.write('Logistic Regression Model Prediction: Adoptable')


