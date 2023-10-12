# C:\Users\techn\Desktop\Coding\Python\pythonProjects\SheetsEditor\car-prices.csv

import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
st.title("Sheets Editor")
st.sidebar.title("Controls:")

c1, c2, c3, c4, c5, c6 = st.columns(6)
	
link = st.text_input("Enter .csv file hyperlink here:")

st.write("\n\n---\n\n")

c1, c2, c3, c4, c5, c6 = st.columns(6)

df = pd.read_csv(link)

edf = st.experimental_data_editor(df)
st.download_button("Download Data", edf)
