import os
from datetime import datetime
from collections import Counter

# List untuk menyimpan catatan belajar
catatan_belajar = []

# ===========================
# FUNGSI UTILITAS
# ===========================

def clear_screen():
    """Membersihkan layar terminal"""
    os.system('clear' if os.name == 'posix' else 'cls')

def welcome_screen():
    """Menampilkan layar selamat datang"""
    clear_screen()
    print("=" * 60)
    print(" " * 15 + "★ APLIKASI STUDY LOG ★")
    print("=" * 60)
    print(" Pencatat Aktivitas Belajar Anda")
    print("=" * 60)
    print()

def pause():
    """Jeda sebelum melanjutkan"""
    input("\nTekan ENTER untuk melanjutkan...")

# ===========================
# FITUR UTAMA
# ===========================

def tambah_catatan():
    """Menambah catatan belajar baru"""
    clear_screen()
    print("=" * 60)
    print(" TAMBAH CATATAN BELAJAR")
    print("=" * 60)
    print()
    
    try:
        # Input mapel
        mapel = input("📚 Nama Mata Pelajaran: ").strip()
        if not mapel:
            print("\n❌ Mata pelajaran tidak boleh kosong!")
            pause()
            return
        
        # Input topik
        topik = input("📝 Topik/Materi: ").strip()
        if not topik:
            print("\n❌ Topik tidak boleh kosong!")
            pause()
            return
        
        # Input durasi dengan validasi
        while True:
            try:
                durasi = float(input("⏱️  Durasi Belajar (dalam menit): "))
                if durasi <= 0:
                    print("   ❌ Durasi harus lebih dari 0!")
                    continue
                break
            except ValueError:
                print("   ❌ Masukkan angka yang valid!")
        
        # Simpan catatan
        catatan = {
            'mapel': mapel,
            'topik': topik,
            'durasi': durasi,
            'tanggal': datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        }
        catatan_belajar.append(catatan)
        
        print("\n✅ Catatan berhasil disimpan!")
        print(f"   Mata Pelajaran: {mapel}")
        print(f"   Topik: {topik}")
        print(f"   Durasi: {durasi} menit")
        
    except KeyboardInterrupt:
        print("\n\n⚠️  Dibatalkan oleh pengguna")
    
    pause()

def lihat_catatan():
    """Menampilkan semua catatan belajar"""
    clear_screen()
    print("=" * 60)
    print(" DAFTAR CATATAN BELAJAR")
    print("=" * 60)
    
    if not catatan_belajar:
        print("\n📭 Belum ada catatan. Mulai tambahkan catatan belajar Anda!")
        pause()
        return
    
    print()
    for index, catatan in enumerate(catatan_belajar, 1):
        print(f"┌─ Catatan {index}")
        print(f"│  📚 Mata Pelajaran  : {catatan['mapel']}")
        print(f"│  📝 Topik/Materi    : {catatan['topik']}")
        print(f"│  ⏱️  Durasi          : {catatan['durasi']} menit")
        print(f"│  📅 Tanggal & Waktu : {catatan['tanggal']}")
        print(f"└─────────────────────────────────────────────────────────")
        print()
    
    pause()

