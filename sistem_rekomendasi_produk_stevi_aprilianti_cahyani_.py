# -*- coding: utf-8 -*-
"""Sistem Rekomendasi Produk - Stevi Aprilianti Cahyani .ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1BphEQ8W5S2OwtKMwg-zimCBSL7EYlZM1

# **SISTEM REKOMENDASI PRODUK - BIG BASKET PRODUCT**

oleh : Stevi Aprilianti Cahyani

BigBasket adalah platform pengiriman bahan makanan daring terbesar di India yang berbasis teknologi dan memungkinkan pengguna untuk membeli berbagai kebutuhan rumah tangga, mulai dari sayuran segar, buah-buahan, daging, makanan siap saji, hingga produk kebersihan rumah, secara online. Platform ini pertama kali diluncurkan pada tahun 2011 oleh perusahaan Innovative Retail Concepts Private Limited, dan kini menjadi bagian dari grup Tata Digital, salah satu konglomerat terbesar di India.

BigBasket melayani jutaan pelanggan di lebih dari 25 kota besar di India, dan telah mengembangkan jaringan yang menghubungkan pelanggan langsung dengan penjual lokal maupun gudang pusat. Melalui pendekatan ini, BigBasket menghadirkan pengalaman belanja bahan makanan yang cepat, efisien, dan dapat diandalkan, terutama bagi masyarakat urban dengan mobilitas tinggi.

## **1. Data Understanding**

### **Import Library**
"""

!pip install tensorflow

# Library standar
import os
import re
import zipfile

# Untuk manipulasi data dan visualisasi
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Untuk preprocessing dan ekstraksi fitur
from sklearn.preprocessing import LabelEncoder, StandardScaler, Normalizer
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.decomposition import TruncatedSVD

# Untuk pembagian data dan pipeline
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.pipeline import make_pipeline

# Untuk evaluasi dan kemiripan
from sklearn.metrics import mean_squared_error, precision_score
from sklearn.metrics.pairwise import cosine_similarity, linear_kernel

# Untuk sistem rekomendasi atau pencarian tetangga terdekat
from sklearn.neighbors import NearestNeighbors

# Untuk upload file di Google Colab
from google.colab import files

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

"""### **Data Loading**"""

# Upload kaggle.json
files.upload()

# Membuat direktori
!mkdir -p ~/.kaggle
# Menyalin file API `kaggle.json`
!cp kaggle.json ~/.kaggle/
# Mengatur permission file `kaggle.json`
!chmod 600 ~/.kaggle/kaggle.json

# Mengunduh dataset "Big Basket Product" dari Kaggle menggunakan Kaggle API
!kaggle datasets download -d amrit0611/big-basket-product-analysis

# Membuka file ZIP dari dataset yang telah diunduh
zip_ref = zipfile.ZipFile('/content/big-basket-product-analysis.zip', 'r')
# Mengekstrak seluruh isi file ZIP ke direktori /content/
zip_ref.extractall('/content/')
# Menutup file ZIP setelah proses ekstraksi selesai
zip_ref.close()

# Membaca file CSV
df_products = pd.read_csv('/content/BigBasket Products.csv')
# Menampilkan isi DataFrame df_FordCar
df_products

"""### **Exploratory Data Analysis**

**1. Melihat ringkasan struktur data frame**
"""

df_products.info()

"""Dataset ini memiliki 10 kolom dengan total 27.555 baris data. Sebagian besar kolom berisi data bertipe *object* (kategori atau teks), beberapa berupa *float64* (angka desimal), dan hanya kolom *index* yang menggunakan tipe *int64* (angka bulat). Berikut adalah penjelasan singkat untuk masing-masing kolom:

* *index*: Nomor urut atau ID unik untuk setiap baris data.
* *product*: Nama produk yang tersedia di platform.
* *category*: Kategori utama produk, seperti bahan makanan, minuman, dan lain-lain.
* *sub\_category*: Klasifikasi yang lebih spesifik dari kategori produk.
* *brand*: Merek produk yang ditawarkan.
* *sale\_price*: Harga jual produk di platform BigBasket.
* *market\_price*: Harga pasar produk di pasaran umum.
* *type*: Jenis produk yang memberikan informasi lebih detail dibandingkan kategori atau sub-kategori.
* *rating*: Penilaian atau rating dari pengguna terhadap produk.
* *description*: Deskripsi singkat atau uraian mengenai produk tersebut.

**2. Memeriksa Statistik Deskriptif**
"""

df_products.describe()

