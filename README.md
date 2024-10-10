# data-annotation-assignment

## Overview
This assignment involves extracting structured data from PDF invoices using Python.

## Files Included
- `create_template.py`: Script to generate a JSON extraction template for specific invoice formats.
- `extract_amount.py`: Script to extract invoice amounts from various formats, handling multiple variations in data presentation.
- `generalize_template.py`: Script to create a generalized extraction template that accommodates different invoice formats and field names.
- `extract_headers.py`: Script to extract header information from invoices, including dates, invoice numbers, and vendor names.
- `extraction_template.json`: Generated JSON template that outlines the structure for extracting invoice data.
- `generalized_template.json`: Generalized JSON template designed to handle variations in invoice layouts.
- `README.md`: Documentation for the project, including setup instructions and usage details.
- `explanation_video.mp4`: Video walkthrough of the project, demonstrating the extraction process and results.

## How to Run the Code
1. Ensure Python is installed on your machine.
2. Open a command line interface.
3. Navigate to the folder containing the scripts.
4. Run each script using:
   ```bash
   python create_template.py
   python extract_amount.py
   python generalize_template.py
   python extract_headers.py


data-annotation-assignment/
├── create_template.py
├── extract_amount.py
├── generalize_template.py
├── extract_headers.py
├── extraction_template.json
├── generalized_template.json
├── README.md
└── explanation_video.mp4


### Explanation of Added Content
- **`extract_headers.py`**: This new script focuses on extracting header information from the invoices, which includes critical fields such as the date, invoice number, and vendor name.
- **Dependencies**: It mentions any necessary Python libraries that might be required to run your scripts.
- **Project Structure**: This section visually outlines the organization of your project files for better clarity.

You can modify the content based on your actual implementation and any other scripts or features you've included. This format helps ensure that users can easily understand the purpose of each file and how to run your project effectively. Let me know if you need any more adjustments!




