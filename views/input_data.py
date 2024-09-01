import streamlit as st
import pandas as pd
import time
st.title("King County House Data")
st.divider()
description = """The dataset, sourced from Kaggle, comprises 21,613 records, each representing a house sale in 
King County, Washington, between May 2014 and May 2015. It includes 21 columns, with 20 columns detailing various 
features of the houses, and 1 column serving as a unique identifier for each property. 
This dataset offers detailed insights into the housing market during that period, providing valuable information 
on the characteristics and sale prices of homes in the region."""

st.write(description)
st.header("Dataset")
st.dataframe(pd.read_csv("inputs/kc_house_data.csv"))
st.header("Column description")
st.dataframe(pd.read_csv("inputs/column_data_des.csv"), hide_index=True)
