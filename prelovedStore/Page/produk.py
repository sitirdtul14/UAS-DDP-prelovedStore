import streamlit as st

# Validasi login
if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.error("Anda harus login untuk mengakses halaman ini.")
    st.stop()

else:
    st.header("atasan")
    products = {
        "Baju": [
            {"nama": "Blouse wanita", "harga": 40000, "gambar": "https://cf.shopee.co.id/file/78483975a03d7071b4bb3b40b82595c7"},
            {"nama": "Kemeja", "harga": 35000, "gambar": "https://down-id.img.susercontent.com/file/25a82e51a09aec6534744d2447c56935"},
            {"nama": "Sweater", "harga": 45000, "gambar": "https://down-id.img.susercontent.com/file/sg-11134201-22120-zfjtri3pellvc7"},
            {"nama": "Kaos", "harga": 25000, "gambar": "https://tshirtbar.id/wp-content/uploads/2023/04/bahan-kaos-oversize.webp"},
            {"nama": "Jas", "harga": 50000, "gambar": "https://cf.shopee.co.id/file/d1868945f3953b7a49900e15273cb1c4"},
            {"nama": "cardigan", "harga": 35000, "gambar": "https://www.uniqlo.com/jp/ja/contents/feature/masterpiece/common_22fw/img/item_09_01.jpg?220211"},
            {"nama": "dress", "harga": 50000, "gambar": "https://down-id.img.susercontent.com/file/id-11134207-7qula-li4398jarsrcfc"},
            {"nama": "gamis", "harga": 50000, "gambar": "https://tse3.mm.bing.net/th?id=OIP.cwgGeFC7Dd48L5FSsHAzrwHaHa&pid=Api&P=0&h=720"},
            {"nama": "croptop", "harga": 15000, "gambar": "https://down-id.img.susercontent.com/file/sg-11134201-7r9bg-ll93om7j8pel76"},
            {"nama": "manset", "harga": 30000, "gambar": "https://cf.shopee.co.id/file/5ae4ed1c15132aed0a69ccc02d257e95"},



        ]
    }
    if "cart" not in st.session_state:
        st.session_state.cart = []

    # Fungsi untuk menambah item ke keranjang
    def add_to_cart(product_name, product_price):
        st.session_state.cart.append({"nama": product_name, "harga": product_price})
        st.success(f"{product_name} berhasil ditambahkan ke keranjang!")

    # Menampilkan produk secara horizontal
    cols = st.columns(5)  # Membuat 5 kolom untuk produk
    for i, product in enumerate(products["Baju"]):
        with cols[i % 5]:  # Menampilkan setiap produk di kolom masing-masing
            st.image(product["gambar"], use_container_width=True)
            st.markdown(f"<div class='product-name' style='color: #2196F3; font-weight: bold;'>{product['nama']}</div>", unsafe_allow_html=True) 
            st.markdown(f"<div class='product-price' style='color: #FF9800;'>{product['harga']}</div>", unsafe_allow_html=True)
            if st.button(f"Tambah ke Keranjang ({product['nama']})", key=f"add_to_cart_{product['nama']}"):
                add_to_cart(product["nama"], product["harga"])

    st.markdown("---")
    st.header("bawahan")
    products = {
        "Celana": [
            {"nama": "Celana Jeans", "harga": 35000, "gambar": "https://cf.shopee.co.id/file/97dde8e47ca46f68495746dd808405c0"},
            {"nama": "Celana Chino", "harga": 30000, "gambar": "https://s1.bukalapak.com/img/1611588691/w-1000/Celana_Chino_Panjang_Pria_scaled.jpg"},
            {"nama": "Celana kulot", "harga": 25000, "gambar": "https://cf.shopee.co.id/file/9274ab560643942a2d50d83faec8119a"},
            {"nama": "celana cutbray", "harga": 15000, "gambar": "https://s2.bukalapak.com/img/2629130621/w-1000/Celana_Jeans_Komprang_Cutbray_Bootcut_NavyZendo.jpg"},
            {"nama": "celana katun", "harga": 20000, "gambar": "https://cf.shopee.co.id/file/966104d4f3f8c35c1b4f4263abe2db77"},
            {"nama": "rok pita", "harga": 40000, "gambar": "https://down-id.img.susercontent.com/file/id-11134207-7rase-m0y76liw261036"},
            {"nama": "rok tutu", "harga": 36000, "gambar": "https://cf.shopee.co.id/file/66bfeae5544e12be14492a1cd2aec76c"},
            {"nama": "rok jeans", "harga": 27000, "gambar": "https://down-id.img.susercontent.com/file/id-11134207-7r990-llxei3xyf5wh55"},
            {"nama": "rok midi", "harga": 40000, "gambar": "https://cf.shopee.co.id/file/8164191168e7eb6ca76a40ad6df3ab4e"},
            {"nama": "rok span", "harga": 30000, "gambar": "https://s1.bukalapak.com/img/6362146511/w-1000/rok_span_scuba_rok_kerja_rok_polos_rok_panjang_wanita.jpg"},


    ]
}

if "cart" not in st.session_state:
    st.session_state.cart = []

# Fungsi untuk menambah item ke keranjang
def add_to_cart(product_name, product_price):
    st.session_state.cart.append({"nama": product_name, "harga": product_price})
    st.success(f"{product_name} berhasil ditambahkan ke keranjang!")