"""Berikut penjelasan singkat dari tabel statistik deskriptif tersebut:

Tabel ini menyajikan ringkasan statistik untuk kolom numerik utama dalam dataset, yaitu `index`, `sale_price`, `market_price`, dan `rating`.

* **index**: Nomor urut data, mulai dari 1 hingga 27.555.
* **sale\_price** (harga jual): Harga jual produk rata-rata sekitar 322,5 Rupee, dengan nilai terendah 2,45 Rupee dan tertinggi 12.500 Rupee. Median harga jual (50%) adalah 190 Rupee, menunjukkan sebagian besar produk dijual di bawah harga tersebut.
* **market\_price** (harga pasar): Harga pasar rata-rata sekitar 382 Rupee, sedikit lebih tinggi dari harga jual. Harga maksimum sama-sama 12.500 Rupee, menunjukkan ada produk dengan harga sangat tinggi.
* **rating**: Rata-rata rating pengguna adalah 3,94 dari maksimal 5. Namun, rating hanya tersedia untuk 18.929 produk dari total 27.555, sehingga tidak semua produk memiliki penilaian.

Variasi harga jual dan harga pasar cukup besar, terlihat dari nilai standar deviasi yang tinggi, menandakan perbedaan harga yang signifikan antar produk. Sedangkan rating cenderung berada di kisaran menengah ke atas dengan variasi yang lebih kecil.

**3. Memeriksa Missing Value**
"""

missing_values = df_products.isnull().sum()
print(f"Terdapat {missing_values.sum()} nilai kosong di beberapa kolom berikut:")
print(missing_values[missing_values > 0])

"""**4. Memeriksa unique column**"""

for column in df_products.columns:
    print(f'terdapat {df_products[column].nunique()}nilai unik di kolom{column}')

"""**5. Visualisasi**

* Distribusi Jumlah Data per Kategori Produk
"""

# Tabel
count_per_category = df_products['category'].value_counts().reset_index()
count_per_category.columns = ['Kategori Produk', 'Jumlah']
print(count_per_category)

# Visualisasi horizontal
plt.figure(figsize=(10,6))
sns.barplot(x='Jumlah', y='Kategori Produk', data=count_per_category)
plt.title('Distribusi Jumlah Data per Kategori Produk', fontweight='bold', fontsize=14)
plt.xlabel('Jumlah')
plt.ylabel('Kategori Produk')
plt.show()

"""Visualisasi ini menunjukkan distribusi jumlah produk berdasarkan kategori dalam dataset. Total terdapat 11 kategori produk dengan variasi jumlah data yang cukup signifikan.

   Kategori **Beauty & Hygiene** mendominasi dengan jumlah produk terbanyak, yakni sebanyak 7.867 item, menunjukkan fokus pasar yang cukup besar pada produk perawatan dan kebersihan. Diikuti oleh kategori **Gourmet & World Food** yang memiliki 4.690 produk, dan **Kitchen, Garden & Pets** dengan 3.580 produk.
        
  Kategori lain seperti **Snacks & Branded Foods** (2.814), **Foodgrains, Oil & Masala** (2.676), dan **Cleaning & Household** (2.675) juga memiliki jumlah produk yang cukup besar, menandakan keberagaman jenis produk yang tersedia.
        
   Sementara itu, kategori dengan jumlah produk paling sedikit adalah **Eggs, Meat & Fish** dengan 350 produk, **Fruits & Vegetables** 557 dan **Baby Care** 610 produk.

* Top 10 Produk Best Seller
"""

# Tabel top 10 produk
top_10_products = (
    df_products[['product', 'category']]
    .value_counts()
    .reset_index(name='jumlah')
    .head(10)
)
top_10_products.columns = ['produk', 'kategori', 'jumlah']
print(top_10_products)

# Visualisasi
plt.figure(figsize=(10, 6))
sns.barplot(x='jumlah', y='produk', data=top_10_products, color='steelblue')
plt.xlabel('Jumlah', fontsize=14)
plt.ylabel('Produk', fontsize=14)
plt.title('Top 10 Produk Best Seller', fontweight='bold', fontsize=18)
plt.yticks(fontsize=12)
plt.xticks(fontsize=12)
plt.tight_layout()
plt.show()

"""Berdasarkan visualisasi data di atas, produk yang paling sering muncul dalam dataset didominasi oleh bahan-bahan yang
     berkaitan dengan kebutuhan memasak, seperti bumbu dapur Turmeric Powder/Arisina Pudi. Selain itu, produk lemak dan
     minyak seperti Extra Virgin Olive Oil dan Cow Ghee/Tuppa juga termasuk yang paling banyak dicatat, mengindikasikan
     popularitas tinggi dalam konsumsi rumah tangga.

* **10 Produk Paling Sedikit Terjual**
"""

