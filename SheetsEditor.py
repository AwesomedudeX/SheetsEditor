# C:\Users\techn\Desktop\Coding\Python\pythonProjects\SheetsEditor\car-prices.csv

import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
st.title("Sheets Editor")

pd.set_option("display.max_rows", None, "display.max_columns", None)

c1, c2, c3, c4, c5, c6 = st.columns(6)
	
link = st.text_input("Enter .csv file hyperlink here:")

st.write("\n\n---\n\n")

c1, c2, c3, c4, c5, c6 = st.columns(6)

df = pd.read_csv(link)
edf = st.experimental_data_editor(df)
path = st.text_input("File Name:")

st.download_button(label="Download Data as Text File", data=str(edf), file_name="car-prices.txt", mime="text/plain")
