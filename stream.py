# import streamlit as st
# import pandas as pd
# import numpy as np
# import time

 
# st.title("5 Minutes Engineering(Title)")
# st.header("5 Minutes Engineering(Header)")
# st.subheader("5 Minutes Engineering(Sub-Header)")
# st.write("5 Minutes Engineering(Text)")
# st.markdown("5 Minutes Engineering(Markdown)")
# st.caption("5 Minutes Engineering(Caption)")

# st.image("path.jpg")
# st.audio("speech.mp3")
# st.video("video.mp4")

# st.checkbox('checkbox')
# st.button('Click button')
# st.radio('Pick your city',['Pune','Mumbai','delhi','surat'])
# st.selectbox('Pick your city',['Pune','Mumbai','delhi','surat'])
# st.multiselect('Pick favourite sports',['cricket', 'football', 'basketball'])
# st.select_slider('Give a Remark', ['Bad', 'Good', 'Excellent'])
# st.slider('Your Marks', 0,100)

# on = st.toggle("Activate feature")
# if on:
#     st.write("Feature activated!")

# number = st.number_input("Insert a number")
# st.write("The current number is ", number)

# d = st.date_input("When's your birthday", value=None)
# st.write("Your birthday is:", d)

# t = st.time_input("Set an alarm for", value=None)
# st.write("Alarm is set for", t)

# st.number_input('Enter your marks', 0,100)
# st.text_input('Enter Text')
# st.date_input('Exam date')
# st.time_input('Exam time')
# st.text_area('Description')
# st.file_uploader('Upload File')
# st.color_picker('Choose a color')

# st.success("Success")
# st.error("Error")
# st.warning("Warning")
# st.info("Information")
# st.exception(RuntimeError("RuntimeError exception"))

# st.sidebar.title("5 Minutes Engineering")
# st.sidebar.image("path.jpg")

# df = pd.DataFrame(np.random.randn(50, 20), columns=("col %d" % i for i in range(20)))
# st.dataframe(df)


# df = pd.DataFrame(
#     np.random.randn(10, 5), columns=("col %d" % i for i in range(5))
# )
# st.table(df)

# col1, col2, col3 = st.columns(3)
# col1.metric("Temperature", "70 °F", "1.2 °F")
# col2.metric("Wind", "9 mph", "-8%")
# col3.metric("Humidity", "86%", "4%")

# prompt = st.chat_input("Say something")
# if prompt:
#     st.write(f"User has sent the following prompt: {prompt}")
    
    

# with st.status("Step 1"):
#     st.write("Step 2")
#     time.sleep(1)
#     st.write("Step 3")
#     time.sleep(1)
#     st.write("Step 4")
#     time.sleep(1)
# st.button("Rerun")


# chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
# st.area_chart(chart_data)

# chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
# st.bar_chart(chart_data)

# chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
# st.line_chart(chart_data)

# df = pd.DataFrame(
#     np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
#     columns=['lat', 'lon'])
# st.map(df)

# chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
# st.scatter_chart(chart_data)

# with st.chat_message("user"):
#     st.write("Hello ji")















import streamlit as st
import pandas as pd
import numpy as np
import time
# import matplotlib.pyplot as plt  # For scatter plot

st.title("5 Minutes Engineering(Title)")
st.header("5 Minutes Engineering(Header)")
st.subheader("5 Minutes Engineering(Sub-Header)")
st.write("5 Minutes Engineering(Text)")
st.markdown("5 Minutes Engineering(Markdown)")
st.caption("5 Minutes Engineering(Caption)")

# Use raw strings or forward slashes for file paths
st.image(r"C:\Users\aamir\Downloads\AI\streamlit\streamlit\path.jpg")
st.audio(r"C:\Users\aamir\Downloads\AI\streamlit\streamlit\speech.mp3")
st.video(r"C:\Users\aamir\Downloads\AI\streamlit\streamlit\video.mp4")

st.checkbox('checkbox')
st.button('Click button')
st.radio('Pick your city', ['Pune', 'Mumbai', 'delhi', 'surat'])
st.selectbox('Pick your city', ['Pune', 'Mumbai', 'delhi', 'surat'])
st.multiselect('Pick favourite sports', ['cricket', 'football', 'basketball'])
st.select_slider('Give a Remark', ['Bad', 'Good', 'Excellent'])
st.slider('Your Marks', 0, 100)

on = st.toggle("Activate feature")
if on:
    st.write("Feature activated!")

number = st.number_input("Insert a number")
st.write("The current number is ", number)

d = st.date_input("When's your birthday", value=None)
st.write("Your birthday is:", d)

t = st.time_input("Set an alarm for", value=None)
st.write("Alarm is set for", t)

st.number_input('Enter your marks', 0, 100)
st.text_input('Enter Text')
st.date_input('Exam date')
st.time_input('Exam time')
st.text_area('Description')
st.file_uploader('Upload File')
st.color_picker('Choose a color')

st.success("Success")
st.error("Error")
st.warning("Warning")
st.info("Information")
st.exception(RuntimeError("RuntimeError exception"))

st.sidebar.title("5 Minutes Engineering")
st.sidebar.image(r"C:\Users\aamir\Downloads\AI\streamlit\streamlit\path.jpg")

df = pd.DataFrame(np.random.randn(50, 20), columns=("col %d" % i for i in range(20)))
st.dataframe(df)

df = pd.DataFrame(
    np.random.randn(10, 5), columns=("col %d" % i for i in range(5))
)
st.table(df)

col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")

prompt = st.chat_input("Say something")
if prompt:
    st.write(f"User has sent the following prompt: {prompt}")

with st.status("Step 1"):
    st.write("Step 2")
    time.sleep(1)
    st.write("Step 3")
    time.sleep(1)
    st.write("Step 4")
    time.sleep(1)

# Rerun button
if st.button("Rerun"):
    st.experimental_rerun()

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
st.area_chart(chart_data)

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
st.bar_chart(chart_data)

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
st.line_chart(chart_data)

df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])
st.map(df)

# Corrected scatter plot using Matplotlib
fig, ax = plt.subplots()
ax.scatter(chart_data['a'], chart_data['b'])
st.pyplot(fig)

with st.chat_message("user"):
    st.write("Hello ji")