from IPython.display import display
# tabel
tidak_laku = pd.DataFrame(df_products[['product', 'category']].value_counts().tail(10)).reset_index()
tidak_laku.columns = ['produk', 'kategori', 'jumlah']
print("Tabel: 10 Produk Paling Sedikit Terjual")
display(tidak_laku)

"""Berdasarkan tabel di atas, terlihat bahwa produk yang  tingkat penjualan terendah didominasi oleh dua kategori utama, yaitu Cleaning & Household dan Beauty & Hygiene. Produk-produk seperti Geometry Box dari berbagai seri dan parfum pria dari seri Gentleman masing-masing hanya tercatat satu kali, mengindikasikan bahwa produk ini memiliki minat yang rendah. Hal ini dapat menjadi bahan evaluasi bagi pengelola produk untuk mengevaluasi efektivitas promosi atau kebutuhan pasar terhadap produk-produk tersebut.

* Daftar Jumlah Top Kategori dengan Rating Tertinggi (5.0)
"""

top_rating = df_products['rating'].max()
best_items = df_products.loc[df_products['rating'] == top_rating]
best_items

# filter data dengan rating 5.0
top_items = df_products[df_products['rating'] == 5.0]

# tabel
tabel_top_items = top_items['category'].value_counts().reset_index()
tabel_top_items.columns = ['Kategori Produk', 'Jumlah Produk']
print(tabel_top_items)

# Visualisasi
plt.figure(figsize=(10,6))
sns.countplot(
    x='category',
    data=top_items,
    color='steelblue',
    order=top_items['category'].value_counts().index
)
plt.xticks(rotation=75)
plt.title('Top Kategori Produk dengan Rating 5.0', fontweight='bold')
plt.xlabel('Kategori Produk')
plt.ylabel('Jumlah Produk')
plt.tight_layout()
plt.show()

"""Visualisasi ini menunjukkan **kategori produk dengan jumlah item terbanyak yang mendapatkan rating tertinggi (5.0)** dari pengguna. Kategori dengan performa terbaik dalam hal kepuasan pengguna adalah:
        
  * **Beauty & Hygiene** dengan **562 produk** ber-rating sempurna, menempati posisi teratas. Ini menandakan bahwa produk-produk kecantikan dan kebersihan memiliki tingkat kepuasan tinggi di kalangan konsumen.
  * **Gourmet & World Food** dan **Kitchen, Garden & Pets** masing-masing memiliki **273** dan **211 produk** dengan rating 5.0, menunjukkan kualitas produk yang baik di kategori makanan khusus dan perlengkapan rumah tangga.
  * **Cleaning & Household** juga memiliki kontribusi besar dengan **135 produk** ber-rating sempurna, yang mungkin mencerminkan keefektifan dan keandalan produk kebersihan.
  * Kategori lain seperti **Snacks & Branded Foods**, **Baby Care**, **Beverages**, dan **Bakery, Cakes & Dairy** juga tercatat memiliki sejumlah produk dengan rating sempurna, meskipun jumlahnya lebih sedikit.

* Daftar Jumlah Kategori dengan Rating Terendah
"""

low_rating = df_products['rating'].min()
low_items = df_products.loc[df_products['rating'] == low_rating]
low_items

# filter data dengan rating 1.0
low_items = df_products[df_products['rating'] == 1.0]

# tabel
tabel_low_items = low_items['category'].value_counts().reset_index()
tabel_low_items.columns = ['Kategori Produk', 'Jumlah Produk']
print(tabel_low_items)

# Visualisasi
plt.figure(figsize=(10,6))
sns.countplot(
    x='category',
    data=low_items,
    color='steelblue',
    order=low_items['category'].value_counts().index
)
plt.xticks(rotation=75)
plt.title('Kategori Produk dengan Rating 1.0', fontweight='bold')
plt.xlabel('Kategori Produk')
plt.ylabel('Jumlah Produk')
plt.tight_layout()
plt.show()

"""Visualisasi tersebut menunjukkan distribusi kategori produk dengan rating terendah (1.0), di mana kategori Beauty & Hygiene memiliki jumlah produk terbanyak yang diberi rating rendah, diikuti oleh Kitchen, Garden & Pets dan Gourmet & World Food. Hal ini mengindikasikan bahwa produk-produk dalam kategori tersebut cenderung mendapat ulasan buruk dari pengguna, sehingga dapat menjadi perhatian khusus untuk evaluasi kualitas atau kepuasan pelanggan.

## **2. Data Preparation**

### **Menghapus kolom yang tidak relevan**

 Melakukan drop pada kolom ``index``, karena kolom tersebut tidak relevan untuk digunakan dalam langkah analisis yang lebih lanjut
"""

df_products.drop('index', axis=1, inplace=True)
print("Berhasil menghapus kolom index!")
df_products.head()

"""### **Menghapus duplikasi data**"""

