# Latihan Soal Algoritma & Struktur Data — Edisi Lengkap (Persiapan UAS)

Kumpulan latihan soal **lebih kompleks dan lebih banyak** beserta **pembahasan** untuk persiapan UAS.
Tingkat kesulitan ditandai: **[Mudah]**, **[Sedang]**, **[Sulit]**.

> Tips belajar: kerjakan dulu soalnya sendiri, baru buka **Pembahasan** untuk mencocokkan.

---

## Daftar Isi
1. Analisis Kompleksitas & Notasi Asimptotik
2. Rekursi & Divide and Conquer
3. Array, Matriks & String
4. Stack & Queue
5. Linked List
6. Tree & Binary Search Tree (BST)
7. Heap & Priority Queue
8. Hashing (Hash Table)
9. Sorting (Lanjutan)
10. Searching (Lanjutan)
11. Graph (BFS & DFS)
12. Soal Campuran (HOTS)

---

## 1. Analisis Kompleksitas & Notasi Asimptotik

**Soal 1.1 [Mudah].** Urutkan fungsi berikut dari pertumbuhan paling lambat ke paling cepat: `O(n^2)`, `O(1)`, `O(n log n)`, `O(2^n)`, `O(log n)`, `O(n)`, `O(n!)`.

<details><summary>Pembahasan 1.1</summary>
<code>O(1) &lt; O(log n) &lt; O(n) &lt; O(n log n) &lt; O(n^2) &lt; O(2^n) &lt; O(n!)</code>
</details>

**Soal 1.2 [Sedang].** Tentukan Big-O dari kode berikut:
```c
for (int i = 1; i <= n; i++)
    for (int j = 1; j <= i; j++)
        op();
```

<details><summary>Pembahasan 1.2</summary>
Jumlah operasi = <code>1 + 2 + ... + n = n(n+1)/2</code> &rarr; <b>O(n^2)</b>.
</details>

**Soal 1.3 [Sedang].** Tentukan Big-O dari:
```c
for (int i = 1; i <= n; i = i * 2)
    for (int j = 1; j <= n; j++)
        op();
```

<details><summary>Pembahasan 1.3</summary>
Loop luar berjalan <code>log2(n)</code> kali, loop dalam <code>n</code> kali &rarr; <b>O(n log n)</b>.
</details>

**Soal 1.4 [Sulit].** Selesaikan rekurens `T(n) = 2T(n/2) + n` dengan Master Theorem.

<details><summary>Pembahasan 1.4</summary>
Bentuk <code>aT(n/b)+f(n)</code> dengan a=2, b=2, f(n)=n. <code>n^(log_b a) = n^1 = n</code>. Karena f(n) = &Theta;(n^(log_b a)) &rarr; Case 2 &rarr; <b>T(n) = O(n log n)</b> (contoh: Merge Sort).
</details>

**Soal 1.5 [Sulit].** Selesaikan rekurens `T(n) = T(n/2) + O(1)`.

<details><summary>Pembahasan 1.5</summary>
Tiap langkah memangkas separuh input dengan kerja konstan &rarr; <b>T(n) = O(log n)</b> (contoh: Binary Search).
</details>

**Soal 1.6 [Sulit].** Sebuah dynamic array menggandakan kapasitas saat penuh. Berapa kompleksitas **amortized** satu operasi `push_back`?

<details><summary>Pembahasan 1.6</summary>
Total biaya penyalinan untuk n penyisipan = 1+2+4+...+n &lt; 2n = O(n). Dibagi n operasi &rarr; <b>O(1) amortized</b> (meskipun satu operasi resize bisa O(n)).
</details>

---

## 2. Rekursi & Divide and Conquer

**Soal 2.1 [Mudah].** Telusuri `factorial(4)` dan sebutkan kedalaman rekursinya.

<details><summary>Pembahasan 2.1</summary>
4*3*2*1 = <b>24</b>. Kedalaman rekursi = <b>4</b> (factorial(4)&rarr;3&rarr;2&rarr;1&rarr;base case 0/1).
</details>

