# Nama = Moh. Yusril Maqoshidana
# NIM = 222410102064

import random
kunciJawaban = random.randint(0, 100)

print('=' * 42)
print('     SELAMAT BERMAIN DI TEBAK NOMER')
print('=' * 42)

kesempatan = 7  # User memiliki 7 kesempatan menebak
Y = 0  # tebakan dimulai dari angka nol

for i in range(kesempatan):
    # user menginput angka
    tebakan = int(input('\nSilakan ketik angka pilihanmu: '))
    Y += 1  # akan bertambah 1 jika user salah dan jika benar maka akan ditampilkan di output sebagai tebakan ke Y kali
    if tebakan == kunciJawaban:
        print(f"Tebakan anda tepat, anda menebak sebanyak {Y} kali")
        break  # jika user benar menebak maka program otomatis berhenti
    else:
        if tebakan < kunciJawaban and Y < kesempatan:  # mempermudah user dalam menebak angka
            print("Tidak tepat, angka terlalu kecil")
        if tebakan > kunciJawaban and Y < kesempatan:
            print("Tidak tepat, angka terlalu besar")

else:  # output ketika sudah menebak lebih dari 7
    print("Anda kurang beruntung")
