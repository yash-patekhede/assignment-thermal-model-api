import math

# Processor physical specifications
die_area = 0.002363      # Square meters
Q = 150.0                # Thermal Design Power in Watts

# Heat sink geometric parameters
sink_length = 0.09       # Meters
sink_width = 0.116       # Meters
base_thickness = 0.0025  # Meters
num_fins = 60            
fin_thickness = 0.0008   # Meters
fin_height = 0.0245      # Meters

# Material and interface properties
k_aluminum = 167.0       # Thermal conductivity in W/m·K
k_tim = 4.0              # Thermal conductivity of interface material in W/m·K
tim_thickness = 0.0001   # Interface layer thickness in meters

# Cooling medium properties for air at 25 degrees Celsius
T_ambient = 25.0         # Degrees Celsius
k_air = 0.0262           # Thermal conductivity in W/m·K
nu_air = 1.57e-05        # Kinematic viscosity in m^2/s
Pr_air = 0.71            # Prandtl Number
air_velocity = 1.0       # Inlet air velocity in m/s

# Thermal resistance components
R_jc = 0.2               # Junction to case thermal resistance in C/W
R_TIM = tim_thickness / (k_tim * die_area)    # Case to interface resistance
R_cond = base_thickness / (k_aluminum * die_area)  # Conduction through base

# Convection characteristics and calculations
# Determine fin spacing and flow Reynolds number
S_f = (sink_width - (num_fins * fin_thickness)) / (num_fins - 1)
Re = (air_velocity * S_f) / nu_air

# Calculate Nusselt number and convection coefficient
Nu = 1.86 * (Re * Pr_air * (2 * S_f / sink_length))**(1/3)
h = Nu * (k_air / (2 * S_f))

# Total heat transfer surface area for convection
A_total = 0.275040       # Total wetted surface area in square meters

# Final convection resistance calculation
R_conv = 1 / (h * A_total)

# Total thermal system resistance summation
R_total = R_jc + R_TIM + R_cond + R_conv

# Final operating temperature of the junction
T_junction = T_ambient + (Q * R_total)

# Display results
print(f"Thermal Resistance Network Results")
print(f"Resistance Junction to Case: {R_jc:.6f} C/W")
print(f"Resistance of TIM:           {R_TIM:.6f} C/W")
print(f"Resistance of Base:          {R_cond:.6f} C/W")
print(f"Resistance of Convection:    {R_conv:.6f} C/W")
print(f"Total System Resistance:     {R_total:.6f} C/W")
print(f"Calculated Junction Temp:    {T_junction:.2f} C")