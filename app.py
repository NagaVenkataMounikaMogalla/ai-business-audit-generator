import streamlit as st
from scraper import scrape_website
from ai_insights import generate_ai_insights
from report_generator import generate_pdf
from email_sender import send_email

st.set_page_config(
    page_title="AI Business Audit Generator",
    layout="centered"
)

st.title("🚀 AI Business Audit Generator")

st.write(
    "Generate personalized company audit reports automatically using AI."
)

with st.form("lead_form"):

    name = st.text_input("Full Name")

    email = st.text_input("Email Address")

    company = st.text_input("Company Name")

    website = st.text_input("Company Website")

    submit = st.form_submit_button("Generate Report")

if submit:

    if not name or not email or not company or not website:

        st.error("Please fill all fields.")

    else:

        with st.spinner("Researching company website..."):

            data = scrape_website(website)

        if "error" in data:

            st.error(data["error"])

        else:

            st.success("Company research completed!")

            st.subheader("Website Title")

            st.write(data["title"])

            st.subheader("Meta Description")

            st.write(data["description"])

            with st.spinner("Generating AI insights..."):

                insights = generate_ai_insights(
                    company,
                    data
                )

            st.subheader("AI Business Audit Report")

            st.write(insights)

            pdf_path = generate_pdf(
                company,
                insights
            )

            with open(pdf_path, "rb") as pdf_file:

                st.download_button(
                    label="📥 Download PDF Report",
                    data=pdf_file,
                    file_name=f"{company}_report.pdf",
                    mime="application/pdf"
                )

            st.info("Attempting to send email...")

            email_sent = send_email(
                email,
                company,
                pdf_path
            )

            if email_sent:

                st.success(
                    "📧 Email sent successfully! Check Inbox/Spam."
                )

            else:

                st.warning(
                    "⚠️ Report generated successfully, but email delivery was delayed. Please use the download button."
                )