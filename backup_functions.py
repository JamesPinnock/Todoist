from api_key import api
import random
from datetime import date

# urgent_and_important = [2157095127, 2157095126]
# important = [2157095127]
# urgent = [2157095126]

def print_all():
    item = api.items.all()
    print(item)

print_all()


def custom_q():
    for project in api.state['filters']:
        print(project['query'])


def custom_():
    for project in api.state['filters']:
        print(project)
        if project['query'] == 'p1':
            print("pro")

def get_all_priority(priority=1):
    ids = []

    # priority 1 == P4
    # priority 2 == P3
    # priority 3 == P2
    # priority 4 == P1 # its really backwards

    for project in api.state['items']:
        try:
            if project['priority'] == priority:
                # print(project)
                ids.append(project['id'])
        except:
            pass
    # print(ids)
    return ids

# randomly choose item from p4 and give a due date
def test_date():
    start_date_today = date.today()
    end_date = date(2022, 1, 16)
    print(start_date_today, end_date)


def random_date():
    # in 5 days
    pass

