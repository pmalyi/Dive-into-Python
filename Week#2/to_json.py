import functools


def to_json(func):
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        result = func(*args, **kwargs)
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
