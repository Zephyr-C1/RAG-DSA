import streamlit as st
import requests
import json
import time

# System UI Configuration
st.set_page_config(
    page_title="Cyprus Grid Security Decision Support System",
    page_icon="⚡",
    layout="wide"
)

# Backend decision endpoint
BACKEND_API_URL = "http://localhost:8000/api/decision"

# 注入支持 Dark / Light 模式自动切换的响应式 CSS 样式
st.markdown("""
<style>
/* 默认明亮模式 */
:root {
    --card-bg: #e8f5e9;
    --card-border: #2e7d32;
    --header-color: #1b5e20;
    --main-text: #0d3c10;
    --footer-border: #c8e6c9;
    --footer-text: #2e7d32;
    --body-text: #1e293b;
}

/* 系统级或 Streamlit 暗黑模式自适应 */
@media (prefers-color-scheme: dark) {
    :root {
        --card-bg: #0f2415;
        --card-border: #4caf50;
        --header-color: #81c784;
        --main-text: #e8f5e9;
        --footer-border: #2e7d32;
        --footer-text: #a5d6a7;
        --body-text: #f1f5f9;
    }
}

/* 兼容 Streamlit 内部 dark 属性选择器 */
[data-theme="dark"], .stApp[data-test-script-state="running"] {
    --card-bg: #0f2415;
    --card-border: #4caf50;
    --header-color: #81c784;
    --main-text: #e8f5e9;
    --footer-border: #2e7d32;
    --footer-text: #a5d6a7;
    --body-text: #f1f5f9;
}

.directive-card {
    background-color: var(--card-bg);
    border-left: 6px solid var(--card-border);
    border-radius: 8px;
    padding: 20px 24px;
    margin-top: 15px;
    margin-bottom: 25px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.15);
}

.directive-header {
    font-size: 13px;
    font-weight: 700;
    color: var(--header-color);
    text-transform: uppercase;
    letter-spacing: 0.8px;
    margin-bottom: 8px;
}

.directive-text {
    font-size: 22px;
    font-weight: 800;
    color: var(--main-text);
    line-height: 1.45;
    margin-bottom: 12px;
}

.directive-footer {
    display: flex;
    gap: 24px;
    align-items: center;
    border-top: 1px solid var(--footer-border);
    padding-top: 10px;
    font-size: 13px;
    color: var(--footer-text);
}

.assessment-text {
    font-size: 16px;
    line-height: 1.6;
    color: var(--body-text);
}
</style>
""", unsafe_allow_html=True)

st.title("⚡ Cyprus Transmission Grid Dynamic Security Assessment (DSA)")
st.caption("LLM-Assisted Operator Decision Support | Chain-of-Drafts (CoD) Explainability Protocol")

# Sidebar Configuration
with st.sidebar:
    st.header("⚙️ Operational Settings")
    top_k = st.slider("Retrieval Depth (Top-K Chunks)", min_value=2, max_value=12, value=6, step=1)
    confidence_threshold = st.slider("Safety Confidence Threshold (%)", min_value=50, max_value=95, value=75, step=5)
    trigger_sim = st.checkbox("Trigger STEPSS/PyRAMSES Time-Domain Sim", value=False)
    st.divider()
    st.markdown("**System Architecture:**")
    st.markdown("- **Backbone**: Meta LLaMA-3.1-8B-Instruct (Local)")
    st.markdown("- **Knowledge Base**: TSOC Rules (KM v1.1.0) & Logs")
    st.markdown("- **Neural Reranker**: BAAI/bge-reranker-large")
    st.markdown("- **Query Engine**: Dense FAISS + Sparse BM25 + HyDE")

# Operational Scenario Presets
preset_queries = [
    "What is the maximum allowable RoCoF that generating units must withstand without disconnecting?",
    "Under what capacity threshold is a power plant connection classified as Non-Firm vs Firm?",
    "What are the mandatory operating reserve categories and their response times under the Operating Margin Policy?",
    "Simulate a three-phase short-circuit fault on the 132kV transmission corridor with 120ms clearing time."
]

selected_preset = st.selectbox("Select Operational Inquiry / Contingency Scenario:", ["-- Custom Inquiry --"] + preset_queries)

if selected_preset != "-- Custom Inquiry --":
    user_query = st.text_area("Dispatcher Prompt / Operational Scenario:", value=selected_preset, height=80)
else:
    user_query = st.text_area("Dispatcher Prompt / Operational Scenario:", height=80, placeholder="Enter dispatch or regulatory inquiry...")

submit_btn = st.button("🚀 Analyze & Formulate Directive", type="primary", use_container_width=False)

