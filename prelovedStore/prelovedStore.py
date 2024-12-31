import streamlit as st

st.set_page_config(
    page_title="PRELOVED STORE",
    layout="wide",
    page_icon="🛒"
)

st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🛍 PRELOVED STORE - Belanja Lebih Mudah! 🛒</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #808080;'>Nikmati pengalaman belanja terbaik hanya di sini!</p>", unsafe_allow_html=True)
st.write("---")


beranda= st.Page("./Page/beranda.py", title="beranda")
keranjang = st.Page("./Page/keranjang.py", title="keranjang")
akun = st.Page("./Page/akun.py", title="akun")
produk = st.Page("./Page/produk.py", title="produk")


pg = st.navigation({

    "akun" : [akun],
    "beranda" : [beranda],
    "produk" : [produk],
    "keranjang" : [keranjang],
})

pg.run()