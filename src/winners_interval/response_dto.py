class ResponseDto:

    @staticmethod
    def to_min_max(query_result):
        min_list = [row for row in query_result if row[-1] == query_result[0][-1]]
        max_list = [row for row in query_result if row[-1] == query_result[-1][-1]]

        min_structured = [
            {
                "producer": row[0],
                "interval": row[3],
                "previousWin": row[1],
                "followingWin": row[2]
            }
            for row in min_list]

        max_structured = [
            {
                "producer": row[0],
                "interval": row[3],
                "previousWin": row[1],
                "followingWin": row[2]
            }
            for row in max_list]

        return {
            "min": min_structured,
            "max": max_structured
        }
