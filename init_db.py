import csv
import sqlite3
import uuid


class InitDB:

    @staticmethod
    def create():
        con = sqlite3.connect("dev_database.db")

        cur = con.cursor()

        cur.execute("drop table if exists indicated_movies;")
        cur.execute("create table indicated_movies("
                    "id varchar(255) primary key,"
                    "title varchar(80) not null,"
                    "year int not null,"
                    "winner tinyint(1) not null default 0);")

        cur.execute("drop table if exists studios;")
        cur.execute("create table studios("
                    "id varchar(255) primary key,"
                    "name varchar(80) not null);")

        cur.execute("drop table if exists producers;")
        cur.execute("create table producers("
                    "id varchar(255) primary key,"
                    "name varchar(80) not null);")

        cur.execute("drop table if exists indicated_movie_studios;")
        cur.execute("create table indicated_movie_studios("
                    "id bigint primary key,"
                    "indicated_movie_id varchar(255) not null,"
                    "studio_id varchar(255) not null,"
                    "constraint fk_indicated_movie_studio_movie foreign key (indicated_movie_id) references indicated_movies (id), "
                    "constraint fk_indicated_movie_studio_studio foreign key (studio_id) references studios (id));")

        cur.execute("drop table if exists indicated_movie_producers;")
        cur.execute("create table indicated_movie_producers("
                    "id bigint primary key,"
                    "indicated_movie_id varchar(255) not null,"
                    "producer_id varchar(255) not null,"
                    "constraint fk_indicated_movie_producer_movie foreign key (indicated_movie_id) references indicated_movies (id), "
                    "constraint fk_indicated_movie_producer_producer foreign key (producer_id) references producers (id));")

        con.close()

    @staticmethod
    def populate(csv_file):
        with open(csv_file, newline='') as csv_file_opened:
            csv_reader = csv.reader(csv_file_opened, delimiter=";")
            # skip header
            next(csv_reader)
            studios_ids = {}
            producers_ids = {}
            indicated_movies_data = []
            indicated_movie_studios_data = []
            indicated_movie_producers_data = []
            for row in csv_reader:
                movie_studios = row[2].replace(' and ', ',').split(',')
                movie_studios = [ms for ms in movie_studios if ms]
                movie_studios = [s.strip() for s in movie_studios]
                movie_studios = [s[4:] if s[0:4] == 'and ' else s for s in movie_studios]
                for ms in movie_studios:
                    k_uppers = [k.upper() for k in studios_ids.keys()]
                    if ms.upper() not in k_uppers:
                        studios_ids[ms] = str(uuid.uuid4())

                movie_producers = row[3].replace(' and ', ',').split(',')
                movie_producers = [mp for mp in movie_producers if mp]
                movie_producers = [s.strip() for s in movie_producers]
                movie_producers = [s[4:] if s[0:4] == 'and ' else s for s in movie_producers]
                for mp in movie_producers:
                    k_uppers = [k.upper() for k in producers_ids.keys()]
                    if mp.upper() not in k_uppers:
                        producers_ids[mp] = str(uuid.uuid4())

                indicated_movie = [str(uuid.uuid4()), row[1], row[0], 1 if row[4] == 'yes' else 0]
                indicated_movies_data.append(indicated_movie)

                indicated_movie_studios = [[indicated_movie[0], studios_ids[s]] for s in movie_studios]
                for ims in indicated_movie_studios:
                    indicated_movie_studios_data.append(ims)

                indicated_movie_producers = [[indicated_movie[0], producers_ids[p]] for p in movie_producers]
                for imp in indicated_movie_producers:
                    indicated_movie_producers_data.append(imp)

            studios_data = [[v, k] for k, v in studios_ids.items()]
            producers_data = [[v, k] for k, v in producers_ids.items()]

        con = sqlite3.connect("dev_database.db")

        cur = con.cursor()

        cur.executemany("INSERT INTO indicated_movies VALUES("
                        "?, ?, ?, ?)", indicated_movies_data)
        cur.executemany("INSERT INTO studios VALUES("
                        "?, ?)", studios_data)
        cur.executemany("INSERT INTO producers VALUES("
                        "?, ?)", producers_data)
        cur.executemany("INSERT INTO indicated_movie_studios (indicated_movie_id, studio_id) VALUES("
                        "?, ?)", indicated_movie_studios_data)
        cur.executemany("INSERT INTO indicated_movie_producers (indicated_movie_id, producer_id) VALUES("
                        "?, ?)", indicated_movie_producers_data)
        con.commit()

        con.close()
