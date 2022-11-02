import streamlit as st
import random
import altair as alt
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.write('Streamlit day 1 dsba5122')
st.header('Homework 1')

st.markdown(
"**QUESTION 1**: In previous homeworks you created dataframes from random numbers.\n"
"Create a datframe where the x axis limit is 100 and the y values are random values.\n"
"Print the dataframe you create and use the following code block to help get you started"
)

st.code(
''' 
x_limit = 

# List of values from 0 to 100 each value being 1 greater than the last
x_axis = np.arange()

# Create a random array of data that we will use for our y values
y_data = []

df = pd.DataFrame({'x': x_axis,
                     'y': y_data})
st.write(df)''',language='python')
x_limit = 100

# List of values from 0 to 100 each value being 1 greater than the last
x_axis = np.arange(0,x_limit,1)

# Create a random array of data that we will use for our y values
y_data = np.random.rand(100)

df = pd.DataFrame({'x': x_axis,
                'y': y_data})
st.write(df)

"**QUESTION 2**: Using the dataframe you just created, create a basic scatterplot and Print it.\n"
"Use the following code block to help get you started."

st.code(
''' 
scatter = alt.Chart().mark_point().encode()

st.altair_chart(scatter, use_container_width=True)''',language='python')

scatter = alt.Chart(df).mark_point().encode(
    x='x', y='y'
)

st.altair_chart(scatter, use_container_width=True)

st.markdown(
"**QUESTION 3**: Lets make some edits to the chart by reading the documentation on Altair.\n"
"https://docs.streamlit.io/library/api-reference/charts/st.altair_chart.  "
"Make 5 changes to the graph, document the 5 changes you made using st.markdown(), and print the new scatterplot.  \n"
"To make the bullet points and learn more about st.markdown() refer to the following discussion.\n"
"https://discuss.streamlit.io/t/how-to-indent-bullet-point-list-items/28594/3"
)

st.markdown("The five changes I made were.....")
st.markdown("""
The 5 changes I made were:
- Change 1: Add a title
- Change 2: add size with a key code and hover for additional information
- Change 3: add annotation 
- Change 4: add a checkbox - (#which I checked)
- Change 5: add a select box - (#which I made my choice)
""")
st.code(
''' 
scatter = alt.Chart().mark_point().encode()

st.altair_chart(scatter, use_container_width=True)''',language='python')

scatter = alt.Chart(df,title="Random Scatter").mark_point().encode(x='x',y='y',size='y',tooltip=['x', 'y']).configure_mark(
    opacity=0.7, 
    color='red'
)

st.altair_chart(scatter, use_container_width=True)

st.title("Question 3")
df = pd.DataFrame(
    np.random.randn(100, 3),
    columns=['a', 'b', 'c'])

c = alt.Chart(df).mark_circle().encode(
    x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])

st.altair_chart(c, use_container_width=True)

ANNOTATIONS = [
    ("0.0", "start"),
]

st.checkbox('check here if you need assistance')

st.selectbox('Select the type of additional training',['101 streamlit','undergrad coding class']) 
st.markdown(
"**QUESTION 4**: Explore on your own!  Go visit https://altair-viz.github.io/gallery/index.html.\n "
"Pick a random visual, make two visual changes to it, document those changes, and plot the visual.  \n"
"You may need to pip install in our terminal for example pip install vega_datasets "
)

st.markdown("""
The 2 changes I made were:
- Change 1: created a title
- Change 2: changed from a scatter plot to a line chart
"""
)

st.title("Question 4")

chart_data = pd.DataFrame(
    np.random.randn(20,3),
    columns=['a', 'b', 'c'])

st.line_chart(chart_data)  
