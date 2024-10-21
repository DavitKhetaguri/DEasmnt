import datetime
import dateutil.parser

def format_pd_date(date):
    return  dateutil.parser.parse(date).date()

def format_date_json(date):
    if not date:
        return None
    return datetime.datetime.strptime(date, '%d.%m.%Y').date()


def compare_dates(date1, date2):
    if not date1 or not date2:
        return False
    return date1 >= date2