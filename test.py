def greet(name: str) -> str:
    """Return a greeting for name."""
    return f"Hello, {name}!"


def add(a: int, b: int) -> int:
    """Return the sum of a and b."""
    return a + b


if __name__ == "__main__":
    # quick self-checks
    assert greet("World") == "Hello, World!"
    assert add(2, 3) == 5
    print(greet("World"))
    print("add(2,3)=", add(2,3))
    print("test.py self-checks passed")
