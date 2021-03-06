from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot('Quotes Bot',read_only = True, logic_adapters=[
        "chatterbot.logic.BestMatch","chatterbot.logic.MathematicalEvaluation"
    ])

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot based on the english corpus
trainer.train("chatterbot.corpus.english")

# Get a response to an input statement
print(chatbot.get_response("Hello, how are you today?"))