**Soal 2.2 [Sedang].** Berapa kompleksitas Fibonacci rekursif naif, dan bagaimana dengan memoization?

<details><summary>Pembahasan 2.2</summary>
Naif: setiap panggilan bercabang dua &rarr; <b>O(2^n)</b> (lebih tepatnya O(&phi;^n)). Dengan memoization tiap nilai dihitung sekali &rarr; <b>O(n)</b> waktu, O(n) memori.
</details>

**Soal 2.3 [Sedang].** Tower of Hanoi dengan 4 cakram butuh berapa langkah minimum? Tuliskan rumusnya.

<details><summary>Pembahasan 2.3</summary>
Rumus <code>2^n - 1</code>. Untuk n=4 &rarr; <code>2^4 - 1 = </code> <b>15 langkah</b>.
</details>

**Soal 2.4 [Sulit].** Tuliskan fungsi rekursif menjumlahkan elemen array dan sebutkan base case-nya.

<details><summary>Pembahasan 2.4</summary>
<pre><code>int sum(int a[], int n) {
    if (n == 0) return 0;        // base case
    return a[n-1] + sum(a, n-1); // recursive case
}</code></pre>
Kompleksitas O(n).
</details>

**Soal 2.5 [Sulit].** Strategi Divide and Conquer punya 3 tahap. Sebutkan dan beri contoh algoritmanya.

<details><summary>Pembahasan 2.5</summary>
<b>Divide</b> (bagi masalah), <b>Conquer</b> (selesaikan sub-masalah secara rekursif), <b>Combine</b> (gabungkan hasil). Contoh: Merge Sort, Quick Sort, Binary Search.
</details>

---

## 3. Array, Matriks & String

**Soal 3.1 [Mudah].** Array `A[0..]` alamat awal 2000, tiap elemen 4 byte. Berapa alamat `A[5]`?

<details><summary>Pembahasan 3.1</summary>
<code>2000 + (5 x 4) = </code> <b>2020</b>.
</details>

**Soal 3.2 [Sedang].** Matriks 2D `M[4][5]` disimpan row-major, alamat awal 1000, elemen 2 byte. Berapa alamat `M[2][3]`?

<details><summary>Pembahasan 3.2</summary>
<code>alamat = base + ((i * jml_kolom) + j) * size = 1000 + ((2*5)+3)*2 = 1000 + 26 = </code> <b>1026</b>.
</details>

**Soal 3.3 [Sedang].** Diberi array, cari dua angka yang jumlahnya = target. Jelaskan solusi O(n).

<details><summary>Pembahasan 3.3</summary>
Gunakan hash set: untuk tiap `x`, cek apakah `target - x` sudah pernah dilihat. Jika ya, ketemu. Satu kali pass &rarr; <b>O(n)</b> waktu, O(n) memori (vs brute force O(n^2)).
</details>

**Soal 3.4 [Sulit].** Jelaskan cara memutar (rotate) array ke kiri sejauh k posisi dengan O(n) waktu dan O(1) memori tambahan.

<details><summary>Pembahasan 3.4</summary>
Teknik 3x reverse: (1) balik 0..k-1, (2) balik k..n-1, (3) balik seluruh array. Hasilnya array tergeser k posisi. Total <b>O(n)</b> waktu, <b>O(1)</b> memori.
</details>

---

## 4. Stack & Queue

**Soal 4.1 [Sedang].** Evaluasi ekspresi postfix: `5 1 2 + 4 * + 3 -`

<details><summary>Pembahasan 4.1</summary>
1+2=3 &rarr; 3*4=12 &rarr; 5+12=17 &rarr; 17-3 = <b>14</b>.
</details>

**Soal 4.2 [Sedang].** Jelaskan algoritma cek tanda kurung seimbang `()[]{}` menggunakan stack.

<details><summary>Pembahasan 4.2</summary>
Iterasi karakter: jika kurung buka &rarr; push; jika kurung tutup &rarr; cek apakah top stack adalah pasangannya, jika ya pop, jika tidak &rarr; tidak seimbang. Di akhir stack harus kosong. Kompleksitas O(n).
</details>

