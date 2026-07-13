# core/utility.py
import config

class TrafficUtilityEvaluator:
    @staticmethod
    def calculate_utility(queue_length, allocated_green_time, emergency_present):
        """
        Implements: U = 0.7 * Flow Efficiency - 0.3 * Accident Risk
        Optimizes traffic clearance vs intersection safety hazards.
        """
        # 1. Flow Efficiency (Higher if allocated time is sufficient for the queue)
        # Optimal time needed is roughly 1.5 seconds per car
        optimal_time_needed = max(config.MIN_GREEN_TIME, queue_length * 1.5)
        flow_efficiency = min(1.0, allocated_green_time / (optimal_time_needed + 1))

        # 2. Accident Risk Factors
        accident_risk = 0.1 # Base baseline risk
        
        # Risk increases heavily if an emergency vehicle is blocked/delayed
        if emergency_present and allocated_green_time < config.MAX_GREEN_TIME:
            accident_risk += 0.6
            
        # Risk increases if green time is too short for a massive queue (sudden braking)
        if queue_length > 25 and allocated_green_time < 10:
            accident_risk += 0.3

        # Final Formula Constraint
        utility_score = (config.WEIGHT_FLOW * flow_efficiency) - (config.WEIGHT_RISK * accident_risk)
        
        return round(utility_score, 3), round(flow_efficiency, 2), round(accident_risk, 2)