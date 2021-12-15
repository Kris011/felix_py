import os
from flask import Flask
print("""
▄████╶╶▄███▄╶╶█╶╶╶╶╶▄█╶╶╶╶╶▄╶╶╶╶╶╶╶█╶▄▄╶╶▀▄╶╶╶╶▄╶
█▀╶╶╶▀╶█▀╶╶╶▀╶█╶╶╶╶╶██╶▀▄╶╶╶█╶╶╶╶╶╶█╶╶╶█╶╶╶█╶╶█╶╶
█▀▀╶╶╶╶██▄▄╶╶╶█╶╶╶╶╶██╶╶╶█╶▀╶╶╶╶╶╶╶█▀▀▀╶╶╶╶╶▀█╶╶╶
█╶╶╶╶╶╶█▄╶╶╶▄▀███▄╶╶▐█╶╶▄╶█╶╶╶╶╶╶╶╶█╶╶╶╶╶╶╶╶█╶╶╶╶
╶█╶╶╶╶╶▀███▀╶╶╶╶╶╶▀╶╶▐╶█╶╶╶▀▄╶╶╶╶╶╶╶█╶╶╶╶╶▄▀╶╶╶╶╶
╶╶▀╶╶╶╶╶╶╶╶╶╶╶╶╶╶╶╶╶╶╶╶╶▀╶╶╶╶╶╶╶╶╶╶╶╶▀╶╶╶╶╶╶╶╶╶╶╶
╶╶╶╶╶╶╶╶╶╶╶╶╶╶╶╶╶╶╶╶╶╶╶╶╶╶╶╶╶╶╶╶╶╶╶╶╶╶╶╶╶╶╶╶╶╶╶╶╶
    \033[1;32m[\033[0m+\033[1;32m]\033[0m Mini web server http basic
    \033[1;32m[\033[0m+\033[1;32m]\033[0m Creado por Hector Diaz
    \033[1;32m[\033[0m+\033[1;32m]\033[0m github: https://github.com/Kris011
    \033[1;31m[\033[0m-\033[1;31m]\033[0m Ctrl C stop server
""")
file = """<h1>Bienvenido a Felix py</h1><br><p>Creado por Hector Diaz</p><br><h3>!Si quieres tu servidor modifica el archivo main.py en la linea 16 donde dice file</h3><br><li>Gracias</li><a href="https://github.com/Kris011">Apoyame en mi github</a>
"""
app = Flask(__name__)
@app.route("/")
def server():
    return (file)
if __name__ == "__main__":
    app.run()    
