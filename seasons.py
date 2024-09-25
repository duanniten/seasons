from datetime import date
import re
import inflect
import sys

class BornDate(date):

    def live_minutes(self):
        return self.today - self

    def season_time(self) -> str:
        p = inflect.engine()
        today = date.today()
        dif_minutes = (today - self).days * 24 * 60
        season_time = str(p.number_to_words(dif_minutes))
        season_time = season_time.replace(' and', '')
        return f'{season_time.capitalize()} minutes'

    @classmethod
    def set_date(cls):
        date_birth = input('Date of Birth: ')
        if matches := re.search(r'([0-9]{4})-(0[0-9]|1[0-2])-([0-2][0-9]|3[0-1])',
                                date_birth):
            y, m, d = matches.groups()
            try:
                return BornDate(int(y), int(m) , int(d))
            except ValueError:
                sys.exit(1)
        else:
            sys.exit(1)

def main():
    born_date = BornDate.set_date()
    print(born_date.season_time())


if __name__ == "__main__":
    main()