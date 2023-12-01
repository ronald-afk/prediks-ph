import pickle
import streamlit as st

model = pickle.load(open('prediksi_ph.sav','rb'))

st.title('Prediksi pH')

Hardness = st.number_input('Input Hardness')
Alkalinity = st.number_input('Input Alkalinity')
CarbonateRoot = st.number_input('Input Carbonate Root')
Nitrate = st.number_input('Input Nitrate')
Nitrite	= st.number_input('Input Nitrite')
Freeclorine = st.number_input('Input Free clorine')
Temperature = st.number_input('Input Temperature')
DissolvedOxygen = st.number_input('Input Dissolved Oxygen')  # Fixed input name

predict = ''

if st.button('Prediksi pH'):
    # Pastikan nilai-nilai ini sesuai dengan format yang diharapkan oleh model
    predict = model.predict([[Hardness, Alkalinity, CarbonateRoot, Nitrate, Nitrite, Freeclorine, Temperature, DissolvedOxygen]])
    st.write('Prediksi pH:', predict)
