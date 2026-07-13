# config.py

# Road Network Layout
LANES = ['North', 'South', 'East', 'West']

# Signal Timing Constraints (in seconds for simulation)
BASE_GREEN_TIME = 15
MAX_GREEN_TIME = 45
MIN_GREEN_TIME = 5
YELLOW_TRANSITION_TIME = 2

# Utility Function Weights (From Assignment Report)
# U = WEIGHT_FLOW * Flow - WEIGHT_RISK * Risk
WEIGHT_FLOW = 0.7
WEIGHT_RISK = 0.3

# Simulation Settings
SENSOR_NOISE_FACTOR = 0.15  # 15% chance of camera blur/partial visibility