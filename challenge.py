from datetime import datetime

pilihan = "beli"

while pilihan == "beli" :
    print("=========================================================")
    print("|\t\t\t BAKSO \t\t\t|")
    print("|\t\t\t DAFTAR MENU \t\t\t|")
    print("| \t1. Bakso Urat    10000 \t\t|")
    print("| \t2. Bakso Sapi    10000 \t\t|")
    print("| \t3. Bakso Ayam    10000 \t\t|")
    print("| \t4. Bakso Beranak 12000 \t\t|")
    print("| \t5. Bakso Telur   12000 \t\t|")
    print("| \t6. Bakso Mercon  15000 \t\t|")
    print("| \t7. Bakso Spesial 15000 \t\t|")
    print("| \t8. Bakso Komplit 20000 \t\t|")
    print("=========================================================")
    print()

    nama = str(input("Masukkan nama pemesan = "))
    print()
    meja = str(input("Masukkan nomor pemesan = "))
    print()
    makanan = int(input("Masukkan bakso yang akan dibeli (Masukkan angka) = "))
    print()
    jumlah = int(input("Jumlah porsi (Masukkan angka)? = "))

    if makanan == 1:
        harga = 10000*jumlah
    elif makanan == 2:
        harga = 10000*jumlah
    elif makanan == 3 : 
        harga = 10000*jumlah
    elif makanan == 4 : 
        harga = 12000*jumlah
    elif makanan == 5 : 
        harga = 12000*jumlah
    elif makanan == 6 : 
        harga = 15000*jumlah
    elif makanan == 7 : 
        harga = 15000*jumlah
    elif makanan == 8 : 
        harga = 20000*jumlah
    

    print()
    print("=========================================")
    print("|\t\tDAFTAR MINUM\t\t|")
    print("|\t1. Es Jeruk\t\t7000\t|")
    print("|\t2. Es teh Manis\t\t5000\t|")
    print("|\t3. Air Putih\t\t3000\t|")
    print("|\t4. Teh Pucuk\t\t4000\t|")
    print("|\t5. Air Es\t\t1000\t|")
    print("=========================================")

    minum = int(input("Minuman yang dipesan (Masukkan angka) = "))
    pcs = int(input("Jumlah pesan minuman (Masukkan angka)? = "))

    if minum == 1:
        jeruk=7000*pcs
        total= harga+jeruk
    elif minum == 2:
        esteh=5000*pcs
        total= harga+esteh
    elif minum == 3:
        air=3000*pcs
        total=harga+air
    elif minum == 4:
        pucuk=4000*pcs
        total=harga+pucuk
    elif minum == 5:
        es = 1000*pcs
        total = harga+es

#Menghitung diskon
    diskon = 0

    if total > 50000:
        diskon = 0.05*total
    elif total > 100000 and total < 250000:
        diskon = 0.10*total
    elif total > 250000:
        diskon = 0.15*total

    harga_bayar = total-diskon

    print("Nama: ",nama)
    print("Nomor meja: ", meja)
    print("Makanan: ",makanan)
    print("Porsi makanan: ",jumlah)
    print("Minuman: ",minum)
    print("Porsi minuman: ",pcs)
    print("Diskon: ",diskon)
    print("Harga bayar: ",harga_bayar)
    print("Tanggal pesan: ",datetime.now())

    transaksi = str(input("Apakah anda akan membeli lagi? (ya/tidak) : "))

    if transaksi == "ya":
        pass
    elif transaksi == "tidak":
        break
