# 📦 Samsung Product MDM Web App

This is a Flask-based web application designed for **Master Data Management (MDM)** of Samsung consumer electronics. It visualizes, serves, and presents normalized product data from a CSV, enriched into structured JSON and brochure-style PDF formats.

## 🚀 Features

- Displays Samsung product data (price, weight, specs, image)
- View all products or a detailed page per product
- Serves enhanced product images and downloadable brochures
- JSON and PDF are generated from the data pipeline

## 📁 Project Structure

```
samsung-mdm-app/
│
├── app.py                         # Flask backend
├── Samsung_MDM.ipynb              # Notebook for data processing & JSON/PDF generation
├── samsung_products.csv           # Source product data
├── output/                        # Generated assets
│   ├── enhanced_images/           # Enhanced product images
│   ├── enriched_data.json         # Structured product data
│   └── product_brochure.pdf       # Brochure-style product catalog
├── templates/
│   └── index.html                 # Home page template
└── README.md                      # Project documentation
```

## ⚙️ How to Run the Project

### ✅ 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/samsung-mdm-app.git
cd samsung-mdm-app
```

### ✅ 2. Install Dependencies

```bash
pip install flask pandas numpy reportlab opencv-python
```

### ✅ 3. Run the App

Make sure `output/enriched_data.json` and `output/enhanced_images/` exist before launching.

```bash
python app.py
```

Visit the app in your browser: [http://127.0.0.1:5000](http://127.0.0.1:5000)

## 📊 Key Endpoints

- `/` - Home page
- `/products` - All product listings with images
- `/products/<id>` - Individual product detail page
- `/images/<image_name>` - Serve enhanced product images
- `/brochure` - Download product brochure as PDF

## 🛠 Technologies Used

- **Flask** for backend and routing
- **Pandas/NumPy** for data preprocessing
- **OpenCV** for image enhancement
- **ReportLab** for PDF brochure generation
