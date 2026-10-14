# Mini Python Toolkit

A small Python package containing examples of basic utilities and tests written
with pytest.

## Requirements

- Python 3.12 or newer

## Install

From the project root, install the package and its development dependencies:

```bash
python -m pip install -e ".[dev]"
```

## Usage

### Calculator

```python
from toolkit import calculator

calculator.add(2, 3)       # 5
calculator.subtract(5, 2) # 3
calculator.multiply(3, 4) # 12
calculator.divide(8, 2)   # 4.0
```

`calculator.divide(a, 0)` raises `ValueError`.

### Text utilities

```python
from toolkit import text_utils

text_utils.reverse_text("hello")                # "olleh"
text_utils.is_palindrome("A man, a plan, a canal: Panama")  # True
text_utils.count_words("hello world")           # 2
```

Palindrome checks ignore capitalization and non-alphanumeric characters.

### Bank account

```python
from toolkit.bank import BankAccount, InsufficientFundsError

account = BankAccount(100)
account.deposit(25)
account.withdraw(40)
print(account.balance)  # 85
```

Starting balances cannot be negative, and deposits and withdrawals must be
positive. Withdrawing more than the available balance raises
`InsufficientFundsError`.

### Todo list

```python
from toolkit.todo import TodoList

todo = TodoList()
todo.add_task("Write documentation")
todo.save("tasks.json")

restored = TodoList()
restored.load("tasks.json")
print(restored.tasks)  # ["Write documentation"]
```

Removing a task that is not in the list raises `ValueError`. Loading a
nonexistent file raises `FileNotFoundError`.

## Run the tests

```bash
python -m pytest
```

The test suite covers the calculator, text utilities, bank account, and todo
list.
