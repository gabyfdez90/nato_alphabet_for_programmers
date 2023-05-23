from app.data import alphabet

def generate_word(dictionary, word):
    """ Auxiliary function to translate_word(), that handles exceptions."""

    try:
          output_list = [dictionary[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet, please.")
        generate_word()
    return output_list


def translate_word(input_word): 
    """ Accepts any word as input and returns a list that represents its translation into Programmers NATO Alphabet."""
    
    #Instanciate a class (alphabet) that reads from the CSV file using Pandas library.

    alphabet_df = alphabet.get_alphabet()

    #Apply dictionary comprehension to create the association between letters and NATO code words. 

    nato_dictionary = {row.letter:row.code for (index,row) in alphabet_df.iterrows()}

    #Create a list of the code words necessary to complete an user input
    input_word = input_word.upper()

    output_list = generate_word(nato_dictionary, input_word)

    return output_list
