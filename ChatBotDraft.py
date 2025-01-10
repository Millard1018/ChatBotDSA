from spellchecker import SpellChecker

class chatBotData:
    def __init__(self, word):
        self.word = word

    def reply(self):
        #SAMPLE NOT FINAL
        data_keywords = []
        values = []

        data = {
            "HOW ARE YOU": ["Fine, Thank you for asking!", "Doing Well", "Great, How about you?"]
            #We can add more reply and question
        }
        noOfWords = {
            "HOW ARE YOU": 3
        }

        for key in data.keys():
            data_keywords.append(key.split()) # If word is different but same meaning(synonyms) we can add that too
        # We can compare a specific word in  words if it has a synonym in the keywords which will count in that specific key

        compare = { # Will compare matches it got
            "HOW ARE YOU": 0
        }
        
        for word in (data_keywords):
            if self.word == word:
                compare[word] += 1

        highest_match = max(compare.values())
        keys = [k for k, v in data.items() if v == highest_match]

        if len(keys) == 1:
            print(f"chatbot name: {data[keys]}")
        else: # If there is a tie
            for key in keys:
                value = noOfWords[key]//highest_match  # if it matches 80% of the words in the sentence then it is assumpted that that will be the correct reply
                valuesdict = {key: value}
                values.append(valuesdict)
            single_dict: dict = max(values, key=lambda x: list(x.values())[0])
            key = single_dict.keys()[0]
            print(f"chatbot name: {data[key]}")


def validation(words: list)->list: # To suggest the most simillar word to the wrongly spelt word
    dictionary = SpellChecker()
    correct_words = []
    final_words = []
    for word in words:
        if word not in dictionary:
            correct_words.append(dictionary.candidate(word))
    
    for word in correct_words:
        final_words.append(chatBotData(word))

    return final_words

def introduction()->None:
    print("chatbot name: Hi my name is -----")
    print("chatbot name: You can ask me anything about -----")
    print("chatbot name: Enter 'exit' to exit the program")

def user_input()->str:
    question: str = input("user: ").upper()
    words = validation(question)

    return words
def chatBotReply(words: list)-> str:
    words.reply

def main()->None:
    introduction()
    while True: 
        words = user_input()
        if words == 'EXIT':
            print("chatbot name: Thank you for chatting with me!")
            quit()
        else:
            chatBotReply(words)

if __name__ == '__main__':
    main()