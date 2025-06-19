// Fungsi Pop Up Tambah Produk
function openInputPopUp() {
    document.getElementById('inputPopUp').classList.remove('hidden');
    document.body.style.overflow = 'hidden';
}

function closeInputPopUp() {
    document.getElementById('inputPopUp').classList.add('hidden');
    document.body.style.overflow = 'auto';
}

// Fungsi Pop Up Restok
function openRestokPopUp() {
    document.getElementById('restokPopUp').classList.remove('hidden');
    document.body.style.overflow = 'hidden';
}

function closeRestokPopUp() {
    document.getElementById('restokPopUp').classList.add('hidden');
    document.body.style.overflow = 'auto';
}

// Fungsi Tutup Pop Up Jika Menekan di Luar Pop Up Modal
window.onclick = function(event) {
    const inputPopUp = document.getElementById('inputPopUp');
    const restokPopUp = document.getElementById('restokPopUp');
    
    if (event.target === inputPopUp) {
        closeInputPopUp();
    }
    if (event.target === restokPopUp) {
        closeRestokPopUp();
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