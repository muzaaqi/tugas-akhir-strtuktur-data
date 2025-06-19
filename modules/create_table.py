import sqlite3

con = sqlite3.connect('./db/database.db', check_same_thread=False)
cur = con.cursor()

def buat_tabel():
    cur.execute('''
    CREATE TABLE IF NOT EXISTS produk (
        sku TEXT PRIMARY KEY UNIQUE,
        nama_produk TEXT NOT NULL,
        harga_satuan REAL NOT NULL,
        jumlah_stok INTEGER NOT NULL,
        terjual INTEGER,
        id_supplier INTEGER,
        dibuat TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        diupdate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (id_supplier) REFERENCES supplier (id)
    )
    ''')

    cur.execute('''
    CREATE TABLE IF NOT EXISTS transaksi (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nama_konsumen TEXT NOT NULL,
        sku TEXT NOT NULL,
        nama_produk TEXT NOT NULL,
        jumlah INTEGER NOT NULL,
        subtotal REAL NOT NULL,
        tanggal TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (sku) REFERENCES produk (sku),
        FOREIGN KEY (nama_produk) REFERENCES produk (nama_produk)
    )
    ''')

    cur.execute('''
    CREATE TABLE IF NOT EXISTS supplier (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nama_perusahaan TEXT NOT NULL,
        alamat TEXT NOT NULL,
        nama_kontak TEXT NOT NULL,
        telepon TEXT NOT NULL UNIQUE,
        tanggal TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')

    con.commit()