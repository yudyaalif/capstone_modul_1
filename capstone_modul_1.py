data = [ 
{'kode': 1141 , 'nama' : 'pensil 2b', 'merk' : 'faber castle' ,'harga satuan' : 6000 , 'jumlah': 25 },
{'kode': 1142 , 'nama' : 'pensil 2b', 'merk' : 'staedler' ,'harga satuan' : 5500 , 'jumlah': 30 },
{'kode': 1143 , 'nama' : 'pulpen hitam 0.5mm', 'merk' : 'standard' ,'harga satuan' : 2500 ,'jumlah': 60 },
{'kode': 1144 , 'nama' : 'pulpen hitam 0.5mm', 'merk' : 'joyko' ,'harga satuan' : 4000 ,'jumlah': 20 },
{'kode': 1145 , 'nama' : 'pulpen hitam 0.5mm', 'merk' : 'pilot' ,'harga satuan' : 3500 ,'jumlah': 30 },
{'kode': 1146 , 'nama' : 'pulpen biru 0.5mm', 'merk' : 'standard' ,'harga satuan' : 3000 ,'jumlah': 20 },
{'kode': 1147 , 'nama' : 'penggaris 30cm', 'merk' : 'faber castle' ,'harga satuan' : 7500 ,'jumlah': 40 },
{'kode': 1148 , 'nama' : 'penggaris 30cm', 'merk' : 'butterfly' ,'harga satuan' : 4000 ,'jumlah': 20 },
{'kode': 1149 , 'nama' : 'penggaris 50cm', 'merk' : 'butterfly' ,'harga satuan' : 7000 ,'jumlah': 30 },
{'kode': 1150 , 'nama' : 'buku tulis A5', 'merk' : 'sinar dunia' ,'harga satuan' : 3000 ,'jumlah': 50 },
{'kode': 1151 , 'nama' : 'buku tulis A5', 'merk' : 'big boss' ,'harga satuan' : 4000 ,'jumlah': 30 },
{'kode': 1152 , 'nama' : 'penghapus', 'merk' : 'joyko' ,'harga satuan' : 5000 ,'jumlah': 30 },
{'kode': 1153 , 'nama' : 'buku gambar A3', 'merk' : 'sinar dunia' ,'harga satuan' : 7000 ,'jumlah': 40 },
{'kode': 1154 , 'nama' : 'tempat pensil', 'merk' : 'deli' ,'harga satuan' : 15000 ,'jumlah': 30 }
]


user_1 = {'nama': 'ridwan', 'pwd': '1204'}
user_2 = {'nama': 'lissa', 'pwd': '2402'}
user_3 = {'nama': 'dini', 'pwd': '1607'}

### Restore Data Semula
def data_back():
    global data
    data = [ 
{'kode': 1141 , 'nama' : 'pensil 2b', 'merk' : 'faber castle' ,'harga satuan' : 6000 , 'jumlah': 25 },
{'kode': 1142 , 'nama' : 'pensil 2b', 'merk' : 'staedler' ,'harga satuan' : 5500 , 'jumlah': 30 },
{'kode': 1143 , 'nama' : 'pulpen hitam 0.5mm', 'merk' : 'standard' ,'harga satuan' : 2500 ,'jumlah': 60 },
{'kode': 1144 , 'nama' : 'pulpen hitam 0.5mm', 'merk' : 'joyko' ,'harga satuan' : 4000 ,'jumlah': 20 },
{'kode': 1145 , 'nama' : 'pulpen hitam 0.5mm', 'merk' : 'pilot' ,'harga satuan' : 3500 ,'jumlah': 30 },
{'kode': 1146 , 'nama' : 'pulpen biru 0.5mm', 'merk' : 'standard' ,'harga satuan' : 3000 ,'jumlah': 20 },
{'kode': 1147 , 'nama' : 'penggaris 30cm', 'merk' : 'faber castle' ,'harga satuan' : 7500 ,'jumlah': 40 },
{'kode': 1148 , 'nama' : 'penggaris 30cm', 'merk' : 'butterfly' ,'harga satuan' : 4000 ,'jumlah': 20 },
{'kode': 1149 , 'nama' : 'penggaris 50cm', 'merk' : 'butterfly' ,'harga satuan' : 7000 ,'jumlah': 30 },
{'kode': 1150 , 'nama' : 'buku tulis A5', 'merk' : 'sinar dunia' ,'harga satuan' : 3000 ,'jumlah': 50 },
{'kode': 1151 , 'nama' : 'buku tulis A5', 'merk' : 'big boss' ,'harga satuan' : 4000 ,'jumlah': 30 },
{'kode': 1152 , 'nama' : 'penghapus', 'merk' : 'joyko' ,'harga satuan' : 5000 ,'jumlah': 30 },
{'kode': 1153 , 'nama' : 'buku gambar A3', 'merk' : 'sinar dunia' ,'harga satuan' : 7000 ,'jumlah': 40 },
{'kode': 1154 , 'nama' : 'tempat pensil', 'merk' : 'deli' ,'harga satuan' : 15000 ,'jumlah': 30 }
]
    print('Data Anda berhasil dikembalikan seperti pada awal!')
    main_menu()
