from mysql.connector import connection
from Model import Model
from DBConnector import DBConnect

class dataBarang(Model):

    def __init__(self):
        super().__init__("data_barang",["namaBarang","hargaJual","hargaBeli","stok"])
    
    def updateNamaBarang(self,namaBaru,id):
        connection = DBConnect()
        query = "UPDATE data_barang SET namaBarang='"+str(namaBaru)+"' WHERE id_Barang= "+str(id)
        print(query)
        result = connection.executeUpdate(query)

    def updateHargaJual(self,harjul,id):
        connection = DBConnect()
        query = "UPDATE data_barang SET hargaJual='"+str(harjul)+"' WHERE id_Barang= "+str(id)
        print(query)
        result = connection.executeUpdate(query)

    def updateHargaBeli(self,harbel,id):
        connection = DBConnect()
        query = "UPDATE data_barang SET hargaBeli='"+str(harbel)+"' WHERE id_Barang= "+str(id)
        print(query)
        result = connection.executeUpdate(query)

    def updateStokBarang(self,stok,id):
        connection = DBConnect()
        query = "UPDATE data_barang SET stok='"+str(stok)+"' WHERE id_Barang= "+str(id)
        print(query)
        result = connection.executeUpdate(query)

    def deleteBarang(self,id):
        connection = DBConnect()
        query = "DELETE FROM data_barang WHERE id_Barang= "+str(id)
        print(query)
        result = connection.executeDelete(query)

    def dataStok(self,id):
        connection = DBConnect()
        query = "SELECT stok FROM data_barang WHERE id_Barang= "+str(id)
        result = connection.executeSelect(query)
        return result[0]
    
    # def ambilDataStok(self,id):
    #     connection = DBConnect()
    #     query = "SELECT stok FROM data_barang WHERE id_Barang= "+str(id)
    #     print(query)
    #     result = connection.executeSelectOne(query)
