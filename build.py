import config
import file_handler


conf = config.Config()


def build():
    image_name = _format_image_name()
    print image_name


def _format_image_name():
    return "{}:{}".format(config.BASE_IMAGE_NAME, conf.go_tag)


def main():
    file_handler.create_dockerfile(conf)
    build()


if __name__ == '__main__':
    main()
