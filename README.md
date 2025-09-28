# Admission Prediction Web App

This project is a web application for predicting the chance of admission based on user input features using a machine learning model trained on university admission data.

## Features
- User-friendly web interface for inputting scores and other details
- Machine learning model (Linear Regression) for prediction
- Visualization and data analysis in Jupyter Notebook

## Technologies Used
- Python (Flask, scikit-learn, pandas, numpy, matplotlib, seaborn)
- HTML, CSS, JavaScript

## Setup Instructions
1. Clone or download this repository.
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run the Flask app:
   ```
   python app.py
   ```
4. Open your browser and go to `http://127.0.0.1:5000`

## File Structure
- `app.py` - Flask backend
- `model.ipynb` - Jupyter notebook for data analysis and model training
- `admission_model.pkl` - Saved machine learning model
- `templates/index.html` - Web page template
- `static/style.css` - CSS styles
- `static/script.js` - JavaScript for frontend
- `requirements.txt` - Python dependencies

## Usage
1. Enter your GRE, TOEFL, CGPA, University Rating, SOP, LOR, and Research experience in the form.
2. Click "Predict" to see your predicted chance of admission.

## License
This project is for educational purposes.
