#importing chatbot and chatbot trainer

from chatterbot import ChatBot
from chatterbot.conversation import Statement
from chatterbot.trainers import ChatterBotCorpusTrainer

#creating chatbot
ChatBot = ChatBot("Bot")

trainer = ChatterBotCorpusTrainer(ChatBot)


#training chatbot
trainer.train("C:\\Users\\ADMIN\\Desktop\\chatBot\\training_data")




while True:
    question = input("YOU->> ")
    print(ChatBot.get_response(Statement(text=question, search_text=question)))
    