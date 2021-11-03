#belajar Argument List

def jumlahkan (satu, dua, tiga=0):
    total = satu + dua + tiga
    print(f"total {satu + dua + tiga} = {total}")

jumlahkan (10, 10, )

def tambah (*list_angka):
    total = 0
    for angka in list_angka:
        total = total + angka
    print( f"total{list_angka} = {total}")

tambah (10, 10, 222.  )