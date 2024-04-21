import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('data.csv')

# Initialize an empty list to store individual contracts along with the date
contracts = []

# Iterate through each row of the DataFrame
for index, row in df.iterrows():
    # Split the text into paragraphs (contracts)
    paragraphs = row['data_on_articleDatePage'].split('\n')
    for paragraph in paragraphs:
        # Strip the paragraph of leading and trailing whitespace
        cleaned_paragraph = paragraph.strip()
        # Check if the paragraph is not empty
        if cleaned_paragraph:
            # Append the contract along with the article date
            contracts.append((cleaned_paragraph, row['article_date']))

# Create a DataFrame with the contracts and their dates
contracts_df = pd.DataFrame(contracts, columns=['Contract', 'Article_Date'])

# Prepare to associate contracts with federal agencies
final_contracts = []
current_agency = None

# Iterate through each row of the contracts DataFrame
for index, row in contracts_df.iterrows():
    if row['Contract'].isupper():  # This row is an agency name
        current_agency = row['Contract']
    else:
        # Append the contract, its associated agency, and article date to the final list
        final_contracts.append((row['Contract'], current_agency, row['Article_Date']))

# Create a DataFrame with contracts, associated agencies, and article dates
final_contracts_df = pd.DataFrame(final_contracts, columns=['Contract', 'Federal_Agency', 'Article_Date'])

final_contracts_df = final_contracts_df[~final_contracts_df['Contract'].str.startswith('*')]

# Write the DataFrame to a CSV file
final_contracts_df.to_csv('contracts_with_tags4.csv', index=False)
