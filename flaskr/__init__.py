# import alikasi flask untuk dipakai diweb kita
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
