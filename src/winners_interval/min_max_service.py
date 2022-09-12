class MinMaxService:

    @staticmethod
    def get_min_max(query_result):
        winner_years = {}
        for r in query_result:
            if winner_years.get(r[0]) is None:
                winner_years[r[0]] = [r[1]]
            else:
                winner_years[r[0]].append(r[1])
        min_interval = 999999
        max_interval = 0
        structured_winners_intervals = []
        for k, v in winner_years.items():
            while len(v) >= 2:
                previous_win = v[-2]
                following_win = v[-1]
                interval = v[-1] - v[-2]
                min_interval = interval if interval < min_interval else min_interval
                max_interval = interval if interval > max_interval else max_interval
                structured_winners_intervals.append(
                    {
                        "producer": k,
                        "interval": interval,
                        "previousWin": previous_win,
                        "followingWin": following_win
                    }
                )
                v.pop()
        min_list = [wi for wi in structured_winners_intervals if wi['interval'] == min_interval]
        max_list = [wi for wi in structured_winners_intervals if wi['interval'] == max_interval]

        return min_list, max_list
