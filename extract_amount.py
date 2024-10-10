def extract_invoice_amount(value_content):
    # Possible variations of amount extraction
    keywords = ["Amount:", "Total Amount:", "Amount Due:"]
    
    for keyword in keywords:
        if keyword in value_content:
            # Split the content by the keyword and extract the next part
            try:
                return value_content.split(keyword)[1].strip().split()[0]  # Extract the amount
            except IndexError:
                return "N/A"  # Handle cases where the amount is not found
    
    return "N/A"  # Default if no keyword is found

# Test cases
test_cases = [
    "Total Amount: $500",
    "Amount: 500",
    "Amount Due: 500.00",
    "Amount: Five Hundred",
    "No amount mentioned."
]

for case in test_cases:
    print(f"Extracted Amount: {extract_invoice_amount(case)}")