print(f"Total Duplicates : {df_products.duplicated().sum()}")
df_products.drop_duplicates(inplace=True)
print(f"Berhasil menghapus duplikasi data!")

"""### **Menangani Missing Value**

* Memeriksa mean & median rating terlebih dahulu
"""

# Mean rating
rating_mean = df_products['rating'].mean()
print(f"Mean rating adalah: {rating_mean:.2f}")

# Median rating
rating_median = df_products['rating'].median()
print(f"Median rating adalah: {rating_median:.2f}")

"""* Menangani missing value pada kolom rating dengan nilai mean rating"""

df_products['rating'] = df_products['rating'].fillna(value=rating_mean)
missing_after = df_products['rating'].isnull().sum()
print(f"Berhasil mengisi missing value dengan mean rating {rating_mean:.2f}")
print(f"Sisa missing value setelah pengisian: {missing_after}")

"""* Menghapus missing value pada kolom `product`, `brand` dan `description`"""

df_products.dropna(inplace=True)

"""* **Memeriksa hasil setelah dilakukan drop missing value**"""

df_products.reset_index(drop=True, inplace=True)
df_products.info()

"""### **Changing Certain Value**

Langkah selanjutnya adalah **mengubah dan membersihkan beberapa nilai dalam dataset**, terutama yang berkaitan dengan data berbasis teks. Pertama, dilakukan **pembuatan salinan** dari `df_products` ke `df_products_copy` sebagai bentuk kehati-hatian agar data asli tetap aman jika terjadi kesalahan saat modifikasi. Kemudian, dibuat fungsi `hapus_spasi` untuk menghilangkan spasi berlebih di awal atau akhir string, yang sangat penting untuk menjaga konsistensi data. Selanjutnya, dibuat fungsi `tps` (tokenisasi dan pembersihan string) yang memecah nilai berbentuk teks panjang dengan pemisah seperti `&`, `,`, `*`, atau baris baru, lalu menghilangkan spasinya. Fungsi ini diterapkan pada kolom `category`, `sub_category`, dan `type`, karena kolom-kolom ini sering berisi beberapa label dalam satu sel. Setelah itu, dilakukan **standarisasi dan pembersihan lebih lanjut** melalui fungsi `cleaner` untuk mengubah huruf menjadi kecil dan menghapus semua spasi di dalam string, baik untuk tipe list maupun string tunggal. Fungsi ini diterapkan pada kolom `category`, `sub_category`, `type`, dan `brand` untuk memastikan semua data teks bersih dan konsisten, sehingga mempermudah proses analisis selanjutnya.

* Membuat salinan df_products ke df_products_copy supaya data asli tetap aman kalau nanti ada modifikasi
"""

df_products_copy = df_products.copy()
print("Berhasil membuat salinan!")

"""* Membuat Fungsi untuk Membersihkan Spasi (Whitespace Stripping)"""

hapus_spasi = lambda a: a.strip()
print("Fungsi hapus_spasi berhasil dibuat!")

"""* Tokenisasi dan Pembersihan String"""

tps = lambda a: list(map(hapus_spasi, re.split('& |, |\*|\n', a)))
print("Fungsi tps berhasil dibuat!")

"""* Penerapan Fungsi Tokenisasi pada Beberapa Kolom"""

for col in ['category', 'sub_category', 'type']:
    df_products_copy[col] = df_products_copy[col].apply(tps)
print("Berhasil menerapkan fungsi tps pada kolom category, sub_category, dan type!")

"""* pembersihan dan standarisasi data teks"""

def cleaner(x):
    if isinstance(x, list):
        return [str.lower(i.replace(" ", "")) for i in x]
    else:
        if isinstance(x, str):
            return str.lower(x.replace(" ", ""))
        else:
            return ''

for col in ['category', 'sub_category', 'type', 'brand']:
    df_products_copy[col] = df_products_copy[col].apply(cleaner)

print("Berhasil membersihkan data pada kolom category, sub_category, type, dan brand!")