###
# Create
def create_data():
        print('Silahkan tambahkan data stock barang')
        kode1 = data[-1]['kode']+ 1
        nama1 = input('Masukan nama barang: ')
        merk1 = input('Masukan merk barang: ')
        while True:
                try:
                        harga_satuan1 = int(input('Masukan harga barang: '))
                        if harga_satuan1 > 0:
                                break
                except:
                        print('Masukan hanya angka')   
        while True:
                try:
                        jumlah1 = int(input('Masukan jumlah barang: '))
                        if jumlah1 > 0:
                                break
                except:
                        print('Masukan hanya angka')
        data.append({'kode' : kode1, 'nama': nama1, 'merk': merk1, 'harga satuan': harga_satuan1, 'jumlah': jumlah1})
        print('''Selamat! Data berhasil ditambahkan.
              Silahkan pilih menu selanjutnya:
              1. Tambahkan data lagi
              2. Kembali ke menu utama
              ''')
        while True:
                try:
                        menu_create = int(input('Masukan angka pilihan menu: '))
                        if menu_create == 1:
                                create_data()
                        elif menu_create == 2:
                                main_menu()
                                break
                        else:
                                print('Masukan angka dalam pilihan menu')
                                continue
                except:
                        print('Masukan angka dalam pilihan menu')
                        continue
                break
# Read
def show_data():
    from tabulate import tabulate
    print(tabulate(data, headers = 'keys', tablefmt = 'pretty'))
    return main_menu()
# Update
def kode_list():
    list_kode = []
    for vn in range(len(data)):
        calon_kode = list(data[vn].values())
        kode_f = calon_kode[0]
        list_kode.append(kode_f)
    return list_kode
###
def harga_list():
    list_harga = []
    for vn in range(len(data)):
        calon_harga = list(data[vn].values())
        harga_f = calon_harga[3]
        list_harga.append(harga_f)
    return list_harga
###
def jumlah_list():
    list_jumlah = []
    for vn in range(len(data)):
        calon_jumlah = list(data[vn].values())
        jumlah_f = calon_jumlah[4]
        list_jumlah.append(jumlah_f)
    return list_jumlah
###
def ubah_harga():
    while True:
        try:
            kodenya = int(input('Masukan kode barang yang akan diupdate: '))
            if kodenya in kode_list() :
                kodi = kode_list().index(kodenya)
                while True:
                    try:
                        ubah = int(input(f'Harga awal barang adalah {harga_list()[kodi]}, silahkan masukan harga baru: '))
                        data[kodi]['harga satuan'] = ubah
                        print(f'Data berhasil ditambahkan!, harga baru dari barang dengan kode {kodenya}, adalah {ubah}')
                        main_menu()    
                        break
                    except:
                        print('Masukan hanya angka harga baru')
            else:
                print('Masukan kode yang sesuai')
                continue
        except:
            print('Masukan hanya angka kode')
            continue
        break
