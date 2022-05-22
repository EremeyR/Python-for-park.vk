"""module with logging configuration testing"""
import logging.config

import sys

import lru_cache

double_output_config = {
    "version": 1,
    "formatters": {
        "stream_form": {
            "format": "[%(asctime)s] %(levelname)s\t%(message)s",
        },
        "file_form": {
            "format": "%(asctime)s\t%(name)s\t%(levelname)s\t%(message)s",
        },
    },
    "handlers": {
        "to_file": {
            "level": "INFO",
            "class": "logging.FileHandler",
            "filename": "custom.log",
            "formatter": "file_form",
        },
        "to_stream": {
            "level": "INFO",
            "class": "logging.StreamHandler",
            "formatter": "stream_form",
        },
    },
    "loggers": {
        "double_output": {
            "level": "INFO",
            "handlers": ["to_file", "to_stream"],
        },
        "file_output": {
            "level": "INFO",
            "handlers": ["to_file"],
        }
    },
}


def test_func(logger):
    """ simple function for logger testing """
    cache = lru_cache.LRUCache(logger, 2)
    cache.set("k1", "val1")
    cache.set("k2", "val2")

    cache.get("k3")
    cache.get("k2")
    cache.get("k1")

    cache.set("k3", "val3")

    cache.get("k3")
    cache.get("k2")
    cache.get("k1")


if __name__ == '__main__':
    logging.config.dictConfig(double_output_config)
    root_logger = logging.getLogger("file_output")

    if len(sys.argv[1:]) > 1:
        root_logger.error("too many arguments")
        raise ValueError

    if len(sys.argv[1:]) == 1:
        if sys.argv[1] != "-s":
            root_logger.error("an unexpected argument")
            raise ValueError

        root_logger = logging.getLogger("double_output")

    test_func(root_logger)
