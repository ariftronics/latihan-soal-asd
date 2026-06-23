# Hanari Bakery - Sistem Informasi Produksi & Manajemen Produk

Proyek PBO: studi kasus produksi bakery. Aplikasi CLI Python yang menerapkan abstraksi, inheritance, dan interface.

## Fitur
- Tambah produk baru
- Tampilkan semua produk (beserta bahan baku, biaya, harga)
- Kalkulator estimasi profit (pilih produk + jumlah pcs)
- Simulasi proses produksi (pengadonan, pengembangan, pemanggangan, topping)

## Cara Menjalankan

```bash
cd hanari-bakery-production-system
python main.py
```

Butuh Python 3.8+ (tanpa dependensi eksternal).

## Struktur OOP
- `Produk` (abstrak): atribut & proses umum semua produk.
- Interface: `Bakeable`, `Packageable`, `Labelable`, `Proofable`, `Toppable`.
- `KueKering` (abstrak) untuk Butter Cookies & Muffin (punya topping).
- Produk: `RotiManis`, `Croissant`, `ButterCookies`, `Muffin`.

## Diagram Class
Lihat `docs/diagram_kelas.md`.

## Anggota Kelompok
1. ... (Ketua / Arsitek)
2. ...
3. ...
4. ...
5. ...