"""### **Content Based Filtering**

Langkah berikutnya sebagai persiapan untuk model dengan **Content-Based Filtering** yaitu dimulai dengan membuat salinan dari `df_products_copy` menjadi `df_cbf`, agar data tetap terjaga saat dilakukan manipulasi lebih lanjut. Setelah itu, dibuat fungsi `combine_features` yang bertujuan untuk menggabungkan informasi dari beberapa kolom penting — seperti `category`, `sub_category`, `brand`, dan `type` — menjadi satu string panjang per baris data. Penggabungan ini dilakukan karena Content-Based Filtering membutuhkan representasi teks dari atribut produk yang dapat dibandingkan satu sama lain. Selanjutnya, dilakukan **ekstraksi fitur menggunakan TF-IDF Vectorizer**, yaitu metode yang mengubah teks menjadi bentuk numerik berdasarkan frekuensi dan kekhasan kata. TF-IDF secara otomatis mengabaikan kata-kata umum (stop words) agar hanya mempertahankan kata yang dianggap penting dalam membedakan satu produk dengan lainnya. Kolom hasil gabungan `gab` dari setiap produk dikonversi menjadi matriks TF-IDF, di mana baris merepresentasikan produk dan kolom merepresentasikan kata unik. Ukuran dari matriks ini adalah `(27201, 3083)`, yang berarti terdapat 27.201 produk dan 3.083 kata unik, siap untuk digunakan dalam perhitungan kemiripan produk berbasis konten.

* Melakukan inisialisasi
"""

df_cbf = df_products_copy.copy()

"""* Menggabungkan isi beberapa kolom jadi satu string per baris"""

# Fungsi untuk menggabungkan beberapa kolom menjadi satu string
def combine_features(row):
    # Gabungkan list kategori menjadi string dengan spasi sebagai pemisah
    categories = ' '.join(row['category'])
    # Gabungkan list sub_kategori menjadi string dengan spasi sebagai pemisah
    sub_categories = ' '.join(row['sub_category'])
    # Ambil nama brand (string)
    brand = row['brand']
    # Gabungkan list tipe menjadi string dengan spasi sebagai pemisah
    types = ' '.join(row['type'])

    # Gabungkan semua string menjadi satu kalimat panjang dengan spasi sebagai pemisah
    combined = f"{categories} {sub_categories} {brand} {types}"
    return combined

# Terapkan fungsi
df_cbf['gab'] = df_cbf.apply(combine_features, axis=1)

"""* Ekstraksi Fitur TF-IDF

Membuat objek TF-IDF Vectorizer yang secara otomatis mengabaikan kata-kata umum dalam bahasa Inggris (stop words) supaya fokus ke kata yang lebih bermakna.
"""

tfidf = TfidfVectorizer(stop_words='english')

"""Mengubah semua teks di kolom 'gab' jadi matriks TF-IDF, di mana setiap baris adalah dokumen (baris data), dan setiap kolom mewakili kata unik yang ditemukan. Nilai di matriks menunjukkan seberapa penting sebuah kata pada dokumen tersebut."""

tfidf_matrix = tfidf.fit_transform(df_cbf['gab'])

"""Menampilkan ukuran matriks TF-IDF."""

tfidf_matrix.shape

"""### **Collaborative Filtering**

* Membuat kolom baru bernama `user_id` di DataFrame
"""

df_products_copy['user_id'] = (df_products_copy.index % 500) + 1

"""Membagi data seolah-olah ada 500 pengguna yang mengulang secara siklik. Hal ini diterapkan karena dataframe tidak mempunyai kolom `user_id`, tapi ingin mensimulasikan data user untuk analisis rekomendasi produk."""

#hasil
df_products_copy

"""* Encoding Label

  Agar algoritma berbasis matriks dapat bekerja, data kategorikal harus dikonversi menjadi bentuk numerik. Ini penting karena Collaborative Filtering, terutama yang menggunakan pendekatan matrix factorization, hanya dapat memproses data numerik. Oleh karena itu, atribut seperti ``user_id`` dan ``product`` perlu diencoding menjadi angka. Proses encoding ini juga berguna untuk membentuk matriks user-item yang dibutuhkan dalam operasi aljabar linear, seperti dekomposisi matriks. Dengan begitu, sistem dapat melakukan perhitungan secara efisien dan tetap mampu menangani dataset berukuran besar.

**Tahap 1 : Encoding `user_id`**

a. Mengambil semua nilai unik dari kolom user_id dan menyimpannya dalam bentuk list
"""

user_list = df_products_copy['user_id'].unique().tolist()
print('Daftar user_id :', user_list)

"""

b. Melakukan encoding user_id"""

user_encoding ={x: i for i, x in enumerate(user_list)}
print('Hasil encoding : ', user_encoding)

"""c. Mapping indexing ke `User_id`

"""

user_encoding_to_user = {i: x for i, x in enumerate(user_list)}
print("Berhasil melakukan encoding angka ke user_id!")
print("Contoh mapping index ke user_id:")

#tampilan
for i in list(user_encoding_to_user.items())[:5]:
    print(f"Index {i[0]} → user_id {i[1]}")

"""Code ini berfungsi untuk melacak hasil encoding ketika nanti kita menggunakan model atau sistem rekomendasi yang memakai angka untuk merepresentasikan user_id, dictionary ini berguna untuk mengubah kembali angka ke bentuk user_id asli saat menampilkan hasil rekomendasi.

---

**Tahap 2 : Encoding `product`**

a. Mengambil semua nilai unik dari kolom 'product' dan menyimpannya dalam bentuk list
"""

