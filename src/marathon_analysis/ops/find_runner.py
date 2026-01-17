from marathon_analysis.utils import datetime_utils
from marathon_analysis.load_data import Data


def _print_helper(
    name: str,
    finish_s: int,
    race: str,
    year: int
) -> None:
    print(f'\nName:\t\t{name}')
    print(f'Race:\t\t{race}')
    print(f'Year:\t\t{year}')
    print(f'Finish:\t\t{datetime_utils.fmt_seconds(finish_s)}\n')


def find_runner_by_name(
    data: Data,
    name: str
) -> None:
    me = data.results.query(f"Name == '{name}'")

    if me.empty:
        print('\nNo Results\n')
        return

    for idx, row in me.iterrows():
        _print_helper(
            name=str(row['Name']),
            finish_s=int(row['Finish']),
            race=str(row['Race']),
            year=int(row['Year']),
        )