def total_waktu():
    """Menghitung dan menampilkan total waktu belajar"""
    clear_screen()
    print("=" * 60)
    print(" STATISTIK WAKTU BELAJAR")
    print("=" * 60)
    print()
    
    if not catatan_belajar:
        print("📭 Belum ada catatan. Silakan tambah catatan terlebih dahulu!")
        pause()
        return
    
    # Hitung total durasi
    total_durasi = sum(catatan['durasi'] for catatan in catatan_belajar)
    
    # Konversi ke jam dan menit
    jam = int(total_durasi // 60)
    menit = int(total_durasi % 60)
    
    print(f"📊 Total Waktu Belajar: {total_durasi} menit")
    print(f"   ({jam} jam {menit} menit)")
    print()
    
    # Statistik per mapel
    print("📚 Breakdown per Mata Pelajaran:")
    print("-" * 60)
    
    mapel_dict = {}
    for catatan in catatan_belajar:
        if catatan['mapel'] not in mapel_dict:
            mapel_dict[catatan['mapel']] = 0
        mapel_dict[catatan['mapel']] += catatan['durasi']
    
    for mapel, durasi in sorted(mapel_dict.items(), key=lambda x: x[1], reverse=True):
        jam_mapel = int(durasi // 60)
        menit_mapel = int(durasi % 60)
        persentase = (durasi / total_durasi) * 100
        print(f"  • {mapel:20} : {durasi:6.1f} menit ({jam_mapel}j {menit_mapel}m) - {persentase:.1f}%")
    
    print("-" * 60)
    print(f"  Jumlah Catatan: {len(catatan_belajar)}")
    
    pause()

def mapel_favorit():
    """Menampilkan mata pelajaran dengan waktu belajar terbanyak"""
    clear_screen()
    print("=" * 60)
    print(" MATA PELAJARAN FAVORIT")
    print("=" * 60)
    print()
    
    if not catatan_belajar:
        print("📭 Belum ada catatan. Silakan tambah catatan terlebih dahulu!")
        pause()
        return
    
    # Hitung durasi per mapel
    mapel_dict = {}
    for catatan in catatan_belajar:
        if catatan['mapel'] not in mapel_dict:
            mapel_dict[catatan['mapel']] = 0
        mapel_dict[catatan['mapel']] += catatan['durasi']
    
    # Urutkan berdasarkan durasi
    mapel_sorted = sorted(mapel_dict.items(), key=lambda x: x[1], reverse=True)
    
    print("🏆 Mata Pelajaran Berdasarkan Waktu Belajar:")
    print("-" * 60)
    
    for rank, (mapel, durasi) in enumerate(mapel_sorted, 1):
        jam = int(durasi // 60)
        menit = int(durasi % 60)
        
        if rank == 1:
            emoji = "🥇"
        elif rank == 2:
            emoji = "🥈"
        elif rank == 3:
            emoji = "🥉"
        else:
            emoji = f"{rank}. "
        
        print(f"{emoji} {mapel:20} : {durasi:6.1f} menit ({jam}j {menit}m)")
    
    print("-" * 60)
    print(f"\n⭐ Mata Pelajaran Favorit: {mapel_sorted[0][0]}")
    print(f"   Total Waktu Belajar: {mapel_sorted[0][1]} menit")
    
    pause()

def hapus_catatan():
    """Menghapus catatan belajar tertentu"""
    clear_screen()
    print("=" * 60)
    print(" HAPUS CATATAN BELAJAR")
    print("=" * 60)
    print()
    
    if not catatan_belajar:
        print("📭 Belum ada catatan untuk dihapus!")
        pause()
        return
    
    # Tampilkan daftar catatan
    for index, catatan in enumerate(catatan_belajar, 1):
        print(f"{index}. {catatan['mapel']} - {catatan['topik']} ({catatan['durasi']} menit)")
    
    print()
    try:
        nomor = int(input("Masukkan nomor catatan yang ingin dihapus (0 untuk batal): "))
        
        if nomor == 0:
            print("Dibatalkan.")
            pause()
            return
        
        if 1 <= nomor <= len(catatan_belajar):
            catatan_dihapus = catatan_belajar.pop(nomor - 1)
            print(f"\n✅ Catatan '{catatan_dihapus['mapel']}' berhasil dihapus!")
        else:
            print(f"\n❌ Nomor tidak valid!")
    
    except ValueError:
        print("❌ Masukkan angka yang valid!")
    
    pause()

# ===========================
# MENU UTAMA
# ===========================

def menu_utama():
    """Menampilkan menu utama aplikasi"""
    while True:
        clear_screen()
        print("=" * 60)
        print(" MENU UTAMA - APLIKASI STUDY LOG")
        print("=" * 60)
        print()
        print("  1️⃣  📝 Tambah Catatan Belajar")
        print("  2️⃣  📖 Lihat Semua Catatan")
        print("  3️⃣  ⏱️  Total Waktu Belajar")
        print("  4️⃣  🏆 Mata Pelajaran Favorit")
        print("  5️⃣  🗑️  Hapus Catatan")
        print("  6️⃣  ❌ Keluar Aplikasi")
        print()
        print("=" * 60)
        
        pilihan = input("Pilih menu (1-6): ").strip()
        
        if pilihan == '1':
            tambah_catatan()
        elif pilihan == '2':
            lihat_catatan()
        elif pilihan == '3':
            total_waktu()
        elif pilihan == '4':
            mapel_favorit()
        elif pilihan == '5':
            hapus_catatan()
        elif pilihan == '6':
            clear_screen()
            print("=" * 60)
            print(" 👋 Terima kasih telah menggunakan Aplikasi Study Log!")
            print(" Semoga aktivitas belajar Anda sukses! 🎓")
            print("=" * 60)
            print()
            break
        else:
            input("❌ Pilihan tidak valid! Tekan ENTER untuk mencoba lagi...")

# ===========================
# MAIN PROGRAM
# ===========================

if __name__ == "__main__":
    welcome_screen()
    input("Tekan ENTER untuk memulai...")
    menu_utama()

