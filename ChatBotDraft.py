from spellchecker import SpellChecker

class chatBotData:
    def __init__(self, sentence):
        self.sentence = sentence

    def reply(self):
        #SAMPLE NOT FINAL
        data = {
            "HOW ARE YOU": ["Fine, Thank you for asking!", "Doing Well", "Great, How about you?"]
            #We can add more reply and question
        }
        no_of_words = {
            "HOW ARE YOU": 3
        }

        '''for key in data.keys():
            data_keywords.append(key.split()) # If word is different but same meaning(synonyms) we can add that too
        # We can compare a specific word in  words if it has a synonym in the keywords which will count in that specific key'''

        compare = {key: 0 for key in data.keys()} # Will compare matches it got
        
        input_words = set(self.sentence.split())
        for key, responses in data.items():
            key_words = set(key.split())
            compare[key] = len(input_words & key_words)  # Count matching words

        highest_match = max(compare.values())
        if highest_match == 0:
            print("chatbot name: I'm sorry, I don't understand that.")
            return

        matching_keys = [k for k, v in compare.items() if v == highest_match]

        if len(matching_keys) == 1:
            print(f"chatbot name: {data[matching_keys[0]][0]}")
        else:
            # If their is a tie
            best_match = max(
                matching_keys,
                key=lambda k: len(input_words & set(k.split())) / no_of_words[k]
            )
            print(f"chatbot name: {data[best_match][0]}")


def validation(sentence: str)->str: # To suggest the most simillar word to the wrongly spelt word
    spell = SpellChecker()
    words = sentence.split()
    corrected_words = [spell.correction(word) for word in words]
    return " ".join(corrected_words)

def introduction()->None:
    print("chatbot name: Hi my name is -----")
    print("chatbot name: You can ask me anything about -----")
    print("chatbot name: Enter 'exit' to exit the program")

def user_input()->str:
    question: str = input("user: ").upper()
    if question == 'EXIT':
        return 'EXIT'
    return validation(question)

def main()->None:
    introduction()
    while True:
        sentence = user_input()
        if sentence == 'EXIT':
            print("chatbot name: Thank you for chatting with me!")
            break
        bot = chatBotData(sentence)
        bot.reply()

if __name__ == '__main__':
    main()