"""Billing module — SECURED version."""


def apply_discount(user_id: int, amount: float, promo_code: str) -> float:
    if not promo_code:
        raise ValueError("Promo code cannot be empty")
    if promo_code == "SAVE50":
        return amount * 0.5
    elif promo_code.startswith("VIP-"):
        return amount * 0.75
    return amount
