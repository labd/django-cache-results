from functools import wraps

from django.core.cache import DEFAULT_CACHE_ALIAS, caches
from django.core.cache.backends.base import DEFAULT_TIMEOUT


def cache_results(key_function, alias=DEFAULT_CACHE_ALIAS, timeout=DEFAULT_TIMEOUT):
    """
    Decorator that allows to cache a function,
    and also allows to skip the cache if needed.

    Usage::

        def key_function(arg1, arg2):
            return f"prefix.{arg1}.{arg2}"

        @cache_results(key_function=key_function)
        def some_function(arg1, arg2):
            return "COMPLEX DATA"

    Normal usage::

        value = some_function(1, 2)

    Skipping the cache::

        value = some_function.bypass_cache(1, 2)

    Updating the cache::

        value = some_function.refresh_cache(1, 2)

    Fetch the key for manual action::

        cache_key = some_function.cache_key(1, 2)
    """
    def dec(func):
        cache = caches[alias]

        @wraps(func)
        def _get_from_cache(*args, **kwargs):
            # Fetch the data from the cache
            cache_key = key_function(*args, **kwargs)
            value = cache.get(cache_key)

            # When data is missing, call the original function to retrieve it.
            if value is None:
                value = func(*args, **kwargs)
                cache.set(cache_key, value, timeout=timeout)
            return value

        @wraps(func)
        def _refresh_cache(*args, **kwargs):
            cache_key = key_function(*args, **kwargs)
            value = func(*args, **kwargs)
            cache.set(cache_key, value, timeout=timeout)
            return value

        def _clear_cache(*args, **kwargs):
            cache_key = key_function(*args, **kwargs)
            cache.delete(cache_key)

        # Expose some variations as attributes.
        _get_from_cache.bypass_cache = func
        _get_from_cache.cache_key = key_function
        _get_from_cache.refresh_cache = _refresh_cache
        _get_from_cache.clear_cache = _clear_cache
        return _get_from_cache
    return dec
