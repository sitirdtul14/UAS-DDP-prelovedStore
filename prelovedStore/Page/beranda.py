import streamlit as st

# Validasi login
if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.error("Anda harus login untuk mengakses halaman ini.")
    st.stop()
else:
    # Cek apakah pengguna ingin melihat beranda atau menjual barang
    if "show_jual_barang" not in st.session_state:
        st.session_state.show_jual_barang = False

    # Jika pengguna memilih untuk menjual barang
    if st.session_state.show_jual_barang:
        st.title("Jual Barang - Preloved Store")
        st.write("Isi form di bawah untuk menjual barang Anda.")

        # Simpan data barang yang dijual di session state
        if "barang_dijual" not in st.session_state:
            st.session_state.barang_dijual = []

        # Form untuk menambah barang baru
        nama_barang = st.text_input("Nama Barang")
        harga_barang = st.number_input("Harga Barang (Rp)", min_value=0, step=1000)
        deskripsi_barang = st.text_area("Deskripsi Barang")
        gambar_barang = st.file_uploader("Unggah Gambar Barang", type=["jpg", "jpeg", "png"])

        # Tombol untuk menjual barang
        if st.button("Jual"):
            if not nama_barang or not harga_barang or not deskripsi_barang:
                st.error("Semua field harus diisi!")
            else:
                # Simpan barang ke dalam session_state
                st.session_state.barang_dijual.append({
                    "nama": nama_barang,
                    "harga": int(harga_barang),  # Pastikan harga adalah angka
                    "deskripsi": deskripsi_barang,
                    "penjual": st.session_state.username,
                    "gambar": gambar_barang
                })
                st.success(f"Barang '{nama_barang}' berhasil ditambahkan untuk dijual!")

        # Tampilkan daftar barang yang dijual
        st.markdown("### Daftar Barang yang Anda Jual")
        if st.session_state.barang_dijual:
            for i, barang in enumerate(st.session_state.barang_dijual, start=1):
                st.markdown(f"{i}. {barang['nama']}")
                st.write(f"Harga: Rp{barang['harga']:,}")
                st.write(f"Deskripsi: {barang['deskripsi']}")
                st.write(f"Penjual: {barang['penjual']}")
                if barang["gambar"]:
                    st.image(barang["gambar"], width=200)
                st.write("---")
        else:
            st.info("Anda belum menjual barang apapun.")

        # Tombol untuk kembali ke halaman beranda
        if st.button("Kembali ke Beranda", key="kembali_ke_beranda"):
            st.session_state.show_jual_barang = False

    # Jika pengguna berada di halaman beranda
    else:
        st.header(f"Selamat datang, {st.session_state.username}!")

       # CSS untuk styling warna
        st.markdown(
            """
                <style>
                .main-header {
                color: #4CAF50;
                font-size: 36px;
                font-weight: bold;
                }
                .sidebar-header {
                    color: #FF5722;
                    font-size: 24px;
                    font-weight: bold;
                }
                .product-name {
                    color: #2196F3;
                    font-weight: bold;
                }
                .product-price {
                    color: #FF9800;
                }
                </style>
                """,
                unsafe_allow_html=True
            )

        # Sidebar Header
        st.sidebar.markdown("<div class='sidebar-header'>Selamat Datang di Toko Online Kami!</div>", unsafe_allow_html=True)
        st.sidebar.image('./Page/prelovedStore.jpg', caption="Promo Terbaik untuk Anda!", use_container_width=True)
        st.sidebar.markdown("---")

        # Header di Halaman Utama
        st.markdown("<div class='main-header'>Selamat Datang di Halaman Utama Toko Online!</div>", unsafe_allow_html=True)
        st.image("./Page/prelovedStore.jpg", caption="Promo Terbaik untuk Anda!", use_container_width=True)

        # Footer
        st.markdown("---")
        st.text("Toko Online | Semua hak dilindungi | 2024")
        st.write(""" Selamat datang di PRELOVED STORE, tempat terbaik untuk menemukan pakaian preloved berkualitas dengan harga terjangkau! Kami menghadirkan koleksi pakaian lengkap yang cocok untuk berbagai gaya dan kebutuhan Anda.

✨ Apa yang Kami Tawarkan?

Baju: Pilihan atasan dari kasual hingga semi-formal untuk menunjang penampilan Anda.            
Celana: Beragam model celana yang nyaman dan stylish untuk aktivitas sehari-hari.    
Rok: Koleksi rok cantik dengan berbagai model yang cocok untuk segala suasana.    
Kerudung: Pilihan kerudung preloved berkualitas untuk melengkapi gaya hijab Anda.  
             
✨ Mengapa Memilih Kami?

Semua barang telah melalui seleksi ketat, memastikan kualitas terbaik untuk Anda.
Mendukung gaya hidup ramah lingkungan dengan memanfaatkan fashion preloved.
Harga terjangkau, cocok untuk Anda yang ingin tetap tampil menawan tanpa menguras budget.
Berikan kesempatan kedua untuk pakaian berkualitas ini dan temukan gaya favorit Anda di PRELOVED STORE! Karena fashion yang indah tak harus baru, tapi tetap penuh cinta. 💖
                 
        hubungi kami : @prelovedStore.co.id
         
#PrelovedFashion #GayaHemat #CintaiKeberlanjutan #JualPreloved
""")
        # Produk Rekomendasi
        st.header("Produk Rekomendasi")
        products = {
            "produk rekomendasi":[
                {"nama": "sendal wanita", "harga": 40000, "gambar": "https://down-id.img.susercontent.com/file/id-11134207-7qula-ljf430ql8zfuf5"},
                {"nama": "Kerudung bergo sport", "harga": 60000, "gambar": "https://down-id.img.susercontent.com/file/9c63b7f1836e6de6b32c5d160b164f19"},
                {"nama": "rok pita", "harga": 40000, "gambar": "https://down-id.img.susercontent.com/file/id-11134207-7rase-m0y76liw261036"},
                {"nama": "Celana kulot", "harga": 25000, "gambar": "https://cf.shopee.co.id/file/9274ab560643942a2d50d83faec8119a"},
                {"nama": "Sweater", "harga": 45000, "gambar": "https://down-id.img.susercontent.com/file/sg-11134201-22120-zfjtri3pellvc7"},
        ]
        }
        if "cart" not in st.session_state:
            st.session_state.cart = []

