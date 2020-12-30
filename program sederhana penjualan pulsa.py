# contoh program sederhana python menggunakan operasi branching atau percabangan dengan menggunakan metode if , elif dan else .

print("===============================================")
print("         Selamat Datang Di Parli Cell          ")
print("       Temmpat menjual kebutuhan ponsel        ")
print("===============================================")
bantu=input('ada yang bisa saya bantu ? [y/n] ')

if bantu == ('Y') or bantu == ('y'):
    print("oke silahkan pilih jenis apa yang ingin anda beli ")
    print("A.pulsa")
    print("B.kuota")
    print("C.kartu")
    beli=input('mau beli apa ? (silahkan masukkan kode seperti di atas) ')
    if beli == ("A") or beli == ("a"):
        print("Jenis Pulsa")
        print("1.xl")
        print("2.axis")
        print("3.telkomsel")
        print("4.3")
        pulsa=input("silahkan pilih Jenis pulsa yang ingin anda beli ")
        if pulsa == ('xl'):
            print('1.Rp:15.000')
            print('2.Rp:20.000')
            print('3.Rp:50.000')
            print('4.Rp:100.000')
            belipulsa=input("silahkan input nominal pulsa yang ingin di beli ")
            if belipulsa == ("1"):
                harga=(15000)
            elif belipulsa == ("2"):
                harga=(20000)
            elif belipulsa == ("3"):
                harga=(50000)
            elif belipulsa == ("4"):
                harga=(100000)
            else:
                print("maaf kode yang anda masukkan salah")

            print("yang anda masukkan adalah ",harga)    
            bayar=int(input("silahkan masukkan uang anda untuk melanjutkan pembayaran "))
            print("total kembalinya adalah",bayar-harga)
        elif pulsa == ('axis'):
            print('Rp:15.000')
            print('Rp:20.000')
            print('Rp:50.000')
            print('Rp:100.000')
        elif pulsa == ('telkomsel'):
            print('Rp:15.000')
            print('Rp:20.000')
            print('Rp:50.000')
            print('Rp:100.000')
        elif pulsa == ('3'):
            print('Rp:15.000')
            print('Rp:20.000')
            print('Rp:50.000')
            print('Rp:100.000')
        else:
            print("kode tidak ada")
    elif beli == ("B") or beli == ("b"):
        print("xl")
        print("axis")
        print("telkomsel")
        print("3")
        kuota=input("silahkan pilih kuota yang ingin anda beli ")
        if kuota == ('xl'):
            print('hanya tersedia kuota hotroad')
        elif kuota == ('axis'):
            print('hanya tersedia kuota rabu rawit')
        elif kuota == ('telkomsel'):
            print('hanya tersedia kuota paket malam')
        elif kuota == ('3'):
            print('hanya tersedia kuota AON')
        else:
            print("kode tidak valid")
    elif beli == ("C") or beli == ("c"):
        print("xl")
        print("axis")
        print("telkomsel")
        print("3")
        kartu=input("silahkan pilih kartu yng ingin anda belli ")
        if kartu == ('xl'):
            print('harga : Rp.10.000')
        elif kartu == ('axis'):
            print('harga : Rp.15.000')
        elif kartu == ('telkomsel'):
            print('harga : Rp.20.000')
        elif kartu == ('3'):
            print('harga : Rp.12.000')
        else:
            print("kode yang anda masukan tidak tersedia ")
    else:
        print("kode salah")
elif bantu == ('N') or bantu == ('n'):
    print("baik terimakasih sudah mau mengunjungi toko kami ")
else:
    print("kode yang anda masukkan salah ")
