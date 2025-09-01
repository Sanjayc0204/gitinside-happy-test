import pytest
from main import add_days_to_date, get_days_between

def test_add_days_to_date():
    assert add_days_to_date("2023-01-01", 5) == "2023-01-06"
    assert add_days_to_date("01/15/2023", -5) == "2023-01-10"
    with pytest.raises(ValueError):
        add_days_to_date("invalid-date", 5)

def test_get_days_between():
    assert get_days_between("2023-01-01", "2023-01-10") == 9
    assert get_days_between("2023-12-31", "2024-01-01") == 1
    with pytest.raises(ValueError):
        get_days_between("invalid", "2023-01-01")