###
def ubah_jumlah():
    while True:
        try:
            kodenya = int(input('Masukan kode barang yang akan diupdate: '))
            if kodenya in kode_list() :
                kodi = kode_list().index(kodenya)
                while True:
                    try:
                        ubah = int(input(f'Jumlah awal barang adalah {jumlah_list()[kodi]}, silahkan masukan update jumlah baru: '))
                        data[kodi]['jumlah'] = ubah
                        print(f'Data berhasil ditambahkan!, jumlah stock baru dari barang dengan kode {kodenya}, adalah {ubah}')
                        main_menu()    
                        break
                    except:
                        print('Masukan hanya angka jumlah baru')
            else:
                print('Masukan kode yang sesuai')
                continue
        except:
            print('Masukan hanya angka kode')
            continue
        break
### Menu utama ubah data
def ubah_data():
    print('''
          Pilih data yang ingin Anda ubah:
          1. Harga
          2. Jumlah
          ''')
    menu = input('Masukan angka menu yang Anda tuju: ')
    if menu == '1':
        print(tabulate(data, headers = 'keys', tablefmt = 'pretty'))
        ubah_harga()
    elif menu == '2':
        print(tabulate(data, headers = 'keys', tablefmt = 'pretty'))
        ubah_jumlah()
    else:
        print('Hanya masukan Angka menu saja')
        ubah_data()
# Delete
from tabulate import tabulate
def delete_data ():
    print(tabulate(data, headers = 'keys', tablefmt = 'pretty'))
    while True:
        try:
            angka = int(input('Masukan kode untuk barang yang ingin dihapus: '))
            if angka in kode_list():
                indx = kode_list().index(angka)
                data.pop(indx)
                print('Data berhasil dihapus!')
                main_menu()
                break
            else:
                print('Input invalid! Masukan kode barang dengan benar')
                continue
        except:
            print('Masukan hanya angka kode')
            continue
        break
# Sort
### List untuk di sort
def namamerk_list():
    list_namamerk = []
    for vn in range(len(data)):
        calon_namamerk = list(data[vn].values())
        namamerk_f = calon_namamerk[1], calon_namamerk[2]
        list_namamerk.append(namamerk_f)
    return list_namamerk
###
def merknama_list():
    list_merknama = []
    for vn in range(len(data)):
        calon_merknama = list(data[vn].values())
        merknama_f = calon_merknama[2], calon_merknama[1]
        list_merknama.append(merknama_f)
    return list_merknama
###
def harganamamerk_list():
    list_harganamamerk = []
    for vn in range(len(data)):
        calon_harga = list(data[vn].values())
        harga_f = calon_harga[3], calon_harga[1], calon_harga[2]
        list_harganamamerk.append(harga_f)
    return list_harganamamerk
###
def jumlahnamanerk_list():
    list_jumlahnamamerk = []
    for vn in range(len(data)):
        calon_jumlah = list(data[vn].values())
        jumlah_f = calon_jumlah[4], calon_jumlah[1], calon_jumlah[2]
        list_jumlahnamamerk.append(jumlah_f)
    return list_jumlahnamamerk
### Sort Ascending
from tabulate import tabulate
def sort_namamerk() :
    urut_namamerk = namamerk_list()
    urut_namamerk.sort()
    tabel_namamerk = []
    for x in urut_namamerk:
        if x in namamerk_list():
            idx = namamerk_list().index(x)
            tabel_namamerk.append(data[idx])
    print(tabulate(tabel_namamerk, headers = 'keys', tablefmt = 'pretty'))
###
def sort_merknama() :
    urut_merknama = merknama_list()
    urut_merknama.sort()
    tabel_merknama = []
    for x in urut_merknama:
        if x in merknama_list():
            idx = merknama_list().index(x)
            tabel_merknama.append(data[idx])
    print(tabulate(tabel_merknama, headers = 'keys', tablefmt = 'pretty'))       
