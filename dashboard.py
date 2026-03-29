import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title='Student Performance Analysis', layout='wide')

df = pd.read_csv('data/students_performance.csv')

st.title('Student Performance Analysis')

col1, col2, col3 = st.columns(3)

col1.metric('Total Data', len(df))
col2.metric('Dropout %', round((df['Status']=='Dropout').mean()*100,2))
col3.metric('Graduate %', round((df['Status']=='Graduate').mean()*100,2))

col1, col2, col3 = st.columns(3)

col1.subheader('Distribution of Status')
fig = px.pie(
    df,
    names='Status',
)
col1.plotly_chart(fig, use_container_width=True)

col2.subheader('Distribution of Age')
fig = px.histogram(
    df,
    x='Age_at_enrollment',
    nbins=20,
)
col2.plotly_chart(fig, use_container_width=True)

df['Gender'] = df['Gender'].map({0: 'Female', 1: 'Male'})
col3.subheader('Distribution of Gender')
fig = px.pie(
    df,
    names='Gender',
)
col3.plotly_chart(fig, use_container_width=True)

st.subheader('Distribution of Admission Grade')
fig = px.histogram(
    df,
    x='Admission_grade',
    color='Status',
    barmode='overlay',
)
st.plotly_chart(fig, use_container_width=True)

col1, col2 = st.columns(2)

col1.subheader('Approved Units (1st Semester)')
fig = px.box(
    df,
    x='Status',
    y='Curricular_units_1st_sem_approved',
    color='Status',
)
col1.plotly_chart(fig, use_container_width=True)

col2.subheader('Approved Units (2nd Semester)')
fig = px.box(
    df,
    x='Status',
    y='Curricular_units_2nd_sem_approved',
    color='Status',
)
col2.plotly_chart(fig, use_container_width=True)

col1, col2 = st.columns(2)

col1.subheader('Debtor Status')
df['Debtor'] = df['Debtor'].map({0: 'No', 1: 'Yes'})
fig = px.histogram(
    df,
    x='Debtor',
    color='Status',
    barmode='group',
)
col1.plotly_chart(fig, use_container_width=True)

col2.subheader('Scholarship Holder')
df['Scholarship_holder'] = df['Scholarship_holder'].map({0: 'No', 1: 'Yes'})
fig = px.histogram(
    df,
    x='Scholarship_holder',
    color='Status',
    barmode='group',
)
col2.plotly_chart(fig, use_container_width=True)
