# import alikasi flask untuk dipakai diweb kita
# import aplikasi flask, os, flash, jsofiny, redirect, dan render_template untuk dipakai di web kita
import os

# import SQL untuk akses datbaase
from cs50 import SQL
# import flash untuk nontifikasi pada web
# import jsofiny untuk memformat data
# import redirect dan render_template untuk berpindah halaman web
# import request dan session untuk mengakses data

from flask import Flask

# mengatur nama aplikasi
app = Flask(__name__)

# mengatur URI (Universal Resource Identifier), dan apa yang di tampilkan jika URI diakses 
@app.route('/') # ketika alamat http://127.0.0.1:5000/ di panggil maka server akan mengeksekusi fungsi hello() 
def hello(): # function dengan nama hello
    return 'Hello,World'

# mengatur URI ke http://127.0.0.1:5000/login, dan mengeksekusi fungsi login() jika diakses di alamat URI http://127.0.0.1:5000/login
@app.route("/login")
def login():
    return 'Halaman login'
