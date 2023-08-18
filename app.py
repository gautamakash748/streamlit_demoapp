import streamlit as st
# streamlit run app.py
st.title("Streamlit demo Manifold AI learning akash")

st.header("Heading of Streamlit ")
st.subheader("Sub Heading of Streamlit")
st.text("This is an example Text")

st.success("Success")
st.warning("Keep Distance warning")
st.info("information")
st.error("Error 404!!")
#st.checkbox("Select/Unselect")
if st.checkbox("Select/Unselect"):
    st.text("Thanks for Selecting")
else:
    st.text("Please Select the checkbox")
state = st.radio("What is your favorite color ?",("Red","Green","Yellow","Black","ALL","Others"))
if state == "Green":
    st.success("Thats my favorite color as well")
occupation = st.selectbox("What do yo do ?",("Student","Coder","Engineer"))

st.text(f"selected option is {occupation}")
if st.button("Submit"):
    st.success("You have Successfully Submitted!!")
st.sidebar.header("Thanks for exploring this part")
st.sidebar.text("Created by akash")

