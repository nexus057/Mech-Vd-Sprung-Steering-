import math

# =========================
# INPUT PARAMETERS
# =========================

wheel_width = 406.4             #Wheel width [mm]
L = 1550                        # Wheelbase [mm]
t_f = 1200 + wheel_width        # Front track width [mm]
R_target = 4000                 # Target turning radius [mm]


# =========================
# ACKERMANN GEOMETRY
# =========================

# Inner wheel steering angle
delta_i = math.atan(L / (R_target - t_f / 2))

# Outer wheel steering angle
delta_o = math.atan(L / (R_target + t_f / 2))

# Convert radians to degrees
delta_i_deg = math.degrees(delta_i)
delta_o_deg = math.degrees(delta_o)


# =========================
# TURNING RADIUS CHECK
# =========================

R_check = L / math.tan(delta_i) + t_f / 2


# =========================
# OUTPUT
# =========================

print("Ackermann Steering Geometry")
print("---------------------------")

print("Wheelbase:", L, "mm")
print("Front track:", t_f, "mm")

print("Inner wheel angle:", delta_i_deg, "degrees")
print("Outer wheel angle:", delta_o_deg, "degrees")

print("Turning radius:", R_check, "mm")
print("Turning radius:", R_check / 1000, "m")
