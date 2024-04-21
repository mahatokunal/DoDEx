import json
import csv
'''
dict_keys(['Company Name', 'Date', 'Place', 'Amount Value', 'Contract Type', 'Completion Date', 'Funds Obligated at Time of Award', 'Contract Acquisition Type', 'Article Date', 'Federal Agency'])
'''
def standardize_field_names(data):
    standardized_data = []
    for item in data:
        standardized_item = {}
        for key, value in item.items():
            standardized_key = key.replace(" ", "_").replace("(", "").replace(")", "")
            if standardized_key.endswith("s"):
                standardized_key = standardized_key[:-1]
            standardized_item[standardized_key] = value
        standardized_data.append(standardized_item)
    return standardized_data

with open("llm_generated_data.json", "r") as json_file:
    data = json.load(json_file)

data = standardize_field_names(data)

fields = list(data[0].keys())

# fields_to_ignore = ["Subcontract Line-Item Number", "Work Location"]
#
# # Filter out ignored fields
# fields = [field for field in fields if field not in fields_to_ignore]
#

# Specify the file name
filename = "output_llm5.csv"

# Write the data to a CSV file
with open(filename, 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fields)

    # Write header
    writer.writeheader()

    for row in data:
        filtered_row = {key: value for key, value in row.items() if key in fields}
        writer.writerow(filtered_row)

print("CSV file has been created successfully!")