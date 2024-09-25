# Bare Lab

**Tugas Individu - Pemrograman Berbasis Platform - Kelas PBP F**

Claudia Paskalia Koesno (2306275355)

## **Laman**
Deployment aplikasi dapat dilihat [di sini](http://claudia-paskalia-barelab.pbp.cs.ui.ac.id/)

---
<details>
<summary> <b> Tugas 2: Implementasi Model-View-Template (MVT) pada Django </b> </summary>

## Implementasi Pembuatan Proyek Django

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

## Alur Request dan Response pada Django

![Django Chart](https://github.com/user-attachments/assets/2afe24bb-2d4b-4a45-93c2-e3650a730780)


1. **Client Request**: Client mengirimkan HTTP request ke server dengan URL tertentu.
2. **URL Routing**: Django mengecek `urls.py` untuk mencocokan URL yang diminta dengan pola URL yang telah ditentukan.
3. **View Execution**: Apabila URL yang diminta ditemukan, Django akan memanggil fungsi view yang sesuai pada berkas `views.py`.
4. **Data Access**: Apabila diperlukan, View akan berinteraksi dengan `models.py` untuk mengambil, mengubah, atau menyimpan data dari atau ke database.
5. **Template Rendering**: Data yang diambil dari model kemudian akan dikirmkan ke file template HTML untuk dirender menjadi suatu halaman web/webpage.
6. **Response**: Django akan mengirimkan HTTP response yang berisi halaman web (atau dapat berupa data lain seperti JSON) kembali ke client.

## Kegunaan Git dalam Pengembangan Perangkat Lunak

Git merupakan sebuah *version control system* untuk pengembangan *software*. Git memudahkan pengembang dalam mengelola versi *source code* program, melacak perubahan kode, mengetahui siapa yang membuat perubahan, serta memutuskan penambahan atau modifikasi baris kode yang akan digunakan. Beberapa keunggulan penggunaan Git dalam pengembangan adalah kecepatannya karena Git dirancang untuk bekerja cepat, meski pada suatu proyek yang sangat besar sekalipun. Selain itu, fitur branch dan merge memudahkan pengembang untuk membuat suatu cabang *source code* baru tanpa mempengaruhi kode utama. Git juga memungkinkan para pengembang untuk bekerja secara kolaboratif, dapat digunakan pada berbagai platform seperti Windows, macOS, dan Linux, yang dilengkapi berbagai fitur keamanan yang kuat.

## Mengapa Django Dijadikan Permulaan Pembelajaran Pengembangan Perangkat Lunak

Django dianggap mudah untuk digunakan sebagai sarana pembelajaran pengembangan perangkat lunak karena arsitekturnya yang modular dan terstruktur, secara khusus arsitektur MVT (Model-View-Template) yang diterapkan oleh Django. Konsep ini memudahkan pengelolaan dan pengaplikasian logika aplikasi dalam pengembangan karena adanya pemisahan komponen-komponen utama dari sebuah aplikasi. Selain itu, Django memiliki dokumentasi yang lengkap dan komunitas developer yang banyak berkontribusi pada ekosistem Django, membuat developer pemula memiliki akses yang luas untuk belajar dan menyelesaikan masalah. Django juga dirancang untuk membantu developer mengembangkan aplikasi dari konsep hingga selesai dengan cepat. Pendekatan tingkat tinggi ini membuat Django dapat menangani banyak kerumitan teknis, sehingga pengembang bisa lebih fokus pada pembuatan aplikasi mereka.

## Mengapa Model pada Django Disebut Sebagai ORM?

Model pada Django memetakan atribut objek Python ke tabel database. Django ORM menyediakan abstraksi tingkat tinggi sehingga pengembang dapat berinteraksi dengan database menggunakan kode Python tanpa perlu menulis query SQL secara langsung. Hal ini membuat pengembang melakukan pengelolaan data di database seperti bekerja dengan objek Python biasa, sehingga memudahkan pengembangan aplikasi.
</details>


<details>
<summary> <b> Tugas 3: Implementasi Form dan Data Delivery pada Django </b> </summary>

## Data Delivery dalam Pengimplementasian Sebuah Platform

Data delivery menjadi suatu aspek penting dalam pengimplementasian sebuah platform karena *data delivey* membangun konektivitas antar sistem untuk berkomunikasi dan bertukar informasi. Misalnya dalam sebuah platform yang melibatkan banyak layanan (aplikasi) seperti pembayaran, pengiriman, dan otentikasi, memerlukan proses data delivery yang cepat dan efisien. Selain itu, proses *data delivery* sering dioptimalkan untuk meningkatkan performa agar data dapat sampai ke pengguna dengan lebih cepat dan efisien. Pengiriman data secara real-time anatara server dan klien atau antar perangkat dapat mendukung terjadinya pembaruan dan pemrosesan data secara langsung, mmeningkatkan pengalaman pengguna melalui penyajian konten yang relevan dan terarah secara real-time.

## Mana yang Lebih Baik antara XML dan JSON? Mengapa JSON Lebih Populer Dibandingkan XML?

**JSON (JavaScript Object Notation)** adalah format pertukaran data yang banyak digunakan dalam proses pengembangan web. Format ini berbasis teks dan menggunakan cara penulisan yang mudah untuk menggambarkan struktur data, seperti array dan objek.

**XML (Extensible Markup Language)** adalah bahasa markup yang menggunakan tag untuk menentukan elemen, dan atribut untuk menentukan sifat-sifatnya. XML memungkinkan struktur yang lebih kompleks dibandingkan JSON dan dapat mendukung lebih banyak jenis data, termasuk teks, angka, dan data biner.

Meskipun pemilihan antara penggunaan JSON dan XML tergantung pada kebutuhan pengembangan, akan tetapi JSON lebih populer dibandingkan dengan XML oleh karena beberapa alasan berikut:
- **Ringan**: JSON adalah format sederhana yang menggunakan sedikit data untuk menggambarkan struktur data yang kompleks. Hal ini membuatnya ideal untuk mentransmisikan data di web, karena mengurangi jumlah data yang perlu dikirim, sehingga dapat meningkatkan kinerja.

- **Mudah diparse**: JSON mudah diparse dan dapat dengan cepat diubah menjadi struktur data yang dapat digunakan di berbagai bahasa pemrograman.

- **Human-readable**: JSON menggunakan sintaks sederhana dan mudah dipahami. Hal ini membuat aplikasi yang menggunakan JSON lebih mudah untuk dikelola dan memudahkan proses debugging.

JSON sering digunakan dalam aplikasi web untuk menyimpan dan mengambil data di sisi klien. Misalnya single-page application bisa menggunakan AJAX untuk mengambil data dari server dan menyajikannya dalam format JSON di sisi pengguna. Hal ini meningkatkan kinerja dan pengalaman pengguna karena data dapat dimuat secara dinamis tanpa harus memuat ulang seluruh halaman. JSON juga lebih disukai untuk *data delivery* antara browser dan server karena menghasilkan file yang lebih ringan dan lebih cepat.

## Fungsi dari Method `is_valid()`

Method `is_valid()` pada form Django digunakan untuk memeriksa apakah data yang dimasukkan memenuhi semua aturan validasi yang ditetapkan. Jika data valid, method ini mengembalikan `True`. Sedangkan jika tidak, maka akan mengembalikan `False` dan mengisi atribut `errors` dengan pesan kesalahan untuk setiap field yang tidak memenuhi kriteria.

Method ini penting karena memastikan hanya data yang valid yang diterima dan diproses. Hal ini guna menghindari kesalahan atau masalah akibat data yang tidak sesuai. Selain itu, `is_valid()` memungkinkan pemberian feedback pada pengguna dengan pesan kesalahan tertentu, sehingga mereka dapat memperbaiki input mereka dan menjaga integritas data dalam aplikasi. Atau dengan kata lain, dilakukan validasi data terlebih dahulu sebelum diproses atau disimpan, sehingga dapat mengurangi risiko kesalahan dan potensi celah keamanan.

## Pentingnya `csrf_token` pada Django

`csrf_token` dalam pembuatan form pada Django digunakan untuk melindungi aplikasi dari serangan Cross-Site Request Forgery (CSRF). Token ini memastikan bahwa permintaan yang dikirimkan berasal dari sumber yang sah, yaitu dari form yang dihasilkan oleh aplikasi web itu sendiri. Melalui verifikasi token pada sisi server, Django mencegah penyerang untuk embuat form palsu yang terlihat sah dari perspektif server.

Tanpa `csrf_token`, aplikasi akan rentan terhadap serangan CSRF, di mana penyerang bisa memanipulasi form dan membuat pengguna tanpa sadar mengirim permintaan berbahaya ke situs web yang sedang mereka kunjungi. Jika pengguna yang sudah terautentikasi mengunjungi situs penyerang, hal ini dapat menyebabkan tindakan yang merugikan, seperti mengakses data sensitif, penghapusan akun, atau melakukan transaksi keuangan, semua tanpa sepengetahuan atau persetujuan pengguna.

## Implementasi Checklist
### Membuat Input Form
1.  Membuat berkas `forms.py` dalam direktori aplikasi `main` untuk membuat form yang dapat menerima data Produk baru.

```python
from django.forms import ModelForm
from main.models import Product

class ProductEntryForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description", "stock", "category", "rating"]
```

2. Pada berkas `views.py`, melakukan pengambilan seluruh objek `Product` pada database.

```python
def show_main(request):
    product_entries = Product.objects.all() #Penambahan pada baris ini

    context = {
        'name': 'Pak Bepe',
        'class': 'PBP D',
        'npm': '2306123456',
        'product_entries' : product_entries, #Penambahan pada baris ini
    }

    return render(request, "main.html", context)
```

3. Pada berkas `views.py`, melakukan import `redirect` pada library `django.shortcuts` untuk melakukan *redirect* serta menambahkan fungsi baru untuk melakukan penambahan data pada database.

```python
def create_product_entry(request):
    form = ProductEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product_entry.html", context)
```

4. Membuat *template* html baru untuk melakukan penambahan objek Product pada direktori `main\templates` dengan filename `create_product_entry.html`.

```python
{% extends 'base.html' %} 
{% block content %}
<h1>Add New Product Entry</h1>

<form method="POST">
  {% csrf_token %}
  <table>
    {{ form.as_table }}
    <tr>
      <td></td>
      <td>
        <input type="submit" value="Add Product Entry" />
      </td>
    </tr>
  </table>
</form>

{% endblock %}
```

5. Menampilkan data Produk dalam bentuk tabel dan melakukan penambahan tombol Add New Product pada `main.html`.

```python
{% if not product_entries %}
<p>Belum ada data produk pada toko.</p>
{% else %}
<table>
  <tr>
    <th>Product Name</th>
    <th>Price</th>
    <th>Description</th>
    <th>Stock</th>
    <th>Category</th>
    <th>Rating</th>
  </tr>

  {% for item in product_entries %}
  <tr>
    <td>{{item.name}}</td>
    <td>{{item.price}}</td>
    <td>{{item.description}}</td>
    <td>{{item.stock}}</td>
    <td>{{item.category}}</td>
    <td>{{item.rating}}</td>
  </tr>
  {% endfor %}
</table>
{% endif %}

<br />

<a href="{% url 'main:create_product_entry' %}">
  <button>Add New Product Entry</button>
</a>
```

6. Melakukan routing URL untuk fungsi `create_product_entry` dengan melakukan import funsi tersebut dan menambahkan path URL pada `urls.py`

```python
urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product-entry', create_product_entry, name='create_product_entry'),
]
```

### Membuat 4 Fungsi pada `views` 

Pada berkas `views.py` pada direktori aplikasi `main` menambahkan import `HttpResponse` dan `Serializer` 

```python
from django.http import HttpResponse
from django.core import serializers
```

**Format XML**

Menambahkan fungsi `show_xml` yang me-return `HttpResponse` berisi data yang sudah di-serialize menjadi XML.

```python
def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
```

**Format JSON**

Menambahkan fungsi `show_JSON` yang me-return `HttpResponse` berisi data yang sudah di-serialize menjadi json.

```python
def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```

Untuk format XML dan JSON by ID, dalam pengambilan hasil query tambahkan filter dengan ID tertentu objek Product.

**Format XML by ID**

```python
def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
```

**Format JSON by ID**

```python
def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```

### Membuat Routing URL

Melakukan import dari `views.py` dan menambahkan keempat path url fungsi-fungsi diatas ke dalam `urlpatterns` pada berkas `urls.py` pada direktori `main`. 

```python
from django.urls import path
from main.views import show_main, create_product_entry, show_xml, show_json, show_xml_by_id, show_json_by_id

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product-entry', create_product_entry, name='create_product_entry'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
]
```
Input form sudah telah selesai dibuat dan siap untuk digunakan. Jalankan command `python manage.py runserver` dan sudah dapat diakses melalui http://localhost:8000.

## Hasil *Screenshot* pada Postman

1. XML
   ![image](https://github.com/user-attachments/assets/1adec133-15df-4acf-a035-f3bca20a3f33)

3. JSON
   ![image](https://github.com/user-attachments/assets/5b372943-b8aa-4dc7-ba0e-cfd1d0ae3382)

4. XML by ID
   ![image](https://github.com/user-attachments/assets/a8fb22c1-fb5d-401f-8c00-ac69c605c280)

6. JSON by ID
   ![image](https://github.com/user-attachments/assets/a5784796-8736-41e7-a344-cb91acb66cc0)
</details>

# Tugas 4: Implementasi Autentikasi, Session, dan Cookies pada Django

## Perbedaan `HttpResponseRedirect` dengan `redirect()`
### `HttpResponseRedirect`
`HttpResponseRedirect` digunakan dalam membuat respons untuk mengarahkan pengguna ke URL tujuan yang terdapat pada argumen. `HttpResponseRedirect` hanya dapat diisi dengan satu argumen, yakni URL tempat pengguna akan diarahkan.

### `redirect()`
Django menyediakan sebuah *shortcut function* `redirect()` yang mengenkapsulasi `HttpResponseRedirect` dan `HttpResponsePermanentRedirect` dengan argumen `permanent=False`. Fungsi *shortcut* `redirect()` akan mengembalikan `HttpResponseRedirect` ke URL yang sesuai dengan argumen yang di-*pass*. Apabila pada `HttpResponseRedirect` argumen hanya bisa berupa URL, pada `redirect` dapat menerima argumen berupa:
- `model`: fungsi `get_absolute_url()` model tersebut akan dipanggil.
- `view`: nama fungsi pada `view` dan biasanya akan menggunakan fungsi `reserve()` untuk mengambil nama pola URL dan mengembalikan path URL yang terkait dengan nama tersebut. 
- `url`: URL absolut atau relatif, yang akan langsung digunakan sebagai lokasi *redirect*.

## Penghubungan model `Product` dengan `User`
Pada file `models.py` melakukan import atas model `User`. Kemudian, pada model `Product` menambahkan variabel user untuk menghubungkan model `User` sebagai berikut

```python
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
```

`models.ForeignKey(User, ...)` membuat hubungan *foreign key*. Hal ini menandakan bahwa model tersebut memiliki hubungan dengan model `User`. *Foreign key* menunjukkan setiap *instance* dari model `Product` terhubung terhadap suatu *instance* tertentu model `User`.

`on_delete=models.CASCADE:` mendefinisikan perilaku saat instance `User` yang direferensikan dihapus. Opsi `CASCADE` berarti jika `User` yang terhubung dengan model ini dihapus, semua instance dari model `Product` yang berhubungan dengan User tersebut juga akan dihapus.

Pada file `views.py` yang terletak di subdirektori `main`, mengubah potongan kode pada fungsi `create_product_entry` menjadi

```python
def create_product_entry(request):
    form = ProductEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        item = form.save(commit=False)
        item.user = request.user
        item.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product_entry.html", context)
```
Parameter `commit=False` berfungsi untuk mencegah Django menyimpan objek yang dibuat dari form secara langsung ke database, sehingga objek tersebut dapat dimodifikasi terlebih dahulu sebelum disimpan ke *database*. Field `user` akan diisi dengan objek `User` dari return value `request.user` yang sedang terotorisasi.

```python
def show_main(request):
    mood_entries = Product.objects.filter(user=request.user)

    context = {
         'name': request.user.username,
         ...
    }
```

Objek `Product` ditampilkan sesuai dengan pengguna yang sedang login. Hal ini dilakukan dengan menyaring objek dan mengambil `Product` yang dimana field `user` terisi dengan objek `User` yang sama dengan pengguna yang sedang login. `request.user.username` berfungsi untuk menampilkan username pengguna yang login pada halaman main.

## Perbedaan antara Autentikasi dan Otorisasi
| Autentikasi | Otorisasi |
| -- | -- |
| Autentikasi adalah proses verifikasi identitas pengguna untuk memastikan bahwa mereka adalah orang yang sesuai saat mengakses sistem atau aplikasi. Dalam Django, autentikasi memastikan bahwa hanya pengguna yang sah dan terdaftar yang dapat mengakses situs web dengan melakukan validasi kredensial seperti nama pengguna dan kata sandi. | Otorisasi menentukan tindakan apa saja yang dapat dilakukan oleh pengguna yang telah terautentikasi, seperti mengedit data atau mengakses halaman tertentu. Dalam Django, otorisasi dilakukan dengan menggunakan dekorator seperti @login_required untuk mengatur apa yang dapat dilakukan dalam situs web setelah berhasil login. |

**Mengapa keduanya penting?** **Autentikasi** penting untuk memastikan bahwa hanya pengguna yang sah yang dapat mengakses sistem, sementara **otorisasi** penting untuk mengatur tindakan apa saja yang dapat dilakukan pengguna setelah mereka berhasil diautentikasi.

## *Cookies* dalam Django
Cookies adalah file teks kecil yang menyimpan data seperti nama pengguna dan kata sandi untuk mengidentifikasi komputer Anda dan meningkatkan pengalaman browsing dengan menyimpan ID unik dari server. Dalam konteks aplikasi web, cookies digunakan untuk berbagai tujuan, termasuk manajemen sesi pengguna, penyimpanan preferensi pengguna,pelacakan aktivitas pengguna, dan tujuan lainnya. Django menggunakan cookies untuk menyimpan ID sesi pengguna, yang dikirim bersamaan dengan setiap *request* untuk mengidentifikasi dan mengelola sesi di server. Ketika sesi berakhir atau pengguna logout, Django menghapus cookie tersebut untuk mengakhiri sesi.

### Keamanan Penggunaan *Cookies*
Sebagian besar orang menganggap *Cookies* alat yang berguna dalam pengembangan web untuk menyimpan dan melacak data antar halaman di sebuah situs web. *Cookies* digunakan untuk menyimpan informasi kecil di browser pengguna, yang membuat suatu website untuk dapat mengingat preferensi pengguna, melacak aktivitas pengguna, dan menjaga *session state*. Meskipun cookies dapat meningkatkan fungsionalitas situs web, kekhawatiran terkait privasi dan keamanan membuat pengembang harus menggunakan cookies dengan hati-hati. 

Secara umum, *cookies* sangat aman jika diimplementasikan dengan benar. Namun, ada beberapa cara bagi penyerang untuk mencuri *cookie* dan menyalahgunakannya. Jika data *cookie* jatuh ke tangan yang salah, penyerang dapat mengakses sesi browsing, mencuri informasi pribadi, atau menyalahgunakan data *cookie*.

Meskipun cookie tidak bisa digunakan untuk mengunduh *malware*, *cookie poisoning* (manipulasi data cookie untuk menyamar sebagai cookie yang sah) dapat membuat penyerang memalsukan identitas pengguna atau menggunakan ID sesi yang valid untuk melakukan tindakan berbahaya di situs web. Selain itu, *zombie cookies*, yaitu cookie yang bisa terus muncul kembali meskipun sudah dihapus, sulit untuk dihilangkan. Untuk menghapusnya, sistem *cleaner* mungkin dibutuhkan untuk menghilangkan *malware* dan file yang tidak diinginkan.

## Implementasi Autentikasi, Session, dan Cookies
### Membuat Fungsi Registrasi
Pada tugas ini, kita akan membuat halaman utama hanya dapat diakses oleh pengguna yang telah memiliki akun (proses **autentikasi**). Untuk mendaftarkan pengguna baru, kita perlu membuat formulir registrasi pengguna.

Pada berkas `views.py` dalam direktori aplikasi `main`, perlu melakukan import `UserCreationForm` dan `messages` pada bagian paling atas. Kemudian, menambahkan fungsi `register` untuk menghasilkan formulir registrasi secara otomatis dan menghasilkan akun pengguna ketika data di-submit dari form.
```python
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)
```

Pada direktori `main\templates` membuat berkas html baru yaitu `register.html` untuk tampilan halama dalam mendaftarkan `User` baru.

Terakhir, mengimport fungsi `register` dari `views` dan menambahkan `urlspatter` pada berkas `urls.py` dalam direktori `main`.
```python
from main.views import register

urlpatterns = [
    ...
    path('register/', register, name='register'),
    ...
]
```

### Membuat Fungsi Login dan Merestriksi Akses Halaman Main
Pada berkas `views.py` dalam subdirektori `main`, menambahkan beberapa import yaitu `authenticate`, `login`, dan `AuthenticationForm`, serta menambahkan fungsi `login_user`.
```python
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main:show_main')

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)
```

Membuat tampilan halaman *login* dengan membuat berkas `login.html` pada direktori `main\templates`.

Terakhir, menambahkan *url path* pada file `urls.py` dengan melakukan import terhadap fungsi `login_user`.
```python
from main.views import login_user

urlpatterns = [
    ...
    path('login/', login_user, name='login'),
    ...
]
```

Untuk **membatasi akses halaman**, perlu ditambahakan modul decorator pada `views.py` di atas fungsi `show_main`.
``` python
from django.contrib.auth.decorators import login_required

...
@login_required(login_url='/login') --> Decorator
def show_main(request):
...
```

### Membuat Fungsi Logout
Terakhir, pada berkas `views.py` menambahkan fungsi `logout_user` dan menambahkan import `logout` pada bagian atas.
```python
from django.contrib.auth import logout

def logout_user(request):
    logout(request)
    return redirect('main:login')
```

Menambahkan tombol logout pada berkas `main.html` pada direktori `main/templates` agar pengguna dapat keluar.

Menambahkan import fungsi `logout_user` pada `views.py` dan menambahkan *url path* ke dalan `urlpatterns`.
```python
from main.views import logout_user

urlpatterns = [
   ...
   path('logout/', logout_user, name='logout'),
]
```

### Menghubungkan `Product` dengan `User`
Agar hanya pengguna yang terotorisasi dapat melihat produk-produknya sendiri, setiap `User` perlu dihubungkan `Product`.

Pada `models.py` menambahkan importr `User` dan menambahkan fiel `user` pada model `Product`
```python
from django.contrib.auth.models import User

class Product (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ...
```

Mengubah fungsi `create_product_entry` pada `views.py` dengan potongan kode di bawah ini
```python
def create_product_entry(request):
    form = ProductEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        item = form.save(commit=False)
        item.user = request.user
        item.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product_entry.html", context)
```

Agar nama pengguna yang sedang login dapat ditampilkan, melakukan beberapa perubahan berikut pada fungsi `show_main`
```python
def show_main(request):
    product_entries = Product.objects.filter(user=request.user)

    context = {
        'name' : request.user.username,
```

Semua perubahan diatas disimpan serta melakukan `python manage.py makemigrations` dan `python manage.py migrate`.

Terakhir, untuk melakukan persiapan dalam melakukan *environment production*, melakukan penambahan sebuah import baru pada berkas `settings.py` pada subdirektori `bare_lab` dan mengganti variabel `DEBUG`.
```python
import os

PRODUCTION = os.getenv("PRODUCTION", False)
DEBUG = not PRODUCTION
```

### Menerapkan *Cookies*
Kita bisa menggunakan cookies untuk melihat data *last login* dari pengguna.

Menambahkan import `HttpResponseRedirect`, `reverse`, dan `datetime` pada berkas `views.py`. Mengubah  fungsi `login_user` pada blok `if form.is_valid()` dengan menambahkan *cookie* `last_login` untuk melihat kapan terakhir kali pengguna melakukan login.
```python
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse

...
if form.is_valid():
    user = form.get_user()
    login(request, user)
    response = HttpResponseRedirect(reverse("main:show_main"))
    response.set_cookie('last_login', str(datetime.datetime.now()))
    return response
...
```

Pada fungsi `show_main` menambahkan key baru yaitu informasi mengenai *last login* dalam `context`.
```python
  context = {
    'name' : request.user.username,
    'class': 'PBP F',
    'product_entries' : product_entries,
    'last_login': request.COOKIES['last_login'], # Penambahan potongan kode ini
}
```

Mengubah fungsi `logout_user` menjadi seperti berikut
```python
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
```
Potongan kode `response.delete_cookie('last_login')` digunakan untuk menghapus *cookie* apabila pengguna melakukan logout.

Untuk menampilkan data *last login*, menambahkan potongan kode berikut pada berkas `main.html`
```python
...
<h5>Sesi terakhir login: {{ last_login }}</h5>
...
```