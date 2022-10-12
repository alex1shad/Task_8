import requests
import datetime as d


class SOFfinder:
    def sof(self):
        date_now = d.datetime.now()
        date_2_da = date_now - d.timedelta(2)
        delta = d.timedelta(minutes=5)
        i = 1
        while date_now > date_2_da:
            date_now_unix = int(date_now.timestamp())
            date_before = date_now - delta
            date_before_unix = int(date_before.timestamp())
            path = f'https://api.stackexchange.com/2.3/questions?\
                fromdate={date_before_unix}&todate={date_now_unix}&order=desc&sort=creation&\
                tagged=python&site=stackoverflow'
            reps = requests.get(path).json()
            for el in reps['items']:
                print(f'Question №{i}\n{el["title"]}\n')
                i += 1
            date_now = date_now - delta


if __name__ == '__main__':
    finder = SOFfinder()
    finder.sof()
