import streamlit

streamlit.title('Tias New Adiner')
streamlit.header('Breakfast Menu')
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text('Hard-Boiled Free-Range Egg')

import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.dataframe(my_fruit_list)

# Lets put a pick list here
fruits_selected = streamlit.multiselect("Pick Some Fruits:", list(my_fruit_list.index))#, ['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

#display the table on page
#streamlit.dataframe(my_fruit_list)
streamlit.dataframe(fruits_to_show)
