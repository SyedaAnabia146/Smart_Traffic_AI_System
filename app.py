import sys
import os

# System pipeline to dynamically current folder (Foolproof Fix)
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import streamlit as st
import time
import pandas as pd
import plotly.express as px
from core.environment import TrafficEnvironment
from core.agent import SmartTrafficAgent
from utils.logger import log_cycle_data

# Page Configurations for Modern Dashboard Look
st.set_page_config(
    page_title="Intelligent Traffic Controller Dashboard",
    page_icon="🚦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Premium Light Theme Grid Styling (Forceful Button Visibility Fix)
st.markdown("""
    <style>
    /* Main body changes to elegant light slate */
    .stApp {
        background-color: #F1F5F9;
        color: #1E293B;
    }
    /* Sidebars clean color tuning */
    [data-testid="stSidebar"] {
        background-color: #E2E8F0 !important;
    }
    
    /* 🚫 Removing the dark header/black bar completely from the top */
    [data-testid="stHeader"] {
        background-color: #F1F5F9 !important;
        box-shadow: none !important;
    }
    header {
        background-color: #F1F5F9 !important;
    }
    div[data-testid="stDecoration"] {
        background-image: none !important;
        background-color: transparent !important;
    }

    /* 👁️ FORCE FULL VISIBILITY ON SIDEBAR TOGGLE BUTTONS */
    button[data-testid="stSidebarCollapseButton"],
    [data-testid="stSidebarCollapseButton"] button,
    [data-testid="stHeader"] button {
        color: #000000 !important;
        fill: #000000 !important;
        background-color: #CBD5E1 !important;
        border: 2px solid #94A3B8 !important;
        border-radius: 8px !important;
        opacity: 1 !important;
        visibility: visible !important;
        display: inline-flex !important;
    }
    
    /* Target the SVG icon inside the button directly to ensure it isn't white */
    button[data-testid="stSidebarCollapseButton"] svg,
    [data-testid="stHeader"] svg {
        fill: #000000 !important;
        color: #000000 !important;
    }

    /* 🚫 Hiding the horizontal line in sidebar completely */
    [data-testid="stSidebar"] hr {
        border-color: transparent !important;
        margin: 10px 0 !important;
    }
    
    /* Fixing LaTeX / Katex text color to be visible on light background */
    .katex {
        color: #0F172A !important;
        font-size: 1.15em;
    }
    .metric-box {
        background-color: #FFFFFF;
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #CBD5E1;
        text-align: center;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
    }
    .lane-card {
        background: #FFFFFF;
        padding: 15px;
        border-radius: 10px;
        margin-bottom: 10px;
        border: 1px solid #E2E8F0;
        border-left: 5px solid #64748B;
        box-shadow: 0 2px 4px rgba(0,0,0,0.02);
        color: #334155;
    }
    .lane-green { border-left: 6px solid #10B981 !important; background-color: rgba(16, 185, 129, 0.08); }
    .lane-yellow { border-left: 6px solid #F59E0B !important; background-color: rgba(245, 158, 11, 0.08); }
    .lane-red { border-left: 6px solid #EF4444 !important; background-color: rgba(239, 68, 68, 0.08); }
    
    /* Fix text contrast labels for Light Mode */
    h1, h2, h3, h4, h5, h6, p {
        color: #0F172A !important;
    }
    </style>
""", unsafe_allow_html=True)

# Application Header
st.title("🚦 Smart Traffic Signal Controller")
st.markdown("### *AI-Driven Stochastic Intersection Simulation Engine*")

# Group Members Details Card (Matches the Premium UI)
st.markdown("""
    <div style="background-color: #FFFFFF; padding: 15px; border-radius: 8px; border: 1px solid #CBD5E1; margin-bottom: 20px; max-width: 600px; box-shadow: 0 4px 6px rgba(0,0,0,0.02);">
        <h4 style="color: #0284C7; margin: 0 0 10px 0; font-weight: bold;">👥 Project Group Members</h4>
        <table style="width: 100%; border-collapse: collapse; color: #334155;">
            <tr style="border-bottom: 1px solid #E2E8F0;">
                <td style="padding: 6px; font-weight: bold; color: #0284C7;">Syeda Anabia (Team Leader)</td>
                <td style="padding: 6px; text-align: right; font-family: monospace; color: #0284C7; font-weight: bold;">2K23/CSE/146</td>
            </tr>
            <tr style="border-bottom: 1px solid #E2E8F0;">
                <td style="padding: 6px;">Kashaf</td>
                <td style="padding: 6px; text-align: right; font-family: monospace;">2K23/CSE/68</td>
            </tr>
            <tr style="border-bottom: 1px solid #E2E8F0;">
                <td style="padding: 6px;">Afia</td>
                <td style="padding: 6px; text-align: right; font-family: monospace;">2K23/CSE/20</td>
            </tr>
            <tr>
                <td style="padding: 6px;">Wareesha</td>
                <td style="padding: 6px; text-align: right; font-family: monospace;">2K23/CSE/153</td>
            </tr>
        </table>
        <p style="margin: 10px 0 0 0; font-size: 13px; color: #64748B; text-align: center;"><b>AI Final Project</b> | BSCS (2K23-Batch) | AI Lab</p>
    </div>
""", unsafe_allow_html=True)

st.write("---")

# 🛠️ SIDEBAR SECTION (Perfect Layout Order & Sidebar Controls)
st.sidebar.header("🛠️ Simulation Control Panel")
total_cycles = st.sidebar.slider("Number of Simulation Cycles", min_value=1, max_value=10, value=3)
delay_speed = st.sidebar.slider("Execution Step Delay (Seconds)", min_value=0.5, max_value=3.0, value=1.5)

# Primary Simulation Action Button
start_sim = st.sidebar.button("⚡ Start AI Traffic Simulation", type="primary")

st.sidebar.write("---")

st.sidebar.subheader("📐 System Weights Configuration")
st.sidebar.info("As per project specifications, the optimization runs on a weighted utility model:")
st.sidebar.latex(r"U = 0.7 \times \text{Flow} - 0.3 \times \text{Risk}")

st.sidebar.write("---")

st.sidebar.subheader("ℹ️ About Project")
st.sidebar.markdown(
    "<div style='background-color: #FFFFFF; padding: 12px; border-radius: 6px; border: 1px solid #CBD5E1; color: #334155; font-size: 13px; box-shadow: 0 2px 4px rgba(0,0,0,0.01);'>"
    "This Smart Traffic AI System is designed to optimize traffic light timings using "
    "advanced predictive analytics and dynamic logic density estimation."
    "</div>", 
    unsafe_allow_html=True
)

# Initialize AI Core Components
env = TrafficEnvironment()
agent = SmartTrafficAgent()

# Trigger Button for the Simulation Loop
if start_sim:
    
    # Placeholders for Dynamic Real-Time UI Components
    status_text = st.empty()
    progress_bar = st.progress(0)
    
    st.subheader("📊 Real-Time Operations Control Room")
    kpi_cols = st.columns(3)
    metric1 = kpi_cols[0].empty()
    metric2 = kpi_cols[1].empty()
    metric3 = kpi_cols[2].empty()
    
    st.write("---")
    st.subheader("🛣️ Junction Lanes Live Deployment Status")
    
    # Creating a 2x2 grid for the 4 intersections
    grid_cols = st.columns(2)
    lane_placeholders = {
        'North': grid_cols[0].empty(),
        'South': grid_cols[1].empty(),
        'East': grid_cols[0].empty(),
        'West': grid_cols[1].empty()
    }

    # Tracking metrics across the run
    cumulative_utility = []
    total_vehicles_cleared = 0
    total_accidents_prevented = 0

    for current_cycle in range(1, total_cycles + 1):
        status_text.markdown(f"#### 🔄 Processing Junction Cycle **{current_cycle} of {total_cycles}**...")
        progress_bar.progress(int((current_cycle / total_cycles) * 100))
        
        # Ingesting simulated sensory readings
        sensor_feed = env.get_sensor_readings()
        
        # Iterating through all lanes sequentially
        for lane in ['North', 'South', 'East', 'West']:
            lane_data = sensor_feed[lane]
            
            # AI Inference Step
            decision = agent.compute_optimal_timing(lane, lane_data)
            
            # Update Local Analytics Accumulators
            cumulative_utility.append(decision['utility_score'])
            total_vehicles_cleared += int(lane_data['actual_queue'] * decision['flow_efficiency'])
            if lane_data['emergency_vehicle'] and decision['allocated_time'] > 30:
                total_accidents_prevented += 1
                
            # Updating Global KPI Dashboard Widgets dynamically
            avg_utility = round(sum(cumulative_utility) / len(cumulative_utility), 2)
            
            metric1.markdown(f"""<div class='metric-box'>
                <h5 style='color: #64748B; margin:0; font-size:12px; font-weight:bold;'>AVERAGE UTILITY SCORE</h5>
                <h2 style='color: #0284C7; margin:5px 0;'>✨ {avg_utility}</h2>
                <span style='color: #16A34A; font-size:12px; font-weight:bold;'>Target Max: 0.70</span>
            </div>""", unsafe_allow_html=True)
            
            metric2.markdown(f"""<div class='metric-box'>
                <h5 style='color: #64748B; margin:0; font-size:12px; font-weight:bold;'>EST. VEHICLES CLEARED</h5>
                <h2 style='color: #16A34A; margin:5px 0;'>🚗 {total_vehicles_cleared}</h2>
                <span style='color: #64748B; font-size:12px;'>Throughput Accumulator</span>
            </div>""", unsafe_allow_html=True)
            
            metric3.markdown(f"""<div class='metric-box'>
                <h5 style='color: #64748B; margin:0; font-size:12px; font-weight:bold;'>CRITICAL RISK AVOIDANCES</h5>
                <h2 style='color: #DC2626; margin:5px 0;'>🛡️ {total_accidents_prevented}</h2>
                <span style='color: #DC2626; font-size:12px; font-weight:bold;'>Emergency Preemptions</span>
            </div>""", unsafe_allow_html=True)

            #  STEP 1: RENDER GREEN PHASE FOR THE ACTIVE LANE
            style_class = "lane-card lane-green"
            em_badge = "🚨 EMERGENCY PRIORITY ACTUATED" if lane_data['emergency_vehicle'] else "Normal Stream"
            blur_badge = "⚠️ Sensor Degraded (Partial Visibility)" if lane_data['partial_visibility_active'] else "🔒 Clear Visibility"
            
            lane_placeholders[lane].markdown(f"""
                <div class="{style_class}">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <h4 style="margin:0; font-weight:bold;">📍 {lane} Lane Status</h4>
                        <span style="background:#10B981; color:white; padding:3px 10px; border-radius:15px; font-size:12px; font-weight:bold;">🟢 SIGNAL: GREEN</span>
                    </div>
                    <p style="margin: 5px 0; color:#334155;"><b>Queue Profile:</b> Observed {lane_data['observed_queue']} cars (Actual: {lane_data['actual_queue']}) | <i>{blur_badge}</i></p>
                    <p style="margin: 5px 0; color:#334155;"><b>AI Execution:</b> Allotting <b>{decision['allocated_time']}s</b> green window due to <i>"{decision['reason']}"</i></p>
                    <p style="margin: 0; font-size:13px; color:#065F46;"><b>Performance Diagnostics:</b> Flow Optimization: {decision['flow_efficiency']} | Risk Metric: {decision['accident_risk']} | <b>Utility U: {decision['utility_score']}</b></p>
                    <span style="font-size:11px; font-weight:bold; color:#DC2626;">{em_badge}</span>
                </div>
            """, unsafe_allow_html=True)
            
            time.sleep(delay_speed) # Simulate the duration passing

            #  STEP 2: TRANSITION TO YELLOW PHASE
            style_class = "lane-card lane-yellow"
            lane_placeholders[lane].markdown(f"""
                <div class="{style_class}">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <h4 style="margin:0; font-weight:bold;">📍 {lane} Lane Status</h4>
                        <span style="background:#F59E0B; color:white; padding:3px 10px; border-radius:15px; font-size:12px; font-weight:bold;">🟡 SIGNAL: YELLOW</span>
                    </div>
                    <p style="margin: 10px 0; color:#D97706; font-weight:500;">⚠️ Clearing intersection. Actuators pulsing yellow warning indicators...</p>
                </div>
            """, unsafe_allow_html=True)
            
            time.sleep(0.8)

            #  STEP 3: RESET BACK TO RED STATE
            style_class = "lane-card lane-red"
            lane_placeholders[lane].markdown(f"""
                <div class="{style_class}">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <h4 style="margin:0; font-weight:bold;">📍 {lane} Lane Status</h4>
                        <span style="background:#EF4444; color:white; padding:3px 10px; border-radius:15px; font-size:12px; font-weight:bold;">🔴 SIGNAL: RED</span>
                    </div>
                    <p style="margin: 10px 0; color:#991B1B;">🔒 Stream closed. Holding vehicle grid queue steady.</p>
                </div>
            """, unsafe_allow_html=True)
            
            # Log all transaction metrics downstream into our analytics engine
            log_cycle_data(
                current_cycle, lane, lane_data['actual_queue'], lane_data['observed_queue'],
                lane_data['partial_visibility_active'], lane_data['emergency_vehicle'],
                decision['allocated_time'], decision['utility_score'],
                decision['flow_efficiency'], decision['accident_risk']
            )
            
    status_text.markdown("### ✅ Simulation Cycle Completed Safely! Analytical Logs Saved.")
    
    # 📈 POST-RUN ANALYTICAL VISUALIZATION GENERATION
    st.write("---")
    st.subheader("📈 Post-Simulation AI System Behavior Analysis")
    
    if pd.io.common.file_exists("traffic_simulation_logs.csv"):
        df = pd.read_csv("traffic_simulation_logs.csv")
        df_recent = df.tail(total_cycles * 4)
        
        chart_cols = st.columns(2)
        
        # Chart 1: Queue vs Allocated Timings
        fig_time = px.bar(df_recent, x="Lane", y="Allocated_Green_Time", color="Sensor_Blurred",
                          barmode="group", title="AI Allocated Green Phase Duration per Lane",
                          labels={"Allocated_Green_Time": "Green Light Window (s)"},
                          color_discrete_map={"Yes": "#E11D48", "No": "#3B82F6"})
        fig_time.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
        chart_cols[0].plotly_chart(fig_time, use_container_width=True)
        
        # Chart 2: Utility Function Convergence Plot
        fig_util = px.line(df_recent, x="Timestamp", y="Utility_Score", markers=True,
                           title="System Mathematical Utility Curve Fluctuations",
                           labels={"Utility_Score": "Evaluated Utility Score (U)"})
        fig_util.update_traces(line_color="#10B981")
        fig_util.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
        chart_cols[1].plotly_chart(fig_util, use_container_width=True)
        
        # Presenting raw logged telemetry files
        st.subheader("📋 System Telemetry Captured Dataset")
        st.dataframe(df_recent, use_container_width=True)