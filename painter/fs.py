import json, pickle


def save_json(data, filename='data.json'):
    with open(filename, 'w') as f:
        json.dump(data, f)

def save_pickle(data, filename='data.pickle'):
    with open(filename, 'wb') as f:
        pickle.dump(data, f)

def load_json(filename='data.json'):
    with open(filename,'r') as f:
        data_new = json.load(f)
    return data_new

def load_pickle(filename='data.pickle'):
    with open(filename, 'rb') as f:
        data_new = pickle.load(f)
    return data_new
