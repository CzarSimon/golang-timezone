import os

import config
import file_handler


conf = config.Config()


exit_success = 0


def build_and_push():
    exit_code = _run_command(_get_build_command())
    if exit_code != exit_success:
        print "build failed!"
        return
    exit_code = _run_command(_get_push_command())
    if exit_code != exit_success:
        print "push failed!"
        return
    print "Successfully built and pushed image"


def _run_command(cmd):
    print cmd
    return os.system(cmd)


def _get_build_command():
    return " ".join([
        "docker",
        "build",
        "-t",
        _format_image_name(),
        file_handler.create_path(conf)
    ])


def _get_push_command():
    return "docker push {}".format(_format_image_name())


def _format_image_name():
    return "{}:{}".format(config.BASE_IMAGE_NAME, conf.go_tag)


def main():
    file_handler.create_dockerfile(conf)
    build_and_push()


if __name__ == '__main__':
    main()
