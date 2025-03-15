
import streamlit as st
from marker.converters.pdf import PdfConverter
from marker.models import create_model_dict
from marker.output import text_from_rendered
import tempfile

# Streamlit app setup
st.title("PDF to Markdown Converter")
st.write("Upload your PDF document to get a markdown version of it.")

# File uploader
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    # Save the uploaded file to a temporary location
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
        temp_file.write(uploaded_file.read())
        temp_file_path = temp_file.name

    # Convert the uploaded PDF to markdown
    converter = PdfConverter(
        artifact_dict=create_model_dict(),
        config={"languages": ["fa"]}  # Set the language to Persian
    )
    rendered = converter(temp_file_path)
    text, _, images = text_from_rendered(rendered)
    
    # Display the markdown text
    st.markdown("### Markdown Output")
    st.code(text, language="markdown")

    # Option to download the markdown file
    st.download_button(
        label="Download Markdown",
        data=text,
        file_name="converted_markdown.md",
        mime="text/markdown"
    )