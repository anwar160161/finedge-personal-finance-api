import time

cache_store = {}


def set_cache(key, value, ttl=60):

    cache_store[key] = {
        "value": value,
        "expiry": time.time() + ttl
    }


def get_cache(key):

    if key not in cache_store:
        return None

    cached = cache_store[key]

    if time.time() > cached["expiry"]:
        del cache_store[key]
        return None

    return cached["value"]


def clear_cache():
    cache_store.clear()