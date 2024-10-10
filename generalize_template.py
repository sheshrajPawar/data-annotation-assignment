import json

def generalize_template():
    template = {
        "Invoice Number": {
            "rule": "Find keywords like 'Invoice No', 'Invoice #', or 'Invoice ID' and extract the numeric value."
        },
        "Invoice Date": {
            "rule": "Look for 'Date' and extract in formats like DD/MM/YYYY or MM-DD-YYYY."
        },
        "Vendor Name": {
            "rule": "Find 'Vendor' or 'Supplier' and extract the name."
        },
        "Line Items": {
            "rule": "Extract items from the table, regardless of column order."
        }
    }
    
    with open('generalized_template.json', 'w') as json_file:
        json.dump(template, json_file, indent=4)

if __name__ == "__main__":
    generalize_template()
