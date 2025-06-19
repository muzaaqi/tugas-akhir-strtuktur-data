import sqlite3
from modules.produk import ProdukBST

con = sqlite3.connect('./db/database.db', check_same_thread=False)
cur = con.cursor()

bst = ProdukBST()

def input_transaksi(nama_konsumen, sku, jumlah):
    if bst.pastikan_sku(sku) == True:
        nama_produk = bst.cari_produk(sku)[1]
        harga_satuan = bst.cari_produk(sku)[2]
        subtotal = float(jumlah) * harga_satuan
        cur.execute('''INSERT INTO transaksi (nama_konsumen, sku, nama_produk, jumlah, subtotal) VALUES (?, ?, ?, ?, ?)''', (nama_konsumen, sku, nama_produk,  jumlah, subtotal))
        cur.execute('''UPDATE produk SET jumlah_stok = jumlah_stok - ?, terjual = terjual + ? WHERE sku = ?''', (jumlah, jumlah, sku))
        con.commit()
        return "Transaksi berhasil ditambahkan"
    else:
        return "Transaksi gagal ditambahkan"

def lihat_transaksi():
    cur.execute('''SELECT * FROM transaksi ORDER BY id''')
    return cur.fetchall()

def lihat_transaksi_subtotal():
    cur.execute('''SELECT * FROM transaksi ORDER BY subtotal DESC''')
    return cur.fetchall()
