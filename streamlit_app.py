import streamlit as st
st.set_page_config(page_title='House Price Predictor', layout="wide")


house_price_predictor = st.Page(
    "views/price_predictor.py",
    title="House Price Predictor",
    default=True,
)
summary = st.Page(
    "views/summary.py",
    title="Summary",
)
input_data = st.Page(
    "views/input_data.py",
    title="Input Dataset",
)


pg = st.navigation(
    {
        "Application": [house_price_predictor],
        "Input Data": [summary, input_data],
    }
)

st.logo("assets/profile-pic(2).png")
st.sidebar.markdown("Contact details : ")
st.sidebar.markdown("Sanchit Aggarwal")
st.sidebar.markdown("+91 910169712")
st.sidebar.markdown("sanchit2509@gmail.com")
st.sidebar.markdown("[👨‍💻 Portfolio](https://sanchit-agg.github.io/SanchitAggarwal.github.io/)")

pg.run()
