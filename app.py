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
</style>
""", unsafe_allow_html=True)

# --- HEADER SECTION ---
st.markdown("<h1 style='text-align: center; color: #264653;'>🩺 NurseSkills Training Copilot</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #6C757D; font-size: 16px;'>Your elite clinical companion for mastering OSCEs, procedures, and precision timing.</p>", unsafe_allow_html=True)
st.markdown("---")

# --- SIDEBAR: INTERACTIVE TOOLS ---
st.sidebar.markdown("### ⏱️ OSCE Pacing Timer")
timer_minutes = st.sidebar.selectbox("Select Station Time:", [5, 10, 15], format_func=lambda x: f"{x} Minutes")
if st.sidebar.button("Start Practice Timer"):
    with st.sidebar:
        st.warning(f"⏱️ Timer active for {timer_minutes} minutes!")
        st.progress(100)
        st.success("🔔 Station Time Complete!")

st.sidebar.markdown("---")
st.sidebar.markdown("### 📚 Quick Standards")
st.sidebar.info("• **Safety (40%):** Critical hygiene & steps\n• **Technique (30%):** Precision & flow\n• **Pacing (30%):** Efficiency & communication")

# --- INPUT SECTION: TEXT OR VOICE OR FILE ---
st.markdown("### 🌿 What clinical bottleneck are you tackling today?")

# Quick select category pills
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

user_challenge = st.text_input(
    label="Challenge input",
    label_visibility="collapsed",
    placeholder="Type your challenge here...",
    value=preset_input
)

# --- VOICE RECORDING & FILE UPLOADER SECTION ---
st.markdown("---")
col_voice, col_file = st.columns(2)

with col_voice:
    st.markdown("🎙️ **Voice Note:**")
    audio_value = st.audio_input("Record hurdle")
    if audio_value:
        st.audio(audio_value)
        user_challenge = "Voice recorded clinical challenge regarding pacing and precision"

with col_file:
    st.markdown("📎 **Upload Photo / Rubric:**")
    uploaded_file = st.file_uploader("Upload asset", type=["png", "jpg", "jpeg", "pdf", "docx"], label_visibility="collapsed")
    if uploaded_file is not None:
        if uploaded_file.type in ["image/png", "image/jpeg"]:
            st.image(uploaded_file, caption="Asset Preview", width=200)
        st.success(f"Attached: {uploaded_file.name}")

# --- DYNAMIC GENERATOR LOGIC ---
st.markdown("")
if st.button("✨ Generate Clinical Action Plan", use_container_width=True):
    if not user_challenge and not audio_value and not uploaded_file:
        st.warning("⚠️ Please provide text, record a voice note, or upload a file first!")
    else:
        with st.spinner("🌿 Synthesizing clinical guidelines..."):
            
            st.success("✨ Custom Clinical Action Plan Ready!")
            
            # Competency Cards
            st.markdown("### 📊 Competency Focus Areas")
            c1, c2, c3 = st.columns(3)
            with c1:
                st.markdown("🛡️ **Safety Check**")
                st.caption("Weight: High (40%)\nStrict hygiene & zero contamination.")
            with c2:
                st.markdown("⚙️ **Precision**")
                st.caption("Weight: Solid (30%)\nEliminate micro-hesitations.")
            with c3:
                st.markdown("💬 **Communication**")
                st.caption("Weight: Vital (30%)\nVerbal consent & reassurance.")

            st.markdown("---")
            st.markdown("### 🎯 Targeted Strategy & Adjustments")
            
            if "time" in user_challenge.lower() or "timing" in user_challenge.lower() or "speed" in user_challenge.lower():
                st.markdown("""
                * ⏱️ **OSCE Pacing Drills:** Break the station down into rigid checkpoints (2m Assessment, 4m Intervention, 2m Closing).
                * 🛡️️ **Safety Buffer:** Practice completing critical safety steps with 90 seconds to spare.
                """)
            elif "sterile" in user_challenge.lower() or "procedure" in user_challenge.lower() or "contamination" in user_challenge.lower():
                st.markdown("""
                * 🧼 **Aseptic Technique Audit:** Run slow-motion repetitions focusing purely on contamination prevention.
                * 🔍 **Checklist Discipline:** Cross-reference every sub-step against standard clinical rubrics.
                """)
            else:
                st.markdown("""
                * 🎯 **Targeted Skill Isolation:** Dedicate today's session solely to repeating this specific friction point smoothly.
                * 📋 **Rubric Alignment:** Check the marking breakdown to ensure communication and safety weights are maximized.
                """)
            
            st.markdown("### 📅 Recommended Next 7 Days")
            st.markdown("""
            * **Days 1–2:** Isolate and correct the specific technique or timing hitch.
            * **Days 3–5:** Integrate the fix back into a timed half-scenario run.
            * **Days 6–7:** Full mock clinical simulation under strict evaluation conditions.
            """)
            
            plan_text = f"WorldSkills Nursing Action Plan for: {user_challenge}"
            st.download_button(
                label="📥 Download Action Plan (.txt)",
                data=plan_text,
                file_name="nurseskills_action_plan.txt",
                mime="text/plain"
            )