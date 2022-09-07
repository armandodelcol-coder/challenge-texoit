import sqlite3

from flask import jsonify

from src.winners_interval.response_dto import ResponseDto


class WinnersIntervalController:

    @staticmethod
    def get_minmax():
        con = sqlite3.connect("dev_database.db")

        cur = con.cursor()
        query = cur.execute("SELECT producer, MAX(year), MIN(year), MAX(year) - MIN(year) as interval "
                            "FROM golden_rasp_awards "
                            "WHERE winner = 1 "
                            "GROUP BY producer HAVING interval > 0 ORDER BY interval ASC")
        result = query.fetchall()
        con.close()
        return jsonify(ResponseDto.to_min_max(result))
