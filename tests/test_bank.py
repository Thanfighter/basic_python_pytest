import pytest
from toolkit.bank import BankAccount, InsufficientFundsError


@pytest.fixture
def account():
    return BankAccount(100)


def test_starting_balance(account):
    assert account.balance == 100


def test_default_balance_is_zero():
    assert BankAccount().balance == 0


def test_deposit(account):
    account.deposit(50)
    assert account.balance == 150


def test_withdraw(account):
    account.withdraw(30)
    assert account.balance == 70


def test_withdraw_everything(account):
    account.withdraw(100)
    assert account.balance == 0


def test_withdraw_too_much_raises_error(account):
    with pytest.raises(InsufficientFundsError):
        account.withdraw(500)


def test_failed_withdraw_keeps_balance(account):
    with pytest.raises(InsufficientFundsError):
        account.withdraw(500)
    assert account.balance == 100


@pytest.mark.parametrize("bad_amount", [0, -10])
def test_deposit_invalid_amount(account, bad_amount):
    with pytest.raises(ValueError):
        account.deposit(bad_amount)


@pytest.mark.parametrize("bad_amount", [0, -10])
def test_withdraw_invalid_amount(account, bad_amount):
    with pytest.raises(ValueError):
        account.withdraw(bad_amount)


def test_negative_starting_balance_raises_error():
    with pytest.raises(ValueError):
        BankAccount(-5)