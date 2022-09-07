import os
from pathlib import Path

from flask import Flask

from init_db import InitDB
from src.winners_interval.winners_interval_controller import WinnersIntervalController

app = Flask(__name__)

InitDB.create()
default_csv_file_path = Path("resources/goldenraspawardslist.csv")
csv_file_path = default_csv_file_path if os.getenv('CSV_FILE_PATH') is None else os.getenv('CSV_FILE_PATH')
InitDB.populate(csv_file_path)


@app.route('/winnersinterval', methods=['GET'])
def get_winners_interval_minmax():
    return WinnersIntervalController.get_minmax()
