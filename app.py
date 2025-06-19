from flask import Flask, flash, render_template, request, url_for
from modules.create_table import buat_tabel
from modules.produk import ProdukBST
from modules.transaksi import input_transaksi, lihat_transaksi, lihat_transaksi_subtotal
from modules.supplier import input_supplier, pastikan_supplier, kaitkan, semua_supplier, semua_produk_terkait

buat_tabel()

bst = ProdukBST()

app = Flask(__name__)
app.secret_key = 'muzone_store'

@app.route('/')
def index():
    semua_produk = bst.semua_produk()
    semua_transaksi = lihat_transaksi()
    data_supplier = semua_supplier()

    total_produk = len(semua_produk)
    total_transaksi = len(semua_transaksi)
    total_supplier = len(data_supplier)
    
    stok_rendah = []
    for produk in semua_produk:
        jumlah_stok = produk[3]
        if jumlah_stok < 5:
            stok_rendah.append(produk)
    stok_rendah = stok_rendah[:5]

    transaksi_terbaru = sorted(semua_transaksi, key=lambda x: x[6], reverse=True)[:5]

    return render_template('index.html', total_produk=total_produk, total_transaksi=total_transaksi, total_supplier=total_supplier, stok_rendah=stok_rendah, transaksi_terbaru=transaksi_terbaru)

@app.route('/produk', methods=['GET', 'POST'])
def produk():
    if request.method == 'POST':
        if request.form.get('form') == 'input_produk':
            sku = request.form['sku']
            nama_produk = request.form['nama_produk']
            harga_satuan = float(request.form['harga_satuan'])
            jumlah_stok = int(request.form['jumlah_stok'])
            pesan_input = bst.input_produk(sku, nama_produk, harga_satuan, jumlah_stok)
            flash(pesan_input)
        elif request.form.get('form') == 'restok':
            sku = request.form['sku']
            if bst.pastikan_sku(sku) == True:
                jumlah_restok = request.form['jumlah_restok']
                pesan_restok = bst.restok_produk(sku, jumlah_restok)
                flash(pesan_restok)

    try:
        semua_produk = bst.semua_produk()
    except Exception as error:
        semua_produk = []
        print(f"Error fetching produk: {error}")
    return render_template('produk.html', semua_produk=semua_produk, )

@app.route('/transaksi', methods=['GET', 'POST'])
def transaksi():
    if request.method == 'POST':
        nama_konsumen = request.form['nama_konsumen']
        sku = request.form['sku']
        jumlah = int(request.form['jumlah'])
        pesan_transaksi = input_transaksi(nama_konsumen, sku, jumlah)
        flash(pesan_transaksi)

    semua_transaksi = lihat_transaksi()
    transaksi_subtotal = lihat_transaksi_subtotal()
    return render_template('transaksi.html', semua_transaksi=semua_transaksi, transaksi_subtotal=transaksi_subtotal)

@app.route('/supplier', methods=['GET', 'POST'])
def supplier():
    if request.method == 'POST':
        print("sukses")
        print(request.form.get('form'))
        if request.form.get('form') == 'supplier':
            print("sukses")
            nama_perusahaan = request.form['nama_perusahaan']
            alamat = request.form['alamat']
            nama_kontak = request.form['nama_kontak']
            telepon = request.form['telepon']
            pesan_supplier = input_supplier(nama_perusahaan, alamat, nama_kontak, telepon)
            flash(pesan_supplier)
        elif request.form.get('form') == 'kaitkan':
            id = request.form['id']
            sku = request.form['sku']
            if pastikan_supplier(id) == True and bst.pastikan_sku(sku) == True:
                pesan_kaitkan = kaitkan(id, sku)
                flash(pesan_kaitkan)
            else:
                return False

    data_supplier = semua_supplier()
    produk_terkait = semua_produk_terkait()
    return render_template('supplier.html', data_supplier=data_supplier, produk_terkait=produk_terkait)

if __name__ == '__main__':
    app.run(debug=True)