import json
import os

# used for sorting elements in json only
def sort(obj):
    if isinstance(obj, dict):
        return {k: sort(v) for k, v in obj.items()}
    return sorted(sort(x) for x in obj) if isinstance(obj, list) else obj

# input - json
# output - pretty printed json with sorted elements
def ordered_json(data):
    if data=="":
        return ""
#    obj=json.loads(data.replace('\r', '\\r').replace('\n', '\\n').replace('\t', '\\t'))
    obj=json.loads(data)
    return json.dumps(sort(obj), sort_keys=True, indent=4, separators=(',', ': '))

# input - path to file
# output - True if file exists, else False
def file_exists(path):
    return bool(os.path.isfile(path))

def replace_rn_n(mytext):
    if mytext=="":
        return ""
    mytext=mytext.replace("\r\n", "\n")
    return mytext