produk_list = df_products_copy['product'].unique().tolist()
print('Daftar produk list :', produk_list)

"""b. Melakukan encoding `product`"""

produk_encoding ={x: i for i, x in enumerate(produk_list)}
print('Hasil encoding : ', produk_encoding)

"""c. Mapping indexing kembali ke product"""

produk_encoding_to_produk = {i: x for i, x in enumerate(produk_list)}
print("Berhasil melakukan encoding angka ke product!")
print("Contoh mapping index ke product :")

#tampilan
for i in list(produk_encoding_to_produk.items())[:5]:
    print(f"Index {i[0]} → produk : {i[1]}")

"""**Tahap 3** : mengubah nilai kategori (userID dan product) menjadi bentuk numerik (encoded)"""

# Mapping user_id asli ke angka
df_products_copy['user'] = df_products_copy['user_id'].map(user_encoding)

# Mapping product ke angka
df_products_copy['produk'] = df_products_copy['product'].map(produk_encoding)

"""**Tahap 4** : Cek hasil"""

users_count = len(user_encoding_to_user) # jumlah user
produk_count = len(produk_encoding_to_produk) # jumlah produk
low_rating = min(df_products_copy['rating']) # rating terendah
top_rating = max(df_products_copy['rating']) # rating tertinggi

print('Total user: {}'.format(users_count))
print('Total produk: {}'.format(produk_count))
print('Rating terendah: {}'.format(low_rating))
print('Rating tertinggi: {}'.format(top_rating))

"""### **Train & Test Split**

**Tahap 1 : Mengacak Dataset**

Data perlu diacak sebelum di-split karena kita ingin memastikan bahwa data latih (training set) dan data uji (testing set) mewakili distribusi data secara umum, bukan urutan tertentu yang bisa mempengaruhi hasil model.
"""

df_products_copy = df_products_copy.sample(frac=1, random_state=69)
df_products_copy

"""**Tahap 2 : Membuat variabel fitur (independen) `x`, yang berisi pasangan antara user dan produk.**

Pada tahapan ini, dilakukan proses pemisahan data menjadi variabel input dan output. Variabel `x` dibuat dengan mengambil kolom `user` dan `produk` dari dataframe `df_products_copy`, yang kemudian dikonversi menjadi array. Tujuan dari proses ini adalah untuk menggabungkan data pengguna dan produk dalam satu bentuk yang dapat digunakan sebagai fitur input oleh model machine learning.
"""

x = df_products_copy[['user', 'produk']].values

"""**Tahap 3 : Melakukan normalisasi rating menggunakan teknik Min-Max Scaling agar berada dalam rentang 0 sampai 1**

Pada baris kode `y = df_products_copy['rating'].apply(lambda x: (x - low_rating) / (top_rating - low_rating)).values`, dilakukan proses normalisasi terhadap data rating. Normalisasi ini bertujuan untuk mengubah skala nilai rating menjadi rentang antara `0` hingga `1`. Hal ini dilakukan agar setiap nilai rating memiliki bobot yang seimbang saat digunakan oleh model pembelajaran mesin.
"""

y = df_products_copy['rating'].apply(lambda x: (x - low_rating) / (top_rating - low_rating)).values

"""**Tahap 4 : Membagi data menjadi data latih (training data) dan data validasi (validation data)**"""

split_data = int(0.8 * df_products.shape[0])
x_train, x_val, y_train, y_val = (
    x[:split_data],
    x[split_data:],
    y[:split_data],
    y[split_data:]
)

# Menampilkan jumlah data latih dan data validasi
print(f"Jumlah data latih: {len(x_train)}")
print(f"Jumlah data validasi: {len(x_val)}")

x_train

y_train

x_val

y_val

"""## **3. Modeling & Result**

### **Content Based Filtering**

**Tahap 1 : Pembuatan Matriks TF-IDF**

Tahap ini menghasilkan representasi numerik dari atribut produk dalam bentuk matriks TF-IDF.
"""

tfidf_matrix

"""**Tahap 2 : Perhitungan Cosine Similarity**

Menghitung tingkat kemiripan antar produk berdasarkan matriks TF-IDF yang sudah dibuat.
"""

cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
cosine_sim

"""**Tahap 3 : Pembuatan Indeks Produk**

Membuat struktur data untuk memetakan nama produk ke indeksnya agar pencarian lebih efisien.
"""

produk_name = df_cbf['product']
indeks_produk = pd.Series(df_cbf.index, index=df_cbf['product'])
indeks_produk

