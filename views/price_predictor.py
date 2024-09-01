import streamlit as st
import pandas as pd
from King_county_price_prediction import king_county_predict
import plotly.express as px


st.title("House Price Prediction")
st.divider()
df = pd.read_csv("inputs/kc_house_data.csv")
col1, col2, col3 = st.columns(3, gap="small", vertical_alignment="center")
with col1:
    bedrooms = st.number_input("Bedrooms", min_value=0, max_value=10)
with col2:
    bathrooms = st.number_input("Bathrooms", min_value=0, max_value=10)
with col3:
    living = st.number_input("Living Area(sqft)", min_value=0)
col4, col5, col6 = st.columns(3, gap="small", vertical_alignment="center")
with col4:
    lot = st.number_input("Lot Area(sqft)", min_value=0)
with col5:
    floors = st.number_input("Floors", step=1, min_value=0)
with col6:
    waterfront = st.selectbox("Waterfront", ["Yes", "No"])
    if waterfront == 'Yes':
        waterfront = 1
    else:
        waterfront = 0
col7, col8, col9 = st.columns(3, gap="small", vertical_alignment="center")
with col7:
    view = st.slider("View (0-4)", 0, 4)
with col8:
    condition = st.slider("Condition (0-5)", 0, 5)
with col9:
    grade = st.slider("Grade (0-13)", 0, 13)
col10, col11 = st.columns(2, gap="small", vertical_alignment="center")
with col10:
    above = st.number_input("Area above ground (sqft)", min_value=0)
with col11:
    basement = st.number_input("Basement Area(sqft)", min_value=0)
yr_built = st.slider("Year Built", df['yr_built'].min(), df['yr_built'].max())
col12, col13, col14 = st.columns(3, gap="small", vertical_alignment="center")
with col12:
    yr_renovated = st.number_input("Year Renovated", min_value=0)
with col13:
    living15 = st.number_input("Avg. living area of nearby houses (sqft)", min_value=0)
with col14:
    lot15 = st.number_input("Avg. lot area of nearby houses (sqft)", min_value=0)
col15, col16 = st.columns(2, gap="small", vertical_alignment="center")
with col15:
    lat = st.slider("Latitude", df['lat'].min(), df['lat'].max(), df['lat'].mean())
with col16:
    long = st.slider("Longitude", df['long'].min(), df['long'].max(), df['long'].mean())

# print([lat][0])
data = {
    'lat': [[lat][0]],
    'long': [[long][0]]
}
map_df = pd.DataFrame(data)
fig2 = px.scatter_mapbox(map_df, lat='lat', lon='long', zoom=10, height=400)
fig2.update_traces(marker=dict(size=10))
fig2.update_layout(mapbox_style="open-street-map")
# st.header("Sample data location")
st.plotly_chart(fig2)


if st.button(label='**Predict Price**'):
    st.subheader('Predicted House Price:')
    model = king_county_predict()
    test_data = {
        'bedrooms': bedrooms,
        'bathrooms': bathrooms,
        'sqft_living': living,
        'sqft_lot': lot,
        'floors': floors,
        'waterfront': waterfront,
        'view': view,
        'condition': condition,
        'grade': grade,
        'sqft_above': above,
        'sqft_basement': basement,
        'yr_built': yr_built,
        'yr_renovated': yr_renovated,
        'lat': lat,
        'long': long,
        'sqft_living15': living15,
        'sqft_lot15': lot15
    }
    test = pd.DataFrame([test_data])
    y_test_pred = model.predict(test)
    st.write(f"$ {y_test_pred[0]}")
