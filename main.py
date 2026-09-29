from expense_manager import ExpenseManager


manager = ExpenseManager()


def test_add_expense():

    expense_id = manager.add_expense(
        "Food",
        "Food",
        150,
        "29-09-2026"
    )

    assert expense_id == 1


def test_search_expense():

    expense = manager.search_expense(1)

    assert expense is not None
    assert expense["amount"] == 150


def test_delete_expense():

    result = manager.delete_expense(1)

    assert result == True


print("All tests completed successfully.")