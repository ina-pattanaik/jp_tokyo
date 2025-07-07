# utils/helpers.py
import random

def generate_username():
    return f"user{random.randint(10000, 99999)}"

