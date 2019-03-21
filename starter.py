#!/usr/bin/env python3
from majestoc_resa import create_app
import argparse
import os


def parse_args(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', '-c', help='Path to a config file')
    return parser.parse_args(argv)


def get_full_path(file_path=None):
    full_path = None
    if file_path:
        basedir = os.path.abspath(os.path.dirname(__file__))
        full_path = os.path.join(basedir, file_path)
    return full_path


def main(argv=None):
    args = parse_args(argv)
    app = create_app(get_full_path(args.config))
    app.run()


if __name__ == "__main__":
    main()
