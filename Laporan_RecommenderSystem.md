# Laporan Proyek Machine Learning - Stevi Aprilianti Cahyani

## Project Overview

BigBasket adalah platform pengiriman bahan makanan daring terbesar di India yang berbasis teknologi dan memungkinkan pengguna untuk membeli berbagai kebutuhan rumah tangga, mulai dari sayuran segar, buah-buahan, daging, makanan siap saji, hingga produk kebersihan rumah, secara online. Platform ini pertama kali diluncurkan pada tahun 2011 oleh perusahaan Innovative Retail Concepts Private Limited, dan kini menjadi bagian dari grup Tata Digital, salah satu konglomerat terbesar di India. [1]

BigBasket melayani jutaan pelanggan di lebih dari 25 kota besar di India, dan telah mengembangkan jaringan yang menghubungkan pelanggan langsung dengan penjual lokal maupun gudang pusat. Melalui pendekatan ini, BigBasket menghadirkan pengalaman belanja bahan makanan yang cepat, efisien, dan dapat diandalkan, terutama bagi masyarakat urban dengan mobilitas tinggi.


![BigBasket](https://indian-retailer.s3.ap-south-1.amazonaws.com/s3fs-public/2020-09/BigBasket.jpg)

Namun, dengan semakin banyaknya produk dan variasi kategori yang ditawarkan, pengguna seringkali mengalami kesulitan dalam menemukan produk yang sesuai dengan kebutuhan mereka. Di sisi lain, para penjual juga menghadapi tantangan dalam menjangkau pelanggan yang benar-benar tertarik dengan produk mereka. Untuk menjawab tantangan ini, dibutuhkan sebuah sistem rekomendasi (recommender system) yang cerdas dan adaptif.

Sistem rekomendasi pada platform e-commerce seperti BigBasket memiliki peran penting dalam membantu pengguna menemukan produk yang relevan secara personal, sekaligus membantu penjual untuk meningkatkan visibilitas produk mereka. Melalui pendekatan berbasis data historis pembelian, interaksi pengguna, serta karakteristik produk, sistem rekomendasi dapat menyarankan produk yang kemungkinan besar akan disukai atau dibutuhkan oleh pelanggan.

Secara teknis, sistem rekomendasi yang akan dikembangkan menggunakan pendekatan kombinasi antara Content-Based Filtering dan Collaborative Filtering, atau dikenal dengan istilah Hybrid Recommender System. Pendekatan ini memungkinkan sistem untuk belajar dari perilaku pengguna, seperti riwayat pembelian dan ulasan, serta dari atribut produk seperti kategori, harga, merek, dan lainnya. Hasilnya adalah rekomendasi yang lebih akurat, personal, dan relevan.



## Business Understanding

### Problem Statements

Perubahan signifikan dalam pola perilaku konsumen menjadi salah satu dampak dari berkembangnya era digital saat ini. Jika dulu masyarakat terbiasa melakukan transaksi secara langsung di toko fisik, kini mereka lebih memilih untuk berbelanja melalui platform digital seperti e-commerce. Pergeseran ini membawa konsekuensi terhadap cara konsumen mengambil keputusan dalam berbelanja, di mana pilihan produk dipengaruhi oleh berbagai aspek seperti harga, kualitas, promosi, serta reputasi penjual atau merek. [2]

Pertumbuhan pesat dunia marketplace turut didorong oleh kemampuan perusahaan dalam menyediakan fitur-fitur yang inovatif dan responsif terhadap kebutuhan pengguna. Di antara sekian banyak fitur tersebut, sistem rekomendasi produk menjadi salah satu elemen kunci yang berpengaruh besar terhadap pengalaman pengguna dan keputusan pembelian. Pasalnya, pengguna kerap dihadapkan pada jumlah pilihan produk yang sangat banyak, sehingga sulit untuk menentukan produk mana yang paling relevan dengan kebutuhan mereka.

Oleh karena itu, penting bagi platform seperti BigBasket untuk membangun sistem rekomendasi yang efektif, personal, dan kontekstual—yakni sistem yang mampu memahami preferensi pengguna berdasarkan perilaku mereka serta menyajikan rekomendasi yang sesuai secara real-time. Penerapan sistem ini tidak hanya bertujuan untuk membantu pengguna menemukan produk yang relevan, tetapi juga untuk mendorong peningkatan penjualan, engagement pengguna, dan loyalitas terhadap platform.

### Goals

Tujuan utama dari proyek ini adalah untuk **mengembangkan sistem rekomendasi produk** yang mampu memberikan **saran produk yang lebih akurat, relevan, dan personal** kepada pengguna **BigBasket**. Sistem ini dirancang agar dapat memahami **perilaku dan preferensi pengguna** dengan menggabungkan informasi dari **data produk**, **riwayat pembelian**, serta **interaksi pengguna lainnya**.

Dengan adanya sistem ini, diharapkan pengguna dapat **lebih mudah menemukan produk yang sesuai dengan kebutuhan mereka**, sehingga meningkatkan **kepuasan berbelanja** secara keseluruhan. Selain itu, sistem ini juga berperan penting dalam mendorong peningkatan **penjualan dan profitabilitas perusahaan**, dengan cara mempertemukan pengguna dengan produk yang kemungkinan besar akan mereka beli.

Secara khusus, tujuan proyek ini mencakup:

* Memberikan **rekomendasi produk yang personal dan kontekstual** berdasarkan karakteristik pengguna dan produk.
* Mengurangi **waktu pencarian** dan meningkatkan **kenyamanan** dalam berbelanja.
* Meningkatkan **retensi pelanggan** melalui pengalaman belanja yang lebih disesuaikan.
* Memanfaatkan algoritma **Content-Based Filtering** dan **Collaborative Filtering** untuk menghasilkan rekomendasi yang **efektif dan efisien**.

###  **Solution Approach**

Untuk mencapai tujuan tersebut, sistem rekomendasi yang dikembangkan akan menggabungkan dua pendekatan utama, yaitu **Content-Based Filtering** dan **Collaborative Filtering**. Kedua metode ini saling melengkapi dalam memahami preferensi pengguna dan memberikan saran produk yang tepat sasaran.

### 1. **Content-Based Filtering**

Pendekatan ini memberikan rekomendasi produk kepada pengguna berdasarkan **kemiripan atribut produk** dengan produk yang sebelumnya pernah mereka lihat atau beli.

### 2. **Collaborative Filtering**

Berbeda dengan pendekatan berbasis konten, **Collaborative Filtering** menganalisis **perilaku pengguna lain** untuk memberikan rekomendasi. Sistem akan mengidentifikasi **pola pembelian**, **ulasan**, atau **rating** dari pengguna lain yang memiliki **kebiasaan serupa**, kemudian menyarankan produk yang disukai oleh kelompok pengguna tersebut.

Dengan kata lain, jika pengguna A dan B memiliki pola perilaku yang mirip, maka produk yang disukai oleh A kemungkinan besar juga akan disukai oleh B. Metode ini mampu menangkap **preferensi implisit** dari pengguna melalui hubungan kolektif antar pengguna.

Dengan **menggabungkan kedua pendekatan ini**, sistem rekomendasi akan mampu memanfaatkan baik **data eksplisit (atribut produk)** maupun **data implisit (perilaku pengguna)**. Hasilnya adalah rekomendasi yang **lebih cerdas, fleksibel, dan akurat**, serta mampu menyesuaikan dengan kebutuhan masing-masing pengguna di platform **BigBasket**.




## Data Understanding
Dataset yang digunakan dalam proyek ini adalah **Big Basket Product Analysis**, yang dapat diakses melalui [**Kaggle**](https://www.kaggle.com/datasets/amrit0611/big-basket-product-analysis).

Selanjutnya, dilakukan proses **Exploratory Data Analysis (EDA)** sebagai tahap awal untuk memahami data lebih dalam. EDA bertujuan untuk mengidentifikasi karakteristik data, menemukan pola atau tren, mendeteksi anomali, serta memverifikasi asumsi-asumsi awal terhadap data. Berikut untuk hasilnya :

1. Melihat Ringkasan Struktur DataFrame
   
   | No  | Column        | Non-Null Count  | Dtype   |
    |-----|---------------|-----------------|---------|
    | 0   | index         | 27,555 non-null | int64   |
    | 1   | product       | 27,554 non-null | object  |
    | 2   | category      | 27,555 non-null | object  |
    | 3   | sub_category  | 27,555 non-null | object  |
    | 4   | brand         | 27,554 non-null | object  |
    | 5   | sale_price    | 27,555 non-null | float64 |
    | 6   | market_price  | 27,555 non-null | float64 |
    | 7   | type          | 27,555 non-null | object  |
    | 8   | rating        | 18,929 non-null | float64 |
    | 9   | description   | 27,440 non-null | object  |

Dataset ini memiliki 10 kolom dengan total 27.555 baris data. Sebagian besar kolom berisi data bertipe *object* (kategori atau teks), beberapa berupa *float64* (angka desimal), dan hanya kolom *index* yang menggunakan tipe *int64* (angka bulat). Berikut adalah penjelasan singkat untuk masing-masing kolom:

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

2. Memeriksa Statistik Deskriptif

   | Statistik | index       | sale\_price  | market\_price | rating       |
    | --------- | ----------- | ------------ | ------------- | ------------ |
    | count     | 27555.00000 | 27555.000000 | 27555.000000  | 18929.000000 |
    | mean      | 13778.00000 | 322.514808   | 382.056664    | 3.943410     |
    | std       | 7954.58767  | 486.263116   | 581.730717    | 0.739063     |
    | min       | 1.00000     | 2.450000     | 3.000000      | 1.000000     |
    | 25%       | 6889.50000  | 95.000000    | 100.000000    | 3.700000     |
    | 50%       | 13778.00000 | 190.000000   | 220.000000    | 4.100000     |
    | 75%       | 20666.50000 | 359.000000   | 425.000000    | 4.300000     |
    | max       | 27555.00000 | 12500.000000 | 12500.000000  | 5.000000     |


Berikut penjelasan singkat dari tabel statistik deskriptif tersebut:

Tabel ini menyajikan ringkasan statistik untuk kolom numerik utama dalam dataset, yaitu `index`, `sale_price`, `market_price`, dan `rating`.

* **index**: Nomor urut data, mulai dari 1 hingga 27.555.
* **sale\_price** (harga jual): Harga jual produk rata-rata sekitar 322,5 Rupee, dengan nilai terendah 2,45 Rupee dan tertinggi 12.500 Rupee. Median harga jual (50%) adalah 190 Rupee, menunjukkan sebagian besar produk dijual di bawah harga tersebut.
* **market\_price** (harga pasar): Harga pasar rata-rata sekitar 382 Rupee, sedikit lebih tinggi dari harga jual. Harga maksimum sama-sama 12.500 Rupee, menunjukkan ada produk dengan harga sangat tinggi.
* **rating**: Rata-rata rating pengguna adalah 3,94 dari maksimal 5. Namun, rating hanya tersedia untuk 18.929 produk dari total 27.555, sehingga tidak semua produk memiliki penilaian.

Variasi harga jual dan harga pasar cukup besar, terlihat dari nilai standar deviasi yang tinggi, menandakan perbedaan harga yang signifikan antar produk. Sedangkan rating cenderung berada di kisaran menengah ke atas dengan variasi yang lebih kecil.

3. Memeriksa Missing Value

   ```
   Terdapat 8743 nilai kosong di beberapa kolom berikut:
    product           1
    brand             1
    rating         8626
    description     115
   ```

4. Memeriksa Unique Column

   ```
   terdapat 27555nilai unik di kolomindex
    terdapat 23540nilai unik di kolomproduct
    terdapat 11nilai unik di kolomcategory
    terdapat 90nilai unik di kolomsub_category
    terdapat 2313nilai unik di kolombrand
    terdapat 3256nilai unik di kolomsale_price
    terdapat 1348nilai unik di kolommarket_price
    terdapat 426nilai unik di kolomtype
    terdapat 40nilai unik di kolomrating
    terdapat 21944nilai unik di kolomdescription
   ```

5. Visualisasi

   * Distribusi Jumlah Data per Kategori Produk

	|   | Kategori Produk             | Jumlah |
	|---|-----------------------------|--------|
	| 0 | Beauty & Hygiene            | 7867   |
	| 1 | Gourmet & World Food        | 4690   |
	| 2 | Kitchen, Garden & Pets      | 3580   |
	| 3 | Snacks & Branded Foods      | 2814   |
	| 4 | Foodgrains, Oil & Masala    | 2676   |
	| 5 | Cleaning & Household        | 2675   |
	| 6 | Beverages                   | 885    |
	| 7 | Bakery, Cakes & Dairy       | 851    |
	| 8 | Baby Care                   | 610    |
	| 9 | Fruits & Vegetables         | 557    |
	|10 | Eggs, Meat & Fish           | 350    |

     ![1_Distribusi Jumlah Data per Kategori Produk](https://github.com/user-attachments/assets/24fc8245-2261-4b73-993f-52f3f4a0461c)

     Visualisasi ini menunjukkan distribusi jumlah produk berdasarkan kategori dalam dataset. Total terdapat 11 kategori produk dengan variasi jumlah data yang cukup signifikan.

   Kategori **Beauty & Hygiene** mendominasi dengan jumlah produk terbanyak, yakni sebanyak 7.867 item, menunjukkan fokus pasar yang cukup besar pada produk perawatan dan kebersihan. Diikuti oleh kategori **Gourmet & World Food** yang memiliki 4.690 produk, dan **Kitchen, Garden & Pets** dengan 3.580 produk.
        
    Kategori lain seperti **Snacks & Branded Foods** (2.814), **Foodgrains, Oil & Masala** (2.676), dan **Cleaning & Household** (2.675) juga memiliki jumlah produk yang cukup besar, menandakan keberagaman jenis produk yang tersedia.
        
   Sementara itu, kategori dengan jumlah produk paling sedikit adalah **Eggs, Meat & Fish** dengan 350 produk, **Fruits & Vegetables** 557 dan **Baby Care** 610 produk.
        

   * Top 10 Produk Best Seller
     
	|   | produk                            | kategori                  | jumlah |
	|---|-----------------------------------|---------------------------|--------|
	| 0 | Turmeric Powder/Arisina Pudi      | Foodgrains, Oil & Masala  | 26     |
	| 1 | Cow Ghee/Tuppa                    | Foodgrains, Oil & Masala  | 14     |
	| 2 | Extra Virgin Olive Oil           | Gourmet & World Food       | 14     |
	| 3 | Colorsilk Hair Colour With Keratin | Beauty & Hygiene         | 12     |
	| 4 | Soft Drink                        | Beverages                 | 12     |
	| 5 | Coriander Powder                  | Foodgrains, Oil & Masala  | 11     |
	| 6 | Ghee/Tuppa                        | Foodgrains, Oil & Masala  | 11     |
	| 7 | Powder - Coriander                | Foodgrains, Oil & Masala  | 11     |
	| 8 | Olive Oil - Extra Virgin          | Gourmet & World Food      | 11     |
	| 9 | Casting Creme Gloss Hair Color    | Beauty & Hygiene          | 10     |

     ![Top 10 Produk Best Seller](https://github.com/user-attachments/assets/26daea23-3539-4185-982b-566aa1c0c274)

     Berdasarkan visualisasi data di atas, produk yang paling sering muncul dalam dataset didominasi oleh bahan-bahan yang 
     berkaitan dengan kebutuhan memasak, seperti bumbu dapur Turmeric Powder/Arisina Pudi. Selain itu, produk lemak dan 
     minyak seperti Extra Virgin Olive Oil dan Cow Ghee/Tuppa juga termasuk yang paling banyak dicatat, mengindikasikan 
     popularitas tinggi dalam konsumsi rumah tangga.


   * 10 Produk Paling Sedikit Terjual

	|   | produk                                                  | kategori                | jumlah |
	|---|----------------------------------------------------------|------------------------|--------|
	| 0 | Geometry Box - Disney, Invento                           | Cleaning & Household   | 1      |
	| 1 | Geometry Box - Asteroid                                  | Cleaning & Household   | 1      |
	| 2 | Geometry Box - Archimedes                                | Cleaning & Household   | 1      |
	| 3 | Genuine Wood Shaving Brush                               | Beauty & Hygiene       | 1      |
	| 4 | Gentleman Urbane Deodorant                               | Beauty & Hygiene       | 1      |
	| 5 | Gentleman Urbane - Eau De Parfum For Men                 | Beauty & Hygiene       | 1      |
	| 6 | Gentleman Classic Deodorant - For Men 150 ml +...        | Beauty & Hygiene       | 1      |
	| 7 | Gentleman Classic Daily Wear Perfume EDC For Men         | Beauty & Hygiene       | 1      |
	| 8 | Gentleman - Urbane Compact Perfume                       | Beauty & Hygiene       | 1      |
	| 9 | Geometry Box - Invento                                   | Cleaning & Household   | 1      |


     Berdasarkan tabel di atas, terlihat bahwa produk yang  tingkat penjualan terendah didominasi oleh dua kategori utama, yaitu Cleaning & Household dan Beauty & Hygiene. Produk-produk seperti Geometry Box dari berbagai seri dan parfum pria dari seri Gentleman masing-masing hanya tercatat satu kali, mengindikasikan bahwa produk ini memiliki minat yang rendah. Hal ini dapat menjadi bahan evaluasi bagi pengelola produk untuk mengevaluasi efektivitas promosi atau kebutuhan pasar terhadap produk-produk tersebut.


   * Daftar Jumlah Top Kategori dengan Rating Tertinggi (5.0)
     
	| index  | product                                  | category              | sub_category            | brand              | sale_price | market_price | type                      | rating | description                                                               |
	|--------|-------------------------------------------|------------------------|--------------------------|--------------------|------------|---------------|----------------------------|--------|---------------------------------------------------------------------------|
	| 13     | Face Wash - Oil Control, Active          | Beauty & Hygiene       | Skin Care                | Oxy                | 110.00     | 110.0         | Face Care                  | 5.0    | This face wash deeply cleanses dirt and impurities...                     |
	| 17     | Smooth Skin Oil - For Dry Skin           | Beauty & Hygiene       | Skin Care                | Aroma Treasures    | 324.00     | 360.0         | Aromatherapy               | 5.0    | Specially crafted for dry skin, this richly formulated oil...            |
	| 25     | Veggie Cutter                            | Kitchen, Garden & Pets | Kitchen Accessories      | IRICH              | 195.00     | 195.0         | Choppers & Graters         | 5.0    | Food Grade High Quality Plastic, Keep and store vegetables...            |
	| 45     | Plain Green Olives                       | Gourmet & World Food   | Tinned & Processed Food  | Figaro             | 179.00     | 179.0         | Olive, Jalapeno, Gherkin   | 5.0    | Olives are small fruits that grow on olive trees...                      |
	| 93     | Topp Up Milk - Elaichi                   | Bakery, Cakes & Dairy  | Dairy                    | Gowardhan          | 80.01      | 90.0          | Flavoured, Soya Milk       | 5.0    | Gowardhan Topp-Up Milk is made by 100% of cow milk...                    |
	| ...    | ...                                       | ...                    | ...                      | ...                | ...        | ...           | ...                        | ...    | ...                                                                       |
	| 27508  | Extra Crisp Sweet Corn                   | Gourmet & World Food   | Tinned & Processed Food  | Daucy              | 202.50     | 225.0         | Beans & Pulses             | 5.0    | We bring for you Europe’s leading brand of canned vegetables...          |
	| 27509  | Palm Jaggery/Bella Crystals              | Foodgrains, Oil & Masala | Salt, Sugar & Jaggery | Draft              | 199.00     | 199.0         | Sugar & Jaggery            | 5.0    | It is a healthy alternative to white sugar and contains minerals...      |
	| 27513  | Water Bottle - Fridge, Tulip, Dark Blue  | Kitchen, Garden & Pets | Storage & Accessories    | Cello              | 109.00     | 137.0         | Water & Fridge Bottles     | 5.0    | Cello Tulip fridge bottle is manufactured by Japan Technology...         |
	| 27516  | EDT Spray - Musk For Men                 | Beauty & Hygiene       | Fragrances & Deos        | Brut               | 595.00     | 595.0         | Men's Deodorants           | 5.0    | Brut Musk was launched in 1986 as an elegant masculine fragrance...      |
	| 27549  | Apple Cider Vinegar Shampoo              | Beauty & Hygiene       | Hair Care                | Morpheme Remedies  | 499.00     | 499.0         | Shampoo & Conditioner      | 5.0    | Say no to dull, lifeless, dry and damaged hair with this herbal shampoo. |
	
	**1407 rows × 10 columns**

     ![Daftar Jumlah Top Kategori dengan Rating Tertinggi (5.0)](https://github.com/user-attachments/assets/dc6c7bce-1fd7-4111-b858-c3b84d80580f)

	|   | Kategori Produk           | Jumlah Produk |
	|---|---------------------------|----------------|
	| 0 | Beauty & Hygiene          | 562            |
	| 1 | Gourmet & World Food      | 273            |
	| 2 | Kitchen, Garden & Pets    | 211            |
	| 3 | Cleaning & Household      | 135            |
	| 4 | Snacks & Branded Foods    | 65             |
	| 5 | Foodgrains, Oil & Masala  | 60             |
	| 6 | Baby Care                 | 47             |
	| 7 | Beverages                 | 37             |
	| 8 | Bakery, Cakes & Dairy     | 17             |

     Visualisasi ini menunjukkan **kategori produk dengan jumlah item terbanyak yang mendapatkan rating tertinggi (5.0)** dari pengguna. Kategori dengan performa terbaik dalam hal kepuasan pengguna adalah:
        
     * **Beauty & Hygiene** dengan **562 produk** ber-rating sempurna, menempati posisi teratas. Ini menandakan bahwa produk-produk kecantikan dan kebersihan memiliki tingkat kepuasan tinggi di kalangan konsumen.
     * **Gourmet & World Food** dan **Kitchen, Garden & Pets** masing-masing memiliki **273** dan **211 produk** dengan rating 5.0, menunjukkan kualitas produk yang baik di kategori makanan khusus dan perlengkapan rumah tangga.
     * **Cleaning & Household** juga memiliki kontribusi besar dengan **135 produk** ber-rating sempurna, yang mungkin mencerminkan keefektifan dan keandalan produk kebersihan.
     * Kategori lain seperti **Snacks & Branded Foods**, **Baby Care**, **Beverages**, dan **Bakery, Cakes & Dairy** juga tercatat memiliki sejumlah produk dengan rating sempurna, meskipun jumlahnya lebih sedikit.

   * Daftar JumlaH Kategori dengan Rating Terendah (1.0)

	|     | Kategori Produk           | Jumlah Produk |
	|-----|---------------------------|----------------|
	| 0   | Beauty & Hygiene          | 192            |
	| 1   | Kitchen, Garden & Pets    | 65             |
	| 2   | Gourmet & World Food      | 58             |
	| 3   | Snacks & Branded Foods    | 22             |
	| 4   | Cleaning & Household      | 19             |
	| 5   | Baby Care                 | 11             |
	| 6   | Foodgrains, Oil & Masala  | 9              |
	| 7   | Beverages                 | 9              |
	| 8   | Bakery, Cakes & Dairy     | 2              |

     ![Daftar Jumlah Kategori dengan Rating Terendah (1.0)](https://github.com/user-attachments/assets/9909dec4-fd70-42e0-a942-bf461b2dfee4)

     Visualisasi tersebut menunjukkan distribusi kategori produk dengan rating terendah (1.0), di mana kategori Beauty & Hygiene memiliki jumlah produk terbanyak yang diberi rating rendah, diikuti oleh Kitchen, Garden & Pets dan Gourmet & World Food. Hal ini mengindikasikan bahwa produk-produk dalam kategori tersebut cenderung mendapat ulasan buruk dari pengguna, sehingga dapat menjadi perhatian khusus untuk evaluasi kualitas atau kepuasan pelanggan.


## Data Preparation

1. Menghapus Kolom yang Tidak Relevan

   Melakukan drop pada kolom ``index``, karena kolom tersebut tidak relevan untuk digunakan dalam langkah analisis yang lebih lanjut, dan berikut adalah hasil dari penghapusan kolom :
   | product | category | sub_category | brand | sale_price | market_price | type | rating | description |
    |--------|----------|--------------|-------|------------|---------------|------|--------|-------------|
    | Garlic Oil - Vegetarian Capsule 500 mg | Beauty & Hygiene | Hair Care | Sri Sri Ayurveda | 220.0 | 220.0 | Hair Oil & Serum | 4.1 | This Product contains Garlic Oil that is known... |
    | Water Bottle - Orange | Kitchen, Garden & Pets | Storage & Accessories | Mastercook | 180.0 | 180.0 | Water & Fridge Bottles | 2.3 | Each product is microwave safe (without lid), ... |
    | Brass Angle Deep - Plain, No.2 | Cleaning & Household | Pooja Needs | Trm | 119.0 | 250.0 | Lamp & Lamp Oil | 3.4 | A perfect gift for all occasions, be it your m... |
    | Cereal Flip Lid Container/Storage Jar - Assorted | Cleaning & Household | Bins & Bathroom Ware | Nakoda | 149.0 | 176.0 | Laundry, Storage Baskets | 3.7 | Multipurpose container with an attractive desi... |
    | Creme Soft Soap - For Hands & Body | Beauty & Hygiene | Bath & Hand Wash | Nivea | 162.0 | 162.0 | Bathing Bars & Soaps | 4.4 | Nivea Creme Soft Soap gives your skin the best... |
    
       
2. Menghapus duplikasi data

   ````
   Total Duplicates : 354
   Berhasil menghapus duplikasi data!
   ```
   
 Sebelum membangun model, kita akan memeriksa duplikasi dalam data dan menghapusnya untuk memastikan data yang digunakan tidak redundan. Hal ini dilakukan untuk meningkatkan kualitas data, yaitu menghindari bias, meningkatkan akurasi serta dapat juga mengurangi beban komputasi. 
   
3. Menangani Missing Value

    Berikut merupakan langkah-langkah yang digunakan untuk menangani missing value pada dataset ini :

     * Memeriksa mean & median rating terlebih dahulu
       ```python
       # Mean rating
        rating_mean = df_products['rating'].mean()
        print(f"Mean rating adalah: {rating_mean:.2f}")

        # Median rating
        rating_median = df_products['rating'].median()
        print(f"Median rating adalah: {rating_median:.2f}")
       ```

       output :
       ```
       Mean rating adalah: 3.94
       Median rating adalah: 4.10
       ```
        Berdasarkan hasil output, dapat diketahui bahwa mean rating adalah 3.94 sedangkan untuk median sebesar 4.10. Nah maka dengan demikian dilakukan penanganan missing value terhadap kolom ``rating`` yang hilang dengan menggunakan nilai mean rating 
       
     * Menangani missing value pada kolom rating dengan nilai mean rating
      
          Kolom rating memiliki sekitar 8.626 nilai kosong dari total 27.555 data. Karena rating bersifat numerik dan merepresentasikan penilaian pengguna terhadap produk, pendekatan yang digunakan untuk mengisi missing value adalah menggunakan nilai rata-rata (mean) dari kolom tersebut. Nilai rata-rata rating dalam dataset adalah 3.94.
    
        ```python
           df_products['rating'] = df_products['rating'].fillna(value=rating_mean)
            missing_after = df_products['rating'].isnull().sum()
            print(f"Berhasil mengisi missing value dengan mean rating {rating_mean:.2f}")
            print(f"Sisa missing value setelah pengisian: {missing_after}")
         ```
       
       output :
       
      ```
           Berhasil mengisi missing value dengan mean rating 3.94
            Sisa missing value setelah pengisian: 0
      ```
                   
     * Menghapus missing value pada kolom ``product``, ``brand`` dan ``description``
  
       ```python
       df_products.dropna(inplace=True)
       ```
       
       Penghapusan missing value pada kolom product, brand, dan description dilakukan karena ketiga kolom tersebut memuat informasi penting yang bersifat deskriptif dan krusial dalam identifikasi serta pemahaman terhadap produk. Mengingat kolom-kolom ini berisi data teks, tidak logis jika diisi dengan nilai umum atau acak karena dapat menyebabkan distorsi pada hasil analisis. Selain itu, jumlah nilai kosong pada ketiga kolom tersebut relatif sangat sedikit dibandingkan total baris data, sehingga penghapusannya tidak berdampak signifikan terhadap ukuran dataset dan justru membantu menjaga kualitas serta konsistensi data yang akan dianalisis. Dan berikut adalah hasil/tampilan tabel setelah dilakukan tahapan ini :

               ```
            RangeIndex: 27087 entries, 0 to 27086  
            Data columns (total 9 columns):  
             #   Column        Non-Null Count  Dtype  
            ---  ------        --------------  -----  
             0   product       27087 non-null  object  
             1   category      27087 non-null  object  
             2   sub_category  27087 non-null  object  
             3   brand         27087 non-null  object  
             4   sale_price    27087 non-null  float64  
             5   market_price  27087 non-null  float64  
             6   type          27087 non-null  object  
             7   rating        27087 non-null  float64  
             8   description   27087 non-null  object  
            ```
       

4. Changing Certain Value

   Langkah selanjutnya adalah **mengubah dan membersihkan beberapa nilai dalam dataset**, terutama yang berkaitan dengan data berbasis teks. Pertama, dilakukan **pembuatan salinan** dari `df_products` ke `df_products_copy` sebagai bentuk kehati-hatian agar data asli tetap aman jika terjadi kesalahan saat modifikasi. Kemudian, dibuat fungsi `hapus_spasi` untuk menghilangkan spasi berlebih di awal atau akhir string, yang sangat penting untuk menjaga konsistensi data. Selanjutnya, dibuat fungsi `tps` (tokenisasi dan pembersihan string) yang memecah nilai berbentuk teks panjang dengan pemisah seperti `&`, `,`, `*`, atau baris baru, lalu menghilangkan spasinya. Fungsi ini diterapkan pada kolom `category`, `sub_category`, dan `type`, karena kolom-kolom ini sering berisi beberapa label dalam satu sel. Setelah itu, dilakukan **standarisasi dan pembersihan lebih lanjut** melalui fungsi `cleaner` untuk mengubah huruf menjadi kecil dan menghapus semua spasi di dalam string, baik untuk tipe list maupun string tunggal. Fungsi ini diterapkan pada kolom `category`, `sub_category`, `type`, dan `brand` untuk memastikan semua data teks bersih dan konsisten, sehingga mempermudah proses analisis selanjutnya.

   * Membuat salinan df_products ke df_products_copy supaya data asli tetap aman jika nanti ada modifikasi

     ```python
     df_products_copy = df_products.copy()
     print("Berhasil membuat salinan!")
     ```

     output :
     ```
     Berhasil membuat salinan!
     ```

    * Membuat Fungsi untuk Membersihkan Spasi (Whitespace Stripping)

      ```python
      hapus_spasi = lambda a: a.strip()
      print("Fungsi hapus_spasi berhasil dibuat!")
      ```

      output :

      ```
      Fungsi hapus_spasi berhasil dibuat!
      ```
      
    * Tokenisasi dan Pembersihan String

      ```python
      tps = lambda a: list(map(hapus_spasi, re.split('& |, |\*|\n', a)))
      print("Fungsi tps berhasil dibuat!")
      ```

      output :
      ```
      Fungsi tps berhasil dibuat!
      ```
      
    * Penerapan Fungsi Tokenisasi pada Beberapa Kolom

      ```python
      for col in ['category', 'sub_category', 'type']:
        df_products_copy[col] = df_products_copy[col].apply(tps)
        print("Berhasil menerapkan fungsi tps pada kolom category, sub_category, dan type!")
      ```

      output :
      ```
      Berhasil menerapkan fungsi tps pada kolom category, sub_category, dan type!
      ```

    * pembersihan dan standarisasi data teks
  
      ```python
      
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
      ```

      output :

      ```
      Berhasil membersihkan data pada kolom category, sub_category, type, dan brand!
      ```

   
5. Content Based Filtering

    Langkah berikutnya sebagai persiapan untuk model dengan **Content-Based Filtering** yaitu dimulai dengan membuat salinan dari `df_products_copy` menjadi `df_cbf`, agar data tetap terjaga saat dilakukan manipulasi lebih lanjut. Setelah itu, dibuat fungsi `combine_features` yang bertujuan untuk menggabungkan informasi dari beberapa kolom penting — seperti `category`, `sub_category`, `brand`, dan `type` — menjadi satu string panjang per baris data. Penggabungan ini dilakukan karena Content-Based Filtering membutuhkan representasi teks dari atribut produk yang dapat dibandingkan satu sama lain. Selanjutnya, dilakukan **ekstraksi fitur menggunakan TF-IDF Vectorizer**, yaitu metode yang mengubah teks menjadi bentuk numerik berdasarkan frekuensi dan kekhasan kata. TF-IDF secara otomatis mengabaikan kata-kata umum (stop words) agar hanya mempertahankan kata yang dianggap penting dalam membedakan satu produk dengan lainnya. Kolom hasil gabungan `gab` dari setiap produk dikonversi menjadi matriks TF-IDF, di mana baris merepresentasikan produk dan kolom merepresentasikan kata unik. Ukuran dari matriks ini adalah `(27201, 3083)`, yang berarti terdapat 27.201 produk dan 3.083 kata unik, siap untuk digunakan dalam perhitungan kemiripan produk berbasis konten.


    * Melakukan inisialisasi

      ```python
      df_cbf = df_products_copy.copy()
      ```

    * Menggabungkan isi beberapa kolom jadi satu string per baris

      ```python
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
      ```
      
    * Ekstraksi Fitur TF-IDF
      Membuat objek TF-IDF Vectorizer yang secara otomatis mengabaikan kata-kata umum dalam bahasa Inggris (stop words) 
      supaya fokus ke kata yang lebih bermakna.
      
      ```python
      tfidf = TfidfVectorizer(stop_words='english')
      ```

      Mengubah semua teks di kolom 'gab' jadi matriks TF-IDF, di mana setiap baris adalah dokumen (baris data), dan setiap kolom mewakili kata unik yang ditemukan. Nilai di matriks menunjukkan seberapa penting sebuah kata pada dokumen 
tersebut.

      ```python
      tfidf_matrix = tfidf.fit_transform(df_cbf['gab'])
      ```

      Menampilkan ukuran matriks TF-IDF.

      ```python
      tfidf_matrix.shape
      ```

      output :

      ```
      (27201, 3083)
      ```
      
      
    
6. Collaborative Filtering

    * Membuat kolom baru bernama ``user_id`` di DataFrame
      ```python
      df_products_copy['user_id'] = (df_products_copy.index % 500) + 1
      ```

      Membagi data seolah-olah ada 500 pengguna yang mengulang secara siklik. Hal ini diterapkan karena dataframe tidak 
      mempunyai kolom ``user_id``, tapi ingin mensimulasikan data user untuk analisis rekomendasi produk.

      ```python
      #hasil
      df_products_copy
      ```

      output :

    
        product                                    | category             | sub_category         | brand                  | sale_price | market_price | type                     | rating | user_id
        -------------------------------------------|----------------------|----------------------|------------------------|------------|---------------|---------------------------|--------|---------
        Garlic Oil - Vegetarian Capsule 500 mg     | [beauty, hygiene]    | [haircare]           | srisriayurveda         | 220.00     | 220.0         | [hairoil, serum]          | 4.1    | 1
        Water Bottle - Orange                      | [kitchen, garden, pets] | [storage, accessories] | mastercook         | 180.00     | 180.0         | [water, fridgebottles]    | 2.3    | 2
        Brass Angle Deep - Plain, No.2             | [cleaning, household] | [poojaneeds]         | trm                    | 119.00     | 250.0         | [lamp, lampoil]           | 3.4    | 3
        Cereal Flip Lid Container/Storage Jar ...  | [cleaning, household] | [bins, bathroomware] | nakoda                 | 149.00     | 176.0         | [laundry, storagebaskets] | 3.7    | 4
        Creme Soft Soap - For Hands & Body         | [beauty, hygiene]    | [bath, handwash]     | nivea                  | 162.00     | 162.0         | [bathingbars, soaps]      | 4.4    | 5
        ...                                        | ...                  | ...                  | ...                    | ...        | ...           | ...                       | ...    | ...
        United Dreams Go Far Deodorant            | [beauty, hygiene]    | [men'sgrooming]      | unitedcolorsofbenetton | 214.53     | 390.0         | [men'sdeodorants]         | 4.5    | 201
        
        27086 rows × 10 columns

      
    * Encoding Label
      
      Agar algoritma berbasis matriks dapat bekerja, data kategorikal harus dikonversi menjadi bentuk numerik. Ini penting karena Collaborative Filtering, terutama yang menggunakan pendekatan matrix factorization, hanya dapat memproses data numerik. Oleh karena itu, atribut seperti ``user_id`` dan ``product`` perlu diencoding menjadi angka. Proses encoding ini juga berguna untuk membentuk matriks user-item yang dibutuhkan dalam operasi aljabar linear, seperti dekomposisi matriks. Dengan begitu, sistem dapat melakukan perhitungan secara efisien dan tetap mampu menangani dataset berukuran besar.
      
      Tahap 1 : Encoding ``user_id``
  
      Tahap ini merupakan proses encoding terhadap kolom `user_id` agar bisa digunakan dalam model machine learning. Pertama, seluruh nilai unik dari `user_id` dikumpulkan dalam bentuk list menggunakan fungsi `.unique().tolist()`, kemudian ditampilkan daftar lengkap user-nya. Setelah itu, dilakukan encoding dengan cara membuat dictionary yang memetakan `user_id` asli ke index numerik mulai dari 0 menggunakan `enumerate`. Hasilnya adalah pasangan seperti `{1: 0, 2: 1, 3: 2, ...}` yang menunjukkan bahwa user dengan ID 1 diubah menjadi 0, dan seterusnya. Terakhir, dibuat mapping sebaliknya yaitu dari indeks numerik ke `user_id` asli, untuk memudahkan interpretasi kembali ke identitas user sebenarnya saat dibutuhkan. Hasil mapping tersebut ditampilkan sebagian untuk memastikan proses encoding berjalan dengan benar, ditandai dengan contoh output seperti “Index 0 → user\_id 1”.

   
       a. Mengambil semua nilai unik dari kolom user_id dan menyimpannya dalam bentuk list
   
          ```python
          user_list = df_products_copy['user_id'].unique().tolist()
          print('Daftar user_id :', user_list)
          ```
         output :
         ```
         Daftar user_id : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 432, 433, 434, 435, 436, 437, 438, 439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 449, 450, 451, 452, 453, 454, 455, 456, 457, 458, 459, 460, 461, 462, 463, 464, 465, 466, 467, 468, 469, 470, 471, 472, 473, 474, 475, 476, 477, 478, 479, 480, 481, 482, 483, 484, 485, 486, 487, 488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500]
         ```
   
      
       b. Melakukan encoding user_id
          ```python
              user_encoding ={x: i for i, x in enumerate(user_list)}
              print('Hasil encoding : ', user_encoding)
          ```
          output :
       ```
          Hasil encoding :  {1: 0, 2: 1, 3: 2, 4: 3, 5: 4, 6: 5, 7: 6, 8: 7, 9: 8, 10: 9, 11: 10, 12: 11, 13: 12, 14: 13, 15: 14, 16: 15, 17: 16, 18: 17, 19: 18, 20: 19, 21: 20, 22: 21, 23: 22, 24: 23, 25: 24, 26: 25, 27: 26, 28: 27, 29: 28, 30: 29, 31: 30, 32: 31, 33: 32, 34: 33, 35: 34, 36: 35, 37: 36, 38: 37, 39: 38, 40: 39, 41: 40, 42: 41, 43: 42, 44: 43, 45: 44, 46: 45, 47: 46, 48: 47, 49: 48, 50: 49, 51: 50, 52: 51, 53: 52, 54: 53, 55: 54, 56: 55, 57: 56, 58: 57, 59: 58, 60: 59, 61: 60, 62: 61, 63: 62, 64: 63, 65: 64, 66: 65, 67: 66, 68: 67, 69: 68, 70: 69, 71: 70, 72: 71, 73: 72, 74: 73, 75: 74, 76: 75, 77: 76, 78: 77, 79: 78, 80: 79, 81: 80, 82: 81, 83: 82, 84: 83, 85: 84, 86: 85, 87: 86, 88: 87, 89: 88, 90: 89, 91: 90, 92: 91, 93: 92, 94: 93, 95: 94, 96: 95, 97: 96, 98: 97, 99: 98, 100: 99, 101: 100, 102: 101, 103: 102, 104: 103, 105: 104, 106: 105, 107: 106, 108: 107, 109: 108, 110: 109, 111: 110, 112: 111, 113: 112, 114: 113, 115: 114, 116: 115, 117: 116, 118: 117, 119: 118, 120: 119, 121: 120, 122: 121, 123: 122, 124: 123, 125: 124, 126: 125, 127: 126, 128: 127, 129: 128, 130: 129, 131: 130, 132: 131, 133: 132, 134: 133, 135: 134, 136: 135, 137: 136, 138: 137, 139: 138, 140: 139, 141: 140, 142: 141, 143: 142, 144: 143, 145: 144, 146: 145, 147: 146, 148: 147, 149: 148, 150: 149, 151: 150, 152: 151, 153: 152, 154: 153, 155: 154, 156: 155, 157: 156, 158: 157, 159: 158, 160: 159, 161: 160, 162: 161, 163: 162, 164: 163, 165: 164, 166: 165, 167: 166, 168: 167, 169: 168, 170: 169, 171: 170, 172: 171, 173: 172, 174: 173, 175: 174, 176: 175, 177: 176, 178: 177, 179: 178, 180: 179, 181: 180, 182: 181, 183: 182, 184: 183, 185: 184, 186: 185, 187: 186, 188: 187, 189: 188, 190: 189, 191: 190, 192: 191, 193: 192, 194: 193, 195: 194, 196: 195, 197: 196, 198: 197, 199: 198, 200: 199, 201: 200, 202: 201, 203: 202, 204: 203, 205: 204, 206: 205, 207: 206, 208: 207, 209: 208, 210: 209, 211: 210, 212: 211, 213: 212, 214: 213, 215: 214, 216: 215, 217: 216, 218: 217, 219: 218, 220: 219, 221: 220, 222: 221, 223: 222, 224: 223, 225: 224, 226: 225, 227: 226, 228: 227, 229: 228, 230: 229, 231: 230, 232: 231, 233: 232, 234: 233, 235: 234, 236: 235, 237: 236, 238: 237, 239: 238, 240: 239, 241: 240, 242: 241, 243: 242, 244: 243, 245: 244, 246: 245, 247: 246, 248: 247, 249: 248, 250: 249, 251: 250, 252: 251, 253: 252, 254: 253, 255: 254, 256: 255, 257: 256, 258: 257, 259: 258, 260: 259, 261: 260, 262: 261, 263: 262, 264: 263, 265: 264, 266: 265, 267: 266, 268: 267, 269: 268, 270: 269, 271: 270, 272: 271, 273: 272, 274: 273, 275: 274, 276: 275, 277: 276, 278: 277, 279: 278, 280: 279, 281: 280, 282: 281, 283: 282, 284: 283, 285: 284, 286: 285, 287: 286, 288: 287, 289: 288, 290: 289, 291: 290, 292: 291, 293: 292, 294: 293, 295: 294, 296: 295, 297: 296, 298: 297, 299: 298, 300: 299, 301: 300, 302: 301, 303: 302, 304: 303, 305: 304, 306: 305, 307: 306, 308: 307, 309: 308, 310: 309, 311: 310, 312: 311, 313: 312, 314: 313, 315: 314, 316: 315, 317: 316, 318: 317, 319: 318, 320: 319, 321: 320, 322: 321, 323: 322, 324: 323, 325: 324, 326: 325, 327: 326, 328: 327, 329: 328, 330: 329, 331: 330, 332: 331, 333: 332, 334: 333, 335: 334, 336: 335, 337: 336, 338: 337, 339: 338, 340: 339, 341: 340, 342: 341, 343: 342, 344: 343, 345: 344, 346: 345, 347: 346, 348: 347, 349: 348, 350: 349, 351: 350, 352: 351, 353: 352, 354: 353, 355: 354, 356: 355, 357: 356, 358: 357, 359: 358, 360: 359, 361: 360, 362: 361, 363: 362, 364: 363, 365: 364, 366: 365, 367: 366, 368: 367, 369: 368, 370: 369, 371: 370, 372: 371, 373: 372, 374: 373, 375: 374, 376: 375, 377: 376, 378: 377, 379: 378, 380: 379, 381: 380, 382: 381, 383: 382, 384: 383, 385: 384, 386: 385, 387: 386, 388: 387, 389: 388, 390: 389, 391: 390, 392: 391, 393: 392, 394: 393, 395: 394, 396: 395, 397: 396, 398: 397, 399: 398, 400: 399, 401: 400, 402: 401, 403: 402, 404: 403, 405: 404, 406: 405, 407: 406, 408: 407, 409: 408, 410: 409, 411: 410, 412: 411, 413: 412, 414: 413, 415: 414, 416: 415, 417: 416, 418: 417, 419: 418, 420: 419, 421: 420, 422: 421, 423: 422, 424: 423, 425: 424, 426: 425, 427: 426, 428: 427, 429: 428, 430: 429, 431: 430, 432: 431, 433: 432, 434: 433, 435: 434, 436: 435, 437: 436, 438: 437, 439: 438, 440: 439, 441: 440, 442: 441, 443: 442, 444: 443, 445: 444, 446: 445, 447: 446, 448: 447, 449: 448, 450: 449, 451: 450, 452: 451, 453: 452, 454: 453, 455: 454, 456: 455, 457: 456, 458: 457, 459: 458, 460: 459, 461: 460, 462: 461, 463: 462, 464: 463, 465: 464, 466: 465, 467: 466, 468: 467, 469: 468, 470: 469, 471: 470, 472: 471, 473: 472, 474: 473, 475: 474, 476: 475, 477: 476, 478: 477, 479: 478, 480: 479, 481: 480, 482: 481, 483: 482, 484: 483, 485: 484, 486: 485, 487: 486, 488: 487, 489: 488, 490: 489, 491: 490, 492: 491, 493: 492, 494: 493, 495: 494, 496: 495, 497: 496, 498: 497, 499: 498, 500: 499}
       ```
   
      c. Mapping indexing ke user_id
      ```python
      user_encoding_to_user = {i: x for i, x in enumerate(user_list)}
        print("Berhasil melakukan encoding angka ke user_id!")
        print("Contoh mapping index ke user_id:")
        
        #tampilan
        for i in list(user_encoding_to_user.items())[:5]:
            print(f"Index {i[0]} → user_id {i[1]}")
      ```
  
      output :
      ```
      Berhasil melakukan encoding angka ke user_id!
        Contoh mapping index ke user_id:
        Index 0 → user_id 1
        Index 1 → user_id 2
        Index 2 → user_id 3
        Index 3 → user_id 4
        Index 4 → user_id 5
      ```
  
      Berdasarkan output diatas, proses encoding untuk ``user_id`` berhasil dilakukan.
  
      
    
      Tahap 2 : Encoding ``product``
  
      Pada tahap ini dilakukan proses encoding terhadap kolom `product` agar dapat digunakan dalam model yang hanya menerima input numerik. Langkah pertama yaitu mengambil seluruh nilai unik dari kolom `product` dan menyimpannya dalam bentuk list menggunakan `.unique().tolist()`. Daftar produk yang dihasilkan kemudian ditampilkan sebagai output. Setelah itu, setiap produk diberi nilai indeks numerik menggunakan `enumerate`, dan hasil encoding ini disimpan dalam dictionary dengan format seperti `'Garlic Oil - Vegetarian Capsule 500 mg': 0`, `'Water Bottle - Orange': 1`, dan seterusnya. Proses ini mengubah nama produk menjadi angka. Selanjutnya, dilakukan mapping sebaliknya dari indeks ke nama produk untuk keperluan interpretasi hasil. Output dari mapping ini juga ditampilkan sebagian untuk menunjukkan bahwa encoding telah dilakukan dengan benar, misalnya “Index 0 → produk : Garlic Oil - Vegetarian Capsule 500 mg”.

      a. Mengambil semua nilai unik dari kolom 'product' dan menyimpannya dalam bentuk list
      ```python
      produk_list = df_products_copy['product'].unique().tolist()
      print('Daftar produk list :', produk_list)
      ```
  
      output :
      ```
      Daftar produk list : ['Garlic Oil - Vegetarian Capsule 500 mg', 'Water Bottle - Orange', 'Brass Angle Deep - Plain, No.2', 'Cereal Flip Lid Container/Storage Jar - Assorted Colour', 'Creme Soft Soap - For Hands & Body', 'Germ - Removal Multipurpose Wipes', 'Multani Mati', 'Hand Sanitizer - 70% Alcohol Base', 'Biotin & Collagen Volumizing Hair Shampoo + Biotin & Collagen Hair Conditioner', 'Scrub Pad - Anti- Bacterial, Regular', 'Wheat Grass Powder - Raw', 'Butter Cookies Gold Collection', 'Face Wash - Oil Control, Active', 'Mold & Mildew Remover with Bleach', 'Just Spray - Mosquito Repellent Room Spray', 'Dove Plastic Soap Case - Assorted Colour', 'Smooth Skin Oil - For Dry Skin', 'Salted Pumpkin', 'Flax Seeds - Roasted', 'Organic Tofu - Soy Paneer', 'Ceramic Barrel Brush - Colour May Vary', 'Instant Noodles - Chicken Satay Flavor', 'Chia Seeds', 'Cleanse Green Tea - Whole Leaf Loose Tea', 'Veggie Cutter', 'Insulated Hot Fresh Casserole For Roti/Chapati - White', 'Granola - Happy Berries', 'Flaxseed - Pesticide Free', 'Paratha Puff', 'Lip Butter - Rose', 'Fruit Power - Masala Sugarcane', 'Chocobakes Choc Filled Cookies', 'Amber - Deodorant Body Spray', 'Green Tea - Tulsi Loose Leaf', 'Pet Solitaire Container Set - Silver', 'Dhania - Dal', 'Pudina Chutney Masala', 'Bodylicious Deodorant Spray - Mate (For Men)', 'Sport Deo Spray - Fresh, for Men', 'Choco Deck - Mini Delights', 'Eau De Toilette - Homme Green', 'Lemon & Tea Tree Oil Soap', 'Flavoured Cream Wafer Roll - Strawberry', 'Storage/Lunch Steel Container with PP Lid - Red', 'Plain Green Olives', 'Quinoa - Organic', 'After Shave Splash - Arctic Ice', 'Colour Catcher Sheets', 'Sauce - Sweet & Sour', 'Super Hot and Sweet Mango Chutney', 'Pani Puri Mix Paste', 'Peach Syrup', 'Acne & Oil Control Face Wash', 'Choco Deck - French Dessert Inspired Layered Bar', 'Extra Fine Green Peas', 'Soothing Cucumber Facial Scrub With Apricot Seeds', 'Foochka', 'Argan-Liquid Gold Hair Spa', 'Baby Bed Protector - Sublimation Print, Pink', 'Corporate Planner Diary With Premium PU Leather Cover With Card Holder', 'Atta Chalan - Stainless Steel, Size- No.8', 'Dog Supplement - Absolute Skin + Coat Tablet', 'Peanut Butter - Creamy, Super', 'Sugar Free Petit Beurre - The Taste of France', 'Aqua Halo Rejuvenating Conditioner', 'Ayurvedic Anti-Tan Face Pack', 'Dog Supplement - Absolute Calcium Tablet', 'Battery Power Kids Toothbrush - Barbie', 'Organic Carom Seeds/Ajwain/Om Kalu', 'Padded Harness - 3/4 inch, Grey Colour', 'Kids Motu Patlu Toothpaste - 2-5 Years, Bubble Fruit Flavour', 'Pure & Gentle Face Wash', 'Sesame Seed Oil', 'Til Dil Seeds', 'Penta Plastic Pet Water Bottle - Green, Wide Mouth', 'Acne Pimple Kit For Acne & Pimple Removal', 'Disposable Bamboo Wood Skewer/Picker Sticks- For Barbeque, 12 Inch', '& Moms Bathing Soap - Jasmine', 'Amla Chatpata Dry Fruit', 'Toothbrush Superhero Assorted, Batman/Spiderman', 'Chips - Topica', 'Cup a Soup - Croutons Cream of Asparagus', 'Organic Dal - Masoor', 'Strawberry Ice Cream', 'Exo Dishwash Bar- Round 700 gm Box + Pril Dishwash Liquid- Active 2X Lime 225 ml', 'Jupiter Water/Juice Glass Tumbler', 'Cheese - Feta Greek, Block', 'Avida 3-in-1 Semi Economy Pouch -  FG01248', 'Bathing Soap - Sandal & Turmeric', 'Sweet Corn Kernels - Chipotle', 'Ashwagandha Tablets', 'Hard Anodised Ezee-Pour Saucepan With Lid - L88', 'Topp Up Milk - Elaichi', 'Namkeen - Madras Mixture', 'Stainless Steel Storage Lunch Container - Flat, Carry Snack Pack', 'Oceans Deodorant for Men - Long Lasting & Fresh Aquatic Fragrance', 'Hair Remover Spray - Foam Lemon', 'Mr. Magic Powder-To-Liquid Germ Protection Handwash Empty Bottle + Refill', 'Frankincense Oil', 'Wonder Diaper Pants - Xtra Large, 12-17 Kg', 'Samrakshana Vaastu Deepa Thailam', 'Quinoa - Organic Black', 'Fructis Serum - Long & Strong', 'Citrus Blast Orange Lemon Soap Free Body Wash', 'Veda Marie Light Biscuits', '2 Fold Umbrella - Auto-Open & Manual Close, Dark Violet', 'Aamras Mango Fruit Juice', 'Henna & Ginseng Anti Hair Loss Shampoo', 'Sandwich Toaster - Non-Stick, Gas', 'Baby Cereal - Ragi Almond & Banana, 6-8 Months, No Preservatives, No Artificial Colours', 'Incense Sticks - Sandal', 'SPF 15 Sunscreen Lotion', 'Fenugreek', 'Caramel Popcorn - Himalayan Salt', 'Cold Pressed Bhringraj Cooling Oil For Hair Fall & Damage Control', 'Sapota - Organically Grown', 'Spiced Tea - Blend Of 7 Refreshing Spices', 'Steel Bowl/Vati/Katori - No. 4, Chutney', 'Adult Dry Cat Food - +1 Year, Ocean Fish', 'Millet Rusk - Sweet', 'Stainless Steel Kadai - Induction Bottom With Glass Lid,  26 cm', 'Power Pocket - Long Lasting Bathroom Fragrance, Berry Rush', 'Cabbage - Red', 'Marvel Spiderman 2-In-1 Snackeez Bottle With Snack Box', 'Refined Oil - Rice Bran (Natural Oryzanol & Vitamin E)', 'Premium Square Plastic Container - Green', 'Instant Popcorn - Butter Delite', 'Cherry Lip Balm 4.5 g + Deep Nourish Elbow & Foot Cream 50 g', 'Nutrition Plus Health Supplement - Joint Support', 'Glass Belleza Bowl - Wine', 'Dark Fantasy - Choco Fills Biscuits - Cookies', 'Banana - Red', 'Chilli\xa0- Bajji, Mild', 'I Love You Fruit N Nut Chocolate', 'Pitted Green Olives', 'Glass Mixing Bowl With Lid - Polo', 'Cake Gel', 'Toffees - Excellence Assorted', 'Organic Idly Podi - Ginger', 'Glass Water Bottle - Aquaria Organic Purple', 'Stainless Steel Pav Bhaji/Idli Oval Shaped Plate', 'Organic Cow Ghee/Tuppa', 'Dates/Kharjura - Deseeded', 'Chutney - Sweet Mango Sliced (without Garlic)', 'Turmeric Powder/Arisina Pudi', 'Bread - Fruit', 'Bombay Street Food Spice Blend', 'Ragi Flakes', 'Mustard Oil - Cold Pressed', 'Juice/Water Glass - Long Drink Nord', 'Glass Amaze Air Tight Jar - Pink', 'Finger Brush For Kids - Blue, Ultra Soft', 'Water/Juice Glass  - Jupiter Long Glass', 'Energy Bar - Choco Crunch', 'Breeze - Razor Blades', 'Confeito Vermicelli Combo, Sprinkles', 'Olive Oil - Classic', 'Octa Plastic Pet Water Bottle - Light Blue, Narrow Mouth', 'Skin Cream', 'One Touch Air Purifier Freshener - Floral Bouquet Refill', 'Water/Juice Glass', 'Color Naturals Creme Riche Ultra Hair Color - Raspberry Red', 'Nomarks - Antimarks Soap For Oily Skin', 'Silver Needles Tulsi White Tea Bags - Rich In Antioxidants, Pure Tea Buds', 'Baby Napkins - Mini Terry', 'Printed Fabric Pencil Pouch - Purple, BB1263DPPL', 'Snacks - Roasted Mixture Lime', 'Organic Dosa Mix - Jowar', 'Lunch Box/Tiffin Set - Green BB 570 2', 'BCAA Energy Drink - Berry Flavour', 'Coffee Energizing Face Scrub', 'Pain Relief - Oil', 'Ultra Soft New Born Diapers - Extra Small', 'Jungle Stimulating Facial Cleanser', 'Ylang Ylang Essential Oil', 'Clear Glycerine Soap - Natural Toning (Tea Tree Oil & Honey)', 'Soap', 'Yellow Balm', 'LED Bulb - 12 Watt, Cool Daylight, B22 Base', 'Coriander Leaves 100 g + Garlic 250 g + Ginger 250 g + Chilli Green Long 250 g', 'Jaggery/Bella Powder - Pesticide Free', 'Ready Masala - Kashmiri Meat', 'Water Saving Aerator, Switch', 'Lemongrass Anti-Pigmentation Massage Cream', 'Breakfast Mix - Finger Millet Ragi Idli', 'Herbal Wine Grapefruit Lip Balm', 'Masala Upma', 'Maharishi Ayurveda Ayush Kwath', 'Svachh Nakshtra Steel Inner Lid Pressure Cooker (20257)', 'Chicken Liver Gourmet Loaf With Pumpkin - Super Food', 'Bath & Body Oil - Oriental Spicy Rose', 'Specialist Skin Care Oil - Scars, Stretch Mark, Ageing, Uneven Skin Tone', 'Brioche', 'Onion - Rings', 'Cotton Mop With Telescopic Handle 150 Cm', 'Kale', 'Notebook - Unruled, Long', 'Instant Noodles - Soy & Vinegar', 'Gluten-Free Quinoa Flour', 'Chikki, Peanut Bar', '1001 Nights Concentrated Oriental Perfume Free From Alcohol For Unisex', 'Man - Indigo Body Mist', 'Fields Of Gold Organic Cumin - Whole', 'Body Massage Oil - Energising', 'Synthetic Food Colour Preparation Lemon Yellow', 'Toothpaste - Gum Care, Expert Protection', 'Bio Myristica Spot Correcting Anti Acne Face Pack', 'Stainless Steel Frying Ladle - No. 9, Silvera', 'OvenOrg Multi Millet Rusk', 'Mahabhringraj Tel - Hairfall Reduction & Dandruff Control', 'Masterchefs Germ Protection Liquid Handwash Refill', 'Black Naturals Hair Colour Shade 1-Deep Black 20 ml + 20 gm', 'Apple Cider Vinegar - Raw Unfiltered Unpasteurized with Cinamon & Honey', 'Brinjal - Varikatri, Organically Grown', 'Wonderz Milk Shakes - Classic Vanilla', 'Marie Light Biscuits - Oats Fibre', 'Masala - Chicken', 'Dark Chocolate- 55% Rich In Cocoa', 'Gentle Baby Wipes', 'Avocado', 'Plastic Dustbin - Beige', 'Pineapple - Chunks, Single Serve', 'Jeera Powder', 'Pure Neem Skin Purifying Face Wash', 'Lemon - Organically Grown', 'Lavender & Vanilla Handmade Luxury Soap', 'Stainless Steel Pressure Cooker - Steeltuff, Induction Base, Silver', 'Steel Deep Dabba/Storage Container - No. 12, Plain', 'Chyawan Fit Sugarfree Chyawanprash - Natural Immunity Booster', 'Morning Dew Perfumed Talc 250 g + English Lavender Perfumed Talc 250 g', 'Energy Bars - Nutty, 4+ Years, 100% Natural & Healthy', 'Banana Stem - Diced', 'Chilli Flakes', 'Bite & Sip Flask And Lunch Box/Tiffin Box - Green Colour', 'Namkeen - Khara Boondi', 'Raw Seeds - Sunflower Pumpkin Flax Seeds', 'Garnet LED White Bulb - 14 Watt, Cool Day, B22', 'Tempeh Cubes - Simply Sriracha Soyabean', 'Green Tea Gentle Detox Set', 'Fresh Catch Fish Fingers', 'Sour Cream & Onion', 'Xylitol Powder', 'Sixer Biscuits - Salted', 'Gokshuradi Guggulu - Urinary Disorders, 500mg', 'Peach Shine Lip Care', 'Skincare Hand Wash Refill', '4mm Aluminium Induction Base Chapati Roti Tawa - Silver', 'Mix - Rava Idli', 'Impress Concentrated Perfume Free From Alcohol For Male', 'Skin Awakening Rinse', 'Pacific Steel Insulated Vacuum Flask', 'Regenerist - Advanced Anti-Ageing Revitalising Hydration Skin Cream Moisturizer SPF 15', 'Cotton Swabs', 'Tropical Fruit Pudding - Lychee, Mango, Strawberry Flavoured', 'Pippali Fruit Powder - Supports Healthy Digestive & Immune System', 'Salt & Peeper Shaker Masala Dabbi With Window', 'Organic - Triphala Powder', 'Aeda Glycerine Bathing Bar - Natural Green', 'Chicken Cocktail Sausage', 'Sun Expert Fairnes Sunscren Lotion SPF 30 PA++', 'Cotton Pads', 'Ashwagandha Powder', 'Frozen - Mixed Vegetables', 'Masala - Kitchen', 'Mustard/Sasive/Rai - Big', 'Ayurvedic Soap', 'Glass Matt Finish Bottle With Plastic Cap - Blue, BB1324', 'Perfume - Youth Dew EDP Spray', 'Organic Idly - Oats', 'Red Curry', 'Hareli Kitchen Jar', 'Heavy Starch - Lemon Fresh Scent', 'United Dreams Go Far Eau De Toilette', 'Ayurvedic Jamun Powder', 'So Soft 2 Ply Face Tissue Box', 'Pomegranate - Single Serve, Peeled', 'Stevia Spoonable - Powder', 'Toor/Arhar Dal', "Peristaltic Nipple - 'S' Hole", 'Fragrance Body Spray - Cool Blue', 'Vitamin C Brightening Peel Off Mask', 'Almond & Rose Soap Value Pack', 'Yippee Noodles - Magic Masala', 'Fields Of Gold Organic Foxtail Millet', 'Wood - Centre Filled Bar Infused With Dark Mousse, Cinnamon & Coffee', 'Basil Seed Drink - Orange', 'Solution Anti Blackhead/Whitehead Masksheet (Pack of 10)', 'Acno Fight Pimple Clearing Gel', 'Pork Classic Salami', 'Gold Flash - Mosquito Repellent Combo Machine & Refill', 'Stainless Steel Airtight Storage Container - SL-1401', 'Whisky Cocktail Mixers - 100% Natural', 'Family Sunscreen Lotion SPF 25', 'Japanese Cooking Rice-Wine', 'Coated Green Peas - Wasabi', 'Charminar Basmati Rice/Basmati Akki - Select', 'Hide & Seek Choco Rolls', 'Hair Fall Control Kit - Oil, Shampoo & Serum', 'Anti-Acne Face Cleanser - With Salyclic Acid, For Oily Skin', 'Gluten-Free Moong Dal Cheela/Dosa Mix', 'Milk Boiler - Aluminium', 'Green Tea - Pure, Bio-Degradable', 'Cube Storage Glass Jar', 'M1 Perfume Spray - For Men', 'Tulsi Mulethi Green Tea', 'Nicer Dicer', 'Masala - Punjabi Chhole', 'Pork - Fresh Bacon, Sliced', 'Active Salt Toothpaste Saver Pack 300g + Sensitive Soft Bristles Toothbrush 4pcs', 'Silicone Feeding Nipple/Teat Regular Neck - Size XL', 'Microwaveable Plastic Multiutility Bowl - Yellow, New Coral, L2272 YL', 'Chicken Jalapeno Cheese Nuggets', 'Milk Delights Face Wash With Honey For Dry Skin', 'Instaglow Oxygen Bleach', 'Soft Drink - Lime Flavoured', 'Coffee Creamer - Coffee-Mate', 'Royce Premium High Quality Pedal Plastic Dustbin / Garbage Bin - Blue', 'Khaas Shampoo Bar - Heena Amla', 'Bubble Glass', 'Dazzle Livid Lilac Dinner Se.....
      ```
  
    
      b. Melakukan encoding product
      ```pythom
      produk_encoding ={x: i for i, x in enumerate(produk_list)}
      print('Hasil encoding : ', produk_encoding)
      ```
  
      output :
      ```
      Hasil encoding :  {'Garlic Oil - Vegetarian Capsule 500 mg': 0, 'Water Bottle - Orange': 1, 'Brass Angle Deep - Plain, No.2': 2, 'Cereal Flip Lid Container/Storage Jar - Assorted Colour': 3, 'Creme Soft Soap - For Hands & Body': 4, 'Germ - Removal Multipurpose Wipes': 5, 'Multani Mati': 6, 'Hand Sanitizer - 70% Alcohol Base': 7, 'Biotin & Collagen Volumizing Hair Shampoo + Biotin & Collagen Hair Conditioner': 8, 'Scrub Pad - Anti- Bacterial, Regular': 9, 'Wheat Grass Powder - Raw': 10, 'Butter Cookies Gold Collection': 11, 'Face Wash - Oil Control, Active': 12, 'Mold & Mildew Remover with Bleach': 13, 'Just Spray - Mosquito Repellent Room Spray': 14, 'Dove Plastic Soap Case - Assorted Colour': 15, 'Smooth Skin Oil - For Dry Skin': 16, 'Salted Pumpkin': 17, 'Flax Seeds - Roasted': 18, 'Organic Tofu - Soy Paneer': 19, 'Ceramic Barrel Brush - Colour May Vary': 20, 'Instant Noodles - Chicken Satay Flavor': 21, 'Chia Seeds': 22, 'Cleanse Green Tea - Whole Leaf Loose Tea': 23, 'Veggie Cutter': 24, 'Insulated Hot Fresh Casserole For Roti/Chapati - White': 25, 'Granola - Happy Berries': 26, 'Flaxseed - Pesticide Free': 27, 'Paratha Puff': 28, 'Lip Butter - Rose': 29, 'Fruit Power - Masala Sugarcane': 30, 'Chocobakes Choc Filled Cookies': 31, 'Amber - Deodorant Body Spray': 32, 'Green Tea - Tulsi Loose Leaf': 33, 'Pet Solitaire Container Set - Silver': 34, 'Dhania - Dal': 35, 'Pudina Chutney Masala': 36, 'Bodylicious Deodorant Spray - Mate (For Men)': 37, 'Sport Deo Spray - Fresh, for Men': 38, 'Choco Deck - Mini Delights': 39, 'Eau De Toilette - Homme Green': 40, 'Lemon & Tea Tree Oil Soap': 41, 'Flavoured Cream Wafer Roll - Strawberry': 42, 'Storage/Lunch Steel Container with PP Lid - Red': 43, 'Plain Green Olives': 44, 'Quinoa - Organic': 45, 'After Shave Splash - Arctic Ice': 46, 'Colour Catcher Sheets': 47, 'Sauce - Sweet & Sour': 48, 'Super Hot and Sweet Mango Chutney': 49, 'Pani Puri Mix Paste': 50, 'Peach Syrup': 51, 'Acne & Oil Control Face Wash': 52, 'Choco Deck - French Dessert Inspired Layered Bar': 53, 'Extra Fine Green Peas': 54, 'Soothing Cucumber Facial Scrub With Apricot Seeds': 55, 'Foochka': 56, 'Argan-Liquid Gold Hair Spa': 57, 'Baby Bed Protector - Sublimation Print, Pink': 58, 'Corporate Planner Diary With Premium PU Leather Cover With Card Holder': 59, 'Atta Chalan - Stainless Steel, Size- No.8': 60, 'Dog Supplement - Absolute Skin + Coat Tablet': 61, 'Peanut Butter - Creamy, Super': 62, 'Sugar Free Petit Beurre - The Taste of France': 63, 'Aqua Halo Rejuvenating Conditioner': 64, 'Ayurvedic Anti-Tan Face Pack': 65, 'Dog Supplement - Absolute Calcium Tablet': 66, 'Battery Power Kids Toothbrush - Barbie': 67, 'Organic Carom Seeds/Ajwain/Om Kalu': 68, 'Padded Harness - 3/4 inch, Grey Colour': 69, 'Kids Motu Patlu Toothpaste - 2-5 Years, Bubble Fruit Flavour': 70, 'Pure & Gentle Face Wash': 71, 'Sesame Seed Oil': 72, 'Til Dil Seeds': 73, 'Penta Plastic Pet Water Bottle - Green, Wide Mouth': 74, 'Acne Pimple Kit For Acne & Pimple Removal': 75, 'Disposable Bamboo Wood Skewer/Picker Sticks- For Barbeque, 12 Inch': 76, '& Moms Bathing Soap - Jasmine': 77, 'Amla Chatpata Dry Fruit': 78, 'Toothbrush Superhero Assorted, Batman/Spiderman': 79, 'Chips - Topica': 80, 'Cup a Soup - Croutons Cream of Asparagus': 81, 'Organic Dal - Masoor': 82, 'Strawberry Ice Cream': 83, 'Exo Dishwash Bar- Round 700 gm Box + Pril Dishwash Liquid- Active 2X Lime 225 ml': 84, 'Jupiter Water/Juice Glass Tumbler': 85, 'Cheese - Feta Greek, Block': 86, 'Avida 3-in-1 Semi Economy Pouch -  FG01248': 87, 'Bathing Soap - Sandal & Turmeric': 88, 'Sweet Corn Kernels - Chipotle': 89, 'Ashwagandha Tablets': 90, 'Hard Anodised Ezee-Pour Saucepan With Lid - L88': 91, 'Topp Up Milk - Elaichi': 92, 'Namkeen - Madras Mixture': 93, 'Stainless Steel Storage Lunch Container - Flat, Carry Snack Pack': 94, 'Oceans Deodorant for Men - Long Lasting & Fresh Aquatic Fragrance': 95, 'Hair Remover Spray - Foam Lemon': 96, 'Mr. Magic Powder-To-Liquid Germ Protection Handwash Empty Bottle + Refill': 97, 'Frankincense Oil': 98, 'Wonder Diaper Pants - Xtra Large, 12-17 Kg': 99, 'Samrakshana Vaastu Deepa Thailam': 100, 'Quinoa - Organic Black': 101, 'Fructis Serum - Long & Strong': 102, 'Citrus Blast Orange Lemon Soap Free Body Wash': 103, 'Veda Marie Light Biscuits': 104, '2 Fold Umbrella..
      ```
      
      c. Mapping indexing kembali ke product
      ```python
      produk_encoding_to_produk = {i: x for i, x in enumerate(produk_list)}
      print("Berhasil melakukan encoding angka ke product!")
      print("Contoh mapping index ke product :")
      
      #tampilan
      for i in list(produk_encoding_to_produk.items())[:5]:
          print(f"Index {i[0]} → produk : {i[1]}")
      ```
  
      output :
  
      ```
      Berhasil melakukan encoding angka ke product!
      Contoh mapping index ke product :
      Index 0 → produk : Garlic Oil - Vegetarian Capsule 500 mg
      Index 1 → produk : Water Bottle - Orange
      Index 2 → produk : Brass Angle Deep - Plain, No.2
      Index 3 → produk : Cereal Flip Lid Container/Storage Jar - Assorted Colour
      Index 4 → produk : Creme Soft Soap - For Hands & Body
      ```

      Tahap 3 : mengubah nilai kategori (userID dan product) menjadi bentuk numerik (encoded)
        ```
        # Mapping user_id asli ke angka
         df_products_copy['user'] = df_products_copy['user_id'].map(user_encoding)
         
         # Mapping product ke angka
         df_products_copy['produk'] = df_products_copy['product'].map(produk_encoding)
        ```

      Pada tahap ini, nilai-nilai kategorikal dari kolom `user_id` dan `product` diubah ke dalam bentuk numerik berdasarkan hasil encoding yang telah dibuat sebelumnya. Proses ini dilakukan dengan menggunakan fungsi `.map()` untuk mencocokkan setiap nilai `user_id` dengan nilai numerik yang sesuai di dalam dictionary `user_encoding`, lalu hasilnya disimpan ke dalam kolom baru bernama `user`. Hal serupa juga diterapkan untuk kolom `product`, yang dipetakan menggunakan dictionary `produk_encoding` dan disimpan dalam kolom baru bernama `produk`. Dengan demikian, dataset kini memiliki representasi numerik dari kedua kolom tersebut, sehingga dapat digunakan sebagai input ke model machine learning tanpa kendala.

      
      Tahap 4 : cek hasil
      ```python
      users_count = len(user_encoding_to_user) # jumlah user
      produk_count = len(produk_encoding_to_produk) # jumlah produk
      low_rating = min(df_products_copy['rating']) # rating terendah
      top_rating = max(df_products_copy['rating']) # rating tertinggi
      
      print('Total user: {}'.format(users_count))
      print('Total produk: {}'.format(produk_count))
      print('Rating terendah: {}'.format(low_rating))
      print('Rating tertinggi: {}'.format(top_rating))
      ```

      output :
      ```
      Total user: 500
      Total produk: 23449
      Rating terendah: 1.0
      Rating tertinggi: 5.0
      ```
      

7. Train & Test Split
   
  * Tahap 1 : Mengacak Dataset
     Data perlu diacak sebelum di-split karena kita ingin memastikan bahwa data latih (training set) dan data uji (testing set) mewakili distribusi data secara umum, bukan urutan tertentu yang bisa mempengaruhi hasil model.
    
     ```python
     df_products_copy = df_products_copy.sample(frac=1, random_state=69)
      df_products_copy
     ```
    
  * Tahap 2 : Membuat variabel fitur (independen) ``x``, yang berisi pasangan antara user dan produk.
     Pada tahapan ini, dilakukan proses pemisahan data menjadi variabel input dan output. Variabel x dibuat dengan mengambil kolom user dan produk dari dataframe df_products_copy, yang kemudian dikonversi menjadi array. Tujuan dari proses ini adalah untuk menggabungkan data pengguna dan produk dalam satu bentuk yang dapat digunakan sebagai fitur input oleh model machine learning.
      ```python
      x = df_products_copy[['user', 'produk']].values
      ```
    
  * Tahap 3 : Melakukan normalisasi rating menggunakan teknik Min-Max Scaling agar berada dalam rentang 0 sampai 1

    Pada baris kode ``y = df_products_copy['rating'].apply(lambda x: (x - low_rating) / (top_rating - low_rating)).values``, dilakukan proses normalisasi terhadap data rating. Normalisasi ini bertujuan untuk mengubah skala nilai rating menjadi rentang antara 0 hingga 1. Hal ini dilakukan agar setiap nilai rating memiliki bobot yang seimbang saat digunakan oleh model pembelajaran mesin. Berikut untuk rumusnya :
    
      ```python
      y = df_products_copy['rating'].apply(lambda x: (x - low_rating) / (top_rating - low_rating)).values
      ```

  * Tahap 4 : Membagi data menjadi data latih (training data) dan data validasi (validation data)

    ```
    split_data = int(0.8 * df_products.shape[0]).
      x_train, x_val, y_train, y_val = (
          x[:split_data],
          x[split_data:],
          y[:split_data],
          y[split_data:]
      )
      
      # Menampilkan jumlah data latih dan data validasi
      print(f"Jumlah data latih: {len(x_train)}")
      print(f"Jumlah data validasi: {len(x_val)}")
    ```

    output :
    ```
    Jumlah data latih: 21669
      Jumlah data validasi: 5418
    ```
         

## Modeling

Pada tahap modeling, sistem rekomendasi dikembangkan menggunakan dua pendekatan algoritmik yang berbeda, yaitu Content-Based Filtering (CBF) dan Collaborative Filtering (CF). Kedua pendekatan ini dipilih untuk memberikan solusi yang saling melengkapi dalam merekomendasikan produk kepada pengguna.

1. Content-Based Filtering
   
   Content-Based Filtering merupakan metode dalam sistem rekomendasi yang memberikan saran produk kepada pengguna dengan mempertimbangkan karakteristik dari item yang sebelumnya mereka minati. Pendekatan ini mengandalkan analisis terhadap fitur produk serta preferensi pengguna untuk menghasilkan rekomendasi yang relevan. Karena tidak memerlukan banyak data interaksi antar pengguna dan item, metode ini sangat cocok digunakan dalam situasi dengan data interaksi yang terbatas. Pendekatan ini juga populer di berbagai bidang karena kemampuannya dalam menyajikan rekomendasi yang bersifat personal dengan menitikberatkan pada informasi konten produk, bukan perilaku pengguna lain.
   
   **Kelebihan Content-Based Filtering**
   
   * **Personal**: Rekomendasi yang diberikan sangat relevan dengan preferensi individu pengguna.
   * **Tidak tergantung pada data pengguna lain**: Tetap bisa bekerja meski hanya ada satu user (cocok untuk skenario cold-start user).
   * **Transparan**: Lebih mudah menjelaskan alasan mengapa sebuah item direkomendasikan (berdasarkan fitur yang mirip).
   
   **Kekurangan Content-Based Filtering**
   
   * **Over-specialization**: Cenderung merekomendasikan item yang mirip terus-menerus, sehingga sulit mengenalkan variasi atau eksplorasi item baru.
   * **Butuh representasi fitur yang baik**: Kualitas rekomendasi sangat bergantung pada seberapa baik atribut item direpresentasikan.
   * **Tidak belajar dari pengguna lain**: Sistem tidak memanfaatkan pola kolektif atau tren umum antar pengguna.

	Berikut merupakan tahapan dalam membangun model content based filtering :
	
	**Tahap 1 :** Pembuatan Matriks TF-IDF
	```python
	tfidf_matrix
	```
	
	output :
	
	```
	<Compressed Sparse Row sparse matrix of dtype 'float64'
		with 177283 stored elements and shape (27087, 3079)>
	```
	
	**Tahap 2:** Perhitungan Cosine Similarity

	Mengukur tingkat kemiripan antar produk berdasarkan hasil matriks TF-IDF. Semakin tinggi nilainya, semakin mirip dua produk tersebut.

	```python
	cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
	cosine_sim
	```
	
	output :
	```
	array([[1.        , 0.        , 0.        , ..., 0.        , 0.        ,
	        0.05562645],
	       [0.        , 1.        , 0.        , ..., 0.        , 0.        ,
	        0.        ],
	       [0.        , 0.        , 1.        , ..., 0.        , 0.        ,
	        0.        ],
	       ...,
	       [0.        , 0.        , 0.        , ..., 1.        , 0.        ,
	        0.        ],
	       [0.        , 0.        , 0.        , ..., 0.        , 1.        ,
	        0.        ],
	       [0.05562645, 0.        , 0.        , ..., 0.        , 0.        ,
	        1.        ]])
	```
	
	**Tahap 3 :** Pembuatan Indeks Produk
   
	 Membuat indeks berdasarkan nama produk agar proses pencarian dan pemetaan produk lebih cepat dan efisien.

	```python
	produk_name = df_cbf['product']
	indeks_produk = pd.Series(df_cbf.index, index=df_cbf['product'])
	indeks_produk
	```

 	output :

	| product                                                              |
	|----------------------------------------------------------------------|
	| Garlic Oil - Vegetarian Capsule 500 mg                               | 0
	| Water Bottle - Orange                                                | 1
	| Brass Angle Deep - Plain, No.2                                       | 2
	| Cereal Flip Lid Container/Storage Jar - Assorted Colour              | 3
	| Creme Soft Soap - For Hands & Body                                   | 4
	| ...                                                                  | ...
	| Wottagirl! Perfume Spray - Heaven, Classic                           | 27082
	| Rosemary                                                             | 27083
	| Peri-Peri Sweet Potato Chips                                         | 27084
	| Green Tea - Pure Original                                            | 27085
	| United Dreams Go Far Deodorant                                       | 27086
	
	27087 rows × 1 columns
  
	
	**Tahap 4 :** Fungsi Rekomendasi Produk
   
  	 Membangun fungsi yang mengembalikan daftar produk yang paling mirip dengan produk yang diminta berdasarkan skor kemiripan tertinggi.
   
	```python
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
	```
	
	**Tahap 5 :** Pemilihan Produk Uji Coba Secara Acak
   
   M	emilih salah satu produk dari dataset sebagai input simulasi permintaan user untuk menguji sistem rekomendasi.
	
	```python
	# Nama produk yang diminta user (dipilih secara acak dari daftar produk)
	nama_produk_diminta = np.random.choice(produk_name.unique())
	nama_produk_diminta
	```
	
	output :

	```
	 I Love You Dark Almond Chocolate Bar, Dark Almond Flavour
	```
	Pada tahap ini, sistem secara acak memilih satu nama produk dari daftar produk_name, yaitu kumpulan nama produk yang tersedia dalam data. Produk ini berperan sebagai input permintaan pengguna yang akan digunakan untuk mencari rekomendasi produk-produk lain yang mirip.
	
	** Tahap 6 :** Menampilkan Hasil Rekomendasi Produk
   
	Menampilkan daftar produk yang paling relevan atau mirip dengan produk yang diminta oleh user, sebagai hasil akhir dari sistem rekomendasi.


	```python
	# Memanggil fungsi rekomendasi
	hasil_rekom = rekomendasi_produk(nama_produk_diminta)
	
	pd.DataFrame({
	    'Produk Diminta': [nama_produk_diminta] * len(hasil_rekom),
	    'Rekomendasi Produk yang Relevan': hasil_rekom
	})
	```
	
	output :

	 | Index | Produk Diminta                                              | Rekomendasi Produk yang Relevan                    |
	|-------|-------------------------------------------------------------|----------------------------------------------------|
	| 3386  | I Love You Dark Almond Chocolate Bar, Dark Almond...        | Butterscotch Chocolate Bar                         |
	| 3662  | I Love You Dark Almond Chocolate Bar, Dark Almond...        | Caramel Chocolate Bar                              |
	| 4097  | I Love You Dark Almond Chocolate Bar, Dark Almond...        | Caramel                                            |
	| 6173  | I Love You Dark Almond Chocolate Bar, Dark Almond...        | 70% Dark Hazelnut Chocolate Bar                    |
	| 6537  | I Love You Dark Almond Chocolate Bar, Dark Almond...        | Banoffee Pie                                       |
	| 8486  | I Love You Dark Almond Chocolate Bar, Dark Almond...        | Thank you Chocolate Bar, Dark                      |
	| 9183  | I Love You Dark Almond Chocolate Bar, Dark Almond...        | Happy Birthday Chocolate Bar                       |
	| 9716  | I Love You Dark Almond Chocolate Bar, Dark Almond...        | Mint Chocolate Bar                                 |
	| 11015 | I Love You Dark Almond Chocolate Bar, Dark Almond...        | Milk Marzipan                                      |
	| 11204 | I Love You Dark Almond Chocolate Bar, Dark Almond...        | Love You To The Moon And Back Signature Blend Bar  |


3. Collaborative Filtering

   Collaborative Filtering adalah pendekatan sistem rekomendasi yang menyarankan item kepada pengguna berdasarkan kesamaan preferensi dengan pengguna lain. Alih-alih menganalisis fitur item, metode ini memanfaatkan pola interaksi historis antar pengguna dan produk, seperti penilaian (rating) atau riwayat pembelian. Dengan mencari pengguna yang memiliki perilaku serupa, sistem dapat memperkirakan item mana yang kemungkinan disukai oleh pengguna target. Pendekatan ini efektif dalam menangkap hubungan tersembunyi antar item dan pengguna, namun memiliki tantangan dalam menghadapi pengguna atau produk baru yang belum memiliki cukup interaksi.
   
   **Kelebihan Collaborative Filtering**
   
   * **Menangkap pola kompleks**: Mampu menemukan hubungan yang tidak langsung antara pengguna dan item melalui data interaksi.
   * **Tidak butuh informasi konten**: Dapat bekerja hanya dengan data perilaku (misalnya rating), tanpa perlu tahu isi atau atribut produk.
   * **Mudah dikembangkan**: Cocok diterapkan di berbagai domain dengan data interaksi pengguna yang cukup besar.
   
   **Kekurangan Collaborative Filtering**
   
   * **Masalah cold-start**: Sulit memberikan rekomendasi pada pengguna baru atau item baru yang belum memiliki data interaksi.
   * **Ketergantungan pada jumlah data**: Akurasi rekomendasi sangat bergantung pada kelengkapan dan volume data historis.
   * **Rentan terhadap sparsity**: Jika matrix interaksi terlalu jarang (banyak nilai kosong), performa model bisa menurun secara signifikan.

     Berikut merupakan tahapan dalam membangun model Collaborative Filtering :

     **Tahap 1 :** Membangun Arsitektur Model Rekomendasi (RecommenderNet)
  
     Model RecommenderNet dibangun menggunakan TensorFlow Keras subclassing API. Model ini menggunakan layer embedding untuk merepresentasikan user dan produk dalam ruang vektor berdimensi kecil. Dot product dari vektor user dan produk digunakan untuk memprediksi skor interaksi di antara keduanya, ditambah bias user dan produk, lalu diberi aktivasi sigmoid.

     ```python
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
     ```
  
     **Tahap 2 :** Inisialisasi dan Kompilasi Model
  
      Model dikompilasi dengan:

        * Loss Function: BinaryCrossentropy, karena target yang digunakan adalah skor antara 0-1.
        * Optimizer: Adam, dengan learning_rate=0.001.
        * Metric Evaluasi: RootMeanSquaredError (RMSE) untuk memantau performa model selama training dan validasi.
          
     ```python
     # inisialisasi model
     model = RecommenderNet(users_count, produk_count, 50)

     # model compile
     model.compile(
     loss = tf.keras.losses.BinaryCrossentropy(),
     optimizer = keras.optimizers.Adam(learning_rate=0.001),
     metrics=[tf.keras.metrics.RootMeanSquaredError()]
     )
     ```
  
     **Tahap 3 :** Menyiapkan Callback Early Stopping

 	 Untuk mencegah overfitting dan menghemat waktu pelatihan, digunakan EarlyStopping yang menghentikan proses training jika validasi RMSE tidak membaik selama 10 epoch berturut-turut.
  
     ```python
     # callbacks
     from tensorflow.keras.callbacks import EarlyStopping
     early_stop = EarlyStopping(monitor='val_root_mean_squared_error',
                              patience=10,
                              verbose=1,
                              restore_best_weights=True)
     ```
  
     output :
     
     ```python
     Epoch 41/50
     2709/2709 ━━━━━━━━━━━━━━━━━━━━ 9s 3ms/step - loss: 0.5206 - root_mean_squared_error: 0.0273 - val_loss: 0.5820 - 
     val_root_mean_squared_error: 0.1538
     Epoch 41: early stopping
     Restoring model weights from the end of the best epoch: 31.
     ```
     
     **Tahap 4 :** Melatih Model dengan Data Pelatihan
     ```python
            # Memulai training
		history = model.fit(
		    x = x_train,
		    y = y_train,
		    batch_size = 8,
		    epochs = 50,
		    callbacks = [early_stop],
		    validation_data = (x_val, y_val)
		)
     ```

     **Tahap 5 :** Memilih satu user secara acak, lalu mengambil semua produk yang belum pernah diberi rating oleh user 
     tersebut
     
     ```python
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
     ```
     
     **Tahap 6 :** Memprediksi dan Menampilkan Hasil Rekomendasi
     
     ```python
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
     ```

     output :

     ```
               732/732 ━━━━━━━━━━━━━━━━━━━━ 2s 2ms/step
		Daftar rekomendasi produk untuk user 110
		------------------------------
		Produk dengan rating tertinggi dari user
		----------------------------------------
		Oil - Gingelly : raschekkuoil
		Syoss - Color Salon Protect Anti Fade, 02 Conditioner : schwarzkopf
		Premium Paraben Free Baby Wet Wipes With Aloe Vera : bodyguard
		Oil - Gingelly : moti's
		Oil - Gingelly : vvv
		Induction Ceramic - Dosa Tawa : nirlon
		Oil - Gingelly : moti's
		Oil - Gingelly : moti's
		Gold Massage Cream : naturesessence
		Oil - Gingelly : idhayam
		Oil - Gingelly : raschekkuoil
		--------------------------------
		Top 10 produk rekomendasi
		--------------------------------
		Man - Green Eau De Toilette Deodorant : nike
		Combo - Precision Safety Razor & 10 Feather Blades : bombayshavingcompany
		Charcoal Bath Soap : bombayshavingcompany
		Wonder Diaper Pants - Large Size : huggies
		Ayush Men Moisturiser : vlcc
		Sportivo Hair Styling Pomade Wax : themancompany
		Natural Body Spray & Fragrance Booster - Ice Dive, Developed With Athletes : adidas
		Original Eau De Toilette Deodorant - For Man : nike
		Body Deodorant - Ultra Sensual : wildstone
		Shea Butter Moisturizing Bath Soap With Coconut Husk & Honey - For Soft Skin : bombayshavingcompany
     ```

		Output di atas merupakan hasil dari model *Top-N Recommendation* berbasis **Collaborative Filtering**, di mana model memberikan rekomendasi produk kepada user berdasarkan **riwayat interaksi dan rating** yang pernah diberikan terhadap produk-produk tertentu.
		
		Pada contoh ini, model memberikan rekomendasi kepada **user dengan ID 110**. User ini sebelumnya telah memberikan rating tinggi terhadap beberapa produk, terutama dari jenis:
		
		* **Oil - Gingelly** dari berbagai brand seperti `raschakkuoil`, `moti's`, `vvv`, dan `idhayam`
		* **Produk perawatan pribadi** seperti `Syoss Conditioner`, `Baby Wet Wipes`, dan `Gold Massage Cream`
		* **Alat masak** seperti `Induction Ceramic - Dosa Tawa`
		
		Dari data tersebut terlihat bahwa user ini memiliki preferensi terhadap produk:
		
		* Kebutuhan rumah tangga (terutama minyak)
		* Produk perawatan tubuh dan kulit
		
		 **Top 10 Produk Rekomendasi**
		
		Model kemudian memberikan 10 produk rekomendasi yang dianggap **relevan dan sesuai** dengan minat user berdasarkan pola interaksi:
		
		| Produk Rekomendasi                                           | Brand                |
		| ------------------------------------------------------------ | -------------------- |
		| Man - Green Eau De Toilette Deodorant                        | nike                 |
		| Combo - Precision Safety Razor & 10 Feather Blades           | bombayshavingcompany |
		| Charcoal Bath Soap                                           | bombayshavingcompany |
		| Wonder Diaper Pants - Large Size                             | huggies              |
		| Ayush Men Moisturiser                                        | vlcc                 |
		| Sportivo Hair Styling Pomade Wax                             | themancompany        |
		| Natural Body Spray & Fragrance Booster - Ice Dive            | adidas               |
		| Original Eau De Toilette Deodorant - For Man                 | nike                 |
		| Body Deodorant - Ultra Sensual                               | wildstone            |
		| Shea Butter Moisturizing Bath Soap With Coconut Husk & Honey | bombayshavingcompany |
		
		 **Kesimpulan**
		
		Model berhasil **menyesuaikan rekomendasi** dengan preferensi user yang tertarik pada produk-produk perawatan pribadi dan rumah tangga. Hal ini terlihat dari mayoritas produk yang direkomendasikan berupa:
		
		* **Parfum, sabun, dan deodoran pria**
		* **Produk pelembab dan perawatan kulit**
		* **Produk dari brand yang populer di segmen grooming & skincare pria**
		
		Hasil ini menunjukkan bahwa **Collaborative Filtering** efektif dalam mengidentifikasi kesamaan pola antar user untuk menghasilkan rekomendasi yang personal dan relevan, bahkan tanpa melihat isi atau atribut produk secara eksplisit.


## Evaluation

Pada proyek sistem rekomendasi ini, dilakukan evaluasi terhadap dua pendekatan yang digunakan: **Content-Based Filtering** dan **Collaborative Filtering**. Masing-masing pendekatan dievaluasi menggunakan metrik yang sesuai dengan karakteristik model dan tujuan yang ingin dicapai.

### A. Content-Based Filtering

Untuk mengevaluasi performa model Content-Based Filtering, digunakan **metrik precision**. Precision dipilih karena fokus utama dari pendekatan ini adalah memberikan rekomendasi produk yang benar-benar relevan dengan preferensi pengguna berdasarkan konten atau atribut produk yang telah disukai sebelumnya.

Secara matematis, **precision** didefinisikan sebagai:

$$
\text{Precision} = \frac{\text{True Positives (TP)}}{\text{True Positives (TP)} + \text{False Positives (FP)}}
$$

Keterangan:

* **True Positives (TP)**: Jumlah produk yang direkomendasikan dan memang relevan bagi pengguna.
* **False Positives (FP)**: Produk yang direkomendasikan tetapi tidak relevan bagi pengguna.

**Kelebihan**:

* Fokus pada relevansi, sehingga cocok untuk personalisasi.
* Tidak bergantung pada interaksi pengguna lain (cocok untuk cold-start user).

**Keterbatasan**:

* Tidak mempertimbangkan item relevan yang tidak direkomendasikan (mengabaikan recall).
* Cenderung memberikan rekomendasi yang terlalu mirip (kurang eksploratif).

**Berikut merupakan fungsi evaluasi yang digunakan:**

   ```python
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
   ```

Fungsi ini membandingkan produk yang direkomendasikan dengan daftar relevansi aktual berdasarkan atribut konten dalam dataset. Produk dianggap relevan jika ada kemiripan konten dengan produk yang diminta, dan precision dihitung berdasarkan rasio antara jumlah produk relevan yang direkomendasikan terhadap total produk yang direkomendasikan.

**Hasil evaluasi menunjukkan bahwa:**

```python
Precision Content-Based Filtering untuk produk 'I Love You Dark Almond Chocolate Bar, Dark Almond Flavour': 1.00
```

Artinya, seluruh produk yang direkomendasikan oleh sistem berdasarkan kemiripan konten dinyatakan relevan dengan produk referensi yang diminta. Nilai precision sebesar 1.00 atau 100% menunjukkan bahwa model bekerja sangat baik dalam mengidentifikasi dan merekomendasikan produk-produk yang sesuai dengan karakteristik konten produk referensi.

Hal ini mengindikasikan bahwa pendekatan Content-Based Filtering efektif dalam menyaring item yang benar-benar relevan terhadap preferensi pengguna berdasarkan fitur produk.


Berikut adalah penulisan ulang bagian **Evaluasi Model Collaborative Filtering** untuk laporan Anda, **disertai dengan penjelasan dan kode programnya**:

---

### B. Content-Based Filtering

Untuk mengevaluasi performa model Collaborative Filtering yang telah dibangun, digunakan metrik **Root Mean Squared Error (RMSE)**. Metrik ini digunakan untuk mengukur sejauh mana prediksi model mendekati nilai aktual (rating dari user). RMSE merupakan salah satu metrik paling umum dalam sistem rekomendasi karena dapat menangkap kesalahan prediksi dalam satuan yang sama dengan data aslinya (misalnya skala rating 1–5).

**Rumus RMSE**

$$
RMSE = \sqrt{ \frac{1}{n} \sum_{i=1}^{n}(y_i - \hat{y}_i)^2 }
$$

Keterangan:

* $y_i$: Nilai aktual (rating yang diberikan user).
* $\hat{y}_i$: Nilai prediksi dari model.
* $n$: Jumlah total prediksi.

 **Kelebihan dan Kekurangan RMSE**

**Kelebihan**:

* Memberikan penalti lebih besar pada kesalahan prediksi yang besar.
* Sangat informatif karena berada pada satuan yang sama dengan data rating.

**Kekurangan**:

* Sensitif terhadap outlier, sehingga prediksi ekstrem bisa memperbesar nilai RMSE secara signifikan.

Berikut kode untuk menampilkan performa model berdasarkan nilai RMSE pada data pelatihan dan validasi selama proses training:

```python
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
```

**Hasil Evaluasi**

Dari hasil visualisasi, diperoleh grafik RMSE sebagai berikut:

![Evaluasi RMSE](attachment:8e7f139e-16be-40df-b8df-a1ebb8c00933.png)

* Garis **biru** menunjukkan nilai RMSE pada data pelatihan (Train RMSE).
* Garis **oranye** menunjukkan nilai RMSE pada data validasi (Val RMSE).

Berdasarkan grafik, terlihat bahwa nilai **Train RMSE** terus menurun hingga mendekati 0, menunjukkan bahwa model belajar dengan baik dari data training. Nilai **Val RMSE** juga menurun secara konsisten dan kemudian stabil di kisaran 0.15, menandakan bahwa model telah mencapai performa optimal tanpa indikasi overfitting yang signifikan.

 **Kesimpulan**

Model Collaborative Filtering mampu memberikan prediksi rating yang cukup akurat, dengan nilai RMSE validasi yang rendah dan stabil. Hal ini menunjukkan bahwa model dapat digunakan untuk merekomendasikan produk yang sesuai dengan preferensi pengguna berdasarkan interaksi historis.


## References

[1] BigBasket. (n.d.). Online Grocery Shopping and Online Supermarket in India. Retrieved May 28, 2025, from https://www.bigbasket.com

[2] Shabrina, V. G. (2019). Pengaruh Revolusi Digital terhadap Pemasaran dan Perilaku Konsumen. Jurnal Pewarta Indonesia, 1(2), 131–141. https://doi.org/10.25008/jpi.v1i2.16
















