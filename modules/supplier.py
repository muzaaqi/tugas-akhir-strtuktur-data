import sqlite3
from modules.produk import ProdukBST
con = sqlite3.connect('./db/database.db', check_same_thread=False)
cur = con.cursor()
bst = ProdukBST()

def input_supplier(nama_perusahaan, alamat, nama_kontak, telepon):
    try:
        cur.execute('''INSERT INTO supplier (nama_perusahaan, alamat, nama_kontak, telepon) VALUES (?, ?, ?, ?)''', (nama_perusahaan, alamat, nama_kontak, telepon))
        con.commit()
    except:
        return "Supplier sudah ada dalam database!"
    return f"Supplier {nama_perusahaan} berhasil ditambahkan!"

def pastikan_supplier(id):
    cur.execute('''SELECT id FROM supplier WHERE id = ?''', (id,))
    if cur.fetchone()[0] is None:
        return False
    else:
        return True

def kaitkan(id, sku):
    if pastikan_supplier(id) == True and bst.pastikan_sku(sku) == True:
        cur.execute('''UPDATE produk SET id_supplier = ?''', (id, ))
        con.commit()
        return f"Berhasil mengaitkan {id} dengan {sku}!"
    else:
        return "ID atau SKU yang anda masukkan tidak sesuai!"

def semua_supplier():
    data_supplier = []
    cur.execute('''SELECT * FROM supplier''')
    semua_supplier = cur.fetchall()
    for supplier in semua_supplier:
        id_supplier = supplier[0]
        cur.execute('''SELECT harga_satuan, terjual FROM produk WHERE id_supplier = ?''', (id_supplier,))
        semua_produk = cur.fetchall()
        jumlah_produk = len(semua_produk)
        if jumlah_produk == 0:
            status = "Supplier Aneh"
            persentase_komisi = 0
        elif 1 <= jumlah_produk <= 2:
            status = "Supplier Kecil"
            persentase_komisi = 0.02
        elif 3 <= jumlah_produk <= 5:
            status = "Supplier Akrab"
            persentase_komisi = 0.04
        else:
            status = "Supplier Juara"
            persentase_komisi = 0.07
        
        total_komisi = 0.0
        for produk in semua_produk:
            harga_satuan, terjual = produk
            total_penjualan = harga_satuan * float(terjual)
            komisi = total_penjualan * persentase_komisi
            total_komisi += komisi
        data_supplier.append((supplier[0], supplier[1], supplier[2], supplier[3], supplier[4], status, total_komisi, supplier[5]))
    return data_supplier
    

def semua_produk_terkait():
    produk_terkait = []

    # Ambil semua supplier
    cur.execute('SELECT id, nama_perusahaan FROM supplier')
    semua_supplier = cur.fetchall()  # list of tuples: [(id1, nama1), (id2, nama2), ...]

    for supplier in semua_supplier:
        cur.execute('''SELECT sku, nama_produk, harga_satuan, terjual FROM produk WHERE id_supplier = ?''', (supplier[0],))
        semua_produk = cur.fetchall()
        for produk in semua_produk:
            sku, nama_produk, harga_satuan, terjual = produk
            total_penjualan = harga_satuan * float(terjual)
            produk_terkait.append((supplier[0], supplier[1], sku, nama_produk, terjual, harga_satuan, total_penjualan))

    return produk_terkait