###
def sort_harganamamerk() :
    urut_harga = harganamamerk_list()
    urut_harga.sort()
    tabel_harganamamerk = []
    for x in urut_harga:
        if x in harganamamerk_list():
            idx = harganamamerk_list().index(x)
            tabel_harganamamerk.append(data[idx])
    print(tabulate(tabel_harganamamerk, headers = 'keys', tablefmt = 'pretty'))
###
def sort_jumlahnamamerk() :
    urut_jumlah = jumlahnamanerk_list()
    urut_jumlah.sort()
    tabel_jumlahnamamerk = []
    for x in urut_jumlah:
        if x in jumlahnamanerk_list():
            idx = jumlahnamanerk_list().index(x)
            tabel_jumlahnamamerk.append(data[idx])
    print(tabulate(tabel_jumlahnamamerk, headers = 'keys', tablefmt = 'pretty'))       
### Sort Descending
def sort_namamerk_t() :
    urut_namamerk = namamerk_list()
    urut_namamerk.sort()
    urut_namamerk.reverse()
    tabel_namamerk = []
    for x in urut_namamerk:
        if x in namamerk_list():
            idx = namamerk_list().index(x)
            tabel_namamerk.append(data[idx])
    print(tabulate(tabel_namamerk, headers = 'keys', tablefmt = 'pretty'))
###
def sort_merknama_t() :
    urut_merknama = merknama_list()
    urut_merknama.sort()
    urut_merknama.reverse()
    tabel_merknama = []
    for x in urut_merknama:
        if x in merknama_list():
            idx = merknama_list().index(x)
            tabel_merknama.append(data[idx])
    print(tabulate(tabel_merknama, headers = 'keys', tablefmt = 'pretty'))       
###
def sort_harganamamerk_t() :
    urut_harga = harganamamerk_list()
    urut_harga.sort()
    urut_harga.reverse()
    tabel_harganamamerk = []
    for x in urut_harga:
        if x in harganamamerk_list():
            idx = harganamamerk_list().index(x)
            tabel_harganamamerk.append(data[idx])
    print(tabulate(tabel_harganamamerk, headers = 'keys', tablefmt = 'pretty'))       
###
def sort_jumlahnamamerk_t() :
    urut_jumlah = jumlahnamanerk_list()
    urut_jumlah.sort()
    urut_jumlah.reverse()
    tabel_jumlahnamamerk = []
    for x in urut_jumlah:
        if x in jumlahnamanerk_list():
            idx = jumlahnamanerk_list().index(x)
            tabel_jumlahnamamerk.append(data[idx])
    print(tabulate(tabel_jumlahnamamerk, headers = 'keys', tablefmt = 'pretty'))       
### Menu utama Sort Data
def sort_data():
    print('''
Silahkan pilih menu dasar sort data: 
    1. Sort by Nama Barang
    2. Sort by Merk Barang
    3. Sort by Harga Barang
    4. Sort by Jumlah Barang
          ''')
    while True:
        try:  
            menu = int(input('Silahkan pilih menu: '))
            if menu == 1:
                while True:
                    print('''
                      Pilih : 1. Untuk urutkan menaik
                              2. Untuk urutkan menurun
                      ''')
                    pilih1 = input('Masukan hanya angka yang ingin dipilih: ')
                    if pilih1 == '1':
                        sort_namamerk()
                        break
                    elif pilih1 == '2':
                        sort_namamerk_t()
                        break
                    else:
                        print('Masukan hanya angka 1 atau 2')
                        continue
            elif menu == 2:
                while True:
                    print('''
                      Pilih : 1. Untuk urutkan menaik
                              2. Untuk urutkan menurun
                      ''')
                    pilih2 = input('Masukan hanya angka yang ingin dipilih: ')
                    if pilih2 == '1':
                        sort_merknama()
                        break
                    elif pilih2 == '2':
                        sort_merknama_t()
                        break
                    else:
                        print('Masukan hanya angka 1 atau 2')
                        continue
            elif menu == 3:
                while True:
                    print('''
                      Pilih : 1. Untuk urutkan menaik
                              2. Untuk urutkan menurun
                      ''')
                    pilih3 = input('Masukan hanya angka yang ingin dipilih: ')
                    if pilih3 == '1':
                        sort_harganamamerk()
                        break
                    elif pilih3 == '2':
                        sort_harganamamerk_t()
                        break
                    else:
                        print('Masukan hanya angka 1 atau 2')
                        continue
            elif menu == 4:
                while True:
                    print('''
                      Pilih : 1. Untuk urutkan menaik
                              2. Untuk urutkan menurun
                      ''')
                    pilih4 = input('Masukan hanya angka yang ingin dipilih: ')
                    if pilih4 == '1':
                        sort_jumlahnamamerk()
                        break
                    elif pilih4 == '2':
                        sort_jumlahnamamerk_t()
                        break
                    else:
                        print('Masukan hanya angka 1 atau 2')
                        continue
            else:
                print('Masukan angka pilihan menu')
                continue
        except:
            print('Data invalid! Hanya masukan angka menu!')
            continue
        break
