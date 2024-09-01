import streamlit as st
import pandas as pd
import plotly.express as px


df = pd.read_csv("inputs/kc_house_data.csv")


fig2 = px.scatter_mapbox(df, lat="lat", lon="long", hover_name="price", zoom=9.5, height=700)
fig2.update_layout(mapbox_style="open-street-map")
st.title("Summary")
st.divider()
st.subheader('Data points representing the location of sample dataset')
st.plotly_chart(fig2)

st.subheader('House Price per feature')
feature = st.selectbox("Select Feature", df.columns.drop(['price', 'id', 'date']))
avg_price_per_feature = df.groupby(feature)['price'].mean().reset_index()
# print(avg_price_per_feature)
fig3 = px.bar(data_frame=avg_price_per_feature, x=feature, y='price')
fig3.update_traces(texttemplate='%{y}', textposition='outside')
fig3.update_layout(bargap=0.2)
st.plotly_chart(fig3)


col1, col2 = st.columns(2, gap="large", vertical_alignment="center")
with col1:
    value_counts = df['bedrooms'].value_counts().reset_index()
    value_counts.columns = ['bedrooms', 'Count']
    fig = px.pie(value_counts, names='bedrooms', values='Count', title="Distribution of Bedrooms count in sample data")
    st.plotly_chart(fig)
with col2:
    value_counts = df['bathrooms'].value_counts().reset_index()
    value_counts.columns = ['bathrooms', 'Count']
    fig = px.pie(value_counts, names='bathrooms', values='Count',
                 title="Distribution of Bathrooms count in sample data")
    st.plotly_chart(fig)

fig = px.histogram(x=df['sqft_living'], nbins=30,
                   title='Histogram representing count of houses w.r.t living area (sqft)')
fig.update_traces(texttemplate='%{y}', textposition='outside')
fig.update_layout(bargap=0.2)
st.plotly_chart(fig)
