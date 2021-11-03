#belajar tipe data dictionary

pelayan ={"Nama" : "Eko", "Kampus" : "UMM", "NIM" : 23 }

nama = pelayan["Nama"]
Kampus = pelayan["Kampus"]
NIM = pelayan["NIM"]

for  key in pelayan:
    value = pelayan [key]
    print (f"{key} : {value}")