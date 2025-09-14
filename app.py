from flask import Flask, render_template
from config import Config
from conexion_db import obtener_conexion

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/test-db')
def test_db():
    from conexion_db import obtener_conexion
    try:
        conn = obtener_conexion()
        conn.close()
        return "✅ Conexión a la base de datos exitosa!"
    except Exception as e:
        return f"❌ Error de conexión: {e}"


if __name__ == "__main__":
    app.run(debug=True)