import streamlit as st
from fpdf import FPDF
import yagmail
import os

# ----------------------------
# Page configuration
# ----------------------------
st.set_page_config(page_title="Interactive Report Generator", layout="wide")

st.title("📄 Interactive Report Generator")

# ----------------------------
# Sidebar Inputs
# ----------------------------
st.sidebar.header("User Input")
name = st.sidebar.text_input("Enter your name", "John Doe")
age = st.sidebar.slider("Select your age", 0, 100, 25)
options = st.sidebar.multiselect(
    "Choose options",
    ["Option A", "Option B", "Option C"],
    default=["Option A"]
)
comments = st.sidebar.text_area("Additional comments", "Type here...")

# ----------------------------
# Real-time display
# ----------------------------
st.header("Preview Report")
st.markdown(f"**Name:** {name}")
st.markdown(f"**Age:** {age}")
st.markdown(f"**Selected Options:** {', '.join(options) if options else 'None'}")
st.markdown(f"**Comments:** {comments}")

# ----------------------------
# Generate PDF
# ----------------------------
def generate_pdf(name, age, options, comments):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 10, "Interactive Report", ln=True, align="C")
    pdf.ln(10)
    
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, f"Name: {name}")
    pdf.multi_cell(0, 10, f"Age: {age}")
    pdf.multi_cell(0, 10, f"Selected Options: {', '.join(options) if options else 'None'}")
    pdf.multi_cell(0, 10, f"Comments: {comments}")
    
    file_path = "my_RESUME.pdf"
    pdf.output(file_path)
    return file_path

pdf_file = generate_pdf(name, age, options, comments)

# ----------------------------
# Download PDF
# ----------------------------
with open(pdf_file, "rb") as f:
    st.download_button(
        label="📥 Download PDF",
        data=f,
        file_name="my_RESUME.pdf",
        mime="application/pdf"
    )

# ----------------------------
# Send Email
# ----------------------------
#Ask them to go to their Google Account Settings.
#​Search for "App Passwords" (2-Factor Authentication must be ON).
#​Generate a password for "Mail" and "Other (Streamlit App)".
#​They will get a 16-character code.
# ----------------------------
st.header("📧 Send Report via Email")
receiver_email = st.text_input("Enter recipient email")

if st.button("Send Email"):
    try:
        # Configure your email credentials here
        sender_email = "mail_id"
        sender_password = "password" # Use App Password if Gmail 2FA is enabled
        
        yag = yagmail.SMTP(sender_email, sender_password)
        yag.send(
            to=receiver_email,
            subject="Your Interactive Report",
            contents="Please find attached the report.",
            attachments=pdf_file
        )
        st.success(f"Email sent successfully to {receiver_email}!")
    except Exception as e:
        st.error(f"Failed to send email: {e}")

# ----------------------------
# Cleanup generated PDF (optional)
# ----------------------------
if os.path.exists(pdf_file):
    os.remove(pdf_file)
