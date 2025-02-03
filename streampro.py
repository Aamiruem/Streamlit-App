import demoji # type: ignore
import streamlit as st
user_input = st.text_area("Enter Your Text")
if(st.button('Get')):
    response = demoji.findall(user_input)
    st.success(response)
