angka = []

bilangan = input("Masukan jumlah bilangan yang diinginkan: ")
bilangan = int(bilangan)

print("Program mengurutkan data ")

for i in range(0, bilangan):
    data = int(input("masukan bilangan ke- " + str(i+1) + " : "))
    angka.append(data)

print("Bilangan yang sudah diurutkan dari terkecil ke terbesar", sorted(angka))
