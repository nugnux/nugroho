import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency

sns.set(style='dark')

# Filter data

with st.sidebar:
    # Menambahkan logo perusahaan
    st.image("https://raw.githubusercontent.com/nugnux/img/main/logoNAP.jpg")
    
    # Mengambil start_date & end_date dari date_input
    date= st.date_input(
        label='Rentang Waktu'
    )
    

# plot number of daily orders (2021)
st.header('Nugroho Dashboard :sparkles:')
st.subheader('Tadaa...')

col1, col2 = st.columns(2)

with col1:
    st.metric("Data: ", value=0)

with col2:
    st.metric("Data Juga: ", value=0)

x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)  # Generating x values from -2*pi to 2*pi
y = np.sin(x)  # Calculating sin(x) values

fig, ax = plt.subplots(figsize=(16, 8))
ax.plot(x, y, label='sin(x)', color='b')  # Plotting sin(x) curve
ax.set_ylabel("Sin x")
ax.set_xlabel("x")
ax.tick_params(axis='y', labelsize=20)
ax.set_xticklabels(ax.get_xticklabels(), rotation=30, ha='right')
ax.tick_params(axis='x', labelsize=15)

st.pyplot(fig)

# aoe
st.subheader("Peminjam")

col1, col2 = st.columns(2)

with col1:
    x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)  # Generating x values from -2*pi to 2*pi
    y = np.sin(x)  # Calculating sin(x) values

    fig, ax = plt.subplots(figsize=(16, 8))
    ax.plot(x, y, label='sin(x)', color='b')  # Plotting sin(x) curve
    ax.set_ylabel("Sin x")
    ax.set_xlabel("x")
    ax.tick_params(axis='y', labelsize=20)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=30, ha='right')
    ax.tick_params(axis='x', labelsize=15)

    st.pyplot(fig)

with col2:
    x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)  # Generating x values from -2*pi to 2*pi
    y = np.sin(x)  # Calculating sin(x) values

    fig, ax = plt.subplots(figsize=(16, 8))
    ax.plot(x, y, label='sin(x)', color='b')  # Plotting sin(x) curve
    ax.set_ylabel("Sin x")
    ax.set_xlabel("x")
    ax.tick_params(axis='y', labelsize=20)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=30, ha='right')
    ax.tick_params(axis='x', labelsize=15)

    st.pyplot(fig)  

x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)  # Generating x values from -2*pi to 2*pi
y = np.sin(x)  # Calculating sin(x) values

fig, ax = plt.subplots(figsize=(16, 8))
ax.plot(x, y, label='sin(x)', color='b')  # Plotting sin(x) curve
ax.set_ylabel("Sin x")
ax.set_xlabel("x")
ax.tick_params(axis='y', labelsize=20)
ax.set_xticklabels(ax.get_xticklabels(), rotation=30, ha='right')
ax.tick_params(axis='x', labelsize=15)

st.pyplot(fig)

st.caption('Copyright © Nugroho Adi Pramono 2023')