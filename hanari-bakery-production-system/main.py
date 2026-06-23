from bakery.butter_cookies import ButterCookies
from bakery.croissant import Croissant
from bakery.katalog import katalog_default
from bakery.muffin import Muffin
from bakery.roti_manis import RotiManis

JENIS_PRODUK = {
    "1": ("Roti Manis", RotiManis),
    "2": ("Croissant", Croissant),
    "3": ("Butter Cookies", ButterCookies),
    "4": ("Muffin", Muffin),
}


def tampilkan_menu() -> None:
    print(
        """
============================================
   HANARI BAKERY - SISTEM PRODUKSI PRODUK
============================================
1. Tambah produk baru
2. Tampilkan semua produk
3. Kalkulator estimasi profit
4. Simulasi proses produksi
5. Keluar
"""
    )


def input_angka(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("  ! Masukkan angka yang valid.")


def tambah_produk(daftar) -> None:
    print("\nPilih jenis produk:")
    for k, (nama, _) in JENIS_PRODUK.items():
        print(f"  {k}. {nama}")
    pil = input("Jenis (1-4): ").strip()
    if pil not in JENIS_PRODUK:
        print("  ! Pilihan tidak valid.")
        return
    _, kelas = JENIS_PRODUK[pil]

    nama = input("Nama produk (kosongkan untuk default): ").strip()
    kode = input("Kode produk (kosongkan untuk default): ").strip()
    pcs = int(input_angka("Jumlah pcs per resep (batch): "))
    biaya = input_angka("Biaya produksi per batch (Rp): ")
    harga = input_angka("Harga jual per batch (Rp): ")

    kwargs = {"biaya_produksi": biaya, "harga_jual": harga, "pcs_per_batch": pcs}
    if nama:
        kwargs["nama"] = nama
    if kode:
        kwargs["kode"] = kode

    produk = kelas(**kwargs)
    daftar.append(produk)
    print(f"  + Produk '{produk.nama}' berhasil ditambahkan.")


def tampilkan_semua(daftar) -> None:
    if not daftar:
        print("  (Belum ada produk.)")
        return
    for i, p in enumerate(daftar, 1):
        print(f"\n#{i}")
        print(p.info())


def pilih_produk(daftar):
    if not daftar:
        print("  (Belum ada produk.)")
        return None
    for i, p in enumerate(daftar, 1):
        print(f"  {i}. {p.nama} ({p.kode})")
    try:
        idx = int(input("Pilih nomor produk: ")) - 1
    except ValueError:
        idx = -1
    if 0 <= idx < len(daftar):
        return daftar[idx]
    print("  ! Pilihan tidak valid.")
    return None


def kalkulator_profit(daftar) -> None:
    p = pilih_produk(daftar)
    if not p:
        return
    jumlah = int(input_angka("Jumlah pcs yang akan diproduksi: "))
    try:
        hasil = p.estimasi_profit(jumlah)
    except ValueError as e:
        print(f"  ! {e}")
        return
    print(f"\n--- Estimasi Profit: {p.nama} ---")
    print(f"Jumlah produksi : {hasil['jumlah_pcs']} pcs")
    print(f"Total modal     : Rp{hasil['total_modal']:,.0f}")
    print(f"Total pendapatan: Rp{hasil['total_pendapatan']:,.0f}")
    print(f"Estimasi profit : Rp{hasil['total_profit']:,.0f}")
    print(f"Margin          : {hasil['margin_persen']:.1f}%")


def simulasi(daftar) -> None:
    p = pilih_produk(daftar)
    if p:
        print()
        print(p.simulasi_produksi())


def main() -> None:
    daftar = katalog_default()
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (1-5): ").strip()
        if pilihan == "1":
            tambah_produk(daftar)
        elif pilihan == "2":
            tampilkan_semua(daftar)
        elif pilihan == "3":
            kalkulator_profit(daftar)
        elif pilihan == "4":
            simulasi(daftar)
        elif pilihan == "5":
            print("Terima kasih telah menggunakan sistem Hanari Bakery!")
            break
        else:
            print("  ! Pilihan tidak valid.")


if __name__ == "__main__":
    main()
