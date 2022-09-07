import sqlite3

from flask import jsonify

from src.winners_interval.min_max_service import MinMaxService


class WinnersIntervalController:

    @staticmethod
    def get_minmax():
        con = sqlite3.connect("dev_database.db")
        cur = con.cursor()
        query = cur.execute("SELECT name, year "
                            "FROM producers, indicated_movie_producers, indicated_movies "
                            "WHERE producers.id = indicated_movie_producers.producer_id AND "
                            "indicated_movie_producers.indicated_movie_id = indicated_movies.id AND "
                            "winner = 1 "
                            "ORDER BY year ASC")
        result = query.fetchall()

        min_list, max_list = MinMaxService.get_min_max(result)

        con.close()
        return jsonify(
            min=min_list,
            max=max_list
        )
