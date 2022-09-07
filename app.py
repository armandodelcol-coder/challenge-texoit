from flask import Flask

from init_db import InitDB
from src.winners_interval.winners_interval_controller import WinnersIntervalController

app = Flask(__name__)

InitDB.create()
InitDB.populate('resources\goldenraspawardslist.csv')


@app.route('/winnersinterval', methods=['GET'])
def get_winners_interval_minmax():
    return WinnersIntervalController.get_minmax()
