import streamlit as st

st.title("Menentukan Indeks Kualitas Udara")
st.header("Indeks Kualitas Udara (IKU)")
st.write("merupakan ukuran komposit atau angka tunggal yang menggambarkan tingkat pencemaran atau status mutu udara di suatu lokasi pada waktu tertentu.Angka ini dihitung berdasarkan konsentrasi berbagai polutan utama seperti partikel debu, Sulfur Dioksida, Karbon Monoksida, Nitrogen Dioksida , dan Ozon.")

sox=st.number_input("masukkan kadar sox: ,min_value=0.0, format="%.6f")
bakumutu_sox=st.number(150)
nox=st.number_input("masukkan kadar nox: ,min_value=0.0, format="%.6f")
bakumutu_nox=st.number(200)

if st.button("Hitung"):
    hasil_sox = sox / bakumutu_sox
    hasil_nox = nox / bakumutu_nox
st.success(f"Hasil SOx = {hasil_sox:.6f}")
st.success(f"Hasil NOx = {hasil_nox:.6f}")


