import openai
import json
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI(api_key="your_api_key")  #  Replace with your actual API key

# Generate product idea from ChatGPT
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "Generate a fun T-shirt product idea with title, description, and tags"}
    ]
)

# Extract content from response
product_idea = response.choices[0].message.content

# Optional: Print raw result
print("🔹 Raw Idea:", product_idea)

#  Static image URL (you can replace this)
image_url = "https://placehold.co/512x512/black/white?text=AI+Tshirt"

#  Create final product data
product_data = {
    "idea": product_idea,
    "image_url": image_url
}

# Save to product.json file
with open("product.json", "w") as f:
    json.dump(product_data, f, indent=4)

print(" Product idea saved to product.json")