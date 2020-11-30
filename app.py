import sqlite3
import pandas as pd
from flask import Flask, request
app = Flask(__name__)

conn = sqlite3.connect("data/chinook.db")
query = """SELECT g.Name AS Genre, i.Total
FROM invoice_items AS ii
LEFT JOIN invoices AS i ON ii.InvoiceId=i.InvoiceId
LEFT JOIN tracks AS t ON ii.TrackId=t.TrackId
LEFT JOIN genres AS g ON t.GenreId=g.GenreId
"""
song_sales = pd.read_sql_query(query, conn)


# Halaman home
@app.route('/')
def home_page():
    return 'Anda Berhasil Mengakses Halaman Awal'

# Genre lagu yang paling banyak dibeli
@app.route('/genre_sale_freq')
def genre_sales_freq():
    genre_fav = song_sales.Genre.value_counts()
    return f"""Informasi pembelian lagu berdasarkan genre-nya: 
    {genre_fav.to_json()}"""

# Total penjualan lagu berdasarkan genre-nya
@app.route('/genre_most_sales')
def genre_most_sales():
    most_sales = pd.crosstab(index=song_sales['Genre'],
                         columns='Total Sales',
                         aggfunc='sum',
                         values=song_sales['Total']
                        ).sort_values(by='Total Sales',
                                      ascending=False)
    return f"""Informasi total penjualan lagu berdasarkan genre-nya:
    {most_sales['Total Sales'].to_json()}
    """

# Rata-rata (average) nilai suatu saham (adjusted close) suatu perusahaan untuk setiap bulannya
@app.route('/stock/<company_name>')
def monthly_adjusted_close_price(company_name):
    stock = pd.read_pickle('data/stock')
    
    # Perbaharui indek yang digunakan
    new_index = pd.date_range(start="2018-01-02", end="2019-03-31")
    stock = stock.reindex(new_index)

    # Isi missing value dengan menggunakan method forward fill
    stock = stock.ffill()

    # Swap urutan indeksnya
    stock = stock.stack().unstack(level=0).stack()

    # Informasi stock suatu perusahaan
    certain_stock = stock.loc[company_name]

    # Ekstrak periode per bulannya dari informasi tanggalnya
    certain_stock = certain_stock.reset_index()
    certain_stock['monthly'] = certain_stock['index'].dt.to_period('M')

    # Hitung nilai rata-rata(average) untuk setiap bulannya
    stock_mean = certain_stock.groupby('monthly')['Adj Close'].mean()
    
    return f"""Rata-rata (average)nilai saham (adjusted close) {company_name} per bulannya:
    {stock_mean.to_json()}
    """
    
if __name__ == '__main__':
    app.run(debug=True, port=5000)