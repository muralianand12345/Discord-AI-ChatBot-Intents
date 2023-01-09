from neuralintents import GenericAssistant

chatbot = GenericAssistant('intents.json', model_name="./models/elitex_model")
chatbot.train_model()
chatbot.save_model()