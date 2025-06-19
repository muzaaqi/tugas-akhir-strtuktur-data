import sqlite3

con = sqlite3.connect('./db/database.db', check_same_thread=False)

class Node:
    def __init__(self, sku, nama_produk, harga_satuan, jumlah_stok):
        self.sku = sku
        self.nama_produk = nama_produk
        self.harga_satuan = harga_satuan
        self.jumlah_stok = jumlah_stok
        self.left = None
        self.right = None

class ProdukBST:
    def __init__(self):
        self.con = con
        self.cur = con.cursor()
        self.root = None

    def input_produk(self, sku, nama_produk, harga_satuan, jumlah_stok):
        new_node = Node(sku, nama_produk, harga_satuan, jumlah_stok)
        try:
            self.cur.execute('''INSERT INTO produk (sku, nama_produk, harga_satuan, jumlah_stok, terjual) VALUES (?, ?, ?, ?, ?)''', (sku, nama_produk, harga_satuan, jumlah_stok, 0))
        except:
            return "Produk tidak dapat ditambahkan!"
        self.con.commit()
        
        if self.root is None:
            self.root = new_node
            return f"{nama_produk} dengan {sku} berhasil ditambhakan!"
        temp = self.root
        while True:
            if new_node.sku == temp.sku:
                return False
            if new_node.sku < temp.sku:
                if temp.left is None:
                    temp.left = new_node
                    return f"{nama_produk} dengan {sku} berhasil ditambhakan!"
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return f"{nama_produk} dengan {sku} berhasil ditambhakan!"
                temp = temp.right

    def restok_produk(self, sku, jumlah_restok):
        try:
            self.cur.execute('''UPDATE produk SET jumlah_stok = jumlah_stok + ?, diupdate = CURRENT_TIMESTAMP WHERE sku = ?''', (jumlah_restok, sku)) 
            self.con.commit()
        except:
            return f"Tidak dapat me-restok produk dengan {sku}!"
        return f"Berhasil me-restok produk dengan sku {sku} berjumlah {jumlah_restok}!"

    def pastikan_sku(self, sku):
        self.cur.execute('''SELECT sku FROM produk WHERE sku = ?''', (sku, ))
        if self.cur.fetchone() is None:
            return False
        else:
            return True

    def cari_produk(self, sku):
        self.cur.execute('''SELECT sku, nama_produk, harga_satuan, jumlah_stok, dibuat, diupdate FROM produk WHERE sku = ?''', (sku,))
        hasil_cari = self.cur.fetchall()[0]
        current = self.root
        while current:
            if sku == current.sku:
                return current.sku
            elif sku < current.sku:
                current = current.left
            else:
                current = current.right
        return hasil_cari

    def semua_produk(self):
        self.cur.execute('SELECT sku, nama_produk, harga_satuan, jumlah_stok, dibuat, diupdate FROM produk ORDER BY sku')
        return self.cur.fetchall()