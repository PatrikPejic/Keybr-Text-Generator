import random as rand

special_chars = ['`', '~', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+',
                 '[', '{', ']', '}', '\\', '|', ';', ':', '\'', '\"', ',', '<', '.', '>', '/', '?']


word_file = open('words.txt', 'r')
lines = word_file.readlines()

NUMBER_OF_SPECIAL_CHARS = len(special_chars)
NUMBER_OF_WORDS = len(lines)
TEXT_SIZE = 5 # amount of senteces in one text 
SENTENCE_SIZE = 13 # number of word in a sentence 

# returns 0 or 1 just like a coin flip
def coin_flip(): 
    return rand.randint(0, 1)

# retunrs a radnom word from the words.txt 
def get_word(): 
    return lines[rand.randint(0, NUMBER_OF_WORDS-1)].strip()

# return random number from 0 to 9 as a string 
def get_random_number():
    return str(rand.randint(0, 9))

# return a random special char form the list 
def get_random_char(): 
    return special_chars[rand.randint(0, NUMBER_OF_SPECIAL_CHARS-1)]

def create_word(): 
    # select random word out of 1000
    word = get_word()
    # randomly capitilize the first letter  
    if coin_flip() : 
        word = word.capitalize()
    if coin_flip(): 
        # add a random number to the word 
        word += get_random_number() 
    if coin_flip(): 
        # add a radom special char to the word 
        word += get_random_char()
    return word 
    

def create_sentence(): 
    sentence = ""
    for i in range(SENTENCE_SIZE): 
        sentence += create_word()
        sentence += " " # add spave between words 
    return sentence

def create_text(): 
    text = ""
    for i in range(TEXT_SIZE): 
        text += create_sentence()
        text += "\n"
    print(text)
        

if __name__ == "__main__":
    # Idee zur Verbeserung Algorithmus schreiben der schaut ob alle Zahlen und Woerter vorhanden sind und wenn ja dann wieder von vorne 
    create_text() 