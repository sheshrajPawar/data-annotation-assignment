import json

def create_extraction_template():
    template = {
        "Invoice Number": {
            "rule": "Find 'Invoice No' or 'Invoice #' and extract the following numeric value."
        },
        "Invoice Date": {
            "rule": "Find 'Date' and extract in DD/MM/YYYY format."
        },
        "Vendor Name": {
            "rule": "Find 'Vendor' and extract the name."
        },
        "Line Items": {
            "rule": "Extract table rows for items with columns: Item Name, Quantity, Price."
        }
    }
    
    with open('extraction_template.json', 'w') as json_file:
        json.dump(template, json_file, indent=4)

if __name__ == "__main__":
    create_extraction_template()
