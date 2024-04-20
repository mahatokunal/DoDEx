import os
import traceback
from typing import List, Dict, AsyncGenerator

import openai
from openai import AsyncOpenAI

from dotenv import load_dotenv
from openai import OpenAIError, OpenAI

# Load .env file
load_dotenv()


openai_model = os.getenv('OPENAI_API_MODEL')

print(
    f"openai_model: {openai_model} openai.api_key: {os.getenv('OPENAI_API_KEY')} openai.api_base: {os.getenv('OPENAI_API_BASE_URL')}")


# async def converse(messages: List[Dict[str, str]]) -> AsyncGenerator[str, None]:
#     """
#     Given a conversation history, generate an iterative response of strings from the OpenAI API.
#
#     :param messages: a conversation history with the following format:
#     `[ { "role": "user", "content": "Hello, how are you?" },
#        { "role": "assistant", "content": "I am doing well, how can I help you today?" } ]`
#
#     :return: a generator of delta string responses
#     """
#     aclient = AsyncOpenAI(api_key=os.getenv('OPENAI_API_KEY'),
#                           base_url=os.getenv('OPENAI_API_BASE_URL'))
#     try:
#         async for chunk in await aclient.chat.completions.create(model=openai_model,
#                                                                  messages=messages,
#                                                                  max_tokens=1600,
#                                                                  stream=True):
#             content = chunk.choices[0].delta.content
#             if content:
#                 yield content
#
#     except OpenAIError as e:
#         traceback.print_exc()
#         yield f"oaiEXCEPTION {str(e)}"
#     except Exception as e:
#         yield f"EXCEPTION {str(e)}"
#
#
# def create_conversation_starter(user_prompt: str) -> List[Dict[str, str]]:
#     """
#     Given a user prompt, create a conversation history with the following format:
#     `[ { "role": "user", "content": user_prompt } ]`
#
#     :param user_prompt: a user prompt string
#     :return: a conversation history
#     """
#     return [{"role": "user", "content": user_prompt}]


def create_conversation_starter(contract_description: str) -> List[Dict[str, str]]:
    """
    Given a contract description, create a conversation history with the following format:
    `[ { "role": "user", "content": user_prompt } ]`

    :param contract_description: a contract description string
    :return: a conversation history
    """
    user_prompt = f"Extract these fields (2. federal_agency as Federal Agency, 3. company_names as Company Name(s), 4. date as Date, 5. place as Place, 6. amount_value as Amount Value, 7. contract_type as Contract Type, 8. completion_date as Completion Date, 9. funds as Funds Obligated at Time of Award, 10. contract_acquisition_type as Contract Acquisition Type) from the following description and put those fields against their values:\n{contract_description}"
    return [{"role": "user", "content": user_prompt}]

async def converse(messages: List[Dict[str, str]]) -> AsyncGenerator[str, None]:
    """
    Given a conversation history, generate an iterative response of strings from the OpenAI API.

    :param messages: a conversation history with the following format:
    `[ { "role": "user", "content": "Hello, how are you?" },
       { "role": "assistant", "content": "I am doing well, how can I help you today?" } ]`

    :return: a generator of delta string responses
    """
    aclient = AsyncOpenAI(api_key=os.getenv('OPENAI_API_KEY'),
                          base_url=os.getenv('OPENAI_API_BASE_URL'))
    try:
        async for chunk in await aclient.chat.completions.create(model=openai_model,
                                                                 messages=messages,
                                                                 max_tokens=4000,
                                                                 stream=True):
            content = chunk.choices[0].delta.content
            if content:
                yield content

    except OpenAIError as e:
        traceback.print_exc()
        yield f"oaiEXCEPTION {str(e)}"
    except Exception as e:
        yield f"EXCEPTION {str(e)}"