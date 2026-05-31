import streamlit as st
import pandas as pd

# ---  Halaman Utama ---
st.set_page_config(
    page_title="Perhitungan IKU",
    page_icon="🌫️",
    layout="wide"
)

# --- Fungsi Halaman Utama (Home) ---
def show_home():
    # Menampilkan gambar udara ambien
    st.image(
        "https://images.unsplash.com/photo-1534274867516-169f9550a1d2?q=80&w=1000&auto=format&fit=crop",
        use_container_width=True
    )
    
    st.markdown("<h1 style='text-align: center; color: #2E86AB;'>Perhitungan Indeks Kualitas Udara (IKU)</h1>", unsafe_allow_html=True)
    st.markdown("---")
    
    st.subheader("Disusun oleh:")
    
    # Daftar anggota 
    members = ["Ariq Dewantoro", "Endhyetto Nugraha Syahanaputra", "Kahlil Ibrahim Tirtana", "Surya Hadi Pranata", "TB.Affandhito Kurniawan N"]
    for i, member in enumerate(members, 1):
        st.write(f"{i}. {member}")

# --- Fungsi Halaman Pengenalan (Option 1) ---
def show_intro():
    # Gambar senyawa SO2 dan NO2
    st.image(
        "https://images.unsplash.com/photo-1532187863486-abf9dbad1b69?q=80&w=1000&auto=format&fit=crop",
        caption="Ilustrasi Senyawa Kimia NO2 dan SO2",
        use_container_width=True
    )
    
    st.markdown("<h1 style='text-align: center; color: #2E86AB;'>Penghitungan Indeks Kualitas Udara (IKU)</h1>", unsafe_allow_html=True)
    st.markdown("<h3>Berdasarkan Lampiran II Peraturan Menteri LHK RI no.27 Tahun 2021</h3>", unsafe_allow_html=True)
    
    st.markdown("""
    Dalam menentukan indeks kualitas udara (IKU) digunakan metode perhitungan indeks NO2 dan SO2 pada udara ambient, 
    kemudian dilanjutkan dengan menghitung Indeks Udara Referensi EU (Uni Eropa) atau disingkat IEU. 
    Angka ini digunakan di Indonesia sebagai salah satu parameter perhitungan Indeks Kualitas Lingkungan Hidup (IKLH) berdasarkan Permen LHK Nomor 27 Tahun 2021 
    sekaligus menentukan kategori kualitas udara di daerah tertentu.
    """)
    
    st.markdown("---")
    st.markdown("### 📋 Baku Mutu Referensi EU (µg/m³)")
    
    col1, col2 = st.columns(2)
    with col1:
        st.info("**Parameter NO2**: 40,00")
    with col2:
        st.info("**Parameter SO2**: 20,00")

    st.markdown("### 📋 Baku Mutu PP No 22 Tahun 2021 (µg/m³)")
    
    col1, col2 = st.columns(2)
    with col1:
        st.info("**Parameter NO2**: 200,00")
    with col2:
        st.info("**Parameter SO2**: 150,00")
    
    st.markdown("---")
    st.markdown("### 📊 Kategori Hasil IKU")
    
    # Membuat DataFrame untuk tabel
    data = {
        'Rentang IKU': ['0-25', '25-50', '50-70', '70-90', '90-100'],
        'Kategori': ['Sangat Kurang', 'Kurang', 'Sedang', 'Baik', 'Sangat Baik']
    }
    df = pd.DataFrame(data)
    
    # Menampilkan tabel 
    st.table(df)

