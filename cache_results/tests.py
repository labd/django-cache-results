"""
Test running
"""
from django.core.cache import cache
from django.test import SimpleTestCase

from cache_results import cache_results


class CacheResultsTest(SimpleTestCase):

    def test_decorator(self):
        nonlocal_dict = {}

        def get_cache_key(arg1):
            return 'foo.{}'.format(arg1)

        @cache_results(key_function=get_cache_key, alias='default')
        def example(arg1):
            nonlocal_dict.setdefault(arg1, 0)
            counter = nonlocal_dict[arg1] + 1
            nonlocal_dict[arg1] = counter
            return "dummy{}".format(counter)

        # First call, enter cache
        example(1)
        self.assertEqual(nonlocal_dict[1], 1)
        self.assertEqual(cache.get(get_cache_key(1)), "dummy1")

        # Calling again should be cached
        example(1)
        example(1)
        self.assertEqual(nonlocal_dict[1], 1)  # still called once

        # Bypass calls the original function
        example.bypass_cache(1)
        example.bypass_cache(1)
        self.assertEqual(nonlocal_dict[1], 3)  # now called trice

        # Refresh updates and recaches
        self.assertEqual(cache.get(get_cache_key(1)), "dummy1")
        example.refresh_cache(1)
        self.assertEqual(nonlocal_dict[1], 4)  # called 4 times
        self.assertEqual(cache.get(get_cache_key(1)), "dummy4")
