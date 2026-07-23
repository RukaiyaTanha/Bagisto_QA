# utils/data_reader.py
import json
import csv
import random
import string
import time


def load_json_data(filename):
    """Reads a JSON file from the test_data folder, returns a Python list/dict"""
    with open(f"test_data/{filename}", "r") as file:
        return json.load(file)


def load_csv_data(filename):
    """Reads a CSV file from test_data folder, returns a list of dictionaries"""
    with open(f"test_data/{filename}", "r") as file:
        reader = csv.DictReader(file)
        return list(reader)


def generate_unique_sku(prefix="test-product"):
    """Generates a unique SKU using the current timestamp"""
    return f"{prefix}-{int(time.time())}"


def generate_random_email():
    """Generates a random fake email"""
    random_string = ''.join(random.choices(string.ascii_lowercase, k=8))
    return f"{random_string}@example.com"


def generate_random_string(length=8):
    """Generates a random string of given length"""
    return ''.join(random.choices(string.ascii_letters, k=length))