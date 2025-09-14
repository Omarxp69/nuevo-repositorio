from flask import Flask, render_template
from config import Config
from conexion_db import obtener_conexion

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)