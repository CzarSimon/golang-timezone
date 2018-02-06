import os


_DOCKERFILE = "resources" + os.sep + "dockerfile-template"
_BASE_PATH = "dockerfiles"
_GO_TAG_KEY = "{$GO_TAG}"
_OS_NAME_KEY = "{$OS_NAME}"
_OS_TAG_KEY = "{$OS_TAG}"


def create_dockerfile(conf):
    dockerfile_template = _get_dockerfile_template()
    dockerfile_content = _populate_dockerfile(dockerfile_template, conf)
    _write(dockerfile_content, create_path(conf))


def create_path(conf):
    return os.sep.join([
        ".",
        _BASE_PATH,
        conf.os_name,
        conf.go_tag
    ])


def _populate_dockerfile(template, conf):
    return reduce(lambda str, kv: str.replace(*kv), _create_replace_tuples(conf), template)


def _write(dockerfile_content, path):
    filename = path + os.sep + "Dockerfile"
    print "Dockerfile:\n{}-------\n".format(dockerfile_content)
    _create_file_if_not_exists(filename)
    with open(filename, 'w') as f:
        f.write(dockerfile_content)


def _create_file_if_not_exists(filename):
    if not os.path.exists(os.path.dirname(filename)):
        try:
            os.makedirs(os.path.dirname(filename))
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise


def _get_dockerfile_template():
    with open(_DOCKERFILE, 'r') as f:
        return f.read()


def _create_replace_tuples(conf):
    return [
        (_GO_TAG_KEY, conf.go_tag),
        (_OS_NAME_KEY, conf.os_name),
        (_OS_TAG_KEY, conf.os_tag)
    ]
