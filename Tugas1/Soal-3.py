# Assignment #1 - Basic Python
# Yanuar Adrian Bomantara
# Soal no 3

# Variable input
teori = float(input("NamaNilai ujian teori :"))
praktek = float(input("Nilai ujian praktek :"))

# Condition
if teori < 70 and praktek < 70 :
    print("Anda harus mengulang ujian teori dan praktek")
elif teori < 70 and praktek >=70 :
    print("Anda harus mengulang ujian teori.")
elif teori >=70 and praktek <70 :
    print("Anda harus mengulang ujian praktek.")
else:
    print("Selamat, anda lulus!.")
