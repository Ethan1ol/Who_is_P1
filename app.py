import streamlit as st
import plotly.graph_objects as go

st.set_page_config(page_title="ApexTelemetry", page_icon="🏎️", layout="wide")

st.title("🏎️ Who is P1")
st.caption("Session Analytics & Driver Head-to-Head Telemetry")

col1, col2, col3, col4 = st.columns(4)
with col1:
    year = st.selectbox("Season", [2024, 2025, 2026], index=0)
with col2:
    grand_prix = st.selectbox("Grand Prix", ["Monza", "Silverstone", "Spa", "Bahrain"])
with col3:
    session_type = st.selectbox("Session", ["Qualifying", "Race", "FP1", "FP2", "FP3"])
with col4:
    sync_mode = st.radio("Sync By", ["Track Distance (m)", "Time (s)"], horizontal=True)

st.divider()

# Driver selection & metrics
d_col1, d_col2 = st.columns(2)
with d_col1:
    st.subheader("Driver 1")
    d1 = st.selectbox("Select Driver A", ["LEC", "HAM", "VER", "NOR", "PIA"], index=0)
    st.metric(label=f"{d1} Lap Time", value="1:19.327", delta="-0.142s")

with d_col2:
    st.subheader("Driver 2")
    d2 = st.selectbox("Select Driver B", ["VER", "LEC", "HAM", "NOR", "PIA"], index=1)
    st.metric(label=f"{d2} Lap Time", value="1:19.469", delta="+0.142s")

# Plotly test trace
fig = go.Figure()
fig.add_trace(go.Scatter(x=[0, 1000, 2500, 4000, 5793], y=[330, 95, 310, 110, 340],
                         mode='lines', name=d1, line=dict(color='#E80020', width=2)))
fig.add_trace(go.Scatter(x=[0, 1000, 2500, 4000, 5793], y=[328, 98, 305, 112, 338],
                         mode='lines', name=d2, line=dict(color='#3671C6', width=2)))

fig.update_layout(
    title="Speed Trace Over Lap Distance",
    xaxis_title="Distance (m)",
    yaxis_title="Speed (km/h)",
    template="plotly_dark",
    hovermode="x unified",
    margin=dict(l=40, r=40, t=50, b=40),
)

st.plotly_chart(fig, use_container_width=True)