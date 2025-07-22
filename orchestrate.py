import subprocess
import json
import requests

# Step 1: Generate content
print("Generating product content...")
content = subprocess.run(
    ["python3", "../python_content/generate_product.py"],
    capture_output=True, text=True
)
product_data = json.loads(content.stdout)

# Save to input file for JS
with open("../js_mockup/input.json", "w") as f:
    json.dump(product_data, f)

# Step 2: Run mock visualizer
print("Running mock visualizer...")
subprocess.run(["node", "../js_mockup/mock_image.js"])

# Load visualized data
with open("../js_mockup/output.json") as f:
    mock_product = json.load(f)

# Step 3: Publish to fake API
print("Publishing to PHP API...")
response = requests.post("http://localhost/php_publisher/publish.php", json=mock_product)

print("Response from Publisher:\n", response.json())