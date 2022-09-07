import re

def solution(new_id):
    lists = ['-', '_', '.']
    new_id = new_id.lower()
    new_id = re.sub(r"[^0-9a-z-_.]", "", new_id)
    new_id = ".".join([i for i in new_id.split(".") if i != ''])
    
    if len(new_id) == 0:
        new_id = 'a' * 3
    elif len(new_id) <= 2:
        new_id = new_id + new_id[-1] * (3-len(new_id))
    elif len(new_id) >= 16:
        new_id = new_id[:15]
        new_id = ".".join([i for i in new_id.split(".") if i != ''])
        
    answer = new_id
    return answer