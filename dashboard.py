import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency

sns.set(style='dark')

# Load data
all_df = pd.read_csv("./bike-sharing-dataset/hour.csv")

datetime_columns = ["dteday"]
all_df.sort_values(by="dteday", inplace=True)
all_df.reset_index(inplace=True)
 
for column in datetime_columns:
    all_df[column] = pd.to_datetime(all_df[column])

# Filter data
min_date = all_df["dteday"].min()
max_date = all_df["dteday"].max()

with st.sidebar:
    # Menambahkan logo perusahaan
    st.image("https://raw.githubusercontent.com/nugnux/img/main/logoNAP.jpg")
    
    # Mengambil start_date & end_date dari date_input
    start_date, end_date = st.date_input(
        label='Rentang Waktu',min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )
    
# st.dataframe(main_df)
main_df = all_df[(all_df["dteday"] >= str(start_date)) & 
                (all_df["dteday"] <= str(end_date))]


# plot number of daily orders (2021)
st.header('Nugroho Dashboard :sparkles:')
st.subheader('Total Peminjaman')

col1, col2 = st.columns(2)

with col1:
    total_orders = main_df.cnt.sum()
    st.metric("Peminjaman: ", value=total_orders)

with col2:
    st.metric("Jam: ", main_df.shape[0])

fig, ax = plt.subplots(figsize=(16, 8))
colors = ["#D3D3D3", "#90CAF9", "#D3D3D3", "#D3D3D3", "#D3D3D3"]
sns.barplot(
        y="cnt", 
        x="dteday",
        data=main_df.sort_values(by="cnt", ascending=False),
        color="green",
        ax=ax
    )
ax.set_ylabel("Jumlah")
ax.set_xlabel("Tanggal")
ax.tick_params(axis='y', labelsize=20)
ax.set_xticklabels(ax.get_xticklabels(), rotation=30, ha='right')
ax.tick_params(axis='x', labelsize=15)

st.pyplot(fig)

# customer demographic
st.subheader("Peminjam")

col1, col2 = st.columns(2)

with col1:
    hari_df = main_df.groupby(by="workingday")["cnt"].mean().reset_index()
    fig, ax = plt.subplots(figsize=(20, 10))
    colors = ["#D3D3D3", "#90CAF9", "#D3D3D3", "#D3D3D3", "#D3D3D3"]
    sns.barplot(
        y="cnt", 
        x="workingday",
        data=hari_df.sort_values(by="cnt", ascending=False),
        palette=colors,
        ax=ax
    )
    ax.set_title("Peminjaman saat weekend.", loc="center", fontsize=50)
    ax.set_ylabel(None)
    ax.set_xlabel(None)
    ax.tick_params(axis='x', labelsize=35)
    ax.tick_params(axis='y', labelsize=30)
    ax.set_xticks([0, 1])
    ax.set_xticklabels(["Weekend", "Hari Kerja"])
    st.pyplot(fig)

with col2:
    libur_df = main_df.groupby(by="holiday")["cnt"].mean().reset_index()
    fig, ax = plt.subplots(figsize=(20, 10))
    colors = ["#D3D3D3", "#90CAF9", "#D3D3D3", "#D3D3D3", "#D3D3D3"]
    
    sns.barplot(
        y="cnt", 
        x="holiday",
        data=libur_df.sort_values(by="cnt", ascending=False),
        palette=colors,
        ax=ax
    )
    ax.set_title("Peminjaman saat libur.", loc="center", fontsize=50)
    ax.set_ylabel(None)
    ax.set_xlabel(None)
    ax.tick_params(axis='x', labelsize=35)
    ax.tick_params(axis='y', labelsize=30)
    ax.set_xticks([0, 1])
    ax.set_xticklabels(["Tidak Libur", "Libur"])
    st.pyplot(fig)

jam_df = main_df.groupby(by="hr")["cnt"].mean().reset_index()
fig, ax = plt.subplots(figsize=(20, 10))
sns.barplot(
    x="hr", 
    y="cnt",
    data=jam_df.sort_values(by="cnt", ascending=False),
    color="green",
    ax=ax
)
ax.set_title("Jumlah rata-rata peminjam tiap jam.", loc="center", fontsize=30)
ax.set_ylabel("Jumlah")
ax.set_xlabel("Waktu")
ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', labelsize=15)
st.pyplot(fig)


# Best Customer Based on RFM Parameters
st.subheader("Hubungan Peminjaman Sepeda terhadap Suhu Rata-rata.")

#plt.figure(figsize=(10, 6))
fig, ax = plt.subplots( figsize=(10, 6))

sns.scatterplot(data=main_df, x='atemp', y='cnt', alpha=0.5)

ax.set_title("Plot antara Jumlah Peminjaman dan Suhu Rata-rata", loc="center", fontsize=30)
ax.set_ylabel("Peminjaman")
ax.set_xlabel("Suhu Rata-rata")
ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', labelsize=15)

st.pyplot(fig)

st.caption('Copyright © Nugroho Adi Pramono 2023')