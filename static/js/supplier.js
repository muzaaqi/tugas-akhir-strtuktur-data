// Fungsi toggle tabel
function toggleTable(tableType) {
    const defaultTableBtn = document.getElementById('defaultTableBtn');
    const produkTableBtn = document.getElementById('produkTableBtn');
        
    defaultTableBtn.classList.remove('active');
    produkTableBtn.classList.remove('active');
        
    if (tableType === 'default') {
        defaultTableBtn.classList.add('active');
        document.getElementById('defaultTable').classList.remove('hidden');
        document.getElementById('produkTable').classList.add('hidden');
    } else {
        produkTableBtn.classList.add('active');
        document.getElementById('produkTable').classList.remove('hidden');
        document.getElementById('defaultTable').classList.add('hidden');
    }
}

// Fungsi Pop Up Tambah Supplier
function openInputPopUp() {
    document.getElementById('inputPopUp').classList.remove('hidden');
    document.body.style.overflow = 'hidden';
}
        
function closeInputPopUp() {
    document.getElementById('inputPopUp').classList.add('hidden');
    document.body.style.overflow = 'auto';
}
        
// Fungsi Pop Up Kaitkan
function openKaitkanPopUp() {
    document.getElementById('kaitkanPopUp').classList.remove('hidden');
    document.body.style.overflow = 'hidden';
}

function closeKaitkanPopUp() {
    document.getElementById('kaitkanPopUp').classList.add('hidden');
    document.body.style.overflow = 'auto';
}

// Fungsi Tutup Pop Up Jika Menekan di Luar Pop Up Modal
window.onclick = function(event) {
    const inputPopUp = document.getElementById('inputPopUp');
    const kaitkanPopUp = document.getElementById('kaitkanPopUp');
            
    if (event.target === inputPopUp) {
        closeInputPopUp();
    }
    if (event.target === kaitkanPopUp) {
        closeKaitkanPopUp();
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