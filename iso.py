import csv
from typing import List
from pathlib import Path
from dataclasses import dataclass, field


@dataclass(order=True)
class Code:
    sort_index: int = field(init=False, repr=False)
    short: str
    alpha2: str
    alpha3: str
    numeric: int
    iso3166_2: str
    independent: str

    def __post_init__(self):
        self.sort_index = ord(self.short[0])

    def internet_domain(self):
        return '.' + self.alpha2.lower()

    '''def __str__(self):
        return f'{self.short}, {self.alpha2}, {self.alpha3}\n{self.numeric}\n' \
               f'ISO 3166-2: {self.iso3166_2}\nIndependent: {self.independent}'''


class Iso:
    def __init__(self):
        self._codes = self._load()

    @staticmethod
    def _load() -> List[Code]:
        content = []
        with (Path(__file__).parent / 'iso.csv').open(mode='r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    line_count += 1
                content.append(Code(row['short_name'], row['alpha2'], row['alpha3'], row['numeric'],
                                    row['iso3166-2'], row['independent']))
                line_count += 1
        return content

    def find(self, code: str):
        for i in self._codes:
            if i.alpha2 == code.upper() or i.alpha3 == code.upper():
                return i
        return None

    def get_name(self, name: str):
        for i in self._codes:
            if name.capitalize() in i.short:
                return i
        return None

    def check(self, code: str):
        for i in self._codes:
            if i.alpha2 == code.upper() or i.alpha3 == code.upper():
                return True
        return False

    @property
    def sort_name(self):
        return sorted(self._codes)

    @property
    def sort_numeric(self):
        return sorted(self._codes, key=lambda x: x.numeric)

    @property
    def sort_alpha2(self):
        return sorted(self._codes, key=lambda x: x.alpha2)

    @property
    def sort_alpha3(self):
        lst = sorted(self._codes, key=lambda x: x.alpha3)
        return lst

    @property
    def sort_independence(self):
        return sorted(self._codes, key=lambda x: x.independent)

    @property
    def codes(self):
        return self._codes

    def __iter__(self):
        for i in self._codes:
            yield i

    def __getitem__(self, key):
        return self._codes[key]

    def __len__(self):
        return len(self._codes)


if __name__ == '__main__':
    iso = Iso()
    print(iso.sort_independence[0])
