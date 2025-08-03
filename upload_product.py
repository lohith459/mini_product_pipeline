import requests
import json

# Replace with your own values
SHOP_NAME = "lohith-merch-store"
ACCESS_TOKEN = "keep your token " # Replace with your actual Admin API token

# API Endpoint to create a product
url = f"https://{SHOP_NAME}.myshopify.com/admin/api/2023-07/products.json"

# Sample product data (you can make it dynamic from product.json)
product_data = {
    "product": {
        "title": "AI Generated T-shirt",
        "body_html": "<strong>A cool shirt created with AI idea!</strong>",
        "vendor": "LohithDev",
        "product_type": "T-shirt",
        "tags": ["AI", "T-shirt", "Fashion"],
        "images": [
            {
                "src": "https://placehold.co/512x512/black/white?text=AI+Tshirt"
            }
        ]
    }
}

# Headers for authentication
headers = {
    "Content-Type": "application/json",
    "X-Shopify-Access-Token": ACCESS_TOKEN
}

# POST request to create product
response = requests.post(url, headers=headers, data=json.dumps(product_data))

# Print response
if response.status_code == 201:
    print("✅ Product uploaded successfully!")
    print("🛍 Product info:", response.json())
else:
    print("❌ Upload failed!")
    print("Status Code:", response.status_code)
    print("Response:",response.text)