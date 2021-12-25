from backup_functions import important, important_urgent, update_items_with_label_and_priorty, urgent,print_all, update_items_with_due_date,get_all_priority
import todoist
import os

api = todoist.TodoistAPI(os.environ["API_TOKEN"])
api.sync()

##########
# important()
# important_urgent()

"""
The order matters annoyingly 
"""
update_items_with_label_and_priorty(urgent(), 2)
update_items_with_label_and_priorty(important(), 3)
update_items_with_label_and_priorty(important_urgent(), 4)
# update_items_with_due_date(get_all_priority())

# update_items([5357142685, 5358150795])
# [5357142685, 5358150795]
# print_all()

# if label == urgent:
    # then mark with piriorty
# Urgent and important p1
# def Important & not urgent p2
# Urgent & unimportant p3
# Unimportant & Not urgent p4
