import openai
import os

#Set your api key here
openai.api_key = '' 

def openai_chat_completion(system_prompt, user_prompt):
    #system_prompt = instruction or context-setting message given to the model as a system-level input. 
    #                It helps guide the overall behavior or tone of the model's responses.
    #user_prompt = the input provided by the user in the conversation
    prompt = [
        {
            "role": "system", 
            "content": system_prompt},
        {
            "role": "user",
            "content": user_prompt,
        },
    ]

    response = openai.ChatCompletion.create(
        model="gpt-4", 
        messages=prompt, 
        temperature=0
    )

    return response["choices"][0]["message"]["content"]
    
