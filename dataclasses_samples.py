from dataclasses import dataclass
from ipaddress import IPv4Address, IPv6Address
import dataclasses

class Foo:
    def __init__(self) -> None:
        self._discovery_table = {}

    def __getattr__(self, name: str):
        print("gettattribute called")
        if name not in self._discovery_table:
            raise AttributeError(f"{name!r} not found")
        return self._discovery_table[name]

def _dict_comprehensions():
    print("Testing dict comprehensions")
    list_of_tuples = [
        ('a', 'Hello'),
        ('b', 'Hola'),
        ('c', '你好'),
    ]

    # swapping the key and values
    # same as list comprehensions, <functor> for <value(s)> in <iterable>
    list_of_tuples_swapped = {hello: letter for letter, hello in list_of_tuples}

    print(f"Printing dict: {list_of_tuples_swapped}")

def main() -> None:
    a = {}
    a["hello"] = []

    f = Foo()
    # getattr works even on user-types
    # object, attribute, default value
    a = getattr(f, "hello", "hello")
    print(f"value of {a=}")

    _dict_comprehensions()

@dataclass
class DiscoveryEntry:
    """Class for keeping discovery entries!"""
    name: str
    ip: str

if __name__ == "__main__":
    main()
