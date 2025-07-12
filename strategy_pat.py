from abc import ABC, abstractmethod

# small strategy pattern code

class SortAlgo(ABC):
    @abstractmethod
    def sort(self, data):
        pass

class ShortSortAlgo(SortAlgo):
    def sort(self, data):
        pass

# this would be my 'context' class
class Sorter:
    def __init__(self, data, sorter: SortAlgo) -> None:
        self._sort: SortAlgo = sorter
        self._data = data

    def sort(self) -> None:
        self._sort.sort(self._data)

def main() -> None:
    sorter = Sorter(bytes.fromhex("1a2b3c"), ShortSortAlgo())
    sorter.sort()

if __name__ == "__main__":
    main()

