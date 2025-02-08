import subprocess
import os
import json
from flask import Flask, render_template, jsonify, send_file

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home-base')
def home_base():
    return render_template('home_base.html')

@app.route('/prizes.json')
def get_prizes():
    json_file_path = os.path.join(os.getcwd(), "prizes.json")
    return send_file(json_file_path, mimetype='application/json', cache_timeout=0)

@app.route('/run-script', methods=['POST'])  
def run_script():
    try:
        script_path = os.path.join(os.getcwd(), 'prize_generator.py')

        # Set correct working directory
        result = subprocess.run(['python', script_path], cwd=os.path.dirname(script_path), capture_output=True, text=True)

        # Debugging output
        print("Script output:", result.stdout)
        print("Script error:", result.stderr)

        # Read updated JSON file
        json_file_path = os.path.join(os.path.dirname(script_path), "prizes.json")
        if os.path.exists(json_file_path):
            with open(json_file_path, "r") as file:
                updated_data = json.load(file)
        else:
            updated_data = {"error": "JSON file not found"}

        return jsonify(updated_data)
    except Exception as e:
        return jsonify({'error': str(e)})
    


if __name__ == '__main__':
    app.run(debug=True)