# Menampilkan produk secara horizontal
cols = st.columns(5)  # Membuat 5 kolom untuk produk
for i, product in enumerate(products["Celana"]):
        with cols[i % 5]:  # Menampilkan setiap produk di kolom masing-masing
            st.image(product["gambar"], use_container_width=True)
            st.markdown(f"<div class='product-name' style='color: #2196F3; font-weight: bold;'>{product['nama']}</div>", unsafe_allow_html=True) 
            st.markdown(f"<div class='product-price' style='color: #FF9800;'>{product['harga']}</div>", unsafe_allow_html=True) 
            if st.button(f"Tambah ke Keranjang ({product['nama']})", key=f"add_to_cart_{product['nama']}"):
                add_to_cart(product["nama"], product["harga"])

st.markdown("---")
st.header("kerudung")
products = {
        "Kerudung": [
            {"nama": "Kerudung SegiEmpat motif bunga", "harga": 50000, "gambar": "https://cf.shopee.co.id/file/06616bc28ddeb864b87ebad2a06dbc60"},
            {"nama": "Kerudung SegiEmpat polos", "harga": 50000, "gambar": "https://down-id.img.susercontent.com/file/sg-11134201-23010-skss4676khmvb0"},
            {"nama": "Kerudung Pashmina kaos", "harga": 60000, "gambar": "https://down-id.img.susercontent.com/file/id-11134207-7qul7-lk0qas7kyoy716"},
            {"nama": "Kerudung bergo sport", "harga": 60000, "gambar": "https://down-id.img.susercontent.com/file/9c63b7f1836e6de6b32c5d160b164f19"},
            {"nama": "pashmina dubai shawl", "harga": 60000, "gambar": "https://down-id.img.susercontent.com/file/id-11134207-7qula-ljf430ql8zfuf5"},

    ],
}

if "cart" not in st.session_state:
    st.session_state.cart = []

# Fungsi untuk menambah item ke keranjang
def add_to_cart(product_name, product_price):
    st.session_state.cart.append({"nama": product_name, "harga": product_price})
    st.success(f"{product_name} berhasil ditambahkan ke keranjang!")

# Menampilkan produk secara horizontal
# Menampilkan produk secara horizontal
cols = st.columns(5)  # Membuat 5 kolom untuk produk
for i, product in enumerate(products["Kerudung"]):
    with cols[i % 5]:  # Menampilkan setiap produk di kolom masing-masing
        st.image(product["gambar"], use_container_width=True)
        st.markdown(f"<div class='product-name' style='color: #2196F3; font-weight: bold;'>{product['nama']}</div>", unsafe_allow_html=True)  # Mengubah warna nama produk
        st.markdown(f"<div class='product-price' style='color: #FF9800;'>{product['harga']}</div>", unsafe_allow_html=True)  # Mengubah warna harga
        if st.button(f"Tambah ke Keranjang ({product['nama']})", key=f"add_to_cart_{product['nama']}"):
            add_to_cart(product["nama"], product["harga"])

st.markdown("---")
st.header("sendal dan sepatu")
products = {
        "Kerudung": [
            {"nama": "sepatu kets", "harga": 50000, "gambar": "https://ecs7.tokopedia.net/img/cache/700/product-1/2018/5/7/2118812/2118812_d0d6fe3d-27b4-4ab1-81d9-f7cab2ee0d7e_700_700.jpg"},
            {"nama": "vantopel wanita", "harga": 50000, "gambar": "https://cf.shopee.co.id/file/71816794933ea71330b90d88ff3d3d85"},
            {"nama": "vantopel pria", "harga": 55000, "gambar": "https://ecs7.tokopedia.net/img/cache/700/product-1/2017/3/7/147672555/147672555_c88bab47-60c1-41fd-8901-1e058259fca9_700_700.jpg"},
            {"nama": "sendal pria", "harga": 35000, "gambar": "https://tse1.mm.bing.net/th?id=OIP.Qs8hlTuCCMA0JB9N0JhCNAHaHa&pid=Api&P=0&h=180"},
            {"nama": "sendal wanita", "harga": 40000, "gambar": "https://cf.shopee.co.id/file/e31afdab5d5fa0e8e7987a3107a71481"},

    ],
}

if "cart" not in st.session_state:
    st.session_state.cart = []

# Fungsi untuk menambah item ke keranjang
def add_to_cart(product_name, product_price):
    st.session_state.cart.append({"nama": product_name, "harga": product_price})
    st.success(f"{product_name} berhasil ditambahkan ke keranjang!")

# Menampilkan produk secara horizontal
# Menampilkan produk secara horizontal
cols = st.columns(5)  # Membuat 5 kolom untuk produk
for i, product in enumerate(products["Kerudung"]):
    with cols[i % 5]:  # Menampilkan setiap produk di kolom masing-masing
        st.image(product["gambar"], use_container_width=True)
        st.markdown(f"<div class='product-name' style='color: #2196F3; font-weight: bold;'>{product['nama']}</div>", unsafe_allow_html=True)  # Mengubah warna nama produk
        st.markdown(f"<div class='product-price' style='color: #FF9800;'>{product['harga']}</div>", unsafe_allow_html=True)  # Mengubah warna harga
        if st.button(f"Tambah ke Keranjang ({product['nama']})", key=f"add_to_cart_{product['nama']}"):
            add_to_cart(product["nama"], product["harga"])