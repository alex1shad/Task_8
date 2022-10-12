import requests
import datetime as d


class SOFfinder:
    def sof(self):
        reps = requests.get(path).json()
        i = 1
        for el in reps['items']:
            print(f'Question №{i}\n{el["title"]}\n')
            i += 1


if __name__ == '__main__':
    date_now = d.datetime.now()
    date_2_da = date_now - d.timedelta(2)
    date_now_unix = int(date_now.timestamp())
    date_2_da_unix = int(date_2_da.timestamp())
    path = f'https://api.stackexchange.com/2.3/questions?pagesize=100&\
                fromdate={date_2_da_unix}&todate={date_now_unix}&order=desc&sort=creation&\
                tagged=python&site=stackoverflow'
    finder = SOFfinder()
    finder.sof()
