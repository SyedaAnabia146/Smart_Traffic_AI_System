# utils/logger.py
import os
import csv
from datetime import datetime

LOG_FILE = "traffic_simulation_logs.csv"

def log_cycle_data(cycle_num, lane, actual_q, observed_q, blurred, emergency, allocated_time, utility, flow, risk):
    """Appends real-time simulation state logs into a structured CSV dataset."""
    file_exists = os.path.isfile(LOG_FILE)
    
    with open(LOG_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        
        # Write headers if the file is being newly created
        if not file_exists:
            writer.writerow([
                "Timestamp", "Cycle_Number", "Lane", "Actual_Queue", 
                "Observed_Queue", "Sensor_Blurred", "Emergency_Present", 
                "Allocated_Green_Time", "Utility_Score", "Flow_Efficiency", "Accident_Risk"
            ])
            
        # Write the simulation state record
        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            cycle_num,
            lane,
            actual_q,
            observed_q,
            "Yes" if blurred else "No",
            "Yes" if emergency else "No",
            allocated_time,
            utility,
            flow,
            risk
        ])