# core/agent.py
import config
from core.utility import TrafficUtilityEvaluator

class SmartTrafficAgent:
    def __init__(self):
        self.base_green = config.BASE_GREEN_TIME
        self.max_green = config.MAX_GREEN_TIME
        self.min_green = config.MIN_GREEN_TIME

    def compute_optimal_timing(self, lane_name, sensor_data):
        """
        AI Decision Logic: Analyzes queues and emergency overrides,
        then calculates the optimal green phase timing.
        """
        observed_q = sensor_data['observed_queue']
        emergency = sensor_data['emergency_vehicle']
        is_blurred = sensor_data['partial_visibility_active']

        # 1. Critical Priority: Emergency Vehicle Override
        if emergency:
            allocated_time = self.max_green
            reason = "Emergency Vehicle Detected (Priority Override)"
            
        # 2. Dynamic Rule Engine based on Traffic Density
        else:
            # Compensating for Partial Observability (Sensor Noise)
            # Agar camera blur hai, toh agent hidden cars ko compensate karne ke liye math apply karega
            estimated_q = observed_q
            if is_blurred:
                estimated_q = int(observed_q * 1.35) # Estimating 35% more traffic hidden from view
            
            # Timing Allocation Logic
            if estimated_q > 25:
                allocated_time = self.base_green + 20  # Heavily congested
                reason = "High Congestion Management"
            elif estimated_q > 12:
                allocated_time = self.base_green + 5   # Moderate traffic
                reason = "Normal Traffic Clearing"
            else:
                allocated_time = self.base_green - 7   # Light traffic
                reason = "Light Traffic Optimization"

        # Boundary Constraints check (Ensure time stays within Min and Max limits)
        allocated_time = max(self.min_green, min(self.max_green, allocated_time))

        # 3. Evaluate the decision using our Mathematical Utility Engine
        # We pass actual_queue to evaluate the true effectiveness of the agent's choice
        utility, flow, risk = TrafficUtilityEvaluator.calculate_utility(
            sensor_data['actual_queue'], allocated_time, emergency
        )

        return {
            "allocated_time": allocated_time,
            "reason": reason,
            "utility_score": utility,
            "flow_efficiency": flow,
            "accident_risk": risk
        }