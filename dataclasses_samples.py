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

def dump(**kwargs):
    print(f"The type of {kwargs=} is {type(kwargs)=}")

# --> https://docs.python.org/3/tutorial/controlflow.html#special-parameters
# *args is a tuple of the other positional arguments
# **dict is a dictionary
def foo_arguments(pos1, pos2, *args, **kwargs):
    print(f"{pos1=}, {type(pos1)=}")
    print(f"{args=}, {type(args)=}")
    print(f"{kwargs=}, {type(kwargs)=}")

    # unpacking arguments
    # --> https://docs.python.org/3/tutorial/controlflow.html#special-parameters
    # same as packing but reversed
    print(*args, sep="\n")
    print(*args, **kwargs)

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

    packet_arguments = {
        "a": 32,
    }

    foo_arguments(1, 2, 3, 4, 5, 6, 7, sep="♥️")

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
