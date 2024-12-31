import streamlit as st

# Simulasi penyimpanan data pengguna (untuk demo saja, pada aplikasi nyata, gunakan database)
users_db = {}

# Fungsi untuk membuat akun baru
def register(username, password):
    if username in users_db:
        st.error("Username sudah digunakan.")
    else:
        users_db[username] = password
        st.session_state.logged_in = True
        st.session_state.username = username
        st.success("Akun berhasil dibuat! Anda sekarang dapat login.")
        
# Fungsi untuk login
def sign_in(username, password):
    if username in users_db and users_db[username] == password:
        st.session_state.logged_in = True
        st.session_state.username = username
        st.success("Login berhasil!")
    else:
        st.error("Username atau password salah.")

# Fungsi untuk logout
def sign_out():
    st.session_state.logged_in = False
    st.session_state.username = ""
    st.success("Anda telah logout.")

# Menu Login/Sign-Up
st.title("selamat datang! silahkan log in atau daftar akun baru")

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if st.session_state.logged_in:
    st.write(f"Selamat datang, {st.session_state.username}!")
    if st.button("Logout"):
        sign_out()
else:
    menu = st.selectbox("Pilih Opsi", ["Login", "Daftar Akun Baru"])

    if menu == "Login":
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        
        if st.button("Login"):
            sign_in(username, password)
    
    elif menu == "Daftar Akun Baru":
        username = st.text_input("Username (untuk Daftar)")
        password = st.text_input("Password (untuk Daftar)", type="password")
        confirm_password = st.text_input("Konfirmasi Password", type="password")
        
        if password != confirm_password:
            st.error("Password dan konfirmasi password tidak cocok.")
        elif st.button("Daftar Akun"):
            register(username, password)