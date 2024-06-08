import os
from pdf2image import convert_from_path
from docx import Document
import streamlit as st
from utils import create_or_empty_dir, convert_pdf_to_images, create_docx_with_text

extracted_images_dir = 'extracted_images'
# Get the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))
uploads_dir = os.path.join(current_dir, 'uploads')
os.makedirs(uploads_dir, exist_ok=True)
converted_docx_dir = os.path.join(current_dir, 'converted_docx')
os.makedirs(converted_docx_dir, exist_ok=True)

# Create a file uploader component
uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

# Check if a file was uploaded
if uploaded_file is not None:
	# Save the uploaded file to the uploads directory
	with open(os.path.join(uploads_dir, uploaded_file.name), "wb") as file:
		file.write(uploaded_file.getbuffer())
	st.success("File uploaded successfully!")
else:
	st.info("Please upload a PDF file.")

# Get a list of all PDF files in the uploads directory
pdf_files = [file for file in os.listdir(uploads_dir) if file.endswith(".pdf")]

# Create a column layout
col1, col2 = st.columns(2)

# Show checkboxes for each PDF file in col1
with col1:
	selected_files = []
	for file in pdf_files:
		checkbox = st.checkbox(file)
		if checkbox:
			selected_files.append(file)

	# Check if any files are selected
	if selected_files:
		# Create a button to trigger the conversion process
		if st.button("Convert"):
			# Create or empty the extracted_images directory
			print(f'Creating or emptying the {extracted_images_dir} directory')
			create_or_empty_dir(extracted_images_dir)

			# Convert selected PDF files to images
			for file in selected_files:
				pdf_path = os.path.join(uploads_dir, file)
				print(f'Converting {file} to images in {extracted_images_dir}')
				convert_pdf_to_images(pdf_path, extracted_images_dir)
				# Create a Word document with text extracted from images
				output_docx = os.path.join(converted_docx_dir, f'{file.replace(".pdf", "")}.docx')
				image_folder = os.path.join(current_dir, extracted_images_dir)
				print(f'Creating {f'{file.replace(".pdf", "")}.docx'} with text extracted from images in {extracted_images_dir}')
				create_docx_with_text(image_folder, output_docx)

			st.success("Conversion completed successfully!")

# Show documents from the converted_docx folder in col2
with col2:
	docx_files = [file for file in os.listdir(converted_docx_dir) if file.endswith(".docx")]
	for file in docx_files:
		st.download_button(f"Download {file}", open(os.path.join(converted_docx_dir, file), "rb").read(), file_name=file, mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document")
