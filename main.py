# streamlit.py
from imports import *
import eda
import world_popularity_analysis
import us_popularity_analysis
import dataset

# Configure the Streamlit page
st.set_page_config(page_title="2020 US Presidential Election Dashboard",
                   page_icon=":bar_chart:",
                   initial_sidebar_state="expanded")

# Apply custom styles
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

st.sidebar.header('US Presidential Election Dashboard `2020`')

# Load the dataframes

# file_id_trump = '1JzvV-U9Ps2ckFTCt8D-fVSq3nVRAndvO'
# url = f'https://drive.google.com/uc?id={file_id_trump}'

# output_trump = 'trump_hourly.csv'
# gdown.download(url, output_trump, quiet=False)

# trump_hourly_df = pd.read_csv(output_trump, encoding='utf-8', lineterminator='\n')

# file_id_biden = '1HzJCf2szv8sCXXw4mTAnjqyV-HBPaQQ_'
# url = f'https://drive.google.com/uc?id={file_id_biden}'

# output_biden = 'biden_hourly.csv'
# gdown.download(url, output_biden, quiet=False)

# biden_hourly_df = pd.read_csv(output_biden, encoding='utf-8', lineterminator='\n')

# country_percentage_analysis_df = pd.read_csv("country_percentage_analysis.csv", encoding='utf-8', lineterminator='\n')
# trump_hourly_df = pd.read_csv("trump_hourly.csv", encoding='utf-8', lineterminator='\n')
# biden_hourly_df = pd.read_csv("biden_hourly.csv", encoding='utf-8', lineterminator='\n')

country_percentage_analysis_df = load_data("country_percentage_analysis.csv")
state_percentage_analysis_df = load_data("state_percentage_analysis.csv")
state_percentage_analysis_df['state'] = state_percentage_analysis_df['state'].astype(str)

# Initialize page state
if 'page' not in st.session_state:
    st.session_state.page = 'World Popularity Analysis'  # Default page

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
# if st.session_state.page == 'Exploratory Data Analysis':
#     eda.run_exploratory_data_analysis(country_percentage_analysis_df)  # Call the function from eda.py

if st.session_state.page == 'World Popularity Analysis':
    world_popularity_analysis.run_world_popularity_analysis(country_percentage_analysis_df)  # Call the function from world_popularity_analysis.py

elif st.session_state.page == 'US Popularity Analysis':
    us_popularity_analysis.run_us_popularity_analysis(state_percentage_analysis_df)  # Call the function from us_popularity_analysis.py

elif st.session_state.page == 'Dataset':
    dataset.run_dataset()

# elif st.session_state.page == 'Sentimental Data Analysis':
#     sentimental_data_analysis.run_sentimental_data_analysis(trump_df, biden_df)  # Call the function from sentimental_data_analysis.py
    


# Sidebar footer
st.sidebar.markdown('''
---
Created with ❤️ by [Gulsah Durmaz](https://github.com/GulsahDurmaz).
''')