### Filter
### Fungsi untuk filter
def list_u_nama():
    new_list = []
    for x in range(len(data)):
        nama_l = list(data[x].values())[1]
        new_list.append(nama_l)
    return new_list
###
def list_u_merk():
    new_list = []
    for x in range(len(data)):
        nama_l = list(data[x].values())[2]
        new_list.append(nama_l)
    return new_list
###
def list_u_harga():
    new_list = []
    for x in range(len(data)):
        nama_l = list(data[x].values())[3]
        new_list.append(nama_l)
    return new_list
#
def harga_sort():
    harga_sort1 = list_u_harga()
    harga_sort1.sort()
    return harga_sort1
###
def list_u_jumlah():
    new_list = []
    for x in range(len(data)):
        nama_l = list(data[x].values())[4]
        new_list.append(nama_l)
    return new_list
#
def jumlah_sort():
    jumlah_sort1 = list_u_jumlah()
    jumlah_sort1.sort()
    return jumlah_sort1
### Menu Utama Filter
def filter_data() :
    print('''
Silahkan pilih filter :
1. Filter berdasarkan nama
2. Filter berdasarkan merk
3. Filter berdasarkan harga
4. Filter berdasarkan jumlah
      ''')
    
    while True:
        pilih = input('Masukan angka menu filter yang ingin Anda tuju: ')
        if pilih == '1':
            while True:
                nama_d1 = input('Masukan kata untuk memfilter: ')
                data_new1 = []
                if nama_d1 in list_u_nama():
                    for tr in data :
                        if list(tr.values())[1] == nama_d1:
                            data_new1.append(tr)
                    print(tabulate(data_new1, headers = 'keys', tablefmt = 'pretty'))
                    main_menu()
                    break
                else:
                    print('Kata yang anda masukan salah atau tidak lengkap!')
                    continue
        elif pilih == '2':
            while True:
                nama_d2 = input('Masukan kata untuk memfilter: ')
                data_new2 = []
                if nama_d2 in list_u_merk():
                    for t in data :
                        if list(t.values())[2] == nama_d2:
                            data_new2.append(t)
                    print(tabulate(data_new2, headers = 'keys', tablefmt = 'pretty'))
                    main_menu()
                    break
                else:
                    print('Kata yang anda masukan salah atau tidak lengkap!')
                    continue
        elif pilih == '3':
            while True:
                try:
                    harga_min = int(input('Masukan rentang harga minimal: '))
                    harga_max = int(input('Masukan rentang harga maksimal: '))
                    new_list_data = []
                    if harga_min > harga_max:
                        print('Rentang harga minimal harus lebih kecil dari harga maksimal!')
                        continue
                    elif harga_min > harga_sort()[-1] or harga_max < harga_sort()[0] :
                        print('Tidak ada barang dalam rentang harga tersebut')
                        continue
                    elif harga_min >= harga_sort()[0] and harga_min <= harga_sort()[-1]:
                        for t in data:
                            if harga_min < list(t.values())[3] < harga_max:
                                new_list_data.append(t)
                        print(tabulate(new_list_data, headers = 'keys', tablefmt = 'pretty'))
                        main_menu()
                        break
                except ValueError:
                    print('Hanya masukan angka!')
                    continue
        elif pilih == '4':
           while True:
                try:
                    jumlah_min = int(input('Masukan rentang jumlah minimal: '))
                    jumlah_max = int(input('Masukan rentang jumlah maksimal: '))
                    new_list_data1 = []
                    if jumlah_min > jumlah_max:
                        print('Rentang jumlah minimal harus lebih kecil dari jumlah maksimal!')
                        continue
                    elif jumlah_min > jumlah_sort()[-1] or jumlah_max < jumlah_sort()[0] :
                        print('Tidak ada barang dalam rentang jumlah tersebut')
                        continue
                    elif jumlah_min >= jumlah_sort()[0] and jumlah_min <= jumlah_sort()[-1]:
                        for t in data:
                            if jumlah_min < list(t.values())[4] < jumlah_max:
                                new_list_data1.append(t)
                        print(tabulate(new_list_data1, headers = 'keys', tablefmt = 'pretty'))
                        main_menu()
                        break
                except ValueError:
                    print('Hanya masukan angka!')
                    continue
        else:
            print('Masukan angka menu')
            continue
        break
