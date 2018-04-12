import datetime
import calendar


def main():
    target_years = []
    for year in range(1006, 1996, 10):
        d = datetime.date(year, 1, 26)
        if d.isoweekday() == 1 and calendar.isleap(year):
            target_years.append(d)

    print(target_years[-2])  # he ain't the youngest, he is the second

    # todo: buy flowers for tomorrow:
    # it's Mozart


if __name__ == '__main__':
    main()
