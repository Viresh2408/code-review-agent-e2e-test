"""Unit tests for billing branch coverage."""

import pytest
from app.billing import apply_discount


def test_apply_discount_empty_promo():
    with pytest.raises(ValueError):
        apply_discount(1, 100.0, "")

def test_apply_discount_save50():
    assert apply_discount(1, 100.0, "SAVE50") == 50.0

def test_apply_discount_vip():
    assert apply_discount(1, 100.0, "VIP-123") == 75.0

def test_apply_discount_no_promo():
    assert apply_discount(1, 100.0, "OTHER") == 100.0
