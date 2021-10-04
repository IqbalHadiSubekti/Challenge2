from datetime import datetime

total1=0
total2=0
totalsemua=0
diskon=0
jenis1=""
jenis2=""

pemesanan = "ya"

while pemesanan == "ya" :

    print("=== Restoran Makanan & Minuman ===")

    nama = input("Masukkan nama Konsumen: ")
    nomer = input("Masukkan nomer meja: ")

    print("")
    print ("Menu Makanan")
        
    def pilihan(i):
            switcher={
                    1:'----Nasi Goreng 12000----',
                    2:'----Sate Ayam 30000----',
                    3:'----Sop Iga 25000----'
                 }
            return switcher.get(i,"Masukan Pilihan yang Benar!")

    print("\nMenu Minuman")
    print("1. Nasi Goreng")
    print("2. Sate Ayam")
    print("3. Sop Iga")

    nomor=int(input("Masukan Pilihan: "))
    menu=pilihan(nomor)
    print (menu)
    porsi1= int(input("Berapa Porsi: "))

    if nomor==1:
        total1=total1+(porsi1*12000)
        print ("Hasilnya = ", total1)
        jenis1=("Es Teh Manis")
    if nomor==2:
        total1=total1+(porsi1*30000)
        print ("Hasilnya = ", total1)
        jenis1=("Es Jeruk")
    if nomor==3:
        total1=total1+(porsi1*25000)
        print ("Hasilnya = ", total1)
        jenis1=("Jus Alpukat")


    def pilihan(i):
            switcher={
                    1:'----Es Teh Manis 3000----',
                    2:'----Es Jeruk 4000----',
                    3:'----Jus Alpukat 9000----'
                 }
            return switcher.get(i,"Masukan Pilihan yang Benar!")

    print("\nMenu Minuman")
    print("1. Es Teh Manis")
    print("2. Es Jeruk")
    print("3. Jus Alpukat")

    nomor=int(input("Masukan Pilihan: "))
    menu=pilihan(nomor)
    print (menu)
    porsi2= int(input("Berapa Gelas: "))

    if nomor==1:
        total2=total2+(porsi2*3000)
        print ("Hasilnya = ", total2)
        jenis2=("Es Teh Manis")
    if nomor==2:
        total2=total2+(porsi2*4000)
        print ("Hasilnya = ", total2)
        jenis2=("Es Jeruk")
    if nomor==3:
        total2=total2+(porsi2*9000)
        print ("Hasilnya = ", total2)
        jenis2=("Jus Alpukat")
        
    totalsemua=total1+total2 

    if totalsemua > 50000:
        diskon = 0.05*totalsemua
    elif 100000 > totalsemua < 250000:
        diskon = 0.10*totalsemua
    elif totalsemua > 250000:
        diskon = 0.15*totalsemua

    harga = totalsemua-diskon

    print("\n=========================")
    print("======= S T R U K =======")
    print("=========================")

    print("Nama Konsumen :", nama)
    print("Nomer Meja :", nomer)
    print("Menu yang dipesan: ",menu)
    print("Harga pesanan", totalsemua)
    print("Jumlah Makanan: ",porsi1)
    print("Jumlah Minuman: ",porsi2)
    print("Diskon: ",diskon)
    print("Harga yang dibayarkan: ",harga)
    print("Tanggal pesan: ",datetime.now())

    lagi = str(input("Apakah anda akan membeli kembali? (ya/tidak) : "))

    if lagi == "ya":
        pass
    elif lagi == "tidak":
        break




