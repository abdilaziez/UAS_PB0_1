from transaksi import dataTransaksi
from data_barang import dataBarang
from Model import Model

def main():
    while(True):
        print("SISTEM KASIR TOKO MEXDI")
        print("""
        1. tambah barang masuk
        2. lihat barang masuk
        3. ubah barang masuk
        4. hapus barang masuk
        5. tambah transaksi
        6. hapus transaksi
        7. lihat transaksi
        8. lihat laporan keuangan
        """)
        inputan = int(input("Masukan Pilihan : "))
        if  inputan == 1:
            insertBarang()
        elif inputan == 2:
            showAllData()
        elif inputan == 3:
            updateBarang()
        elif inputan == 4:
            deleteBarang()
        elif inputan == 5 :
            insertTransaksi()
        elif inputan == 6:
            deleteTransaksi()
        elif inputan == 7:
            showDataTransaksi()
        elif inputan == 8:
            laporanKeuangan()
        finish = input("Selesai? (Y/N)")
        if finish == 'Y':
            break

def insertBarang():
    print("----------TAMBAH DATA BARANG MASUK-------------")
    put_nama = str(input("Masukan nama barang : "))
    put_harbel = str(input("Masukan harga beli : "))
    put_harjul = str(input("Masukkan harga jual : "))
    put_stok = str(input("Masukkan jumlah stok barang : "))
    model = dataBarang()
    model.insert([put_nama,put_harjul,put_harbel,put_stok])


def showAllData():
    print("-----------DAFTAR BARANG MASUK-----------")
    model = dataBarang()
    data = model.getAllData()
    for colomn in data:
        print("id : ", colomn[0])
        print("nama barang : ", colomn[1])
        print("harga jual : ", colomn[2])
        print("stok : ", colomn[3])
        print("*"*10)

# def showStok():
#     id = int(input("id nya : "))
#     model = dataTransaksi()
#     data = model.dataPembelian(id)

def updateBarang():
    import Model
    model = dataBarang()
    print("------------UPDATE BARANG MASUK-----------")
    showAllData()
    id_barang=int(input("masukkan ID barang yang ingin anda rubah : "))
    print("-" * 30)
    print("data apa yang ingin anda ganti?")
    print("1.Nama Barang")
    print("2.Harga Beli")
    print("3.Harga Jual")
    print("4.Stok Barang")
    pilihan=int(input("masukkan pilihan : "))
    if pilihan==1:
        nama_baru=str(input("masukkan nama baru : "))
        model.updateNamaBarang(nama_baru,id_barang)
    elif pilihan==2:
        harbel_baru=str(input("masukkan harga beli baru : "))
        model.updateHargaBeli(harbel_baru,id_barang)
    elif pilihan==3:
        harjul_baru=str(input("masukkan harga jual baru : "))
        model.updateHargaJual(harjul_baru,id_barang)
    elif pilihan==4:
        stok_baru=str(input("masukkan jumlah stok baru : "))
        model.updateStokBarang(stok_baru,id_barang)

def deleteBarang():
    model = dataBarang()
    print("-------------DELETE BARANG MASUK-----------")
    showAllData()
    ID=int(input("masukkan ID barang yang ingin anda hapus"))
    model.deleteBarang(ID)


def insertTransaksi():
    print("---------TAMBAH TRANSAKSI---------")
    print("Daftar Barang Toko : ")
    showAllData()
    put_tanggal=str(input("Masukkan tanggal transaksi : tahun-bulan-tanggal "))
    pilihan=str(input("masukkan id barang yang dipilih : "))
    jumlah=str(input("masukkan jumlah barang yang dibeli : "))
    model = dataTransaksi()
    model1 = dataBarang()
    model.insert([put_tanggal,pilihan,jumlah])
    # stok = model1.dataStok(pilihan)
    # pembelian = model.dataPembelian(pilihan)
    # stok_baru = stok - pembelian
    # model1.updateStokBarang(stok_baru,pilihan)
    while str(input("Ingin tambah barang : ")).upper()=="Y":
        pilihan=str(input("masukkan id barang yang dipilih : "))
        jumlah=str(input("masukkan jumlah barang yang dibeli : "))
        model = dataTransaksi()
        model.insert([put_tanggal,pilihan,jumlah])
        # stok = model1.dataStok(pilihan)
        # pembelian = model.dataPembelian(pilihan)
        # stok_baru = stok - pembelian
        # model1.updateStokBarang(stok_baru,pilihan)
def showDataTransaksi():
    print("-----------DAFTAR TRANSAKSI-----------")
    model = dataTransaksi()
    data = model.getDataTransaksi()

def deleteTransaksi():
    model = dataTransaksi()
    print("-----------DELETE TRANSAKSI--------------")
    showDataTransaksi()
    ID=int(input("masukkan ID transaksi yang ingin anda hapus"))
    model.deleteTransaksi(ID)

def laporanKeuangan():
    model = dataTransaksi()
    print("-------------LAPORAN KEUANGAN------------")
    data = model.showLaporanKeuangan()

main()







