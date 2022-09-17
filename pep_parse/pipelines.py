import csv
import datetime as dt
from collections import defaultdict

from pep_parse.settings import BASE_DIR, RESULT_DIR


class PepParsePipeline:

    def __init__(self):
        self.filepath = BASE_DIR / RESULT_DIR
        self.filepath.mkdir(exist_ok=True)

    def open_spider(self, spider):
        self.statuses = defaultdict(int)

    def process_item(self, item, spider):
        self.statuses[item['status']] += 1
        return item

    def close_spider(self, spider):
        now = dt.datetime.utcnow().strftime('%Y-%m-%d_%H-%M-%S')
        filename = f'status_summary_{now}.csv'
        with open(
            self.filepath / filename,
            mode='w',
            encoding='utf-8'
        ) as csvfile:
            csv_writer = csv.writer(
                csvfile,
                dialect=csv.unix_dialect,
                quoting=csv.QUOTE_NONE
            )
            csv_writer.writerows([
                ['Статус', 'Количество'],
                *self.statuses.items(),
                ['Total', sum(self.statuses.values())]
            ])
