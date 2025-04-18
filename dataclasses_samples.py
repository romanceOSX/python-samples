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

def main() -> None:
    a = {}
    a["hello"] = []

    f = Foo()
    # getattr works even on user-types
    a = getattr(f, "hello", "hello")
    print(f"value of {a=}")

@dataclass
class DiscoveryEntry:
    """Class for keeping discovery entries!"""
    name: str
    ip: str

if __name__ == "__main__":
    main()
