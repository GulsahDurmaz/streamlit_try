# streamlit.py
from imports import *
import eda

# Configure the Streamlit page
st.set_page_config(page_title="2020 US Presidential Election Dashboard",
                   page_icon=":bar_chart:",
                   initial_sidebar_state="expanded")

# Apply custom styles
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

st.sidebar.header('US Presidential Election Dashboard `2020`')

# Load the country_percentage_analysis.csv into pandas
country_percentage_analysis_df = pd.read_csv("country_percentage_analysis.csv", encoding='utf-8', lineterminator='\n')
trump_hourly_df = pd.read_csv("trump_hourly.csv", encoding='utf-8', lineterminator='\n')
biden_hourly_df = pd.read_csv("biden_hourly.csv", encoding='utf-8', lineterminator='\n')

# Tarih sütununu datetime formatına dönüştür
trump_hourly_df['created_at'] = pd.to_datetime(trump_hourly_df['created_at'], errors='coerce')
biden_hourly_df['created_at'] = pd.to_datetime(biden_hourly_df['created_at'], errors='coerce')

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

# Display content based on the active page
if st.session_state.page == 'Exploratory Data Analysis':
    eda.run_exploratory_data_analysis(trump_hourly_df, biden_hourly_df, country_percentage_analysis_df)  # Call the function from eda.py
