# streamlit.py
from imports import *

# Configure the Streamlit page
st.set_page_config(page_title="2020 US Presidential Election Dashboard",
                   page_icon=":bar_chart:",
                   initial_sidebar_state="expanded")

# Apply custom styles
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

st.sidebar.header('US Presidential Election Dashboard `2020`')

# Download the donaldtrump.csv file
file_id_trump = '1Q5XKzaaHTXrXIT_W2kWyBkTSmWg4uANU'
url = f'https://drive.google.com/uc?id={file_id_trump}' 

output_trump = 'donaldtrump.csv'
gdown.download(url, output_trump, quiet=False)

# Load the donaldtrump.csv into pandas
trump_df = pd.read_csv(output_trump, encoding='utf-8', lineterminator='\n')

# Download the joebiden.csv file
file_id_biden = '1UWrfKj-YtbFwsixUs-SG4U35QncgpONI'
url = f'https://drive.google.com/uc?id={file_id_biden}'  # Use the direct download link

output = 'joebiden.csv'
gdown.download(url, output, quiet=False)

# Load the joebiden.csv into pandas
biden_df = pd.read_csv(output, encoding='utf-8', lineterminator='\n')

st.dataframe(trump_df.head(3))
st.dataframe(biden_df.head(3))

# Initialize page state
if 'page' not in st.session_state:
    st.session_state.page = 'Exploratory Data Analysis'  # Default page

# Sidebar buttons for page navigation
if st.sidebar.button("Exploratory Data Analysis"):
    st.session_state.page = 'Exploratory Data Analysis'

if st.sidebar.button("World Popularity Analysis"):
    st.session_state.page = 'World Popularity Analysis'

if st.sidebar.button("US Popularity Analysis"):
    st.session_state.page = 'US Popularity Analysis'

if st.sidebar.button("Sentimental Data Analysis"):
    st.session_state.page = 'Sentimental Data Analysis'

if st.sidebar.button("Dataset"):
    st.session_state.page = 'Dataset'
