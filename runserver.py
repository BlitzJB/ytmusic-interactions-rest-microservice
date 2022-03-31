from server import app

import json
runconfig = json.load(open('runconfig.json'))
DEBUG = runconfig.get('debug', False)
HOST = runconfig.get('host', '0.0.0.0')
PORT = runconfig.get('port', 5000)

if __name__ == '__main__':
    app.run(debug=DEBUG, host=HOST, port=PORT)