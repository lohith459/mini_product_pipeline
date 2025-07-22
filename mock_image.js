// js_mockup/mock_image.js
const fs = require('fs');

const mockVisualizer = (productData) => {
  return new Promise((resolve) => {
    const mockImageUrl = productData.image_url + "?mock=true";
    const result = {
      product_id: "mock123",
      title: productData.title,
      image_url: mockImageUrl
    };
    resolve(result);
  });
};

const input = fs.readFileSync('input.json', 'utf-8');
const product = JSON.parse(input);

mockVisualizer(product).then(result => {
  fs.writeFileSync('output.json', JSON.stringify(result, null, 2));
});