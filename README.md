# LAB - Class 42

## Project: Pythonisms

### Author: Negin Koushkakinejad

Overview:

The "pythonisms" project demonstrates the use of Pythonic language features to make code more readable, elegant, and efficient. By leveraging iterators/generators, decorators, and dunder (special) methods, we can write code that is not only functional but also clear and concise.

Iterators/Generators:

The BinaryTree class uses an in-order traversal generator to allow iteration through its nodes. This enables the tree to be used in for-loops, list comprehensions, and conversion to list or other collection types.

Decorators:

The timer decorator is used to measure the execution time of functions. This can be useful for debugging, optimization, or simply understanding the performance of different parts of the code.

Dunder Methods:

The BinaryTree class implements several dunder methods to enhance its usability and integration with Python's built-in features:

__str__: Returns a string representation of the tree as a list of its values.
__repr__: Provides a more detailed representation, useful for debugging.
__eq__: Allows comparison of two trees based on their values.
__bool__: Enables truth value testing, with an empty tree evaluating to False.


How to initialize/run your application:

create a new virtual environment named pythonisms-env and activate it:
python3 -m venv pythonisms-env
source pythonisms-env/bin/activate

How do you run tests?

pip install pytest

pytest
