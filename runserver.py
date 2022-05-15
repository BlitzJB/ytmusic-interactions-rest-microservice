from server import app

from os import mkdir, path

import json

runconfig = json.load(open("runconfig.json"))
DEBUG = runconfig.get("DEBUG", False)
HOST = runconfig.get("HOST", "0.0.0.0")
PORT = runconfig.get("PORT", 5000)


def onmount():
    if not path.exists(runconfig["DOWNLOADS_PATH"]):
        mkdir(runconfig["DOWNLOADS_PATH"])


if __name__ == "__main__":
    onmount()
    app.run(debug=DEBUG, host=HOST, port=PORT)
