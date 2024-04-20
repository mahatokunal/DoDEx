from WebScraper.llm import converse, create_conversation_starter
import json
import asyncio


async def extract_contract_data(article_date, contract_description):
    # conversation_history = create_conversation_starter(f"Extract detailed contract information from the following description:\n{contract_description}")
    conversation_history = create_conversation_starter(
        f"Extract these fields (2. federal_agency as Federal Agency, 3. company_names as Company Name(s), 	4. date as Date, 	5. place as Place, 	6. amount_value as Amount Value, 	7. contract_type as Contract Type, 	8. completion_date as Completion Date, 	9. funds as Funds Obligated at Time of Award, 	10. contract_acquisition_type as Contract Acquisition Type)from the following description and put those fields against their values:\n{contract_description}")
    # async for response in converse(conversation_history):
    #     print(f"Extracted Data: {response}")

    response_buffer = ""
    async for response in converse(conversation_history):
        response_buffer += response

    print(f"Extracted Data: {response_buffer}")

async def main():
    with open('data.json', 'r') as file:
        data = json.load(file)

    tasks = []
    for date, description in data.items():
        # Assuming each date might have multiple entries separated by a special delimiter or each entry is a separate paragraph
        entries = description.split("\n\n")
        for entry in entries:
            if entry.strip():
                # Schedule the extraction task for each contract entry
                # print("date = " , date + "entry = " , entry +  "\n")
                task = extract_contract_data(date, entry)
                tasks.append(task)

    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())