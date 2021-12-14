from api_key import api
import random
from datetime import date

# urgent_and_important = [2157095127, 2157095126]
# important = [2157095127]
# urgent = [2157095126]

def print_all():
    item = api.items.all()
    print(item)

# print_all()


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

def important():
    '''
    Will update all the item with the labels that are inclued
    :return:
    A list of objects based on the list below
    '''
    important = [2157095127]
    ids = []
    for project in api.state['items']:
        # print((project['labels']))
        try:
            if important[0] in project['labels']:  # and len(project['labels']) == 1:
                # print(project["labels"])
                # print(project['content'])
                ids.append(project['id'])
        except:
            pass
    return ids

def urgent():
    '''
    Will update all the item with the labels that are inclued
    :return:
    A list of objects based on the list below  (Urgent)
    '''
    urgent = [2157095126]
    ids = []
    for project in api.state['items']:
        # print((project['labels']))
        try:
            if urgent[0] in project['labels'] and len(project['labels']) == 1:
                # print(project['content'])
                ids.append(project['id'])
        except:
            pass
    return ids

def important_urgent():
    '''
    Will update all the item with the labels that are inclued
    :return:
    A list of objects based on the list below ('important_urgent')
    '''
    important_urgent = [2157095127, 2157095126]
    ids = []
    for project in api.state['items']:
        # print(project['labels'][:2])
        try:
            if project['labels'][:2] == important_urgent:
                print(project['content'])
                ids.append(project['id'])
        except:
            pass
    return ids

def update_items_with_label_and_priorty(listing, priority):
    ''' This will update a list item in place '''
    labels = [2158964524]
    for id in listing:
        item = api.items.get_by_id(id)
        item.update(priority=priority)
        api.commit()

def update_items_with_due_date(listing):
    import time

    while True:
        localtime = time.localtime()
        # result = time.strftime("%I:%M:%S %p", localtime)
        ''' This will update a list item in place '''
        # for id in listing:
        try:
            random_task = random.choice(listing)  # random choice from list
            item = api.items.get_by_id(random_task)
            number_of_days = random.randint(14, 29)
            print(number_of_days)
            if item['due'] == None and localtime == "05:00 PM":
                item.update(due={'string': f'in {number_of_days} days'})
                api.commit()
            else:
                print("Item has date added")
        except:
            pass

# update_items_with_due_date(get_all_priority(3))
# get_all_priority(3)