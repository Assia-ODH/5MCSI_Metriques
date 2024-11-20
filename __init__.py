from flask import Flask, render_template_string, render_template, jsonify
from flask import render_template
from flask import json
from datetime import datetime
from urllib.request import urlopen
import sqlite3
                                                                                                                                       
app = Flask(__name__)

@app.route("/contact/")
def MaPremiereAPI():
    return "<h2>Ma page de contact</h2>"
  
@app.route('/tawarano/')
def meteo():
    try:
        # Appel de l'API
        response = urlopen('https://samples.openweathermap.org/data/2.5/forecast?lat=0&lon=0&appid=xxx')
        raw_content = response.read()
        json_content = json.loads(raw_content.decode('utf-8'))
        
        # Initialisation des résultats
        results = []
        for list_element in json_content.get('list', []):
            dt_value = list_element.get('dt')
            # Sécurisation de l'accès aux données et conversion
            temp_kelvin = list_element.get('main', {}).get('temp')
            if temp_kelvin is not None:
                temp_day_value = temp_kelvin - 273.15
                results.append({'Jour': dt_value, 'temp': round(temp_day_value, 2)})  # Temp arrondie à 2 décimales
            else:
                results.append({'Jour': dt_value, 'temp': 'Donnée manquante'})
        
        return jsonify(results=results)

    except Exception as e:
        return jsonify({'error': str(e)}), 500
      
@app.route('/')
def hello_world():
    return render_template('hello.html')

if __name__ == "__main__":
    app.run(debug=True)
