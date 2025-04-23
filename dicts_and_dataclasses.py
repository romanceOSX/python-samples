# we can refer to foo.var inside foo, but the declaration has to be run once
def foo():
    if not hasattr(foo, "counter"):
        foo.counter = 0
    foo.counter += 1

    print("doing some work in foo()")
    print(f"foo() called {foo.counter} times")

# we can also take a more functional approach and declare it as an upvalue inside a decorator
def count_calls(f):
    call_counter = 0
    def wrap():
        f()
        count_calls.call_counter += 1
        print(f"{f.__name__} called {call_counter} times")
    return wrap

@count_calls
def bar():
    print("doing some work in bar()")

def main():
    foo()
    foo()
    foo()
    foo()
    bar()
    bar()
    bar()
    bar()
    bar()

if __name__ == "__main__":
    main()

