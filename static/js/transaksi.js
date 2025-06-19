// Fungsi Toggle Sort
function toggleSort(sortType) {
    const defaultSortBtn = document.getElementById('defaultSortBtn');
    const subtotalSortBtn = document.getElementById('subtotalSortBtn');

    defaultSortBtn.classList.remove('active');
    subtotalSortBtn.classList.remove('active');

    if (sortType === 'default') {
        defaultSortBtn.classList.add('active');
        document.getElementById('defaultSort').classList.remove('hidden');
        document.getElementById('subtotalSort').classList.add('hidden');
    } else {
        subtotalSortBtn.classList.add('active');
        document.getElementById('subtotalSort').classList.remove('hidden');
        document.getElementById('defaultSort').classList.add('hidden');
    }
}

// Fungsi Pop Up Transaksi
function openTransaksiPopUp() {
    document.getElementById('transaksiPopUp').classList.remove('hidden');
    document.getElementById('errorAlert').classList.add('hidden');
    document.body.style.overflow = 'hidden';
}

function closeTransaksiPopUp() {
    document.getElementById('transaksiPopUp').classList.add('hidden');
    document.getElementById('transaksiForm').reset();
    document.getElementById('errorAlert').classList.add('hidden');
    document.body.style.overflow = 'auto';
}

// Fungsi Tutup Pop Up Jika Menekan di Luar Pop Up Modal
window.onclick = function(event) {
    const transaksiPopUp = document.getElementById('transaksiPopUp');

    if (event.target === transaksiPopUp) {
        closeTransaksiPopUp();
    }
}

// Fungsi Menghilangkan Pesan Setelah 3 Detik
setTimeout(() => {
    const alerts = document.querySelectorAll('.flash-alert');
    alerts.forEach(alert => {
    alert.classList.add('opacity-0', 'translate-y-2');
    setTimeout(() => alert.remove(), 500);
    }, 3000);
});

renderTable();