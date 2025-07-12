from abc import ABC, abstractmethod

# ELEMENTS
# - strategy interface
# - concrete strategies
# - context
# - client

# DOUBTS
#
# Where should we introduce the arguments the strategy needs to operate on?
#   Normally these are introduced when calling the context calls the strategy itself
#   this because we don't want to couple the context with the data
#   Yes Sometimes this coupling is preffered
#
# Why not just skip the context?
#   The context's role is doing the 'How', while the client's role is declaring
#   the 'What', if we ever need to change the strategie's signature, the client
#   won't suffer any changes, also common business logic such as validating data
#   sanity checks or switching strategies are runtime, is better done through a
#   context, this is the end goal of separation of concerns

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

