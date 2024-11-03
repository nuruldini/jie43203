import pandas as pd
import streamlit as st

file_path = 'https://raw.githubusercontent.com/nuruldini/jie43203/refs/heads/main/onlinefoods.csv'

df = pd.read_csv(file_path)

st.write(df)


