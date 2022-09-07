import csv
import random

if __name__ == '__main__':
    fieldnames = ['year', 'title', 'studios', 'producers', 'winner']
    producers = [f'Producer {p}' for p in range(1, 15)]
    rows = []
    winners_year = []
    for year in range(1980, 2023):
        for year_movie in range(1, 16):
            choice = 'no'
            if year not in winners_year:
                choice = random.choice(['yes', 'no'])
                if choice == 'yes':
                    winners_year.append(year)
            rows.append(
                {
                    'year': year,
                    'title': f"Movie - {year} - {year_movie}",
                    'studios': f"Studio - {year} - {year_movie}",
                    'producers': random.choice(producers),
                    'winner': choice
                }
            )

    with open('resources\goldenraspawardslist.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=';')
        writer.writeheader()
        writer.writerows(rows)
