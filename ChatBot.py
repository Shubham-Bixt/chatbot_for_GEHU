
# import required packages
from chatterbot import ChatBot
from chatterbot.conversation import Statement
from chatterbot.trainers import ChatterBotCorpusTrainer

# create ChatBot
chatBot = ChatBot('ChatBot')

# create ChatBot trainer
trainer = ChatterBotCorpusTrainer(chatBot)

# Train ChatBot with your custom .yml file
trainer.train("C:\\Users\\ADMIN\\Desktop\\chatBot\\training_data")

# keep communicating with ChatBot
while True:
    # take user input/query
    query = input(">>> ")

    # response from ChatBot
    print(chatBot.get_response(Statement(text=query, search_text=query)))