**Soal 4.3 [Sedang].** Circular queue berukuran 5, `front=2`, `rear=0`. Berapa jumlah elemen di dalamnya?

<details><summary>Pembahasan 4.3</summary>
<code>jumlah = (rear - front + size) % size = (0 - 2 + 5) % 5 = </code> <b>3 elemen</b>.
</details>

**Soal 4.4 [Sulit].** Konversi infix `A + B * C - (D / E)` ke postfix.

<details><summary>Pembahasan 4.4</summary>
Hasil: <b>A B C * + D E / -</b>. (`*` prioritas lebih tinggi dari `+`; tanda kurung memaksa `D/E` dihitung sebagai satu unit.)
</details>

**Soal 4.5 [Sulit].** Bagaimana mengimplementasikan Queue menggunakan dua Stack? Berapa kompleksitas amortized dequeue?

<details><summary>Pembahasan 4.5</summary>
Gunakan stack <code>in</code> untuk enqueue. Saat dequeue, jika <code>out</code> kosong, pindahkan semua dari <code>in</code> ke <code>out</code> (terbalik), lalu pop dari <code>out</code>. Tiap elemen dipindah maksimal sekali &rarr; <b>O(1) amortized</b>.
</details>

---

## 5. Linked List

**Soal 5.1 [Sedang].** Tuliskan langkah membalik (reverse) singly linked list secara iteratif.

<details><summary>Pembahasan 5.1</summary>
Gunakan 3 pointer prev=NULL, curr=head. Tiap langkah: simpan <code>next=curr-&gt;next</code>; <code>curr-&gt;next=prev</code>; <code>prev=curr</code>; <code>curr=next</code>. Akhirnya head=prev. Kompleksitas <b>O(n)</b>, memori O(1).
</details>

**Soal 5.2 [Sulit].** Jelaskan algoritma Floyd (tortoise & hare) untuk mendeteksi cycle pada linked list.

<details><summary>Pembahasan 5.2</summary>
Dua pointer: <code>slow</code> bergerak 1 langkah, <code>fast</code> 2 langkah. Jika ada cycle, keduanya akan bertemu; jika <code>fast</code> mencapai NULL &rarr; tidak ada cycle. Kompleksitas <b>O(n)</b> waktu, <b>O(1)</b> memori.
</details>

**Soal 5.3 [Sedang].** Bagaimana mencari node tengah linked list dalam satu kali traversal?

<details><summary>Pembahasan 5.3</summary>
Pointer slow (1 langkah) dan fast (2 langkah). Saat fast mencapai akhir, slow ada di tengah. <b>O(n)</b>, satu kali pass.
</details>

**Soal 5.4 [Sulit].** Diberi hanya pointer ke sebuah node (bukan head), hapus node tersebut dari singly linked list. (Node bukan node terakhir.)

<details><summary>Pembahasan 5.4</summary>
Salin data node berikutnya ke node ini, lalu lewati node berikutnya: <code>node-&gt;data = node-&gt;next-&gt;data; node-&gt;next = node-&gt;next-&gt;next;</code>. Kompleksitas <b>O(1)</b>.
</details>

**Soal 5.5 [Sedang].** Lengkapi tabel kompleksitas operasi (array vs singly linked list).

<details><summary>Pembahasan 5.5</summary>
<table>
<tr><th>Operasi</th><th>Array</th><th>Linked List</th></tr>
<tr><td>Akses index ke-i</td><td>O(1)</td><td>O(n)</td></tr>
<tr><td>Sisip di awal</td><td>O(n)</td><td>O(1)</td></tr>
<tr><td>Sisip di akhir</td><td>O(1)*</td><td>O(n) / O(1) bila ada tail</td></tr>
<tr><td>Cari nilai</td><td>O(n)</td><td>O(n)</td></tr>
</table>
<small>*amortized untuk dynamic array</small>
</details>

---

## 6. Tree & Binary Search Tree (BST)

