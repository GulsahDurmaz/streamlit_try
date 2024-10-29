# eda.py
from imports import *

def run_exploratory_data_analysis(trump_df, biden_df):
    st.markdown("## Exploratory Data Analysis")
    st.markdown("""
    The 2020 United States presidential election was held on **November 3, 2020**. The major candidates were incumbent 
    Republican President Donald Trump and Democratic former Vice President Joe Biden. In the months leading up to the 
    election, social media played a significant role in shaping public opinion, with platforms like Twitter serving as a 
    key battleground for discussions, endorsements, and criticism.
    """)

    st.markdown("**Why Twitter?**")
    st.markdown("""
    Social media platforms like Facebook and Twitter have transformed how we interact and share news. As of June 2019, Twitter had over 348M users posting 500M tweets daily, enabling users to influence trends and shape news coverage.

    Twitter has become increasingly important in electoral campaigning, with politicians and parties actively using the platform. This rise in political activity on Twitter has attracted researchers' interest, making election prediction based on Twitter data a popular field. Researchers now analyze citizen sentiment to estimate candidate performance in elections ([Garcia et al., 2019](https://dl.acm.org/doi/pdf/10.1145/3339909)).
    """)