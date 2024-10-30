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

# Load the dataframes
file_id_percentage_analysis = '1txBTA2dmdbSE2vF4w_IkTu88bIQcP9IT'
url = f'https://drive.google.com/uc?id={file_id_percentage_analysis}'

output_country_percentage = 'country_percentage_analysis.csv'
gdown.download(url, output_country_percentage, quiet=False)

country_percentage_analysis_df = pd.read_csv(output_country_percentage, encoding='utf-8', lineterminator='\n')

# file_id_trump = '1WpETEa2HRT3JX-0w-7ZrzPu_8M10UB8W'
# url = f'https://drive.google.com/uc?id={file_id_trump}'

# output_trump = 'trump_hourly.csv'
# gdown.download(url, output_trump, quiet=False)

# trump_hourly_df = pd.read_csv(output_trump, encoding='utf-8', lineterminator='\n')

# file_id_biden = '1mqju0IZTdPP6Ug-Ipl1S6kvsIkN9-7MH'
# url = f'https://drive.google.com/uc?id={file_id_biden}'

# output_biden = 'biden_hourly.csv'
# gdown.download(url, output_biden, quiet=False)

# biden_hourly_df = pd.read_csv(output_biden, encoding='utf-8', lineterminator='\n')

# country_percentage_analysis_df = pd.read_csv("country_percentage_analysis.csv", encoding='utf-8', lineterminator='\n')
# trump_hourly_df = pd.read_csv("trump_hourly.csv", encoding='utf-8', lineterminator='\n')
# biden_hourly_df = pd.read_csv("biden_hourly.csv", encoding='utf-8', lineterminator='\n')

# Tarih sütununu datetime formatına dönüştür
# trump_hourly_df['created_at'] = pd.to_datetime(trump_hourly_df['created_at'], errors='coerce')
# biden_hourly_df['created_at'] = pd.to_datetime(biden_hourly_df['created_at'], errors='coerce')

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

# # Display content based on the active page
# if st.session_state.page == 'Exploratory Data Analysis':
#     eda.run_exploratory_data_analysis(trump_hourly_df, biden_hourly_df, country_percentage_analysis_df)  # Call the function from eda.py
