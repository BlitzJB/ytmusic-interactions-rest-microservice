from flask import jsonify, request

from .app import app
from ytmusic.recommendations import get_recommendations
from ytmusic.search import get_search_results

@app.route('/check')
def __check():
    return 'OK'

@app.route('/recommendations')
def __recommendations():
    video_id = request.args.get('video_id')
    lim = request.args.get('lim', 50, int)
    return jsonify(get_recommendations(video_id, lim))

@app.route('/search')
def __search():
    query = request.args.get('query')
    lim = request.args.get('lim', 50, int)
    return jsonify(get_search_results(query, lim))