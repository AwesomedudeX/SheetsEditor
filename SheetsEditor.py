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
name = st.text_input("File Name:")

if name[-4:] != ".txt":
	name = name + ".txt"

st.download_button(label="Download Data as Text", data=str(edf), file_name=".txt", mime="text/plain")
