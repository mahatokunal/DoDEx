import csv
import json
import asyncio
from openpyxl import Workbook
from WebScraper.llm import converse, create_conversation_starter
from csv_processor import process_csv
import pandas as pd

# Create a workbook and select the active worksheet
wb = Workbook()
ws = wb.active


async def extract_contract_data(article_date, federal_agency, contract_description, csv_writer):
    conversation_history = create_conversation_starter(
        f"{contract_description}: From the given contract, create a json with following schema from the above text article - Company Name(s), 	Date, 	Place, 	Amount Value, 	Contract Type, 	Completion Date, 	Funds Obligated at Time of Award, 	Contract Acquisition Type")
    response_buffer = ""
    async for response in converse(conversation_history):
        response_buffer += response

    # Assuming the response is structured in a single line of text separated by commas or semicolons
    try:
        # Splitting the response into components
        print(f"Extracted Data: {response_buffer}")
        # details = response_buffer.split(';')
        # # print(details)
        # details = [detail.strip() for detail in details]  # Clean up any leading/trailing whitespace
        # Insert the federal agency at the beginning of the list
        # csv_writer.writerow(details)
        # ws.append(details)
        # print(f"Extracted and wrote data for {article_date} and {federal_agency}")

        # Create a dictionary with the data

        data_dict = json.loads(response_buffer)
        data_dict['Article Date'] = article_date
        data_dict['Federal Agency'] = federal_agency
        return data_dict

    except Exception as e:
        print(f"Failed to parse or write data: {e}")


async def main():
    process_csv('data.csv', 'contracts_with_tags.csv')
    data = pd.read_csv('contracts_with_tags.csv')

    # Prepare a list to store the data
    data_list = []

    with open('llm_generated_data.csv', 'w', newline='') as file:
        csv_writer = csv.writer(file)
        # Writing headers to the CSV file
        csv_writer.writerow(
            ['Article Date', 'Federal Agency', 'Company Name(s)', 'Date', 'Place', 'Amount Value', 'Contract Type',
             'Completion Date', 'Funds Obligated at Time of Award', 'Contract Acquisition Type'])

        tasks = []
        for index, row in data.iterrows():
            contract = row['Contract']
            federal_agency = row['Federal_Agency']
            article_date = row['Article_Date']

            task = extract_contract_data(article_date, federal_agency, contract, csv_writer)
            tasks.append(task)

        print("tasks = ", tasks)

        # Wait for all tasks to complete
        results = await asyncio.gather(*tasks)

        # Add the results to the data list
        data_list.extend(results)

        # Add the results to the data list
        data_list.extend(results)

        # Write the data list to a .json file
        with open('llm_generated_data.json', 'w') as file:
            json.dump(data_list, file)

        # Save the workbook
        wb.save("llm_generated_data.xlsx")


if __name__ == "__main__":
    asyncio.run(main())
