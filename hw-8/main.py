import weakref

import cProfile
import pstats
import io

from memory_profiler import profile

from lru_cache import LRUCache


class User:
    def __init__(self, name, age, sex):
        self.__name = name
        self.__age = age
        self.__sex = sex

    def increase_age(self):
        self.__age += 1

    def change_name(self, name):
        self.__name = name


class UserSlot:
    __slots__ = ("__name", "__age", "__sex")

    def __init__(self, name, age, sex):
        self.__name = name
        self.__age = age
        self.__sex = sex

    def increase_age(self):
        self.__age += 1

    def change_name(self, name):
        self.__name = name


@profile
def mem_stat():
    cache_size = 10_000
    users_cache = LRUCache(cache_size)
    slot_users_cache = LRUCache(cache_size)
    weakref_users_cache = LRUCache(cache_size)

    for i in range(cache_size):
        users_cache.set(i, User("Ivan", 30, "male"))

    for i in range(cache_size):
        slot_users_cache.set(i, UserSlot("Ivan", 30, "male"))

    original_ivan = User("Ivan", 30, "male")
    for i in range(cache_size):
        weakref_users_cache.set(i, weakref.ref(original_ivan))


if __name__ == '__main__':
    pr = cProfile.Profile()
    pr.enable()

    mem_stat()

    pr.disable()
    out = io.StringIO()
    ps = pstats.Stats(pr, stream=out)
    ps.print_stats()

    print(out.getvalue())
