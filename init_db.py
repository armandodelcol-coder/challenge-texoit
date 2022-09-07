import csv
import sqlite3
import uuid


class InitDB:

    @staticmethod
    def create():
        con = sqlite3.connect("dev_database.db")

        cur = con.cursor()

        cur.execute("drop table if exists golden_rasp_awards;")
        cur.execute("create table golden_rasp_awards("
                    "id varchar(255) primary key, "
                    "title varchar(80) not null,"
                    "studio varchar(80) not null,"
                    "producer varchar(80) not null,"
                    "year int not null,"
                    "winner tinyint(1) not null default 0);")
        con.close()

    @staticmethod
    def populate(csv_file):
        with open(csv_file, newline='') as csv_file_opened:
            csv_reader = csv.reader(csv_file_opened, delimiter=";")
            # skip header
            next(csv_reader)
            data = [[str(uuid.uuid4()), row[1], row[2], row[3], row[0], 1 if row[4] == 'yes' else 0]
                    for row in csv_reader]

        con = sqlite3.connect("dev_database.db")

        cur = con.cursor()

        cur.executemany("INSERT INTO golden_rasp_awards VALUES("
                        "?, ?, ?, ?, ?, ?)", data)
        con.commit()

        con.close()
