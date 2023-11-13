import os
import time
import random
from tabulate import tabulate

#GAME
def game():
    rock = '''
        _______
    ---'   ____)
        (_____)
        (_____)
        (____)
    ---.__(___)
    '''

    paper = '''
        _______
    ---'   ____)__
            ______)
            _______)
            _______)
    ---.__________)
    '''

    scissors = '''
        _______
    ---'   ____)_______
            ___________)
        _______________)
        (____)
    ---.__(___)
    '''

    game_images = [rock, paper, scissors]

    user_input = input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n")

    # Check if the input is a digit and in the range 0-2
    if user_input.isdigit():
        user_choice = int(user_input)
        if 0 <= user_choice <= 2:
            print("You chose:")
            print(game_images[user_choice])
            
            # Computer's choice
            computer_choice = random.randint(0, 2)
            print("Computer chose:")
            print(game_images[computer_choice])

            # Game result conditions
            if user_choice == computer_choice:
                print("It's a draw! \n  REDEEM YOUR VOUCHER: 'ICUTBAIK1'")
            elif (user_choice == 0 and computer_choice == 2) or \
                (user_choice == 1 and computer_choice == 0) or \
                (user_choice == 2 and computer_choice == 1):
                print("You win! \n  REDEEM YOUR VOUCHER: 'ICUTBAIK2'")
            else:
                print("You lose")
        else:
            print("You typed an invalid number, YOU ARE LOSER!")
    else:
        # The input is not a digit (it might be a letter or something else)
        print("You did not enter a number, YOU ARE LOSER!")
    time.sleep(5)
    os.system('cls')  

#Dummy Produk
listProduk = [
    {
        'nama': 'Marlboro Merah',
        'stock': 20,
        'harga': 10000
    },
    {
        'nama': 'Marlboro Putih',
        'stock': 15,
        'harga': 15000
    },
    {
        'nama': 'Marloboro Mentol',
        'stock': 25,
        'harga': 20000
    }
]

#Variabel penampungan sementara
cart = []

#opsi admin 1 (show produk)
def menampilkanDaftarProduk() :
    os.system('cls')
    print('Daftar Produk\n')
    print(tabulate(listProduk, headers='keys', tablefmt='simple', showindex="always"))
    # for i in range(len(listProduk)) :
    #     print('{}\t| {}  \t| {}\t| {}'.format(i,listProduk[i]['nama'],listProduk[i]['stock'],listProduk[i]['harga']))

#opsi admin 2 (add produk)
def menambahProduk() :
    os.system('cls')
    namaProduk = input('Masukkan Nama Produk : ')
    stockProduk = int(input('Masukkan Stock Produk : '))
    hargaProduk = int(input('Masukkan Harga Produk : '))
    listProduk.append({
        'nama': namaProduk,
        'stock': stockProduk,
        'harga': hargaProduk
    })
    menampilkanDaftarProduk()

#opsi admin 3 (delete produk)
def menghapusProduk() :
    menampilkanDaftarProduk()
    indexProduk = int(input('Masukkan index Produk yang ingin dihapus : '))
    del listProduk[indexProduk]
    menampilkanDaftarProduk()

#opsi admin 4 (update produk)
def mengubahProduk():
    os.system('cls')
    menampilkanDaftarProduk()
    indexProduk = int(input('Masukkan indeks produk yang ingin diubah: '))
    if indexProduk >= 0 and indexProduk < len(listProduk):
        namaProdukBaru = input('Masukkan Nama Produk baru : ')
        stockProdukBaru = input('Masukkan Stock Produk baru : ')
        hargaProdukBaru = input('Masukkan Harga Produk baru : ')
        
        if namaProdukBaru != '':
            listProduk[indexProduk]['nama'] = namaProdukBaru
        if stockProdukBaru != '':
            listProduk[indexProduk]['stock'] = int(stockProdukBaru)
        if hargaProdukBaru != '':
            listProduk[indexProduk]['harga'] = int(hargaProdukBaru)
        
        print("Produk telah diupdate.")
        menampilkanDaftarProduk()
    else:
        print('Indeks produk tidak valid!')

