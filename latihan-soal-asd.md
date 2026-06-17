# Latihan Soal Algoritma & Struktur Data (Persiapan UAS)

Kumpulan latihan soal **bertahap** (mudah → sedang → sulit) beserta **pembahasan**.
Topik sesuai RPS: analisis kompleksitas (Big-O), array, stack & queue, linked list, sorting, dan searching.

> Tips belajar: kerjakan dulu soalnya sendiri, baru buka bagian **Pembahasan**.

---

## Daftar Isi
1. [Analisis Kompleksitas (Big-O)](#1-analisis-kompleksitas-big-o)
2. [Array](#2-array)
3. [Stack & Queue](#3-stack--queue)
4. [Linked List](#4-linked-list)
5. [Sorting](#5-sorting)
6. [Searching](#6-searching)

---

## 1. Analisis Kompleksitas (Big-O)

**Soal 1.1 (Mudah).** Tentukan Big-O dari potongan kode berikut:
```c
for (int i = 0; i < n; i++) {
    printf("%d", i);
}
```

<details><summary>Pembahasan 1.1</summary>

Loop berjalan sebanyak `n` kali dengan operasi konstan di dalamnya → **O(n)** (linear).
</details>

**Soal 1.2 (Sedang).** Tentukan Big-O dari:
```c
for (int i = 0; i < n; i++)
    for (int j = 0; j < n; j++)
        sum += a[i][j];
```

<details><summary>Pembahasan 1.2</summary>

Dua loop bersarang masing-masing `n` → `n × n` = **O(n²)** (kuadratik).
</details>

**Soal 1.3 (Sulit).** Tentukan Big-O dari:
```c
for (int i = 1; i < n; i = i * 2) {
    printf("%d", i);
}
```

<details><summary>Pembahasan 1.3</summary>

`i` digandakan tiap iterasi (1, 2, 4, 8, …). Jumlah iterasi sampai melewati `n` = log₂(n) → **O(log n)**.
</details>

---

## 2. Array

**Soal 2.1 (Mudah).** Array `A` punya alamat awal 1000 dan tiap elemen `int` = 4 byte. Berapa alamat `A[3]`?

<details><summary>Pembahasan 2.1</summary>

Alamat = base + (index × size) = 1000 + (3 × 4) = **1012**.
</details>

**Soal 2.2 (Sedang).** Sebutkan keunggulan & kelemahan array dibanding linked list.

<details><summary>Pembahasan 2.2</summary>

- **Keunggulan:** akses acak **O(1)** lewat index; hemat memori (tanpa pointer).
- **Kelemahan:** ukuran statis; sisip/hapus di tengah butuh geser elemen → **O(n)**.
</details>

---

## 3. Stack & Queue

**Soal 3.1 (Mudah).** Stack (bawah→atas): `2, 5, 8`. Setelah `pop()` lalu `push(10)`, isi stack jadi apa?

<details><summary>Pembahasan 3.1</summary>

`pop()` membuang `8` (LIFO) → `2, 5`. Lalu `push(10)` → **`2, 5, 10`**.
</details>

**Soal 3.2 (Sedang).** Queue kosong. Operasi: `enqueue(A), enqueue(B), dequeue(), enqueue(C), dequeue()`. Apa yang tersisa?

<details><summary>Pembahasan 3.2</summary>

FIFO: A,B masuk → dequeue keluar **A** → C masuk → dequeue keluar **B** → sisa **[C]**.
</details>

**Soal 3.3 (Sulit).** Ubah infix `A + B * C` ke postfix dan jelaskan peran stack.

<details><summary>Pembahasan 3.3</summary>

Postfix: **`A B C * +`**. Stack menyimpan operator berdasarkan prioritas; `*` lebih tinggi dari `+`, jadi `B C *` dihitung dulu lalu dijumlah dengan `A`.
</details>

---

## 4. Linked List

**Soal 4.1 (Mudah).** Apa beda singly dan doubly linked list?

<details><summary>Pembahasan 4.1</summary>

- **Singly:** 1 pointer (`next`) → hanya maju.
- **Doubly:** 2 pointer (`prev` & `next`) → maju & mundur, tapi butuh memori lebih.
</details>

**Soal 4.2 (Sedang).** `head → 10 → 20 → 30 → NULL`. Tuliskan langkah menyisipkan node `15` di antara `10` dan `20`.

<details><summary>Pembahasan 4.2</summary>

1. Buat `newNode` (data = 15).
2. `newNode->next = node(10)->next;` (menunjuk ke 20)
3. `node(10)->next = newNode;`

Hasil: `10 → 15 → 20 → 30`. Jika posisi diketahui → **O(1)**.
</details>

**Soal 4.3 (Sulit).** Kenapa pencarian di linked list O(n), dan kenapa linked list cocok untuk stack/queue?

<details><summary>Pembahasan 4.3</summary>

- Linked list tak punya index, harus telusuri dari `head` → **O(n)**.
- Cocok untuk stack/queue karena ukuran **dinamis** dan push/pop di ujung bisa **O(1)** tanpa geser elemen.
</details>

---

## 5. Sorting

**Soal 5.1 (Mudah).** Urutkan `[5, 2, 9, 1]` menaik dengan **Bubble Sort**, tunjukkan tiap pass.

<details><summary>Pembahasan 5.1</summary>

- Pass 1: [2, 5, 1, 9]
- Pass 2: [2, 1, 5, 9]
- Pass 3: [1, 2, 5, 9]
</details>

**Soal 5.2 (Sedang).** Jelaskan ide dasar **Merge Sort** dan kenapa O(n log n).

<details><summary>Pembahasan 5.2</summary>

Divide & Conquer: bagi dua sampai 1 elemen, lalu gabung terurut. Tingkat pembagian = log n, tiap tingkat butuh n operasi → **O(n log n)** di semua kasus.
</details>

**Soal 5.3 (Sulit).** Kapan **Quick Sort** worst case O(n²)? Cara menghindarinya?

<details><summary>Pembahasan 5.3</summary>

Worst case saat pivot selalu buruk (mis. data sudah terurut & pivot elemen pertama/terakhir) → partisi 1 vs n-1. Hindari dengan **pivot acak** atau **median-of-three**. Rata-rata tetap **O(n log n)**.
</details>

**Soal 5.4 (Tabel kompleksitas).** Lengkapi kompleksitas rata-rata Bubble, Selection, Insertion, Merge, Quick.

<details><summary>Pembahasan 5.4</summary>

| Algoritma | Best | Average | Worst | Stabil? |
|---|---|---|---|---|
| Bubble Sort | O(n) | O(n²) | O(n²) | Ya |
| Selection Sort | O(n²) | O(n²) | O(n²) | Tidak |
| Insertion Sort | O(n) | O(n²) | O(n²) | Ya |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | Ya |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | Tidak |
</details>

---

## 6. Searching

**Soal 6.1 (Mudah).** Berapa perbandingan **linear search** terburuk pada array 8 elemen?

<details><summary>Pembahasan 6.1</summary>

Worst case = **8** perbandingan → **O(n)**.
</details>

**Soal 6.2 (Sedang).** Array terurut `[1, 3, 5, 7, 9, 11, 13]`. Tunjukkan langkah **binary search** mencari `11`.

<details><summary>Pembahasan 6.2</summary>

1. mid index 3 → A[3]=7 < 11 → ke kanan
2. mid index 5 → A[5]=11 ✓ ketemu (2 langkah, **O(log n)**)
</details>

**Soal 6.3 (Sulit).** Kenapa binary search butuh data terurut, dan apa konsekuensinya pada pemilihan algoritma?

<details><summary>Pembahasan 6.3</summary>

Binary search membuang separuh ruang pencarian tiap langkah berdasarkan urutan. Jika data acak & dicari sekali → pakai linear search O(n). Jika dicari berkali-kali → urutkan dulu O(n log n) lalu binary search O(log n) per query.
</details>

---

_Dibuat sebagai materi belajar mandiri untuk persiapan UAS Algoritma & Struktur Data._
