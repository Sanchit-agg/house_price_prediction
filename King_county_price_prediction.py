import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_percentage_error
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.metrics import accuracy_score
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import streamlit as st


@st.cache_resource(show_spinner="Running Model...")
def king_county_predict():
    houses = pd.read_csv("inputs/kc_house_data.csv")
    houses['date'] = pd.to_datetime(houses['date'])
    houses = houses.sample(frac=1, random_state=5)
    houses.drop_duplicates(subset=['lat', 'long'], keep='first', inplace=True)

    features = ['bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'floors', 'waterfront',
                'view', 'condition', 'grade', 'sqft_above', 'sqft_basement', 'yr_built',
                'yr_renovated', 'lat', 'long', 'sqft_living15', 'sqft_lot15']

    X = houses[features]
    y = houses['price']

    X_train_val, X_test, y_train_val, y_test = train_test_split(X, y, test_size=0.2, random_state=5)
    X_train, X_val, y_train, y_val = train_test_split(X_train_val, y_train_val, test_size=0.25, random_state=5)

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_val_scaled = scaler.transform(X_val)
    X_test_scaled = scaler.transform(X_test)

    model = RandomForestRegressor(n_estimators=100, random_state=5)
    model.fit(X_train, y_train)

    y_train_pred = model.predict(X_train)

    train_mape = mean_absolute_percentage_error(y_train, y_train_pred)
    train_mse = mean_squared_error(y_train, y_train_pred)
    train_rmse = np.sqrt(train_mse)
    train_r2 = r2_score(y_train, y_train_pred)

    # print("Training Set Results:")
    # print(f"Root Mean Squared Error: ${train_rmse:,.2f}")
    # print(f"Mean Absolute Percentage Error: {train_mape:.4f}")
    # print(f"R-squared Score: {train_r2:.4f}")

    y_val_pred = model.predict(X_val)

    val_mape = mean_absolute_percentage_error(y_val, y_val_pred)
    val_mse = mean_squared_error(y_val, y_val_pred)
    val_rmse = np.sqrt(val_mse)
    val_r2 = r2_score(y_val, y_val_pred)

    # print("Validation Set Results:")
    # print(f"Root Mean Squared Error: ${val_rmse:,.2f}")
    # print(f"Mean Absolute Percentage Error: {val_mape:.4f}")
    # print(f"R-squared Score: {val_r2:.4f}")
    return model
    # print("Printing y_test_prd : ",y_test_pred)
    # inverse_transform_1 = scaler.inverse_transform(y_test_pred)
    # print("Printing X_test[0] value : ", X_test.iloc[0])
    # print("Printing X_test scaled[0] value : ", X_test.iloc[0])
    # print("Printing Y_pred value : ", y_test_pred[0])
    # print("Printing Inverse scaled value : ", inverse_transform_1[0])
    # print("Printing Expected value :", y_test.iloc[0])
    # test_mape = mean_absolute_percentage_error(y_test, y_test_pred)
    # test_mse = mean_squared_error(y_test, y_test_pred)
    # test_rmse = np.sqrt(test_mse)
    # test_r2 = r2_score(y_test, y_test_pred)
    #
    # print("\nTest Set Results:")
    # print(f"Root Mean Squared Error: ${test_rmse:,.2f}")
    # print(f"Mean Absolute Percentage Error: {test_mape:.4f}")
    # print(f"R-squared Score: {test_r2:.4f}")
