#membuat program menggunakan for-loop, list dan range

banyak = int(input("berapa jumlah datanya?"))

nama =[]
umur =[]
alaamat =[]
sekolah =[]

for i in range (0,banyak):
    print(f"data ke {i}")
    input_nama = input("Nama = ")
    input_umur =int(input("Umur ="))
    input_alamat = input("alamat =")
    input_sekolah = input("sekolah =")

    nama.append(input_nama)
    umur.append(input_umur)
    alaamat.append(input_alamat)
    sekolah.append(input_sekolah)

for i in range(0, len(nama)):
    data_nama = nama[i]
    data_umur = umur[i]
    data_alaamat = alaamat [i]
    data_sekolah = sekolah [i]
    print(f"{data_nama} berumur {data_umur} dan tinggal di{data_alaamat} sekolah di{data_sekolah}")
    print("========================================================================================")

