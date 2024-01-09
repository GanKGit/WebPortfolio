import streamlit as st
import pandas as ps
from pathlib import Path

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("image/gan.jpg")

with col2:
    st.title("Ganesh Sivagnanam")
    content = """
    Ganesh Sivagnanam is a seasoned Program/Project manager with 23+ years of experience.
    He has delivered projects more than 360K man-day worth of projects in the capacity
    of Delivery lead, Technical architect, Project leader, Scrum master in matrix and
    functional organization
    """
    st.info(content)

content2= """
    Below are some of the successful projects executed
"""
st.write(content2)

col3, col4 = st.columns(2)

layout_data= ps.read_csv("Layout/layout.csv", sep=",")

with col3:
    for index, row in layout_data[:2].iterrows():
        st.header (row['Project Name'])
        st.image(row['Image'])
        st.write(row['Description'])

with col4:
    for index, row in layout_data[2:].iterrows():
        st.header(row['Project Name'])
        st.image(row['Image'])
        st.write(row['Description'])
    # with col3:
#     st.image(layout_data[1][2])


