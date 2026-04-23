def siapkan_nada():
    # Menggabungkan 4 teks menjadi satu string
    isi_nada = """
[Teks 1]
... mengajarkan gerakan pertama: "Goyang
Eucalyptus". Aku sudah bisa melakukan "Lompat Pohon" ...
... Pak Wombat mengajarkan gerakan baru: "Pelukan Bambu" ...

[Teks 2]
... Bu Landak, mengajarkan teknik dasar: "Petik Senar" ...
... Bu Landak memperkenalkan "Gesek Pelan" ...
... Kami mempraktikkan "Tiup Lembut" ...

[Teks 3]
... pose dasar bernama "Berdiri Anggun" ...
... mencoba gerakan "Guling Depan" ...
... gerakan baru: "Jungkir Balik" ...
... gerakan "Ayun Pita" ...

[Teks 4]
... mengajarkan teknik "Sapuan Kuas" ...
... bernama "Cipratan Warna" ...
... teknik baru: "Gores Dalam" ...
"""
    # Membuat file fisik Nada.txt
    with open("Nada.txt", "w", encoding="utf-8") as f:
        f.write(isi_nada)

# BAGIAN 2: FUNGSI GERAKAN 
def gerakan(filename):
    hasil_ekstraksi = []
    
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            isi_teks = file.read()
            
            # Logika mencari teks di antara tanda kutip
            start_index = isi_teks.find('"')
            while start_index != -1:
                end_index = isi_teks.find('"', start_index + 1)
                if end_index != -1:
                    # Mengambil teks (termasuk tanda kutipnya)
                    teks_kutipan = isi_teks[start_index:end_index + 1]
                    
                   
                    teks_bersih = teks_kutipan.replace('\n', ' ')
                    
                    
                    while "  " in teks_bersih:
                        teks_bersih = teks_bersih.replace("  ", " ")
                        
                    hasil_ekstraksi.append(teks_bersih)
                    start_index = isi_teks.find('"', end_index + 1)
                else:
                    break
                    
        # Mengembalikan hasil dalam bentuk String dipisahkan koma
        return ",".join(hasil_ekstraksi)
        
    except FileNotFoundError:
        return "File tidak ditemukan"

# BAGIAN 3: EKSEKUSI 
# 1. Buat filenya dulu
siapkan_nada()

# 2. Jalankan fungsinya
output = gerakan("Nada.txt")
print(output)