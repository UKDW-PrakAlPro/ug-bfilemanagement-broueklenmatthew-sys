# 1. Menyiapkan data buku ke dalam file buku.txt
data_buku = """Python Programming|John Doe|2020|Tersedia
Data Engineering|Jane Smith|2019|Dipinjam
Machine Learning|Andrew Ng|2021|Tersedia
Artificial Intelligence|Stuart Russell|2018|Tersedia
Deep Learning|Ian Goodfellow|2016|Dipinjam
Clean Code|Robert C. Martin|2008|Tersedia
The Pragmatic Programmer|Andrew Hunt|1999|Tersedia
Database Systems|Raghu Ramakrishnan|2017|Dipinjam
Computer Networks|Andrew S. Tanenbaum|2011|Tersedia
Operating System Concepts|Abraham Silberschatz|2018|Dipinjam
Introduction to Algorithms|Thomas H. Cormen|2009|Tersedia
Software Engineering|Ian Sommerville|2015|Tersedia
Big Data Analytics|Viktor Mayer-Schönberger|2013|Dipinjam
Cyber Security Basics|Charles J. Brooks|2019|Tersedia
Cloud Computing|Rajkumar Buyya|2020|Dipinjam"""

with open("buku.txt", "w") as f:
    f.write(data_buku)

# 2. Fungsi cari_buku[cite: 2, 3]
def cari_buku(daftar_judul, hanya_tersedia=False):
    total_ditemukan = 0
    
    # Membaca data dari file buku.txt
    try:
        with open("buku.txt", "r") as file:
            baris_data = [line.strip() for line in file.readlines() if line.strip()]
    except FileNotFoundError:
        print("File 'buku.txt' tidak ditemukan.")
        return

    # Iterasi pencarian berdasarkan daftar judul yang diminta[cite: 2, 3]
    for judul_cari in daftar_judul:
        ditemukan_per_judul = False
        
        for baris in baris_data:
            # Memisahkan data kolom menggunakan split("|")
            parts = baris.split("|")
            judul, penulis, tahun, status = parts
            
            # Logika pencarian: tidak case-sensitive dan sebagian kata[cite: 2]
            if judul_cari.lower() in judul.lower():
                # Filter status jika hanya_tersedia bernilai True[cite: 2]
                if hanya_tersedia and status != "Tersedia":
                    continue
                
                # Output format sesuai permintaan gambar[cite: 2]
                print("==============================")
                print(f"Judul   : {judul}")
                print(f"Penulis : {penulis}")
                print(f"Tahun   : {tahun}")
                print(f"Status  : {status}")
                print("==============================")
                
                total_ditemukan += 1
                ditemukan_per_judul = True
        
        # Jika satu kata kunci tidak ditemukan sama sekali[cite: 2]
        if not ditemukan_per_judul:
            print(f"Buku '{judul_cari}' tidak ditemukan / tidak tersedia")

    # Menampilkan total akumulasi pencarian[cite: 2]
    print(f"Total buku ditemukan: {total_ditemukan}")

# 3. Menjalankan Test Case (JANGAN DIUBAH)[cite: 3]
print("HASIL TESTCASE:")
cari_buku(["python", "data", "cihuy"])
print("\n"+"-"*30+"\n")
cari_buku(["cyber", "learning"], hanya_tersedia=True)
print("\n"+"-"*30+"\n")
cari_buku(["system", "code"])
print("\n"+"-"*30+"\n")
cari_buku(["data"], hanya_tersedia=True)
print("\n"+"-"*30+"\n")
cari_buku(["Blockchain", "Quantum"])
print("\n"+"-"*30+"\n")
cari_buku(["bAsIcS","cOncEPTs"])