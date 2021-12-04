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