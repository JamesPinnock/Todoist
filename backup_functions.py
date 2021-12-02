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