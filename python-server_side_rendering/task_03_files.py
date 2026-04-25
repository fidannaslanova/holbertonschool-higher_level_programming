#!/usr/bin/python3
"""Module that displays product data from JSON or CSV files"""
from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)


def read_json():
    """Reads products from JSON file"""
    with open('products.json', 'r') as f:
        return json.load(f)


def read_csv():
    """Reads products from CSV file"""
    products = []
    with open('products.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)
    return products


@app.route('/products')
def products():
    """Route that displays products from JSON or CSV"""
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source == 'json':
        data = read_json()
    elif source == 'csv':
        data = read_csv()
    else:
        return render_template('product_display.html',
                               error="Wrong source")

    if product_id:
        data = [p for p in data if str(p['id']) == str(product_id)]
        if not data:
            return render_template('product_display.html',
                                   error="Product not found")

    return render_template('product_display.html', products=data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
