# from text_logger import TextLogger

# logger = TextLogger("log.txt")


# logger = CsvLogger('log.csv')

import sys
from dependency_injector import containers, providers
from dependency_injector.wiring import inject, Provide
from colors import ColorList
from text_logger import TextLogger
from csv_logger import CsvLogger


class TextLoggerContainer(containers.DeclarativeContainer):

    logger_service = providers.Factory(TextLogger, file_name="log.txt")

    colors_list_service = providers.Factory(
        ColorList,
        logger=logger_service
    )


class CsvLoggerContainer(containers.DeclarativeContainer):

    logger_service = providers.Factory(CsvLogger, file_name="log.csv")

    colors_list_service = providers.Factory(
        ColorList,
        logger=logger_service
    )


def select_logger(use_csv=False):
    if use_csv:
        return providers.Factory(CsvLogger, file_name="log.csv")
    else:
        return providers.Factory(TextLogger, file_name="log.txt")


class Container(containers.DeclarativeContainer):

    logger_service = select_logger(True)

    colors_list_service = providers.Factory(
        ColorList,
        logger=logger_service
    )


# logger = TextLogger('log.txt')


# color_list = ColorList(logger)

@inject
def main(color_list=Provide[Container.colors_list_service]):

    color_list.append("red", "ff0000")
    color_list.append("green", "00ff00")
    color_list.append("blue", "0000ff")

    for color in color_list:
        print(color.id, color.name, color.hexcode)


container = Container()
container.wire(modules=[sys.modules[__name__]])

main()
