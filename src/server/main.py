from flask import Flask, json

app = Flask(__name__)

@app.route('/')
def get_stats():
    return json.jsonify({ 'switches': 0, 'gloveTime': 0 })