"""**Tahap 4 : Fungsi Rekomendasi Produk**

Mendefinisikan fungsi yang menerima nama produk dan mengembalikan daftar produk rekomendasi berdasarkan nilai kemiripan tertinggi.
"""

def rekomendasi_produk(produk_name, cosine_sim=cosine_sim):
    # Mengambil indeks produk berdasarkan nama produk
    indx = indeks_produk[produk_name]

    # Mengambil skor kemiripan dari produk yang diminta terhadap seluruh produk
    skor_kemiripan = list(enumerate(cosine_sim[indx]))

    # Mengurutkan produk berdasarkan skor kemiripan tertinggi
    skor_kemiripan = sorted(skor_kemiripan, key=lambda x: x[1], reverse=True)

    # Mengambil 10 produk teratas (tidak termasuk produk itu sendiri)
    skor_kemiripan = skor_kemiripan[1:11]

    # Mendapatkan indeks dari produk-produk yang direkomendasikan
    indeks_rekomendasi = [i[0] for i in skor_kemiripan]

    # Mengembalikan nama-nama produk hasil rekomendasi
    return df_cbf['product'].iloc[indeks_rekomendasi]

"""**Tahap 5 : Pemilihan Produk Uji Coba Secara Acak**

Memilih secara acak sebuah produk sebagai input untuk menguji fungsi rekomendasi.
"""

# Nama produk yang diminta user (dipilih secara acak dari daftar produk)
nama_produk_diminta = np.random.choice(produk_name.unique())
nama_produk_diminta

"""Pada tahap ini, sistem secara acak memilih satu nama produk dari daftar produk_name, yaitu kumpulan nama produk yang tersedia dalam data. Produk ini berperan sebagai input permintaan pengguna yang akan digunakan untuk mencari rekomendasi produk-produk lain yang mirip.

**Tahap 6 : Menampilkan Hasil Rekomendasi Produk**
"""

# Memanggil fungsi rekomendasi
hasil_rekom = rekomendasi_produk(nama_produk_diminta)

pd.DataFrame({
    'Produk Diminta': [nama_produk_diminta] * len(hasil_rekom),
    'Rekomendasi Produk yang Relevan': hasil_rekom
})

"""### **Collaborative Filtering**

Tahap 1 : Membangun Arsitektur Model Rekomendasi (RecommenderNet)
"""

class RecommenderNet(tf.keras.Model):

    def __init__(self, users_count, produk_count, embedding_size, **kwargs):
        super(RecommenderNet, self).__init__(**kwargs)
        self.users_count = users_count
        self.produk_count = produk_count
        self.embedding_size = embedding_size

        # Layer embedding untuk user (jumlah user, ukuran embedding)
        self.user_embedding = layers.Embedding(
            input_dim=users_count,
            output_dim=embedding_size,
            embeddings_initializer='he_normal',
            embeddings_regularizer=keras.regularizers.l2(1e-6)
        )
        self.user_bias = layers.Embedding(users_count, 1)

        # Layer embedding untuk produk (jumlah produk, ukuran embedding)
        self.produk_embedding = layers.Embedding(
            input_dim=produk_count,
            output_dim=embedding_size,
            embeddings_initializer='he_normal',
            embeddings_regularizer=keras.regularizers.l2(1e-6)
        )
        self.produk_bias = layers.Embedding(produk_count, 1)

    def call(self, inputs):
        # inputs shape = (batch_size, 2) => kolom 0: user_id, kolom 1: produk_id

        user_vector = self.user_embedding(inputs[:, 0])
        user_bias = self.user_bias(inputs[:, 0])

        produk_vector = self.produk_embedding(inputs[:, 1])
        produk_bias = self.produk_bias(inputs[:, 1])

        # Hitung dot product antara embedding user dan produk
        dot_user_produk = tf.reduce_sum(user_vector * produk_vector, axis=1, keepdims=True)

        # Jumlahkan dot product dengan bias user dan bias produk
        x = dot_user_produk + user_bias + produk_bias

        # Aktivasi sigmoid untuk output skor prediksi antara 0-1
        return tf.nn.sigmoid(x)

"""Tahap 2 : Inisialisasi dan Kompilasi Model"""

# inisialisasi model
model = RecommenderNet(users_count, produk_count, 50)

# model compile
model.compile(
    loss = tf.keras.losses.BinaryCrossentropy(),
    optimizer = keras.optimizers.Adam(learning_rate=0.001),
    metrics=[tf.keras.metrics.RootMeanSquaredError()]
)

"""Tahap 3 : Menyiapkan Callback Early Stopping"""

# callbacks
from tensorflow.keras.callbacks import EarlyStopping
early_stop = EarlyStopping(monitor='val_root_mean_squared_error',
                              patience=10,
                              verbose=1,
                              restore_best_weights=True)

