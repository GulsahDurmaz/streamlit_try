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

# File ID from the shareable link
# Correct URL for gdown
file_id = '1UWrfKj-YtbFwsixUs-SG4U35QncgpONI'
url = f'https://drive.google.com/uc?id={file_id}'  # Use the direct download link


# Download the CSV file
output = 'joebiden.csv'
gdown.download(url, output, quiet=False)

# Load the CSV into pandas
biden_df = pd.read_csv(output, encoding='utf-8', lineterminator='\n')

st.dataframe(biden_df.head(3))

