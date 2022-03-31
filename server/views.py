from flask import jsonify, request, render_template, send_from_directory

from .app import app
from ytmusic.recommendations import get_recommendations
from ytmusic.search import get_search_results
from ytmusic.download import DOWNLOAD_PATH, download_audio


@app.route('/')
def __index():
    return render_template('docs.html')

@app.route('/check')
def __check():
    return 'OK'

@app.route('/recommendations')
def __recommendations():
    video_id = request.args.get('video_id')
    lim = request.args.get('lim', 50, int)
    if not video_id: return jsonify({'error': 'specify video_id da bunda'}), 400
    return jsonify(get_recommendations(video_id, lim))

@app.route('/search')
def __search():
    query = request.args.get('query')
    lim = request.args.get('lim', 50, int)
    if not query: return jsonify({'error': 'specify query da bunda'}), 400
    return jsonify(get_search_results(query, lim))

@app.route('/download')
def __download():
    video_id = request.args.get('video_id')
    if not video_id: return jsonify({'error': 'specify video_id da bunda'}), 400
    fname = download_audio(video_id, DOWNLOAD_PATH)
    print(DOWNLOAD_PATH.split('/')[-1], fname)
    return send_from_directory('.' + DOWNLOAD_PATH, fname) # send_from_dir takes app instnatiated file as root. we need to go one dir out