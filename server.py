#!/usr/bin/env python
from flask import Flask, request
from flask.json import load, loads, dumps, jsonify

CONFIG_FILE = "config.json"
ENVIRONMENT = "local"

app = Flask(__name__)

@app.route('/health')
def get_health():
    return 'healthy'

if __name__ == "__main__":
    with open(CONFIG_FILE, 'r') as f:
        configurations = load(f)[ENVIRONMENT]
    app.run(
        debug = configurations.get('DEBUG_MODE'),
        host = '0.0.0.0',
        port = configurations.get('SERVER_PORT'),
        threaded = True
    )
