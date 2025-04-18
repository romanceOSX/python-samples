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

    # this is just unpacking a sequence btw
    a = [1, 2, 3, 4, 5]
    b = [*a]
    print(f"{b=}")

    # same case for dictionaries
    custom_dict = {**kwargs}
    print(f"{custom_dict=}")

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

# examples on matching dictionaries
def _match_dict():
    my_dict = {
        'type': 'book',
        'authors': [
            'William',
            'Cornellious'
        ],
        'author': "mcKensey"
    }

    match my_dict:
        case {'type': 'book', 'authors': name}:
            print(f'{name=}, {type(name)=}')

def _get_attribute():
    a = {}
    a["hello"] = []

    f = Foo()
    # getattr works even on user-types
    # object, attribute, default value
    a = getattr(f, "hello", "hello")
    print(f"value of {a=}")

@dataclass
class DiscoveryEntry:
    """Class for keeping discovery entries!"""
    name: str = None
    ip: str = None

class Table:
    def __init__(self) -> None:
        self._table: list[DiscoveryEntry] = [
            DiscoveryEntry("hello", "172.16.0.2")
        ]

    def append(self, entry: DiscoveryEntry):
        self._table.append(entry)

    def get_entry(self, ip: str):
        entry = {entry.ip: entry for entry in self._table}
        return entry.get(ip, None)
    
    def __repr__(self) -> str:
        return f"{self._table!r}"

def _dataclass_test():
    table = Table()
    a = table.get_entry("172.16.0.2")
    print(f"This is the table after gett-ign {table=}")
    print(f"This is the value of {a=}")
    entry = DiscoveryEntry()
    print(f"This is my {entry=}")
    # indexing strategies
    pass

def main() -> None:
    #_get_attribute()
    #_dict_comprehensions()
    #_match_dict()
    _dataclass_test()

if __name__ == "__main__":
    main()

