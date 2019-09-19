#!/usr/bin/env python3.7
from csv_transform import transform
import sys

def get_name(**kwargs):
    return kwargs['name']

if __name__ == "__main__":

    if len(sys.argv) < 3:
        print("Usage: python3 example.py input.csv output.csv")

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    output_mapping = [
        ('id', lambda **kwargs: kwargs['id']),
        ('name', lambda **kwargs: kwargs['name']),
        # Drop age
    ]

    transform(input_path, output_path, output_mapping)
