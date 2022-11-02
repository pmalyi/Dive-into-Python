# Key-value сховище (по зразку з coursera)
import json
import os
import tempfile
import argparse


def read_data(storage_path):
    if not os.path.exists(storage_path):
        return {}
    with open(storage_path, 'r') as inF:
        raw_data = inF.read()
        if raw_data:
            return json.loads(raw_data)
        return {}


def write_data(storage_path, data):
    with open(storage_path, 'w') as outF:
        outF.write(json.dumps(data))


def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('--key', help='Key')
    parser.add_argument('--val', help='Value')
    return parser.parse_args()


def put(storage_path, key, value):
    data = read_data(storage_path)
    data[key] = data.get(key, list())
    data[key].append(value)
    write_data(storage_path, data)


def get(storage_path, key):
    data = read_data(storage_path)
    return data.get(key, [])


def main(storage_path):
    arg = parse()
    if arg.key and arg.val:
        put(storage_path, arg.key, arg.val)
    elif arg.key:
        print(*get(storage_path, arg.key), sep=', ')
    else:
        print('The program is called with invalid parameters.')


if __name__ == '__main__':
    storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
    main(storage_path)
