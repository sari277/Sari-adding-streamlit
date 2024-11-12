import streamlit as st

# Set the title with color
st.markdown("<h1 style='text-align: center; color: #FF6347;'>Fun Adding App for Toddlers</h1>", unsafe_allow_html=True)
st.write("Let's add two numbers together!")

# Input fields for the two numbers
first_number = st.number_input("Enter the first number:", step=1)
second_number = st.number_input("Enter the second number:", step=1)

# Button to perform addition
if st.button("Add"):
    result = first_number + second_number
    # Display the result with color
    st.markdown(f"<h2 style='color: #32CD32;'>The sum is: {result}</h2>", unsafe_allow_html=True)
