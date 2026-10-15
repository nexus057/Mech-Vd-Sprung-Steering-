import math
# Suspension hardpoints, metres, vehicle coordinate system
# Assumed convention: +X = front, +Y = left, +Z = up
# "dist" = straight-line distance from the origin (your 4th column)

hardpoints = {
    # ---------------- FRONT LEFT (+X, +Y) ----------------
    "FL_UCA_FRONT":         {"x":  0.805032, "y":  0.259336, "z": 0.272263, "dist": 0.8885149538},
    "FL_UCA_REAR":          {"x":  0.705186, "y":  0.259336, "z": 0.266707, "dist": 0.7972923425},
    "FL_UPPER_BALL_JOINT":  {"x":  0.755109, "y":  0.626708, "z": 0.26701,  "dist": 1.016979282},
    "FL_LCA_FRONT":         {"x":  0.8135,   "y":  0.23,     "z": 0.16,     "dist": 0.8603965655},
    "FL_LCA_REAR":          {"x":  0.7135,   "y":  0.23,     "z": 0.16,     "dist": 0.7665391379},
    "FL_LOWER_BALL_JOINT":  {"x":  0.7635,   "y":  0.631188, "z": 0.14701,  "dist": 1.00147016},
    "FL_TIE_INNER":         {"x":  0.79,     "y":  0.259336, "z": 0.12265,  "dist": 0.8404749749},
    "FL_TIE_OUTER":         {"x":  0.79,     "y":  0.6421,   "z": 0.145,    "dist": 1.028308033},

    # ---------------- FRONT RIGHT (+X, -Y) ----------------
    "FR_UCA_FRONT":         {"x":  0.805032, "y": -0.259336, "z": 0.272263, "dist": 0.8885149538},
    "FR_UCA_REAR":          {"x":  0.705186, "y": -0.259336, "z": 0.266707, "dist": 0.7972923425},
    "FR_UPPER_BALL_JOINT":  {"x":  0.755109, "y": -0.626708, "z": 0.26701,  "dist": 1.016979282},
    "FR_LCA_FRONT":         {"x":  0.8135,   "y": -0.23,     "z": 0.16,     "dist": 0.8603965655},
    "FR_LCA_REAR":          {"x":  0.7135,   "y": -0.23,     "z": 0.16,     "dist": 0.7665391379},
    "FR_LOWER_BALL_JOINT":  {"x":  0.7635,   "y": -0.631188, "z": 0.14701,  "dist": 1.00147016},
    "FR_TIE_INNER":         {"x":  0.79,     "y": -0.259336, "z": 0.12265,  "dist": 0.8404749749},
    "FR_TIE_OUTER":         {"x":  0.79,     "y": -0.6421,   "z": 0.145,    "dist": 1.028308033},

    # ---------------- REAR LEFT (-X, +Y) ----------------
    "RL_UCA_FRONT":         {"x": -0.715542, "y":  0.258292, "z": 0.267647, "dist": 0.8064428235},
    "RL_UCA_REAR":          {"x": -0.815458, "y":  0.258292, "z": 0.2594,   "dist": 0.8938539405},
    "RL_UPPER_BALL_JOINT":  {"x": -0.7655,   "y":  0.632043, "z": 0.26701,  "dist": 1.027989759},
    "RL_LCA_FRONT":         {"x": -0.7135,   "y":  0.23,     "z": 0.16,     "dist": 0.7665391379},
    "RL_LCA_REAR":          {"x": -0.8135,   "y":  0.23,     "z": 0.16,     "dist": 0.8603965655},
    "RL_LOWER_BALL_JOINT":  {"x": -0.7635,   "y":  0.635061, "z": 0.14701,  "dist": 1.003915666},
    "RL_TIE_INNER":         {"x": -0.79,     "y":  0.258292, "z": 0.215,    "dist": 0.8585101964},
    "RL_TIE_OUTER":         {"x": -0.79,     "y":  0.632,    "z": 0.215,    "dist": 1.034286711},

    # ---------------- REAR RIGHT (-X, -Y) ----------------
    "RR_UCA_FRONT":         {"x": -0.715542, "y": -0.258292, "z": 0.267647, "dist": 0.8064428235},
    "RR_UCA_REAR":          {"x": -0.815458, "y": -0.258292, "z": 0.2594,   "dist": 0.8938539405},
    "RR_UPPER_BALL_JOINT":  {"x": -0.7655,   "y": -0.632043, "z": 0.26701,  "dist": 1.027989759},
    "RR_LCA_FRONT":         {"x": -0.7135,   "y": -0.23,     "z": 0.16,     "dist": 0.7665391379},
    "RR_LCA_REAR":          {"x": -0.8135,   "y": -0.23,     "z": 0.16,     "dist": 0.8603965655},
    "RR_LOWER_BALL_JOINT":  {"x": -0.7635,   "y": -0.635061, "z": 0.14701,  "dist": 1.003915666},
    "RR_TIE_INNER":         {"x": -0.79,     "y": -0.258292, "z": 0.215,    "dist": 0.8585101964},
    "RR_TIE_OUTER":         {"x": -0.79,     "y": -0.632,    "z": 0.215,    "dist": 1.034286711},
}

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


"""
Final output should inculde
both inner and outer wheel angles
angle difference
ackerman percentage
graph inner and outer angles vs rack displacement
"""
