from flask import Flask, jsonify, send_from_directory, abort, render_template
import os
import json

app = Flask(__name__)

ROOT = os.getcwd()
OUTPUT_DIR = os.path.join(ROOT, 'output')
ENHANCED_IMG_DIR = os.path.join(OUTPUT_DIR, 'enhanced_images')
JSON_FILE = os.path.join(OUTPUT_DIR, 'enriched_data.json')
PDF_FILE = os.path.join(OUTPUT_DIR, 'product_brochure.pdf')

with open(JSON_FILE, 'r', encoding='utf-8') as f:
    products = json.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/products')
def list_products():
    html = """
    <h1>Samsung Products</h1>
    <table border="1" cellpadding="10" cellspacing="0" width="100%">
        <tr>
            <th>Product</th>
            <th>Price</th>
            <th>Weight (kg)</th>
            <th>Image</th>
            <th>Details</th>
        </tr>
    """
    for p in products:
        img_url = f"/images/{os.path.basename(p.get('Enhanced Image Path',''))}"
        html += f"""
        <tr>
            <td>{p.get('Product')}</td>
            <td>{p.get('Price (INR)')}</td>
            <td>{p.get('Weight (kg)')}</td>
            <td><img src="{img_url}" alt="{p.get('Product')}" width="100"></td>
            <td><a href="/products/{p.get('ID')}">View Details</a></td>
        </tr>
        """
    html += "</table><p><a href='/'>Back to Home</a></p>"
    return html

@app.route('/products/<int:product_id>')
def get_product_page(product_id):
    product = next((p for p in products if p.get('ID') == product_id), None)
    if not product:
        abort(404, description="Product not found")
    img_url = f"/images/{os.path.basename(product.get('Enhanced Image Path',''))}"
    html = f"""
    <h1>{product.get('Product')}</h1>
    <img src="{img_url}" alt="{product.get('Product')}" width="300"><br><br>
    <ul>
        <li>Price: {product.get('Price (INR)')}</li>
        <li>Weight: {product.get('Weight (kg)')} kg</li>
        <li>Dimensions: {product.get('Dimensions')}</li>
        <li>Storage: {product.get('Storage')}</li>
        <li>Battery Life: {product.get('Battery Life')}</li>
        <li>Water Resistance: {product.get('Water Resistance')}</li>
        <li>Camera: {product.get('Camera')}</li>
        <li>Processor: {product.get('Processor')}</li>
        <li>Material: {product.get('Material')}</li>
    </ul>
    <p><a href="/products">Back to Products</a></p>
    <p><a href="/">Back to Home</a></p>
    """
    return html

@app.route('/images/<path:image_name>')
def get_image(image_name):
    image_path = os.path.join(ENHANCED_IMG_DIR, image_name)
    if os.path.exists(image_path):
        return send_from_directory(ENHANCED_IMG_DIR, image_name)
    else:
        abort(404, description="Image not found")

@app.route('/brochure')
def get_brochure():
    if os.path.exists(PDF_FILE):
        return send_from_directory(OUTPUT_DIR, 'product_brochure.pdf')
    else:
        abort(404, description="Brochure not found")

if __name__ == '__main__':
    app.run(debug=True)
