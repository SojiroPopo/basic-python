# Assignment #1 - Basic Python
# Yanuar Adrian Bomantara
# Soal no 2

# Variable input
r = input("Jari-jari lingkaran (cm) :")

# Luas lingkaran
luas = 22/7*(float(r)**2)

# Print text hasil input
text = "Luas lingkaran dengan jari-jari {} cm adalah {:.2f} cm\u00b2.".format(r, luas)
print(text)