# --- Fungsi Halaman Perhitungan (Option 2) ---
def show_calculator():
    st.markdown("<h1 style='text-align: center; color: #2E86AB;'>Menghitung IKU</h1>", unsafe_allow_html=True)
    
    st.markdown("""
    silahkan masukkan data kadar polutan NO2 dan SO2 dalam microgram per meter kubik (µg/m³).
    Untuk memasukkan lebih dari 1 data, pisahkan dengan tanda koma (,).
    """)
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📈 Data NO2")
        no2_input = st.text_area(
            "Masukkan data NO2 (pisahkan dengan koma):",
            placeholder="Contoh: 40, 42, 38",
            key="no2_input"
        )
    
    with col2:
        st.subheader("📈 Data SO2")
        so2_input = st.text_area(
            "Masukkan data SO2 (pisahkan dengan koma):",
            placeholder="Contoh: 20, 18, 22",
            key="so2_input"
        )
    
    st.markdown("---")
    
    if st.button("HITUNG", type="primary", use_container_width=True):
        if not no2_input.strip() or not so2_input.strip():
            st.error("⚠️ Error: Harap masukkan data untuk both NO2 and SO2!")
        else:
            try:
                # Input data
                no2_list = [float(x.strip()) for x in no2_input.split(',') if x.strip()]
                so2_list = [float(x.strip()) for x in so2_input.split(',') if x.strip()]
                
                # Validasi minimal 1 data
                if len(no2_list) < 1 or len(so2_list) < 1:
                    st.error("⚠️ Error: Minimal masukkan 1 data untuk NO2 dan SO2!")
                    return
                
                # Baku Mutu
                Baku_NO2 = 40.00
                Baku_SO2 = 20.00
                
                # --- Perhitungan ---
                
                # 1. Hitung Rata-rata
                rerata_no2 = sum(no2_list) / len(no2_list)
                rerata_so2 = sum(so2_list) / len(so2_list)
                
                # 2. Rumus 1: Indeks NO2
                indeks_no2 = rerata_no2 / Baku_NO2
                
                # 3. Rumus 2: Indeks SO2
                indeks_so2 = rerata_so2 / Baku_SO2
                
                # 4. Rumus 3: IEU (Indeks Eropa)
                IEU = (indeks_no2 + indeks_so2) / 2
                
                # 5. Rumus 4: IKU
                IKU = 100 - ((50 / 0.9) * (IEU - 0.1))
                
                # --- Tampilan Hasil ---
                st.markdown("---")
                st.subheader("📊 Hasil Perhitungan")
                
                # Metric Cards
                m1, m2, m3 = st.columns(3)
                m1.metric("Rata-rata NO2", f"{rerata_no2:.2f} µg/m³", f"{indeks_no2:.2f}")
                m2.metric("Rata-rata SO2", f"{rerata_so2:.2f} µg/m³", f"{indeks_so2:.2f}")
                m3.metric("Indeks Europa (IEU)", f"{IEU:.4f}")
                
                st.markdown("---")
                
                # Hasil Akhir
                st.success(f"### 🎯 Nilai IKU Akhir: {IKU:.2f}")
                
                # Kategori
                if IKU >= 90:
                    kategori = "🌟 Sangat Baik"
                elif IKU >= 70:
                    kategori = "✅ Baik"
                elif IKU >= 50:
                    kategori = "⚠️ Sedang"
                elif IKU >= 25:
                    kategori = "❌ Kurang"
                else:
                    kategori = "❌ Sangat Kurang"
                
                st.info(f"### Kategori Kualitas Udara: {kategori}")
                
                # Detail Perhitungan 
                with st.expander("Lihat Detail Perhitungan"):
                    st.write(f"**Input NO2**: {no2_list}")
                    st.write(f"**Input SO2**: {so2_list}")
                    st.write(f"**Rata-rata NO2**: {rerata_no2:.2f}")
                    st.write(f"**Rata-rata SO2**: {rerata_so2:.2f}")
                    st.write(f"**Indeks NO2** (Rerata NO2 / Baku NO2): {rerata_no2:.2f} / {Baku_NO2} = {indeks_no2:.4f}")
                    st.write(f"**Indeks SO2** (Rerata SO2 / Baku SO2): {rerata_so2:.2f} / {Baku_SO2} = {indeks_so2:.4f}")
                    st.write(f"**IEU** ((Indeks NO2 + Indeks SO2) / 2): ({indeks_no2:.4f} + {indeks_so2:.4f}) / 2 = {IEU:.4f}")
                    st.write(f"**IKU** (100 - (50/0.9 x (IEU - 0.1))): 100 - (55.555... x {IEU - 0.1:.4f}) = {IKU:.2f}")
                
            except ValueError:
                st.error("⚠️ Error: Pastikan format input adalah angka valid dan dipisahkan dengan koma!")
            except ZeroDivisionError:
                st.error("⚠️ Error: Baku mutu tidak boleh nol!")
            except Exception as e:
                st.error(f"⚠️ Terjadi kesalahan: {str(e)}")

# --- Main App ---
def main():
    # Sidebar Navigasi
    st.sidebar.title("📑 MENU")
    
    menu_options = {
        "Halaman Utama": "home",
        "Pengenalan dan Baku mutu": "intro",
        "Perhitungan IKU": "calc"
    }
    
    selection = st.sidebar.radio("Pilih Halaman:", list(menu_options.keys()))
    
    # Pemilihan Halaman
    if menu_options[selection] == "home":
        show_home()
    elif menu_options[selection] == "intro":
        show_intro()
    elif menu_options[selection] == "calc":
        show_calculator()

if __name__ == "__main__":
    main()
