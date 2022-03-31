from server import app

import json
runconfig = json.load(open('runconfig.json'))
DEBUG = runconfig.get('DEBUG', False)
HOST = runconfig.get('HOST', '0.0.0.0')
PORT = runconfig.get('PORT', 5000)

if __name__ == '__main__':
    app.run(debug=DEBUG, host=HOST, port=PORT)