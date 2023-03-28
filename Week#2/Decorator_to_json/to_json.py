# Декоратор to_json
import functools
import json


def to_json(func):
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        result = func(*args, **kwargs)
        result = json.dumps(result)
        print(result)
        return result
    return wrapped


@to_json
def get_data():
    return {
        'data': 42,
    }


get_data()
# вернёт '{"data": 42}'
