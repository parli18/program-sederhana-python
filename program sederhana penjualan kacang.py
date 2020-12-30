print("=====================================================================")
print("                                MINIMARKET INDO                      ")
print("               Jl.Pedongkelan Belakang Rt.14 Rw.13 No.12             ")
print("                            Telp: 089664329614                       ")
print("                             kamis 10/12/2020                        ")
print("=====================================================================")

pilihan="y"
while pilihan == "y" or pilihan == "Y":
    pilihan=input("selamat datang mau lanjur berbelanja ? [y/n] ")
    if pilihan == "y" or pilihan == "Y":
        pilihan=20
    elif pilihan == "n" or pilihan == "N":
        print("baik terimakasih sudah mau mampir ke toko kami ")
        break
    else:
        print("kode tidak valid")
        break
    
    print("Berikut adalah produk yang tersedia di toko kami ")
    print("""              1.kacang 1 (gr)               Rp.15.000
              2.Telur 1/4 (gr)              Rp.12.000
              3.Minyak Sayur 2(Lt)          Rp.25.000
              4.Santan (1/4)                Rp.8.000
              5.Gula  1(kg)                 Rp.14.000""")

    belanja=input("silahkan maukkan produk yang ingin di beli ")

    if belanja == "kacang":
        bayar=12000
    elif belanja == "minyak sayur":
        bayar=25000
    elif belanja == "santan":
        bayar=8000
    elif belanja == "gula":
        bayar=14000
    else:
        print("tolong masukkan nama produk yang benar terimakasih")

    print("produk yang anda pilih adalah",belanja,"dengan harga",bayar,)
    pembayaran=input("mau bayar? [y/n] ")
    if pembayaran == "y":
        uang=int(input("silahkan masukkan uang anda untuk melanjutkan pembayaran "))
        print("total belanja adalah",bayar)
        print("total kembalinya adalah",uang-bayar)   
    else:
        print("") 
    
    