###Anggota Kelompok MinafCorp : <br><br>
Masabil Arraya Muhammad  - 2206082101 <br>
I Made Surya Anahata Putra - 2206081370 <br>
Novita Mulia Sari - 2206032785 <br>
Ayu Siti Nasya Ningrum - 2206025426 <br>
Farrel Sheva Alkautsar - 2206030344 <br>

---

# Aplikasi BooketList

### i. Cerita aplikasi yang diajukan serta manfaatnya

Dalam dunia yang semakin digital, membaca buku telah menjadi kegiatan yang semakin mudah diakses dan dinikmati oleh banyak orang. “Booketlist” lahir dari kebutuhan untuk menghubungkan penulis dan pembaca dalam satu platform yang interaktif dan informatif.

BooketList adalah aplikasi database buku yang berfungsi sebagai jembatan antara penulis (writer) dan pembaca (reader). Aplikasi ini menyediakan ruang bagi penulis untuk mempromosikan karya mereka, sementara pembaca dapat menemukan, mereview, dan membuat daftar buku yang ingin mereka baca.

### ii. Manfaat Aplikasi

Untuk Penulis:

- Promosi Efektif: Platform untuk mempromosikan karya dengan audiens yang tepat.
- Feedback Langsung: Menerima ulasan dan kritik konstruktif dari pembaca.

Untuk Pembaca:

- Temukan Buku: Akses ke database buku yang luas dan beragam.
- Ulasan dan Rating: Membaca ulasan dari komunitas sebelum memutuskan buku apa yang akan dibaca.
- Daftar Bacaan: Merencanakan dan melacak buku yang ingin atau telah dibaca.



Untuk Komunitas:

- Diskusi Literasi: Forum untuk diskusi dan apresiasi literatur.
- Event dan Workshop: Informasi tentang event literasi atau workshop penulisan.


### iii. Daftar modul yang akan diimplementasikan

**1. Modul Registrasi dan Autentikasi:** <br>
Deskripsi: 
- Pengguna dapat mendaftar sebagai user atau writer melalui formulir registrasi.
- Autentikasi dengan menggunakan email dan kata sandi.
- Lupa kata sandi dan pengaturan profil untuk setiap role. <br>

Fitur CRUD:
- Create: Mendaftarkan akun baru.
- Read: Melihat profil pengguna.
- Update: Mengubah data profil pengguna.
- Delete: Menghapus akun pengguna.
 
**2. Modul Manajemen Buku (untuk Writer):** <br>
Deskripsi: <br>
- Writer dapat menambahkan, mengedit, atau menghapus buku yang telah dipublikasikan.
- Melampirkan sampul buku, deskripsi, dan metadata lainnya. <br>

Fitur CRUD: 
- Create: Menambahkan buku baru.
- Read: Menampilkan daftar buku yang telah dipublikasikan oleh writer tersebut.
- Update: Mengedit detail dan konten buku.
- Delete: Menghapus buku.
 
**3. Modul Ulasan dan Rating:** <br>
Deskripsi: <br>
- User dapat meninggalkan ulasan dan rating untuk buku.
- Writer dapat merespons ulasan pada buku mereka.<br>

Fitur CRUD: 
- Create: Menambahkan ulasan dan rating baru.
- Read: Menampilkan ulasan dan rating.
- Update: Mengedit ulasan dan rating (dalam jangka waktu tertentu).
- Delete: Menghapus ulasan dan rating pengguna sendiri.
 
**4. Modul Wishlist:** <br>
Deskripsi: 
- User dapat menambahkan buku ke daftar keinginan atau wishlist. <br>

Fitur CRUD: 
- Create: Menambah buku ke wishlist.
- Read: Menampilkan daftar buku di wishlist.
- Update: Mengedit catatan atau prioritas buku di wishlist.
- Delete: Menghapus buku dari wishlist.
  
**5. Modul Update:** <br>
Deskripsi: 
- Modul ini menyediakan informasi terbaru tentang buku atau penulis, serta update platform lainnya.<br>

Fitur CRUD: 
- Create: Menambahkan berita atau pengumuman baru.
- Read: Menampilkan daftar berita atau pengumuman.
- Update: Mengubah atau memperbarui berita atau pengumuman.
- Delete: Menghapus berita atau pengumuman yang sudah tidak relevan.
  
**6. Modul Keanggotaan Premium: (Optional)** <br>
Deskripsi: <br>
- Pengguna dapat berlangganan keanggotaan premium untuk mendapatkan fitur atau konten eksklusif. <br>

Fitur CRUD: 
- Create: Mengaktifkan keanggotaan premium.
- Read: Menampilkan status dan detil keanggotaan.
- Update: Mengubah paket atau detil keanggotaan.
- Delete: Membatalkan keanggotaan premium.
 



### iv. Sumber dataset katalog buku

https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset

### v. Role atau peran pengguna beserta deskripsinya (karena bisa saja lebih dari satu jenis pengguna yang mengakses aplikasi)
- Pembaca
> Pembaca adalah member Reguler by default yang mempunyai beberapa Modul, seperti Modul langganan, modul ulasan dan rating, serta modul wishlist.
- Penulis
> Penulis adalah entitas yang mempunyai akses ke modul Manajemen Buku.
- Admin
> Admin adalah entitas yang mempunyai akses ke modul Update. (Unfix)
