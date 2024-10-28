import streamlit as st

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
