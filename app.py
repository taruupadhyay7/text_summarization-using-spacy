import streamlit as st
import pdfplumber
from extractive import extractive_summarize, get_topic_keywords
from abstractive import abstractive_summarize

# ───────────────────────────────
# PAGE CONFIG
# ───────────────────────────────
st.set_page_config(
    page_title="Text Summarizer",
    page_icon="📝",
    layout="centered"
)

# ───────────────────────────────
# HEADER
# ───────────────────────────────
st.title("📝 Text Summarizer App")
st.write("Summarize any article, email or PDF instantly using AI.")
st.divider()

# ───────────────────────────────
# INPUT SECTION
# ───────────────────────────────
st.subheader("📥 Step 1 — Input Your Text")
option = st.radio("Choose input type:", ["Paste Text", "Upload PDF"])

text = ""

if option == "Paste Text":
    text = st.text_area("Paste your article, email or any text here:", height=250)

elif option == "Upload PDF":
    uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")
    if uploaded_file is not None:
        with pdfplumber.open(uploaded_file) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + " "
        if text.strip():
            st.success(f"✅ PDF uploaded! {len(text.split())} words extracted.")
        else:
            st.error("Could not extract text from this PDF.")

st.divider()

# ───────────────────────────────
# METHOD SELECTION
# ───────────────────────────────
st.subheader("⚙️ Step 2 — Choose Summarization Method")

method = st.radio(
    "Choose method:",
    ["Extractive", "Abstractive"],
    help="Extractive picks key sentences. Abstractive generates new sentences using AI."
)

if method == "Extractive":
    num_sent = st.slider("How many sentences in summary?", min_value=1, max_value=10, value=5)

st.divider()

# ───────────────────────────────
# SUMMARIZE BUTTON
# ───────────────────────────────
st.subheader("🚀 Step 3 — Summarize")

if st.button("✨ Summarize Now", use_container_width=True):
    if text.strip() == "":
        st.error("⚠️ Please paste some text or upload a PDF first!")
    elif len(text.split()) < 30:
        st.warning("⚠️ Text is too short. Please provide at least 30 words.")
    else:
        with st.spinner("Summarizing... please wait ⏳"):
            if method == "Extractive":
                summary = extractive_summarize(text, num_sent)
                keywords = get_topic_keywords(text, top_n=5)
            else:
                st.info("⏳ Loading AI model for first time may take 1-2 minutes...")
                summary = abstractive_summarize(text)
                keywords = get_topic_keywords(text, top_n=5)

        st.divider()

        # ── Keywords ──
        st.subheader("🔑 Topic Keywords")
        keyword_display = "  ".join([f"`{k}`" for k in keywords])
        st.markdown(keyword_display)

        # ── Summary ──
        st.subheader("📄 Your Summary")
        st.success(summary)

        # ── Stats ──
        col1, col2, col3 = st.columns(3)
        col1.metric("Original Words", len(text.split()))
        col2.metric("Summary Words", len(summary.split()))
        col3.metric("Reduced By", f"{round((1 - len(summary.split()) / len(text.split())) * 100)}%")

        st.caption(f"✅ Summarized using: **{method}** method")