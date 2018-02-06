import argparse


BASE_IMAGE_NAME = "czarsimon/golang-timezone"


# Default tags
_DEFAULT_GO_TAG = "1.8-alpine3.6"
_DEFAULT_OS_NAME = "alpine"
_DEFAULT_OS_TAG = "3.6"


class Config(object):
    def __init__(self):
        parser = _setup_argparser()
        args = parser.parse_args()
        self.go_tag = args.go_tag
        self.os_name = args.os_name
        self.os_tag = args.os_tag


def _setup_argparser():
    parser = argparse.ArgumentParser(
        description='Builds a golang-timezone image with a specified go version and target os')
    parser.add_argument("--go-tag", default=_DEFAULT_GO_TAG)
    parser.add_argument("--os-name", default=_DEFAULT_OS_NAME)
    parser.add_argument("--os-tag", default=_DEFAULT_OS_TAG)
    return parser
