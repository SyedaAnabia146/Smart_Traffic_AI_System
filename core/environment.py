# core/environment.py
import random
import config

class TrafficEnvironment:
    def __init__(self):
        self.lanes = config.LANES

    def get_sensor_readings(self):
        """Simulates real-time data from Junction Cameras & Inductive Loops"""
        environment_state = {}
        
        for lane in self.lanes:
            # Stochastic nature: Random traffic build-up (0 to 35 cars)
            actual_queue = random.randint(0, 35)
            
            # Emergency Vehicle Detection (10% chance)
            emergency_detected = random.choice([True] + [False] * 9)
            
            # Partially Observable: Adding sensor noise (e.g., dust/rain blocking line of sight)
            observed_queue = actual_queue
            is_blurred = random.random() < config.SENSOR_NOISE_FACTOR
            
            if is_blurred:
                # Sensor cannot see perfectly, underestimates the queue by 20-40%
                observed_queue = int(actual_queue * random.uniform(0.6, 0.8))
            
            environment_state[lane] = {
                "actual_queue": actual_queue,
                "observed_queue": observed_queue, # What the AI actually sees
                "emergency_vehicle": emergency_detected,
                "partial_visibility_active": is_blurred
            }
            
        return environment_state