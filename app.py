from flask import Flask, jsonify, send_from_directory
import requests
import random
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os

# Load environment variables from.env file
load_dotenv()

app = Flask(__name__)

# Get the API key from the environment variable
NASA_API_KEY = os.getenv('NASA_API_KEY')
if not NASA_API_KEY:
    raise ValueError("No NASA API key found in environment variables")

APOD_URL = 'https://api.nasa.gov/planetary/apod'

def get_random_date():
    start_date = datetime.strptime('1995-06-16', '%Y-%m-%d')
    end_date = datetime.today()
    random_date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
    return random_date.strftime('%Y-%m-%d')

@app.route('/random-apod', methods=['GET'])
def random_apod():
    random_date = get_random_date()
    response = requests.get(APOD_URL, params={'api_key': NASA_API_KEY, 'date': random_date})
    if response.status_code == 200:
        data = response.json()
        return jsonify(data)
    else:
        return jsonify({'error': 'Failed to fetch data from NASA API'}), response.status_code

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

if __name__ == '__main__':
    app.run(debug=True)
