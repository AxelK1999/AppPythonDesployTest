from flask import Flask, jsonify, render_template

app = Flask(__name__)

#import webbrowser
# Ruta que deseas abrir
#URL = "http://localhost:3500"

# Ruta para devolver JSON
@app.route('/api/data', methods=['GET'])
def get_json():
    data = {
        "message": "¡Hola! Este es un mensaje en formato JSON.",
        "status": "success"
    }
    return jsonify(data)

# Ruta para devolver HTML
@app.route('/')
def index():
    return render_template('index.html')

# Configuración para servir archivos estáticos desde la carpeta 'static'
@app.route('/static-files')
def static_files():
    return "Esta ruta está configurada para servir archivos estáticos."

if __name__ == '__main__':

    # Abre la URL en el navegador predeterminado
    #webbrowser.open(URL)
    
    app.run(debug=True, port=3500)
