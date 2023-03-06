import streamlit

streamlit.title('Tias New Adiner')
streamlit.header('Breakfast Menu')
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text('Hard-Boiled Free-Range Egg')

import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)

# Lets put a pick list here
streamlit.multiselect("Pick Some Fruits:", list(my_fruit_list.index))

#display the table on page
streamlit.dataframe(my_fruit_list)
