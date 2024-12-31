import streamlit as st

st.title("Keranjang Anda")

st.markdown("<h2 style='color: #FF4500;'>🛒 Keranjang Belanja</h2>", unsafe_allow_html=True)

if "cart" not in st.session_state:
    st.session_state.cart = []

if st.session_state.cart:
    total_items = len(st.session_state.cart)
    total_price = sum(item["harga"] for item in st.session_state.cart)
    
    # Tampilkan daftar item di keranjang
    for i, item in enumerate(st.session_state.cart, start=1):
        st.write(f"{i}. {item['nama']} - Rp{item['harga']:,}")
    st.write(f"Total Barang: {total_items}")
    st.write(f"Total Harga: Rp{total_price:,}")

    # Pilihan diskon
    discount_percentage = 10 if total_price > 300000 else 0
    discount_amount = total_price * discount_percentage / 100
    final_price = total_price - discount_amount
    
    if discount_percentage > 0:
        st.success(f"Anda mendapatkan diskon {discount_percentage}% sebesar Rp{discount_amount:,}!")
    
    # Menghapus barang
    st.write("---")
    st.markdown("### batalkan pesanan:")
    items_to_remove = []
    for i, item in enumerate(st.session_state.cart, start=1):
        checkbox = st.checkbox(f"Hapus {item['nama']} - Rp{item['harga']:,}", key=f"checkbox_{i}")
        if checkbox:
            items_to_remove.append(i-1)  # Menyimpan indeks item yang dipilih untuk dihapus

    if items_to_remove:
        if st.button("Hapus Barang Terpilih"):
            for index in reversed(items_to_remove):  # Menghapus dari belakang untuk menghindari masalah indeks
                st.session_state.cart.pop(index)
            st.success("Barang terpilih berhasil dihapus!")
            st.rerun()  # Rerun untuk memperbarui tampilan keranjang 

    # Pilihan metode pengiriman
    st.write("---")
    st.markdown("### Pilih Metode Pengiriman:")
    shipping_methods = {
        "Reguler (Rp10.000)": 10000,
        "Express (Rp20.000)": 20000,
        "Same Day (Rp30.000)": 30000,
    }
    selected_shipping = st.radio("Metode Pengiriman", list(shipping_methods.keys()))
    shipping_cost = shipping_methods[selected_shipping]

    # Menghitung ulang total barang dan harga setelah penghapusan
    total_items = len(st.session_state.cart)
    total_price = sum(item["harga"] for item in st.session_state.cart)
    st.write(f"Total Barang: {total_items}")
    st.write(f"Total Harga: Rp{total_price:,}")

    # Total yang harus dibayar
    st.write("---")
    st.markdown("### checkout:")
    final_total = final_price + shipping_cost
    st.write(f"Ongkos Kirim: Rp{shipping_cost:,}")
    st.write(f"Total yang Harus Dibayar: Rp{final_total:,}")

    # Tombol konfirmasi
    if st.button("Konfirmasi Pembelian"):
        st.session_state.cart = []
        st.success("Terima kasih telah berbelanja! Pesanan Anda akan segera diproses.")
        st.balloons()

else:
    st.warning("Keranjang belanja Anda kosong.")