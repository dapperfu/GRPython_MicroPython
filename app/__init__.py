from flask import Flask
app = Flask(__name__)
from flask import request
from flask import jsonify

import time
import datetime

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/<sensor>/<int:value>')
def log_sensor(sensor, value):
    # NoSQL Data Logging.
    logfile=f"{request.remote_addr}_log.csv"
    epoch = time.time()
    iso8601 = datetime.datetime.now().isoformat()
    with open(logfile, "a") as fid:
        print(f"{epoch},{iso8601},{sensor},{value}", file=fid)
    
 
    # Cloud Computing
    led_status = {
        "green": int(value),
        "red": 0,
        "blue": 0,
    }

    return jsonify(led_status)
