# UAS PEMROGRAMAN KOMPUTER D

# PROGRAM GAME SEDERHANA

import random
z = random.randrange(1, 6)
x = random.randrange(1, 6)

print('''Selamat Datang di Game Random Fighter

Karakter Hero :
1. Penyerang
2. Bertahan''')

opsi = int(input('Pilih Kategori Hero (Masukan Angka) :'))

if opsi == 1:
    print('''
Hero :''')
    hero = ['1. Martis', '2. Alucard']
    a, b = hero
    print(a)
    print(b)
    pilihan = int(input('Pilih Hero anda (Masukan Angka) :'))

    if pilihan == 1:
        print('''
Pertarungan Dimulai!!!''')

        class fighter:

            def __init__(self, nama, power):
                self.nama = nama
                self.power = power

            def tampilkan_profil(self):
                print("   Nama  : ", self.nama)
                print("   Power : ", self.power)

        fighter1 = fighter("Martis", z)
        fighter2 = fighter("Alucard", x)

        print('1. Hero')
        fighter1.tampilkan_profil()
        print('2. Hero')
        fighter2.tampilkan_profil()

        player1 = {'name': 'Martis', 'power': z + 1}
        player2 = {'name': 'Alucard', 'power': x}
        def attack(attacker, defender):
            if (attacker['power'] > defender['power']):
                print('WIN')
            else:
                print('LOSE')
        attack(player1, player2)

    elif pilihan == 2:
        print('''
Pertarungan Dimulai!!!''')

        class fighter:

            def __init__(self, nama, power):
                self.nama = nama
                self.power = power

            def tampilkan_profil(self):
                print("   Nama  : ", self.nama)
                print("   Power : ", self.power)

        fighter1 = fighter("Martis", z)
        fighter2 = fighter("Alucard", x)

        print('1. Hero')
        fighter1.tampilkan_profil()
        print('2. Hero')
        fighter2.tampilkan_profil()

        player1 = {'name': 'Martis', 'power': z - 1}
        player2 = {'name': 'Alucard', 'power': x}
        def attack(attacker, defender):
            if (attacker['power'] > defender['power']):
                print('WIN')
            else:
                print('LOSE')
        attack(player2, player1)

    else:
        print('unknown')

elif opsi == 2:
    print('''
Hero :''')
    hero = ['1. Martis', '2. Alucard']
    a, b = hero
    print(a)
    print(b)
    pilihan = int(input('Pilih Hero anda (Masukan Angka) :'))

    if pilihan == 1:
        print('''
Pertarungan Dimulai!!!''')

        class fighter:

            def __init__(self, nama, defend):
                self.nama = nama
                self.defend = defend

            def tampilkan_profil(self):
                print("   Nama  : ", self.nama)
                print("   Defend : ", self.defend)


        fighter1 = fighter("Martis", z)
        fighter2 = fighter("Alucard", x)

        print('1. Hero')
        fighter1.tampilkan_profil()
        print('2. Hero')
        fighter2.tampilkan_profil()

        player1 = {'name': 'Martis', 'defend': z}
        player2 = {'name': 'Alucard', 'defend': x - 1}
        def defend(attacker, defender):
            if (attacker['defend'] < defender['defend']):
                print('WIN')
            else:
                print('LOSE')
        defend(player2, player1)

    elif pilihan == 2:
        print('''
Pertarungan Dimulai!!!''')

        class fighter:

            def __init__(self, nama, defend):
                self.nama = nama
                self.defend = defend

            def tampilkan_profil(self):
                print("   Nama  : ", self.nama)
                print("   Defend : ", self.defend)

        fighter1 = fighter("Martis", z)
        fighter2 = fighter("Alucard", x)

        print('1. Hero')
        fighter1.tampilkan_profil()
        print('2. Hero')
        fighter2.tampilkan_profil()

        player1 = {'name': 'Martis', 'defend': z}
        player2 = {'name': 'Alucard', 'defend': x + 1}
        def defend(attacker, defender):
            if (attacker['defend'] < defender['defend']):
                print('WIN')
            else:
                print('LOSE')
        defend(player1, player2)

    else:
        print('unknown')

else:
    print('unknown')
