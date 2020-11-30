# capstone-flask-api
Ini merupakan capstone-project Data Analytics Specialization dari Algoritma Data Science Bootcamp.

___
## Dependencies : 
Bisa dilihat di file requirements.txt
___
## Goal
1. Membuat Flask APP yang berfungsi sebagai API yang memberikan data dalam format JSON
2. Membuat minimal 2 endpoint statis (atau lebih) dan 1 endpoint dinamis(atau lebih) menggunakan routing
3. Melakukan deployment Flask APP ke Heroku

___
Project telah dideploy dan bisa diakses melalui : https://capstone-flask-api.herokuapp.com

Here's the list of its endpoints: 
```
1. / , method = GET
Halaman awal dari project.

2. /genre_sale_freq , method = GET
Akan mengembalikan genre lagu yang paling banyak dibeli (frequency).
Data yang digunakan yaitu:
    - chinook.db
    
3. /genre_most_sales , method = GET
Akan mengembalikan total penjualan lagu untuk masing-masing genre.
Data yang digunakan yaitu:
    - chinook.db
    
4. /stock/<company_name> , method = GET
Akan mengembalikan rata-rata (average) nilai suatu saham (adjusted close) suatu perusahaan untuk setiap bulannya.
Data yang digunakan yaitu:
    - chinook.db

Untuk menggunakannya perlu untuk mengganti bagian '<company_name>' dengan nama perusahaan yang ingin dilihat informasinya.
Berdasarkan dataset yang digunakan, maka perusahaan yang dapat diakses yaitu = {AAPL, FB, GOOGL}
```

If you want to try it, you can access (copy-paste it) : 
- https://capstone-flask-api.herokuapp.com
- https://capstone-flask-api.herokuapp.com/genre_sale_freq
- https://capstone-flask-api.herokuapp.com/genre_most_sales
- https://capstone-flask-api.herokuapp.com/stock/AAPL
- https://capstone-flask-api.herokuapp.com/stock/FB
- https://capstone-flask-api.herokuapp.com/stock/GOOGL
