from flask import Flask, request, jsonify
import requests

app = Flask(__name__)
API_KEY = 'b8aa0045'

@app.route('/')
def home():
    return 'IMDb ID API is running!'

@app.route('/geturl')
def geturl():
    title = request.args.get('title')
    season = request.args.get('season')
    episode = request.args.get('episode')
    
    if not title or not season or not episode:
        return jsonify({'error': 'Missing parameters'}), 400

    res = requests.get(f"http://www.omdbapi.com/?t={title}&apikey={API_KEY}")
    data = res.json()

    if data.get('Response') == 'True':
        imdb_id = data.get('imdbID')
        url = f"https://vidfast.pro/tv/{imdb_id}/{season}/{episode}"
        return jsonify({'url': url})
    else:
        return jsonify({'error': 'Title not found'}), 404
