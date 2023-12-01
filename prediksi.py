import pickle
import streamlit as st

try:
    # Cek apakah file model ada di direktori yang benar
    model = pickle.load(open('prediksi_ph.sav', 'rb'))
except Exception as e:
    st.error(f"Error loading the model: {e}")
    st.stop()

st.title('Prediksi pH')

Hardness = st.number_input('Input Hardness')
Alkalinity = st.number_input('Input Alkalinity')
CarbonateRoot = st.number_input('Input Carbonate Root')
Nitrate = st.number_input('Input Nitrate')
Nitrite = st.number_input('Input Nitrite')
Freeclorine = st.number_input('Input Free clorine')
Temperature = st.number_input('Input Temperature')
DissolvedOxygen = st.number_input('Input Dissolved Oxygen')  

predict = ''

if st.button('Prediksi pH'):
    # Pastikan nilai-nilai ini sesuai dengan format yang diharapkan oleh model
    if hasattr(model, 'predict'):
        predict = model.predict([[Hardness, Alkalinity, CarbonateRoot, Nitrate, Nitrite, Freeclorine, Temperature, DissolvedOxygen]])
        st.write('Prediksi pH:', predict)
    else:
        st.error("Model tidak memiliki metode 'predict'.")
