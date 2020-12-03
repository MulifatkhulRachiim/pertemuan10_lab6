while True:
    print("")
    print("================================")
    print("======== DATA MAHASISWA ========")
    print("================================")
    x = input("(L)ihat \n(T)ambah \n(U)bah \n(H)apus \n(K)eluar \nPilih menu : ")
    if x.lower() == "l":
        tampilkan()
    elif x.lower() == "t":
        tambah()
    elif x.lower() == "u":
        ubah()
    elif x.lower() == "h":
        hapus()
    elif x.lower() == "k":
        print()
        print("=================================")
        print("====== KELUAR DARI PROGRAM ======")
        print("=================================")
        break

    else:
        print()
        print("==================================")
        print("== Pilihan Anda Tidak Tersedia ==")
        print("== Pilihlah Menu Yang Tersedia ==")
        print("==================================")