**Soal 6.1 [Sedang].** Diberi pohon biner:
```
        A
       / \
      B   C
     / \   \
    D   E   F
```
Tuliskan hasil traversal Preorder, Inorder, dan Postorder.

<details><summary>Pembahasan 6.1</summary>
<b>Preorder</b> (Root,Left,Right): A B D E C F<br>
<b>Inorder</b> (Left,Root,Right): D B E A C F<br>
<b>Postorder</b> (Left,Right,Root): D E B F C A
</details>

**Soal 6.2 [Sedang].** Sisipkan urutan `50, 30, 70, 20, 40, 60, 80` ke BST kosong. Gambarkan strukturnya.

<details><summary>Pembahasan 6.2</summary>
<pre>        50
       /  \
     30    70
    / \   /  \
   20 40 60  80</pre>
Setiap nilai &lt; node ke kiri, &gt; node ke kanan.
</details>

**Soal 6.3 [Mudah].** Traversal apa pada BST yang menghasilkan data terurut menaik?

<details><summary>Pembahasan 6.3</summary>
<b>Inorder</b> (Left, Root, Right) menghasilkan urutan menaik pada BST.
</details>

**Soal 6.4 [Sulit].** Berapa kompleksitas pencarian di BST untuk kasus terbaik dan terburuk? Jelaskan penyebabnya.

<details><summary>Pembahasan 6.4</summary>
BST seimbang &rarr; tinggi log n &rarr; pencarian <b>O(log n)</b>. BST timpang/skewed (misal sisip data yang sudah terurut) &rarr; menyerupai linked list, tinggi n &rarr; <b>O(n)</b>. Solusi: pohon seimbang (AVL, Red-Black).
</details>

**Soal 6.5 [Sedang].** Berapa jumlah maksimum node pada pohon biner dengan tinggi `h` (akar tinggi 0)?

<details><summary>Pembahasan 6.5</summary>
<code>2^(h+1) - 1</code> node. Contoh h=3 &rarr; 15 node.
</details>

---

## 7. Heap & Priority Queue

**Soal 7.1 [Mudah].** Pada heap berbasis array (index mulai 0), tuliskan rumus index parent dan kedua anak dari node index `i`.

<details><summary>Pembahasan 7.1</summary>
Parent: <code>(i-1)/2</code> &middot; Anak kiri: <code>2i+1</code> &middot; Anak kanan: <code>2i+2</code>.
</details>

**Soal 7.2 [Sedang].** Bentuk min-heap dari array `[5, 3, 8, 1, 2]` (jelaskan hasil akhirnya).

<details><summary>Pembahasan 7.2</summary>
Setelah build-heap, akar = elemen terkecil (1). Salah satu bentuk valid: <code>[1, 2, 8, 5, 3]</code> (tiap parent &le; anak-anaknya).
</details>

**Soal 7.3 [Sedang].** Setelah extract-min dari min-heap, operasi apa yang dilakukan untuk mengembalikan properti heap, dan berapa kompleksitasnya?

<details><summary>Pembahasan 7.3</summary>
Pindahkan elemen terakhir ke akar, lalu lakukan <b>heapify-down (sift-down)</b> menukar dengan anak terkecil sampai posisi benar. Kompleksitas <b>O(log n)</b>.
</details>

**Soal 7.4 [Sulit].** Membangun heap dari n elemen acak: O(n log n) atau O(n)? Jelaskan.

<details><summary>Pembahasan 7.4</summary>
<b>O(n)</b> bila memakai build-heap bottom-up (sift-down dari node non-daun). Analisis deret menunjukkan total kerja terbatas pada O(n), bukan O(n log n) seperti dugaan naif.
</details>

---

## 8. Hashing (Hash Table)

**Soal 8.1 [Mudah].** Hash table ukuran 10 dengan `h(k) = k mod 10`. Di slot mana key 27 disimpan?

<details><summary>Pembahasan 8.1</summary>
<code>27 mod 10 = 7</code> &rarr; slot <b>7</b>.
</details>

**Soal 8.2 [Sedang].** Jelaskan perbedaan penanganan kolisi **chaining** vs **open addressing (linear probing)**.