# Fungsi untuk menambah item ke keranjang
        def add_to_cart(product_name, product_price):
            st.session_state.cart.append({"nama": product_name, "harga": product_price})
            st.success(f"{product_name} berhasil ditambahkan ke keranjang!")

        # Menampilkan produk dalam 5 kolom
        cols = st.columns(5)  # Membuat 5 kolom untuk produk
        for i, product in enumerate(products["produk rekomendasi"]):
            with cols[i % 5]:  # Menampilkan setiap produk di kolom masing-masing
                st.image(product["gambar"], use_container_width=True)
                st.markdown(f"<div class='product-name'>{product['nama']}</div>", unsafe_allow_html=True)
                st.markdown(f"<div class='product-price'>{product['harga']}</div>", unsafe_allow_html=True)
                if st.button(f"Tambah ke Keranjang ({product['nama']})", key=f"add_to_cart_{product['nama']}"):
                    add_to_cart(product["nama"], product["harga"])
        # Tombol untuk membuka halaman jual barang
        st.markdown("---")
        st.header("Jual Barang")
        st.write("""
                Di sini Anda bisa menjual barang-barang Anda✨
                 
                Punya barang-barang yang sudah tidak terpakai tapi masih bagus?
                 
                Yuk, kasih mereka kesempatan kedua untuk dicintai! 💖 
                """)
        if st.button("Jual Barang", key="jual_barang"):
            st.session_state.show_jual_barang=True