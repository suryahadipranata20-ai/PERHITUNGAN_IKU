import streamlit as st
import pandas as pd

# --- Konfigurasi Halaman ---
st.set_page_config(
    page_title="Kalkulator IKU",
    page_icon=":cloud:",
    layout="centered"
)

# --- Fungsi Halaman Utama (Home) ---
def show_home():
    #Gambar Unsur Kimia / Udara Ambien (Menggunakan gambar placeholder dari Unsplash yang relevan)
    st.image("https://images.unsplash.com/photo-1569163139599-0f4517e36f51?q=80&w=1000&auto=format&fit=crop", caption="Aspek Kimia Udara Ambien")
    
    st.title("Perhitungan Indeks Kualitas Udara (IKU)")
    st.markdown("---")
    
    st.subheader("Disusun oleh:")
    members = [
        "1. Ariq",
        "2. Endhyeto", 
        "3. Kahlil", 
        "4. Surya", 
        "5. Affan"
    ]
    
    for member in members:
        st.write(member)

# --- Fungsi Halaman Pengenalan (Option 1) ---
def show_intro():
    #Gambar Senyawa SO2 dan NO2
    st.image("https://images.unsplash.com/photo-1532187863486-abf9dbad1b69?q=80&w=1000&auto=format&fit=crop", caption="Senyawa Kimia NO2 dan SO2") #Gambar kimia umum
    
    st.title("Penghitungan Indeks Kualitas Udara (IKU)")
    st.subheader("Berdasarkan Lampiran II Peraturan Menteri LHK RI no.27 Tahun 2021")
    
    st.markdown("""
    Dalam menentukan indeks kualitas udara (IKU) digunakan metode perhitungan indeks NO2 dan SO2 pada udara ambient, 
    kemudian dilanjutkan dengan menghitung Indeks Udara Referensi EU (Uni Eropa) atau disingkat IEU. 
    Angka ini digunakan di Indonesia sebagai salah satu parameter perhitungan Indeks Kualitas Lingkungan Hidup (IKLH) berdasarkan Permen LHK Nomor 27 Tahun 2021 
    sekaligus menentukan kategori kualitas udara di daerah tertentu.
    """)
    
    st.info("Baku mutu referensi EU (mikrogram/m³):")
    st.write("- Parameter NO2: **40,00**")
    st.write("- Parameter SO2: **20,00**")
    
    st.markdown("### Kategori Hasil IKU")
    
    # Membuat Tabel Kategori
    data_kategori = {
        "Rentang IKU": ["0 - 25", "25 - 50", "50 - 70", "70 - 90", "90 - 100"],
        "Kategori": ["Sangat Kurang", "Kurang", "Sedang", "Baik", "Sangat Baik"]
    }
    df = pd.DataFrame(data_kategori)
    
    # Menampilkan tabel dengan style
    st.table(df)

# --- Fungsi Halaman Perhitungan (Option 2) ---
def show_calculator():
    st.title("Menghitung IKU")
    
    st.markdown("Masukkan data kadar polutan (dalam µg/m³). Pisahkan angka dengan koma jika memasukkan banyak data.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Data NO2")
        no2_input = st.text_area("Masukkan data NO2 (pisahkan dengan koma)", "40, 42, 38", height=150)
    
    with col2:
        st.subheader("Data SO2")
        so2_input = st.text_area("Masukkan data SO2 (pisahkan dengan koma)", "20, 18, 22", height=150)
    
    if st.button("Hitung"):
        try:
            # Proses Input NO2
            no2_list = [float(x.strip()) for x in no2_input.split(',') if x.strip()]
            
            # Proses Input SO2
            so2_list = [float(x.strip()) for x in so2_input.split(',') if x.strip()]
            
            # Validasi Minimal 1 Data
            if not no2_list or not so2_list:
                st.error("Error: Harap masukkan setidaknya 1 data untuk NO2 dan SO2.")
                return

            # --- Perhitungan ---
            # Baku Mutu
            Baku_NO2 = 40.00
            Baku_SO2 = 20.00
            
            # Rata-rata input
            rerata_no2 = sum(no2_list) / len(no2_list)
            rerata_so2 = sum(so2_list) / len(so2_list)
            
            # Rumus 1: Indeks NO2
            indeks_no2 = rerata_no2 / Baku_NO2
            
            # Rumus 2: Indeks SO2
            indeks_so2 = rerata_so2 / Baku_SO2
            
            # Rumus 3: IEU (Indeks Eropa)
            IEU = (indeks_no2 + indeks_so2) / 2
            
            # Rumus 4: IKU
            IKU = 100 - ((50 / 0.9) * (IEU - 0.1))
            
            # Tampilan Hasil
            st.markdown("---")
            st.subheader("Hasil Perhitungan")
            
            res_col1, res_col2, res_col3 = st.columns(3)
            res_col1.metric("Rata-rata NO2", f"{rerata_no2:.2f} µg/m³", f"{indeks_no2:.2f} Index")
            res_col2.metric("Rata-rata SO2", f"{rerata_so2:.2f} µg/m³", f"{indeks_so2:.2f} Index")
            res_col3.metric("Indeks Eropa (IEU)", f"{IEU:.4f}")
            
            st.success(f"### Nilai IKU Akhir: {IKU:.2f}")
            
            # Kategori
            kat = "Tidak Terdefinisi"
            if 0 <= IKU <= 25: kat = "Sangat Kurang"
            elif 25 < IKU <= 50: kat = "Kurang"
            elif 50 < IKU <= 70: kat = "Sedang"
            elif 70 < IKU <= 90: kat = "Baik"
            elif 90 < IKU <= 100: kat = "Sangat Baik"
            
            st.info(f"Kategori Kualitas Udara: **{kat}**")
            
        except ValueError:
            st.error("Error: Pastikan format angka benar dan tidak ada huruf di dalam input.")
        except ZeroDivisionError:
            st.error("Error: Baku mutu tidak boleh nol.")
        except Exception as e:
            st.error(f"Terjadi kesalahan: {e}")

# --- Kontrol Utama Navigasi ---
def main():
    st.sidebar.title("Menu Navigasi")
    
    menu_options = ["Halaman Utama", "Pengenalan dan Baku mutu", "Perhitungan IKU"]
    choice = st.sidebar.radio("Pilih Halaman:", menu_options)
    
    if choice == "Halaman Utama":
        show_home()
    elif choice == "Pengenalan dan Baku mutu":
        show_intro()
    elif choice == "Perhitungan IKU":
        show_calculator()

if __name

