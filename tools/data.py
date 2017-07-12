import json

def read_json(fname):
    with open(fname) as f:
        data = f.read()
        data = json.loads(data)
    return data


