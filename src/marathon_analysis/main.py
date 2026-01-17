import argparse
from marathon_analysis import load_data
from marathon_analysis.ops import find_runner


def arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('name', nargs="+")
    args = parser.parse_args()
    return args.name


def main() -> None:
    name = arguments()
    data = load_data.load()
    find_runner.find_runner_by_name(
        data=data,
        name=' '.join(name)
    )


if __name__ == "__main__":
    main()