<details><summary>Pembahasan 8.2</summary>
<b>Chaining</b>: tiap slot menyimpan linked list berisi semua key yang ber-hash sama. <b>Linear probing</b>: bila slot terisi, cari slot kosong berikutnya secara berurutan. Chaining lebih tahan beban penuh; probing hemat memori tapi rawan clustering.
</details>

**Soal 8.3 [Sedang].** Apa itu load factor, dan apa yang terjadi bila terlalu tinggi?

<details><summary>Pembahasan 8.3</summary>
<code>load factor = jumlah_elemen / ukuran_tabel</code>. Bila terlalu tinggi, kolisi meningkat dan operasi melambat &rarr; perlu <b>rehashing</b> (perbesar tabel & sisipkan ulang).
</details>

**Soal 8.4 [Sulit].** Berapa kompleksitas rata-rata dan terburuk operasi search pada hash table?

<details><summary>Pembahasan 8.4</summary>
Rata-rata <b>O(1)</b>. Terburuk <b>O(n)</b> bila semua key berkolisi ke slot yang sama (fungsi hash buruk).
</details>

---

## 9. Sorting (Lanjutan)

**Soal 9.1 [Sulit].** Lakukan satu langkah partition Lomuto pada `[7, 2, 1, 6, 8, 5, 3, 4]` dengan pivot = 4 (elemen terakhir). Tunjukkan hasilnya.

<details><summary>Pembahasan 9.1</summary>
Elemen &le; 4 dipindah ke kiri pivot: hasil <code>[2, 1, 3, 4, 8, 5, 7, 6]</code>, pivot 4 berada di posisi akhir yang benar (indeks 3).
</details>

**Soal 9.2 [Sedang].** Gabungkan (merge) dua array terurut `[1, 4, 7]` dan `[2, 3, 8]`.

<details><summary>Pembahasan 9.2</summary>
Bandingkan kepala tiap array, ambil yang terkecil: <b>[1, 2, 3, 4, 7, 8]</b>. Kompleksitas O(n+m).
</details>

**Soal 9.3 [Sedang].** Kapan Counting Sort efisien, dan berapa kompleksitasnya?

<details><summary>Pembahasan 9.3</summary>
Efisien saat rentang nilai (k) kecil relatif terhadap n. Kompleksitas <b>O(n + k)</b>, bukan berbasis perbandingan, dan stabil.
</details>

**Soal 9.4 [Sulit].** Radix Sort LSD menyortir `[170, 45, 75, 90, 802, 24, 2, 66]`. Berapa kali pass yang dibutuhkan dan mengapa?

<details><summary>Pembahasan 9.4</summary>
Angka terbesar (802) punya 3 digit &rarr; <b>3 pass</b> (satuan, puluhan, ratusan). Tiap pass memakai counting sort stabil. Kompleksitas O(d(n+b)).
</details>

**Soal 9.5 [Sedang].** Apa arti algoritma sorting yang **stabil**, dan sebutkan dua contoh yang stabil dan dua yang tidak.

<details><summary>Pembahasan 9.5</summary>
Stabil = mempertahankan urutan relatif elemen bernilai sama. Stabil: Merge Sort, Insertion Sort, Bubble Sort, Counting Sort. Tidak stabil: Quick Sort, Selection Sort, Heap Sort.
</details>

---

## 10. Searching (Lanjutan)

**Soal 10.1 [Sedang].** Berapa maksimum perbandingan binary search pada array 1000 elemen?

<details><summary>Pembahasan 10.1</summary>
<code>ceil(log2(1000)) = 10</code> &rarr; maksimum <b>10 perbandingan</b>.
</details>

**Soal 10.2 [Sulit].** Modifikasi binary search untuk menemukan **kemunculan pertama** sebuah nilai pada array terurut yang punya duplikat. Jelaskan idenya.

<details><summary>Pembahasan 10.2</summary>
Saat menemukan nilai target, jangan langsung berhenti: simpan indeks, lalu lanjutkan mencari ke <b>setengah kiri</b> (<code>high = mid - 1</code>) untuk menemukan indeks lebih kecil. Tetap <b>O(log n)</b>.
</details>

