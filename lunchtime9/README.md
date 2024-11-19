# Lunchtime #9: mypy

[mypy](https://mypy.readthedocs.io/en/stable/) is a static type checker for Python.
By adding type annotations to your code mypy can find a variety of bugs.
These type annotations also act as machine-checked documentation of your code,
and your IDE can make use of them to improve its code completion.
They don't affect how your program runs, as the Python interpreter ignores
these type annotations at run-time