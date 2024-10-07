import streamlit as st
st.header('st.button')

if st.button('Say hello'):
     st.write('Why hello there')
elif st.button('Say goodbye'):
     st.write('Goodbye')
else:
    st.write('Hi')