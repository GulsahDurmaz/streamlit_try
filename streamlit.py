import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import pycountry
import streamlit as st
import gdown

from data_loader import *

# Configure the Streamlit page
st.set_page_config(page_title="2020 US Presidential Election Dashboard",
                #    layout='wide',
                   page_icon=":bar_chart:",
                   initial_sidebar_state="expanded")

def main():
    st.title("My Streamlit App")
    st.write("Hello, world!")

if __name__ == "__main__":
    main()

file_id_trump = '1Q5XKzaaHTXrXIT_W2kWyBkTSmWg4uANU'
url = f'https://drive.google.com/uc?id={file_id_trump}' 

# Download the CSV file
output_trump = 'donaldtrump.csv'
gdown.download(url, output_trump, quiet=False)

# Load the CSV into pandas
trump_df = pd.read_csv(output_trump, encoding='utf-8', lineterminator='\n')

# File ID from the shareable link
# Correct URL for gdown
file_id = '1UWrfKj-YtbFwsixUs-SG4U35QncgpONI'
url = f'https://drive.google.com/uc?id={file_id}'  # Use the direct download link


# Download the CSV file
output = 'joebiden.csv'
gdown.download(url, output, quiet=False)

# Load the CSV into pandas
biden_df = pd.read_csv(output, encoding='utf-8', lineterminator='\n')

st.dataframe(trump_df.head(3))
st.dataframe(biden_df.head(3))

