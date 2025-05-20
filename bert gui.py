import streamlit as st
from load_dataset import dataset_to_text_2 # Replace with your actual data preparation script
from pre_train import pre_train # Replace with your actual training script

st.title('BERT Model Training Interface')

# Step 1: Data Preparation
st.header('Step 1: Data Preparation')
uploaded_file = st.file_uploader("Upload your data file", type=["csv", "xlsx", "txt"])
if uploaded_file is not None:
    if st.button('Generate TXT File'):
        dataset_to_text_2(uploaded_file)  # Function to generate .txt file
        st.success('TXT file generated successfully!')

# Step 2: Model Pre-Training
st.header('Step 2: Model Pre-Training')
if st.button('Start Pre-Training'):
    pre_train()  # Function to start pre-training
    st.success('Model pre-training initiated!')