**Soal 10.3 [Sedang].** Apa keunggulan Interpolation Search dibanding Binary Search, dan kapan ia bekerja terbaik?

<details><summary>Pembahasan 10.3</summary>
Interpolation Search memperkirakan posisi berdasarkan nilai (bukan selalu tengah). Pada data terurut yang <b>terdistribusi merata</b>, rata-rata <b>O(log log n)</b>, namun worst case O(n).
</details>

---

## 11. Graph (BFS & DFS)

**Soal 11.1 [Sedang].** Bandingkan kebutuhan memori adjacency matrix vs adjacency list untuk graf dengan V simpul dan E sisi.

<details><summary>Pembahasan 11.1</summary>
Adjacency matrix: <b>O(V^2)</b> (boros untuk graf jarang). Adjacency list: <b>O(V + E)</b> (efisien untuk graf jarang).
</details>

**Soal 11.2 [Sedang].** Graf tak berarah dengan sisi: A-B, A-C, B-D, C-D, D-E. Tuliskan urutan BFS mulai dari A (tetangga diproses urut abjad).

<details><summary>Pembahasan 11.2</summary>
BFS: <b>A, B, C, D, E</b> (level demi level memakai queue).
</details>

**Soal 11.3 [Sedang].** Untuk graf pada soal 11.2, tuliskan urutan DFS mulai dari A (tetangga urut abjad).

<details><summary>Pembahasan 11.3</summary>
DFS: <b>A, B, D, C, E</b> (menelusuri sedalam mungkin memakai stack/rekursi). Catatan: urutan bisa berbeda tergantung urutan kunjungan tetangga.
</details>

**Soal 11.4 [Sulit].** Algoritma apa yang tepat mencari jarak terpendek pada graf **tak berbobot**, dan berapa kompleksitasnya dengan adjacency list?

<details><summary>Pembahasan 11.4</summary>
<b>BFS</b> menemukan jarak terpendek (jumlah sisi) pada graf tak berbobot. Kompleksitas <b>O(V + E)</b>. (Untuk graf berbobot non-negatif gunakan Dijkstra.)
</details>

---

## 12. Soal Campuran (HOTS)

**Soal 12.1 [Sedang].** Struktur data apa paling tepat untuk fitur **Undo** pada aplikasi editor? Mengapa?

<details><summary>Pembahasan 12.1</summary>
<b>Stack</b> (LIFO) — aksi terakhir adalah yang pertama dibatalkan.
</details>

**Soal 12.2 [Sedang].** Struktur data apa untuk antrian cetak (print spooler)? Mengapa?

<details><summary>Pembahasan 12.2</summary>
<b>Queue</b> (FIFO) — dokumen yang pertama masuk dicetak lebih dulu.
</details>

**Soal 12.3 [Sulit].** Kamu butuh menyimpan jutaan kata dan melakukan autocomplete prefiks dengan cepat. Struktur data apa yang cocok?

<details><summary>Pembahasan 12.3</summary>
<b>Trie (prefix tree)</b> — pencarian/penambahan berdasarkan prefiks dalam O(panjang kata), efisien untuk autocomplete.
</details>

**Soal 12.4 [Sedang].** Butuh lookup data berdasarkan key (mis. ID -> data mahasiswa) secepat mungkin. Struktur apa?

<details><summary>Pembahasan 12.4</summary>
<b>Hash Table</b> — rata-rata O(1) untuk insert/search/delete berdasarkan key.
</details>

**Soal 12.5 [Sulit].** Sebuah program memanggil sort O(n log n) lalu untuk tiap elemen melakukan binary search O(log n). Berapa total kompleksitasnya?

<details><summary>Pembahasan 12.5</summary>
Sort O(n log n) + (n x O(log n)) = O(n log n) + O(n log n) = <b>O(n log n)</b>.
</details>

---

_Edisi Lengkap — materi belajar mandiri untuk persiapan UAS Algoritma & Struktur Data._
