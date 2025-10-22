import random  # untuk membuat angka acak

# 1. Variabel
angka_rahasia = random.randint(1, 10)
tebakan = 0
percobaan = 0

print("=== Tebak Angka 1-10 ===")

# 2. Perulangan
while tebakan != angka_rahasia:
    tebakan = int(input("Masukkan tebakanmu: "))
    percobaan += 1

    # 3. Percabangan
    if tebakan < angka_rahasia:
        print("Terlalu kecil! Coba lagi.")
    elif tebakan > angka_rahasia:
        print("Terlalu besar! Coba lagi.")
    else:
        print(f"Benar! Angka rahasianya adalah {angka_rahasia}.")
        print(f"Kamu menebak dengan benar dalam {percobaan} kali percobaan.")
