class Color:

    def __init__(self, id, name, hexcode):
        self.id = id
        self.name = name
        self.hexcode = hexcode


class ColorList:

    def __init__(self, logger):
        self._colors = []
        self._logger = logger

    def append(self, color_name, color_hexcode):

        new_color = Color(
            max([color.id for color in self._colors] or [0]) + 1,
            color_name,
            color_hexcode
        )

        self._colors.append(new_color)
        self._logger.log(f"appended new color: {new_color.id}")

    def __iter__(self):
        return self._colors.__iter__()

    def __next__(self):
        return self._colors.__next__()