"""Tahap 4 : Melatih Model dengan Data Pelatihan"""

# Memulai training
history = model.fit(
    x = x_train,
    y = y_train,
    batch_size = 8,
    epochs = 50,
    callbacks = [early_stop],
    validation_data = (x_val, y_val)
)

"""Tahap 5 : Memilih satu user secara acak, lalu mengambil semua produk yang belum pernah diberi rating oleh user tersebut"""

# Mengambil sample user
Id_User = df_products_copy.user_id.sample(1).iloc[0]
produk_rating_by_user = df_products_copy[df_products_copy.user_id == Id_User]

# Ambil semua produk yang belum pernah dirating oleh user
produk_not_rating = [
    [produk_encoding[x]] for x in df_products_copy['product'].unique()
    if x not in produk_rating_by_user['product'].values and x in produk_encoding
]

user_encoder = user_encoding.get(Id_User)

user_produk_array = np.hstack(
    ([[user_encoder]] * len(produk_not_rating), produk_not_rating)
)

"""Tahap 6 : Memprediksi dan Menampilkan Hasil Rekomendasi"""

# Prediksi skor untuk kombinasi user dan produk yang belum dirating
prediksi_rating = model.predict(user_produk_array).flatten()

# Ambil indeks 10 prediksi tertinggi (rekomendasi terbaik)
indeks_rating_tertinggi = prediksi_rating.argsort()[-10:][::-1]

# Mapping kembali indeks produk yang direkomendasikan ke nama produk asli
produk_rekomendasi_id = [
    produk_encoding_to_produk.get(produk_not_rating[i][0]) for i in indeks_rating_tertinggi
]
# Hapus duplikat sambil mempertahankan urutan
produk_rekomendasi_id = list(dict.fromkeys(produk_rekomendasi_id))

# Tampilkan ID user yang sedang dianalisis
print('Daftar rekomendasi produk untuk user {}'.format(Id_User))
print('---' * 10)

# Tampilkan produk-produk yang paling disukai user berdasarkan rating tertinggi
print('Produk dengan rating tertinggi dari user')
print('----' * 10)

produk_top_user = (
    produk_rating_by_user.sort_values(by='rating', ascending=False)
    .head(5)['product'].values
)

# Salin data utama untuk dipakai menampilkan detail brand, dsb.
df_produk_detail = df_products_copy.copy()
produk_dinilai_user = df_produk_detail[df_produk_detail['product'].isin(produk_top_user)]

# Tampilkan produk-produk yang pernah dirating user
for row in produk_dinilai_user.itertuples():
    print(row.product, ':', row.brand)

print('----' * 8)
print('Top 10 produk rekomendasi')
print('----' * 8)

# Ambil detail produk-produk hasil rekomendasi
produk_rekomendasi_final = df_produk_detail[df_produk_detail['product'].isin(produk_rekomendasi_id)].drop_duplicates(subset='product')

# Tampilkan daftar produk hasil rekomendasi
for row in produk_rekomendasi_final.itertuples():
    print(row.product, ':', row.brand)

"""## Evaluation

### Content Based Filtering
"""

def evaluate_precision(nama_produk, hasil_rekomendasi, df_cbf):
    """
    Evaluasi precision untuk rekomendasi produk berdasarkan kemiripan konten.

    Parameters:
    - nama_produk (str): Produk referensi dari user
    - hasil_rekomendasi (list): Daftar produk hasil rekomendasi
    - df_cbf (DataFrame): Dataset dengan fitur gabungan konten produk

    Returns:
    - float: Skor precision
    """
    # Tandai produk yang relevan di dalam dataset
    df_cbf['relevant'] = df_cbf['product'].isin(hasil_rekomendasi).astype(int)

    # Ambil data produk yang termasuk hasil rekomendasi
    df_relevan = df_cbf[df_cbf['product'].isin(hasil_rekomendasi)]

    y_true = df_relevan['relevant'].values
    y_pred = [1] * len(y_true)

    precision = precision_score(y_true, y_pred, zero_division=0)
    return precision

# Evaluasi
precision_cb = evaluate_precision(nama_produk_diminta, hasil_rekom, df_cbf)
print(f"Precision Content-Based Filtering untuk produk '{nama_produk_diminta}': {precision_cb:.2f}")

"""### Collaborative Filtering"""

# Evaluasi visual terhadap performa model
plt.plot(history.history['root_mean_squared_error'], label='Train RMSE')
plt.plot(history.history['val_root_mean_squared_error'], label='Val RMSE')
plt.title('Evaluasi Model Collaborative Filtering')
plt.xlabel('Epoch')
plt.ylabel('Root Mean Squared Error')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()