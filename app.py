from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Clothing Scraper is Running on Render!"

@app.route('/search', methods=['POST'])
def search():
    data = request.json
    print("Received:", data)

    # Fake product results
    fake_results = [
        {
            "product_name": "Brown Leather Boots",
            "price": "£129",
            "size_available": "10",
            "image_url": "https://m.media-amazon.com/images/I/81ZDyj1EmmL._AC_UY500_.jpg",
            "product_url": "https://www.amazon.co.uk/dp/B08H5P9L2L"
        },
        {
            "product_name": "White Adidas Trainers",
            "price": "£95",
            "size_available": "9",
            "image_url": "https://m.media-amazon.com/images/I/61qOT2LQfKL._AC_UX695_.jpg",
            "product_url": "https://www.adidas.co.uk/product/white-trainers"
        }
    ]

    return jsonify(fake_results)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
