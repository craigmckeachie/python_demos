import json
import csv
import yaml


class DictionaryList:

    def __init__(self):
        self._items = []

    def __next_id(self):
        if not self._items:
            return 1
        else:
            return max([item["id"] for item in self._items]) + 1

    def append(self, **item):

        item["id"] = self.__next_id()
        self._items.append(item)
        return self

    def to_console(self):

        for item in self._items:
            for key in sorted(item):
                print(f"{key}: {item[key]}")


class JsonOutputMixin:

    def to_json(self):
        return json.dumps(self._items)


class CsvOutputMixin:

    def to_csv(self, csv_file_name):

        with open(csv_file_name, "w") as csv_file:
            csv_writer = csv.DictWriter(csv_file, self._items[0])
            csv_writer.writeheader()
            for item in self._items:
                csv_writer.writerow(item)


class YamlOutputMixin:

    def to_yaml(self):
        return yaml.dump(self._items)


class ColorList(DictionaryList, JsonOutputMixin, CsvOutputMixin,
                YamlOutputMixin):

    def append(self, color_name, color_hexcode):
        super().append(name=color_name, hexcode=color_hexcode)


def main():

    colors = ColorList()
    colors.append("red", "ff0000")
    colors.append("green", "00ff00")
    colors.append("blue", "0000ff")

    colors.to_console()

    print(colors.to_json())

    colors.to_csv("colors.csv")

    print(colors.to_yaml())


if __name__ == "__main__":
    main()
