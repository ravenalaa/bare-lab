## Tugas 2: Implementasi MVT pada Django

Claudia Paskalia Koesno (2306275355) / PBP - F

Deployment aplikasi dapat dilihat [di sini](http://claudia-paskalia-barelab.pbp.cs.ui.ac.id/)

---

### Implementasi Pembuatan Proyek Django

**1. Pembuatan proyek Django baru**

Membuat direktori proyek, kemudian mengaktifkan *virtual environment* yang digunakan untuk melakukan instalasi atas beberapa *depndencies* yang dibutuhkan. Menginisialisasi pembuatan proyek Django dengan menjalankan perintah `django-admin startproject <nama_projek>`.

**2. Pembuatan aplikasi main pada proyek**

Memastikan virtual environment telah diaktifkan, kemudian menjalankan perintah `python manage.py startapp main` pada direktori utama, serta mendaftarkan aplikasi main pada direktori proyek melalui berkas `settings.py`.

**3. Routing pada proyek untuk menjalankan aplikasi main**

Pada berkas `urls.py` yang terletak dalam direktori **proyek**, dari `django.urls` impor fungsi `include` yang berfungsi untuk mengimpor rute URL dari aplikasi main ke dalam berkas `urls.py` proyek.

**4. Membuat model pada aplikasi main dengan nama *Product***

Pada direktori aplikasi **main**, definisikan model **Product** seperti membuat class dengan attribute atau field yang sesuai. Pada tugas ini, atribut yang diwajibkan adalah `name` dengan tipe data `CharField`, `price` dengan tipe data `IntegerField`, serta `description` dengan tipe data `TextField`. Setelah itu dilakukan migrasi model agar Django dapat melacak perubahan data pada proyek. Untuk ini, perlu dijalankan perintah `python manage.py makemigrations` kemudian `python manage.py migrate`. Kedua perintah tersebut perlu dijalankan kembali apabila kita melakukan perubahan terhadap model yang dibuat.

**5. Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML**

Membuat suatu fungsi dengan parameter **request** untuk mengatur permintaan HTTP dan menampilkan tampilan yang sesuai. Dalam fungsi tersebut, mengembalikan fungsi dengan perintah `return render(request, "<file_name>.html", <dict>)`. Argumen dalam fungsi tersebut berupa:
- **request:** Objek permintaan HTTP yang dikirim oleh pengguna.
- **<file_name.html>:** Nama berkas template yang akan digunakan untuk me-render tampilan.
- **dict: Dictionary yang berisi data untuk diteruskan ke tampilan dan digunakan dalam penampilan dinamis.**

**6. Membuat sebuah routing pada `urls.py` aplikasi main untuk memetakan fungsi yang telah dibuat pada `views.py`**

Membuat berkas `urls.py` dalam direktori aplikasi main untuk mengatur rute URL pada aplikasi main. Hal ini dilakukan agar URL dapat dipetakan dengan fungsi yang berada pada `views.py` sehingga pengguna dapat mengakses konten dari halaman yang sesuai.

**7. Melakukan deployment ke PWS**

Membuat proyek baru pada PWS, kemudian menambahkan URL deployment PWS pada bagian `ALLOWED_HOSTS` di berkas `settings.py` pada direktori proyek. Ketika status deployment sudah `Successful` maka proyek sudah dapat diakses pada URL deployment. Selanjutnya, perubahan yang dilakukan pada proyek dapat kembali di-*push* dengan menjalan perintah `git push pws <NAMA_BRANCH>:master` pada PWS.

**8. Membuat sebuah README.md**

Membuat berkas `README.md` yang berisi mengenai informasi serta tautan menuju aplikasi PWS yang sudah di-deploy, langkah pembuatan sebuah proyek Django, serta jawaban atas pertanyaan mengenai framework Django, serta fungsi dan kegunaan Git.

### Alur Request dan Response pada Django

![alt text](<Django Chart (1).jpg>)

1. **Client Request**: Client mengirimkan HTTP request ke server dengan URL tertentu.
2. **URL Routing**: Django mengecek `urls.py` untuk mencocokan URL yang diminta dengan pola URL yang telah ditentukan.
3. **View Execution**: Apabila URL yang diminta ditemukan, Django akan memanggil fungsi view yang sesuai pada berkas `views.py`.
4. **Data Access**: Apabila diperlukan, View akan berinteraksi dengan `models.py` untuk mengambil, mengubah, atau menyimpan data dari atau ke database.
5. **Template Rendering**: Data yang diambil dari model kemudian akan dikirmkan ke file template HTML untuk dirender menjadi suatu halaman web/webpage.
6. **Response**: Django akan mengirimkan HTTP response yang berisi halaman web (atau dapat berupa data lain seperti JSON) kembali ke client.

### Kegunaan Git dalam Pengembangan Perangkat Lunak

Git merupakan sebuah *version control system* untuk pengembangan *software*. Git memudahkan pengembang dalam mengelola versi *source code* program, melacak perubahan kode, mengetahui siapa yang membuat perubahan, serta memutuskan penambahan atau modifikasi baris kode yang akan digunakan. Beberapa keunggulan penggunaan Git dalam pengembangan adalah kecepatannya karena Git dirancang untuk bekerja cepat, meski pada suatu proyek yang sangat besar sekalipun. Selain itu, fitur branch dan merge memudahkan pengembang untuk membuat suatu cabang *source code* baru tanpa mempengaruhi kode utama. Git juga memungkinkan para pengembang untuk bekerja secara kolaboratif, dapat digunakan pada berbagai platform seperti Windows, macOS, dan Linux, yang dilengkapi berbagai fitur keamanan yang kuat.

### Mengapa Django Dijadikan Permulaan Pembelajaran Pengembangan Perangkat Lunak

Django dianggap mudah untuk digunakan sebagai sarana pembelajaran pengembangan perangkat lunak karena arsitekturnya yang modular dan terstruktur, secara khusus arsitektur MVT (Model-View-Template) yang diterapkan oleh Django. Konsep ini memudahkan pengelolaan dan pengaplikasian logika aplikasi dalam pengembangan karena adanya pemisahan komponen-komponen utama dari sebuah aplikasi. Selain itu, Django memiliki dokumentasi yang lengkap dan komunitas developer yang banyak berkontribusi pada ekosistem Django, membuat developer pemula memiliki akses yang luas untuk belajar dan menyelesaikan masalah. Django juga dirancang untuk membantu developer mengembangkan aplikasi dari konsep hingga selesai dengan cepat. Pendekatan tingkat tinggi ini membuat Django dapat menangani banyak kerumitan teknis, sehingga pengembang bisa lebih fokus pada pembuatan aplikasi mereka.

### Mengapa Model pada Django Disebut Sebagai ORM?

Model pada Django memetakan atribut objek Python ke tabel database. Django ORM menyediakan abstraksi tingkat tinggi sehingga pengembang dapat berinteraksi dengan database menggunakan kode Python tanpa perlu menulis query SQL secara langsung. Hal ini membuat pengembang melakukan pengelolaan data di database seperti bekerja dengan objek Python biasa, sehingga memudahkan pengembangan aplikasi.