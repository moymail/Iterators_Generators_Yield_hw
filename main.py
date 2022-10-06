nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]

# 1. Итератор, который принимает список списков, и возвращает их плоское представление.


class FlatIterator:

    def __init__(self, new_list):
        self.new_list = [object for item in nested_list for object in item]

    def __iter__(self):
        self.cursor = -1
        return self

    def __next__(self):
        self.cursor += 1
        if self.cursor == len(self.new_list):
            raise StopIteration
        return self.new_list[self.cursor]


if __name__ == '__main__':

    for element in FlatIterator(nested_list):
        print(element)

    flat_list = [item for item in FlatIterator(nested_list)]
    print(flat_list)

# 2. Генератор, который принимает список списков, и возвращает их плоское представление.


def flat_generator(new_list_1):
    for item in new_list_1:
        for elem in item:
            yield elem


if __name__ == '__main__':

    for item_1 in flat_generator(nested_list):
        print(item_1)
