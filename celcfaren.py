import streamlit as st #import streamlit right after installing it to the system

st.header('''Temperature Conversion App''') #Head / App title

#Converting temperature to Fahrenheit 
st.write('''Slide to convert Celcius to Fahrenheit''')
value = st.slider('Temperature in Celcius')
 
st.write(value, '°C is ', (value * 9/5) + 32, '°F')
st.write('Conversion formula: (°C x 9/5) + 32 = °F')
 
#Converting temperature to Celcius
st.write('''Slide to convert Fahrenheit to Celcius''')
value = st.slider('Temperature in Fahrenheit')
 
st.write(value, '°F is ', (value - 32) * 5/9, '°C')
st.write('Conversion formula: (°F - 32) x 5/9 = °C')
