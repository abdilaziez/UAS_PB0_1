from mysql.connector import connection
from Model import Model
from DBConnector import DBConnect
from data_barang import dataBarang

class dataTransaksi(Model):

    def __init__(self):
        super().__init__("transaksi",["tanggal","id_Barang","jumlahBarang"])

    def getDataTransaksi(self):
        connection = DBConnect()
        query = "SELECT transaksi.tanggal, data_barang.namaBarang , data_barang.hargaBeli , data_barang.hargaJual , transaksi.jumlahBarang ,(data_barang.hargaJual*transaksi.jumlahBarang) AS harga_total FROM transaksi JOIN data_barang ON transaksi.id_Barang = data_barang.id_Barang ORDER BY transaksi.tanggal"
        result = connection.executeSelect(query)
        for colomn in result:
            print("tanggal : ", colomn[0])
            print("nama barang : ", colomn[1])
            print("harga beli : ", colomn[2])
            print("harga jual : ", colomn[3])
            print("jumlah yang dibeli : ", colomn[4])
            print("harga total : ", colomn[3])
            print("*"*10)

    def getDataTotalBayar():
        connection = DBConnect()
        query = "SELECT (hargaJual * 2) FROM data_barang WHERE id_Barang = 3"
        result = connection.executeSelect(query)
        print(result)


    def showLaporanKeuangan():
        connection = DBConnect()
        query = "SELECT transaksi.tanggal, SUM(transaksi.jumlahBarang * data_barang.hargaJual) AS pendapatan_kotor,SUM((transaksi.jumlahBarang * data_barang.hargaJual) - (transaksi.jumlahBarang * data_barang.hargaBeli)) AS pendapatan_bersih FROM transaksi JOIN data_barang ON transaksi.id_Barang=data_barang.id_Barang GROUP BY transaksi.tanggal"
        result = connection.executeSelect(query)
        return result
            

    def deleteTransaksi(self,id):
        connection = DBConnect()
        query = "DELETE FROM transaksi WHERE id= "+str(id)
        print(query)
        result = connection.executeDelete(query)

    def dataPembelian(self,id):
        connection = DBConnect()
        query = "SELECT jumlahBarang FROM transaksi WHERE id_Barang= "+str(id)
        result = connection.executeSelect(query)
        return result[0]
    # def kurangiStok(self,id):
    #     connection = DBConnect()
    #     query = "UPDATE data_barang SET stok = stok - jumlahBarang WHERE id_Barang= "+str(id)
    #     print(query)
    #     result = connection.executeUpdate(query)

