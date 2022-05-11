"""module with utils functions"""
import argparse


def server_args_parser():
    """args parser for server"""
    parser = argparse.ArgumentParser(description='server_args')

    parser.add_argument('-w', type=int, default=5, help='number of workers')
    parser.add_argument('-k', type=int, default=5, help='top size')
    args = parser.parse_args()
    return args


def client_args_parser():
    """args parser for client"""
    parser = argparse.ArgumentParser(description='client_args')

    parser.add_argument('-m', type=int, default=5, help='number of threads')
    parser.add_argument('-p', type=str, default="urls.txt", help='path')
    args = parser.parse_args()
    return args