# Main menu
def main_menu():
    print('''
--- Selamat datang dalam menu utama---
          
    Silahkan pilih menu :
    1. Lihat data
    2. Tambahkan data
    3. Ubah data
    4. Hapus Data
    5. Urutkan
    6. Filter
    7. Restore Data Awal
    8. Keluar
          ''')
    menu = input('Masukan angka menu yang Anda tuju: ')
    if menu == '1':
        show_data()
    elif menu == '2':
        create_data()
    elif menu == '3':
        ubah_data()
    elif menu == '4':
        delete_data()
    elif menu =='5':
        sort_data()
        main_menu()
    elif menu == '6':
        filter_data()
    elif menu == '7':
        data_back()
    elif menu == '8':
        print('Terima kasih, sampai berjumpa kembali')
    else:
        print('Hanya masukan Angka pada pilihan menu!')
        main_menu()
#Log in
from tabulate import tabulate
def login():
    print(''' 
        ---Selamat datang dalam sistem gudang Toko Bahagia---

        Silahkan pilih pilihan log in terlebih dahulu
        1. Pengelola Gudang
        2. Pengunjung
          ''')   
    while True:
        log_in = input('Masukan pilihan log in(angka 1 atau 2): ')
        if log_in == '1':
            print('Masukan nama user dan password dengan benar')
            while True:
                user1 = input('Masukan nama user: ')
                if user1 in user_1.values():
                    print('Silahkan masukan password sesuai dengan user')
                    while True:    
                        pasword1 = input('Masukan password: ')
                        if pasword1 in user_1.values():
                            main_menu()
                            break
                        else:
                            print('Masukan password dengan benar')
                            continue
                elif user1 in user_2.values():
                    print('Silahkan masukan password sesuai dengan user')
                    while True:    
                        pasword1 = input('Masukan password: ')
                        if pasword1 in user_2.values():
                            main_menu()
                            break
                        else:
                            print('Masukan password dengan benar')
                            continue
                elif user1 in user_3.values():
                    print('Silahkan masukan password sesuai dengan user')
                    while True:    
                        pasword1 = input('Masukan password: ')
                        if pasword1 in user_3.values():
                            main_menu()
                            break
                        else:
                            print('Masukan password dengan benar')
                            continue
                else:
                    print('Masukan user dengan benar')
                    continue 
                break
        elif log_in == '2':
            user2 = input('Masukan nama Anda: ')
            while True:
                print('''
        Silahkan pilih menu berikut :
        1. Lihat data
        2. Sorting Data             
        3. Keluar
                      ''')
                user2_menu = input('Masukan angka menu yang ingin Anda tuju: ')
                if user2_menu == '1':
                    print(tabulate(data, headers = 'keys', tablefmt = 'pretty'))
                    continue
                elif user2_menu == '2':
                    sort_data()
                else:
                    break
        else:
            print('Masukan hanya angka 1 atau 2')
            continue
        break

login()