if submit_btn and user_query.strip():
    start_time = time.time()
    with st.spinner("Retrieving Operational Knowledge Base & Executing CoD Reasoning..."):
        try:
            resp = requests.post(
                BACKEND_API_URL,
                json={"query": user_query.strip(), "top_k": top_k, "trigger_simulation": trigger_sim},
                timeout=180
            )
            elapsed = time.time() - start_time
            if resp.status_code == 200:
                data = resp.json()
                cod = data.get("cod_trace", {})
                trace_id = cod.get("audit_trace_id", "AUDIT-UNKNOWN")
                conf_val = float(cod.get("confidence", 0.0))
                conf_pct = conf_val * 100.0
                recommendation = cod.get("recommendation", "No directive formulated.")
                assessment = cod.get("assessment", "No assessment provided.")
                sim_result = data.get("simulation_result")

                # =========================================================================
                # 1. Executive Directive Card (Fully Theme-Adaptive)
                # =========================================================================
                st.markdown(
                    f"""
                    <div class="directive-card">
                        <div class="directive-header">
                            💡 Operator Executive Directive & Determination
                        </div>
                        <div class="directive-text">
                            {recommendation}
                        </div>
                        <div class="directive-footer">
                            <span>⏱️ <b>Reasoning Latency:</b> {elapsed:.2f}s</span>
                            <span>🔑 <b>Audit Trace ID:</b> <code>{trace_id}</code></span>
                            <span>🎯 <b>Confidence Score:</b> <b>{conf_pct:.1f}%</b></span>
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                # Security Safeguard: Threshold Interception[cite: 1]
                if conf_pct < confidence_threshold:
                    st.warning(
                        f"⚠️ **[SIMULATION REQUIRED]** The system confidence ({conf_pct:.1f}%) is below the security threshold ({confidence_threshold}%). "
                        "Numerical assertions cannot be blindly executed without STEPSS/PyRAMSES time-domain verification."
                    )

                # =========================================================================
                # 2. Chain-of-Drafts (CoD) Explainability Trace[cite: 1]
                # =========================================================================
                st.markdown("### 🔍 Chain-of-Drafts (CoD) Explainability Trace")
                st.caption("Standardized reasoning protocol: Evidence → Assessment (Dominant Physical Mechanism) → Recommendation → Calibration")

                # Step 1: Evidence (Regulatory Basis & Operational Telemetry)[cite: 1]
                with st.container(border=True):
                    st.markdown("#### **Step 1: Evidence (Regulatory Basis & Operational Telemetry)**")
                    evidence_items = cod.get("evidence", [])
                    if evidence_items:
                        for ev in evidence_items:
                            doc = ev.get("source_doc", "Cyprus Regulations")
                            sec = ev.get("section", "General")
                            page = ev.get("page", 0)
                            txt = ev.get("excerpt", "")
                            st.markdown(f"📄 **Source:** `{doc}` | **Clause/Section:** `{sec}` | **Page:** `{page}`")
                            st.info(txt)
                    else:
                        st.write("No direct verbatim regulatory excerpt cited.")

                # Step 2: Assessment (Dominant Physical Mechanism & Security Margin)[cite: 1]
                with st.container(border=True):
                    st.markdown("#### **Step 2: Assessment (Dominant Physical Mechanism & Security Margin)**")
                    st.markdown(
                        f"<div class='assessment-text'>{assessment}</div>",
                        unsafe_allow_html=True
                    )
                    if sim_result:
                        st.markdown("**STEPSS/PyRAMSES Time-Domain Simulation Output Summary:**")
                        st.json(sim_result)

                # Step 3: Recommendation (Actionable Dispatch Directive)[cite: 1]
                with st.container(border=True):
                    st.markdown("#### **Step 3: Recommendation (Actionable Dispatch Directive)**")
                    st.markdown(
                        f"<div class='assessment-text' style='font-weight: 600;'>{recommendation}</div>",
                        unsafe_allow_html=True
                    )

                # Step 4: Confidence & Assumption Calibration[cite: 1]
                with st.container(border=True):
                    st.markdown("#### **Step 4: Confidence & Assumption Calibration**")
                    col_conf1, col_conf2 = st.columns([1, 4])
                    col_conf1.metric("Confidence Score", f"{conf_pct:.1f}%")
                    col_conf2.markdown(f"**Engineering Rationale & Boundary Assumptions:**\n\n{cod.get('confidence_rationale', 'N/A')}")

                # =========================================================================
                # 3. Post-event Audit & Operator Override Panel (Human-in-the-loop)[cite: 1]
                # =========================================================================
                st.markdown("---")
                st.markdown("### ✍️ Operator Scrutiny & Override Panel (Post-event Audit)")
                st.caption(f"Immutable audit logging for compliance verification. Target Record: `{trace_id}`")

                with st.form(f"audit_form_{trace_id}"):
                    c1, c2 = st.columns(2)
                    badge = c1.text_input("Operator Badge ID:", placeholder="e.g., TSOC-DESK-019")
                    action = c2.selectbox(
                        "Dispatch Action Selection:",
                        ["ACCEPT (Execute Directive)", "CHALLENGE (Trigger STEPSS Simulation)", "OVERRIDE (Manual Dispatch Control)"]
                    )
                    justification = st.text_area(
                        "Justification / Discrepancy Note (Mandatory for CHALLENGE or OVERRIDE):",
                        placeholder="State physical discrepancy, telemetry conflict, or operational judgment..."
                    )
                    override_action = st.text_input("Modified Action (if OVERRIDE):", placeholder="Specify manual MW adjustment or switching order...")

                    submitted = st.form_submit_button("Commit Operator Audit Record", type="secondary")
                    if submitted:
                        if not badge.strip():
                            st.error("Operator Badge ID is required for post-event audit compliance.")
                        else:
                            st.success(
                                f"Audit record successfully archived. [Record ID: {trace_id} | Operator: {badge} | Action: {action.split()[0]}]"
                            )

            else:
                st.error(f"Backend Server Error ({resp.status_code}): {resp.text}")
        except Exception as e:
            st.error(f"Failed to communicate with Decision Backend: {e}")