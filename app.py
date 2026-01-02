from flask import Flask, request, jsonify

app = Flask(__name__)

def thermal_solver(Q, num_fins):
    # Geometric and material constants
    T_ambient = 25.0
    air_velocity = 1.0
    die_area = 0.002363
    sink_length = 0.09
    sink_width = 0.116
    base_thickness = 0.0025
    fin_thickness = 0.0008
    k_aluminum = 167.0
    k_tim = 4.0
    tim_thickness = 0.0001
    k_air = 0.0262
    nu_air = 1.57e-05
    Pr_air = 0.71
    A_total = 0.275040

    # Individual thermal resistances
    R_jc = 0.2
    R_TIM = tim_thickness / (k_tim * die_area)
    R_cond = base_thickness / (k_aluminum * die_area)

    # Convection physics logic
    S_f = (sink_width - (num_fins * fin_thickness)) / (num_fins - 1)
    Re = (air_velocity * S_f) / nu_air
    Nu = 1.86 * (Re * Pr_air * (2 * S_f / sink_length))**(1/3)
    h = Nu * (k_air / (2 * S_f))
    R_conv = 1 / (h * A_total)

    # Total resistance and junction temperature
    R_total = R_jc + R_TIM + R_cond + R_conv
    T_junction = T_ambient + (Q * R_total)
    
    return T_junction, R_total

@app.route('/calculate', methods=['GET'])
def calculate():
    # Extract parameters from the URL or use default values
    Q = float(request.args.get('power', 150.0))
    fins = int(request.args.get('num_fins', 60))
    
    temp, resistance = thermal_solver(Q, fins)
    
    return jsonify({
        "junction_temperature_C": round(temp, 2),
        "total_resistance_CW": round(resistance, 4)
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)