import streamlit as st
from fpdf import FPDF
import yagmail
import os

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(page_title="Interactive Report Generator", layout="wide")
st.title("📝 Interactive Report Generator")

# --------------------------------------------------
# SIDEBAR INPUTS
# --------------------------------------------------
st.sidebar.header("User Input")

name = st.sidebar.text_input("Enter your name", "John Doe")
age = st.sidebar.slider("Select your age", 0, 100, 25)

options = st.sidebar.multiselect(
    "Choose options",
    ["Option A", "Option B", "Option B", "Option C"],
    default=["Option A"]
)

comments = st.sidebar.text_area("Additional comments", "")

receiver_email = st.sidebar.text_input("Enter email to send PDF")

# --------------------------------------------------
# LIVE PREVIEW
# --------------------------------------------------
st.header("📄 Report Preview")

st.write(f"**Name:** {name}")
st.write(f"**Age:** {age}")
st.write(f"**Selected Options:** {', '.join(options) if options else 'None'}")
st.write(f"**Comments:** {comments if comments else 'No comments provided'}")

# --------------------------------------------------
# PDF GENERATION FUNCTION
# --------------------------------------------------
def generate_pdf(name, age, options, comments):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    pdf.set_left_margin(15)
    pdf.set_right_margin(15)
    pdf.set_font("Arial", size=12)

    pdf.cell(0, 10, "Interactive Report", ln=True)
    pdf.ln(5)

    pdf.cell(0, 10, f"Name: {name}", ln=True)
    pdf.cell(0, 10, f"Age: {age}", ln=True)
    pdf.cell(0, 10, f"Options: {', '.join(options) if options else 'None'}", ln=True)
    pdf.ln(5)

    safe_comments = comments.strip()
    if not safe_comments:
        safe_comments = "No comments provided."

    pdf.cell(0, 10, "Comments:", ln=True)
    pdf.multi_cell(0, 8, safe_comments)

    file_path = "report.pdf"
    pdf.output(file_path)

    return file_path

# --------------------------------------------------
# BUTTON ACTIONS
# --------------------------------------------------
col1, col2 = st.columns(2)

# Generate & Download PDF
with col1:
    if st.button("📥 Generate & Download PDF"):
        pdf_file = generate_pdf(name, age, options, comments)
        with open(pdf_file, "rb") as f:
            st.download_button(
                label="⬇ Download PDF",
                data=f,
                file_name="report.pdf",
                mime="application/pdf"
            )
        st.success("✅ PDF generated successfully!")

# Email PDF
with col2:
    if st.button("📧 Send PDF to Email"):
        if receiver_email:
            pdf_file = generate_pdf(name, age, options, comments)

            # ⚠️ USE GMAIL APP PASSWORD ONLY
            sender_email = "nikhithamurthy542@gmail.com"
            sender_password = "qvqu ztvx bhqz tiwx"

            try:
                yag = yagmail.SMTP(sender_email, sender_password)
                yag.send(
                    to=receiver_email,
                    subject="Your Generated Report",
                    contents="Please find the attached PDF report.",
                    attachments=pdf_file
                )
                st.success(f"📨 PDF successfully sent to {receiver_email}")
            except Exception as e:
                st.error(f"❌ Failed to send email: {e}")
        else:
            st.warning("⚠️ Please enter a receiver email address.")
