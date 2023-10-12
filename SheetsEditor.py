# C:\Users\techn\Desktop\Coding\Python\pythonProjects\SheetsEditor\car-prices.csv

import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
st.title("Sheets Editor")

c1, c2, c3, c4, c5, c6 = st.columns(6)
	
link = st.text_input("Enter .csv file hyperlink here:")

st.write("\n\n---\n\n")

c1, c2, c3, c4, c5, c6 = st.columns(6)

df = pd.read_csv(link)
edf = st.experimental_data_editor(df)
path = st.text_input("Save As:")

if path[-4:] != ".csv":
	path = path + ".csv"

file = open(path, "w")

file.write(edf)
