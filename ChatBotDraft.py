from spellchecker import SpellChecker
from deep_translator import GoogleTranslator

def validation(sentence: str)->str: # To suggest the most simillar word to the wrongly spelt word
    spell = SpellChecker()
    words = sentence.split()
    corrected_words = [spell.correction(word) for word in words]
    return " ".join(corrected_words)

def main_introduction()->None:
    print("Chatbot Name")
    language: str = input("chatbot name: Pumili ng wika na nais | Choose your preferred language: Filipino or English").upper()
    functions: dict = {"FILIPINO": fil_introuction, "ENGLISH": en_introduction}
    choice:function = functions.get(language, None)
    while True:
        if choice:
            choice()
        else:
            print("Ang wikang pinili ay wala sa aming system | The language you pick is not available in our system")
            language = input("Ilagay muli ang nais na wika | Entered again your preferred language")
        
def en_introduction()->str:
    print("chatbot name: Hi my name is -----")
    print("chatbot name: You can ask me anything about the province of Laguna")
    print("chatbot name: Enter 'exit' to exit the program")
    return "ENGLISH"

def fil_introuction()->str:
    print("chatbot name: Kamusta ang pangalan ay -----")
    print("chatbot name: Pwede mo kong tanungin ng tungkol sa lalawigan Laguna")
    print("chatbot name: I-type lamang ang 'exit' upang matapos ang program")
    return "FILIPINO"

def user_input_EN()->str:
    question: str = input("user: ").upper().strip()
    if question == 'EXIT':
        return 'EXIT'
    return validation(question)

def user_input_fil()->str:
    question: str = input("user: ").upper().strip()
    translation = GoogleTranslator(source='fil', target='en').translate(question)
    translation = translation.upper().strip()
    if question == 'EXIT':
        return 'EXIT'
    return validation(question)

def reply(sentence: str)->None:
        #SAMPLE NOT FINAL
        data = {
            "HOW ARE YOU": "Fine, Thank you for asking!"
            #We can add more reply and question
        }
        '''for key in data.keys():
            data_keywords.append(key.split()) # If word is different but same meaning(synonyms) we can add that too
        # We can compare a specific word in  words if it has a synonym in the keywords which will count in that specific key'''

        compare: dict = {key: 0 for key in data.keys()} # Will start at 0 and For every key/question in data
        
        input_words = set(sentence.split()) # Converted to set to efficiently handles matching, and split keys in the data
                                                # input_words is a set of word per word from self.sentence/from the input of the user
        for key, responses in data.items():
            key_words = set(key.split()) # key_word is a set of word per word from each key in data
            compare[key] = len(input_words & key_words)  # This will match how many words match in input_words & key_words using &/ intersection operator

        highest_value = max(compare.values())
        highest_matches:list = [v for v in compare.values if v == highest_value] # Will look from the values from compare and will find the largest values

        if not highest_matches or highest_matches == 0: # No match, highest matches does not have any element and is equal to 0
            print("chatbot name: I'm sorry, I don't understand that.")
            return

        matching_keys = [k for k, v in compare.items() if v == highest_matches] # Will look for the keys in compare that will match the value of highest_matches
        if len(matching_keys) == 1: # If it is only 1 match
            print(f"chatbot name: {data[matching_keys[0]]}")
        else:
            # If their is a tie, the first match will be picked
            print(f"chatbot name: {data[matching_keys[0]]}")

def main()->None:
    language = main_introduction()
    while True:
        if language is "FILIPINO" :
            sentence = user_input_fil()
        else:
            sentence = user_input_EN()
        if sentence == 'EXIT':
            print("chatbot name: Thank you for chatting with me!")
            break
        reply(sentence)

if __name__ == '__main__':
    main()