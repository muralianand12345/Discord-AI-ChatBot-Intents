## Imports
# importing neuralintents python package
from neuralintents import GenericAssistant

# declaring chatbot | intents.json | models
chatbot = GenericAssistant('intents.json', model_name="./models/elitex_model")
# loading model
chatbot.load_model()

# function ai_response for our bot.py
def ai_response(m):
    response = chatbot.request(m)
    if response is None:
        pass
    return response