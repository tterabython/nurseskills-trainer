import streamlit as st
import time

# Page configuration
st.set_page_config(
    page_title="NurseSkills Training Copilot",
    page_icon="🩺",
    layout="centered"
)

# --- CUSTOM AESTHETIC STYLING (CLINICAL MINT VIBE) ---
st.markdown("""
<style>
    .main {
        background-color: #F4F9F9;
    }
    .stAlert, div.css-1r7slds {
        border-radius: 12px;
    }
    .stButton>button {
        border-radius: 20px;
        font-weight: 600;
        border: none;
        background: linear-gradient(135deg, #2A9D8F 0%, #21867A 100%);
        color: white;
        box-shadow: 0 4px 12px rgba(42, 157, 143, 0.3);
    }
    .stButton>button:hover {
        background: linear-gradient(135deg, #21867A 0%, #1B6F64 100%);
        box-shadow: 0 6px 15px rgba(42, 157, 143, 0.4);
    }
    div.stButton > button:active {
        transform: scale(0.98);
    }
</style>
""", unsafe_allow_html=True)

# --- HEADER SECTION ---
st.markdown("<h1 style='text-align: center; color: #264653;'>🩺 NurseSkills Training Copilot</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #6C757D; font-size: 16px;'>Your elite clinical companion for mastering OSCEs, procedures, and precision timing.</p>", unsafe_allow_html=True)
st.markdown("---")

# --- SIDEBAR: INTERACTIVE TOOLS ---
st.sidebar.markdown("### ⏱️ OSCE Pacing Timer")
st.sidebar.markdown("Practice your station speed under pressure.")
timer_minutes = st.sidebar.selectbox("Select Station Time:", [5, 10, 15], format_func=lambda x: f"{x} Minutes")
if st.sidebar.button("Start Practice Timer"):
    with st.sidebar:
        st.warning(f"⏱️ Timer started for {timer_minutes} minutes! Focus on workflow.")
        # Visual countdown simulation helper
        progress_bar = st.progress(0)
        status_text = st.empty()
        total_seconds = timer_minutes * 60
        # A quick visual pulse simulation for the user
        status_text.text("Station Active: Maintain sterile field & communication.")
        progress_bar.progress(100)
        st.success("🔔 Time Check Complete!")

st.sidebar.markdown("---")
st.sidebar.markdown("### 📚 Quick Standards")
st.sidebar.info("• **Safety (40%)**: Critical actions & hygiene\n• **Technique (30%)**: Precision & accuracy\n• **Pacing (30%)**: Efficiency & communication")

# --- MAIN INPUT SECTION ---
st.markdown("### 🌿 What clinical bottleneck are you tackling today?")

# Quick select pills layout using buttons or text pre-fill
col1, col2, col3 = st.columns(3)
preset_input = ""

with col1:
    if st.button("⏱️ Running out of time"):
        preset_input = "struggling with time on module and pacing"
with col2:
    if st.button("🧼 Sterile technique flaw"):
        preset_input = "sterile procedure contamination or aseptic technique error"
with col3:
    if st.button("📋 Assessment sequencing"):
        preset_input = "assessment accuracy and head-to-toe sequencing"

# Text box input (can be pre-filled via quick select or typed manually)
user_challenge = st.text_input(
    label="Challenge input",
    label_visibility="collapsed",
    placeholder="e.g., timing on sterile procedure, documentation pacing, assessment accuracy...",
    value=preset_input
)

# --- DYNAMIC GENERATOR LOGIC ---
if st.button("✨ Generate Clinical Action Plan", use_container_width=True):
    if not user_challenge:
        st.warning("⚠️ Please select a quick tag above or type your challenge so your copilot can map out the solution!")
    else:
        with st.spinner("🌿 Synthesizing clinical guidelines against WorldSkills standards..."):
            
            st.success("✨ Custom Clinical Action Plan Ready!")
            
            # Visual Breakdown Cards using columns
            st.markdown("### 📊 Competency Focus Areas")
            c1, c2, c3 = st.columns(3)
            with c1:
                st.markdown("🛡️ **Safety Check**")
                st.caption("Weight: High (40%)\nFocus on strict hygiene & zero contamination loops.")
            with c2:
                st.markdown("⚙️ **Precision**")
                st.caption("Weight: Solid (30%)\nEliminate micro-hesitations in technique.")
            with c3:
                st.markdown("💬 **Communication**")
                st.caption("Weight: Vital (30%)\nMaintain verbal consent and patient reassurance.")

            # Dynamic response card
            st.markdown("---")
            st.markdown("### 🎯 Targeted Strategy & Adjustments")
            st.info(f"**Addressing focus:** *'{user_challenge}'*")
            
            if "time" in user_challenge.lower() or "timing" in user_challenge.lower() or "speed" in user_challenge.lower() or "pacing" in user_challenge.lower():
                st.markdown("""
                * ⏱️ **OSCE Pacing Drills:** Break the station down into rigid checkpoints (e.g., 2m Assessment, 4m Intervention, 2m Closing).
                * 🛡️ **Safety Buffer:** Practice completing the critical safety steps with 90 seconds to spare.
                * 📋 **Streamlined Flow:** Eliminate backtracking during physical assessments by following a strict systematic order.
                """)
            elif "sterile" in user_challenge.lower() or "procedure" in user_challenge.lower() or "technique" in user_challenge.lower() or "contamination" in user_challenge.lower():
                st.markdown("""
                * 🧼 **Aseptic Technique Audit:** Run slow-motion repetitions focusing purely on contamination prevention and hand hygiene checkpoints.
                * 🔍 **Checklist Discipline:** Cross-reference every sub-step against standard clinical rubrics to avoid missed points.
                """)
            else:
                st.markdown("""
                * 🎯 **Targeted Skill Isolation:** Dedicate today's session solely to repeating this specific friction point 3 times smoothly.
                * 📋 **Rubric Alignment:** Check the marking breakdown to ensure communication and patient safety weights are maximized.
                * 🩺 **Mock Scenario:** Run a mini 5-minute simulation tomorrow focusing only on overcoming this hurdle.
                """)
            
            st.markdown("### 📅 Recommended Next 7 Days")
            st.markdown("""
            * **Days 1–2:** Isolate and correct the specific technique or timing hitch using slow-motion loops.
            * **Days 3–5:** Integrate the fix back into a timed half-scenario run.
            * **Days 6–7:** Full mock clinical simulation under strict evaluation conditions.
            """)
            
            # Download Plan Option
            plan_text = f"WorldSkills Nursing Action Plan for: {user_challenge}"
            st.download_button(
                label="📥 Download Action Plan (.txt)",
                data=plan_text,
                file_name="nurseskills_action_plan.txt",
                mime="text/plain"
            )