#opsi Customer (beli produk)
def membeliProduk():
    os.system('cls')
    menampilkanDaftarProduk()
    
    while True:
        input_index = input('Masukkan index Produk yang ingin dibeli : ')
        input_qty = input('Masukkan jumlah yang ingin dibeli : ')

        if input_index.isdigit() and input_qty.isdigit():
            indexProduk = int(input_index)
            qtyProduk = int(input_qty)

            if indexProduk >= len(listProduk):
                print("Index produk tidak valid.")
                continue

            os.system('cls')
            if qtyProduk > listProduk[indexProduk]['stock']:
                print('Stock tidak cukup, stock {} tinggal {}'.format(listProduk[indexProduk]['nama'], listProduk[indexProduk]['stock']))
            else:
                cart.append({
                    'nama': listProduk[indexProduk]['nama'], 
                    'qty': qtyProduk, 
                    'harga': listProduk[indexProduk]['harga'], 
                    'index': indexProduk
                })

            print('Isi Cart :')
            cart_table = [[item['nama'], item['qty'], item['harga']] for item in cart]
            print(tabulate(cart_table, headers=['Nama', 'Qty', 'Harga'], tablefmt='simple'))

            checker = input('Mau beli yang lain? (ya/tidak) = ')
            os.system('cls')

            if checker.lower() == 'tidak':
                break

        else:
            print("Harap masukkan angka.")
            continue

        os.system('cls')
        menampilkanDaftarProduk()

    os.system('cls') 
    kodevoucer = input("masukkan kode voucer anda:")
    os.system('cls')
    print('Pembayaran')
    print(tabulate(cart_table, headers=['Nama', 'Qty', 'Harga'], tablefmt='simple'))
    totalHarga = 0

    for item in cart:
        if kodevoucer == "ICUTBAIK1":
            totalHarga += item['qty'] * item['harga'] * 90/100    
        elif kodevoucer == "ICUTBAIK2":
            totalHarga += item['qty'] * item['harga'] * 95/100 
        else:
            totalHarga += item['qty'] * item['harga']

    while True:
        print('Total Yang Harus Dibayar = {}'.format(totalHarga))
        jmlUang = input('Masukkan jumlah uang : ')

        if jmlUang.isdigit():
            jmlUang = int(jmlUang)
            if jmlUang >= totalHarga:
                kembali = jmlUang - totalHarga
                print('Terima kasih \n\nUang kembali anda : {}'.format(kembali))
                for item in cart:
                    listProduk[item['index']]['stock'] -= item['qty']
                cart.clear()
                time.sleep(3)
                os.system('cls')
                break
            else:
                kekurangan = totalHarga - jmlUang
                print('Uang anda kurang sebesar {}'.format(kekurangan))
                time.sleep(3)
                os.system('cls')
        else:
            print("Harap masukkan jumlah uang dalam format angka.")
            time.sleep(3)
            os.system('cls')


# Tampilan Front End
while True :                                                                                
    pilihanMenu = input('''
        WELCOME USER!

        Who Is This :
        1. Admin
        2. Customer
        
       Love a game, Wanna Play?                 
        3.GAME

        Insert user : ''')
    os.system('cls')

      # MENU ADMIN
    if(pilihanMenu == '1') :                                                                
        while True:
            password = input("Masukkan Password:")
            if (password == "icutcantik"):
                os.system('cls')
                while True :
                    pilihanAdmin = input('''
                    Welcome Admin

                    List Menu :
                    1. Show Product
                    2. Add Product
                    3. Delete Product
                    4. Update Product
                    5. Main menu

                    Masukkan angka Menu yang ingin dijalankan : ''')
                    if(pilihanAdmin == '1') :
                        menampilkanDaftarProduk()
                    elif(pilihanAdmin == '2') :
                        menambahProduk()
                    elif(pilihanAdmin == '3') :
                        menghapusProduk()
                    elif(pilihanAdmin == '4') :
                        mengubahProduk()
                    elif(pilihanAdmin == '5') :
                        print(pilihanMenu)
                        os.system('cls')
                        break    
        
            else:  
                print("Password anda salah")
                time.sleep(3)
                os.system('cls')
            break   
      # MENU CUSTOMER 
    elif(pilihanMenu == '2') :                                                             
        membeliProduk()
        # MENU GAME
    elif(pilihanMenu == '3') :                                                            
        game() 
      
    else:
        print("silahkan pilih menu 1, 2, atau 3")
        time.sleep(3)
        os.system('cls')