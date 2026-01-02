# Thermal Model API
A Flask-based API that calculates the junction temperature of a heat sink based on design parameters.

## How to Run
1. Install dependencies: `pip install -r requirements.txt`
2. Start the server: `python app.py`
3. Access in browser: `http://127.0.0.1:5000/calculate?power=150&num_fins=60`

## Validation
The model is validated against engineering reference data. The simulation yields the following results:

* **Junction Temperature ($T_j$):** 80.97°C
* **Total Thermal Resistance ($R_{total}$):** 0.3731 °C/W
