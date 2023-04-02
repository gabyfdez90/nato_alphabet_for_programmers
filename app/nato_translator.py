from app.data import alphabet

def translate_word(input_word): 
    """ Accepts any word as input and returns a list that represents its translation into Programmers NATO Alphabet."""
    
    #Instanciate a class (alphabet) that reads from the CSV file using Pandas library.

    alphabet_df = alphabet.get_alphabet()

    #Apply dictionary comprehension to create the association between letters and NATO code words. 

    nato_dictionary = {row.letter:row.code for (index,row) in alphabet_df.iterrows()}

    #Create a list of the code words necessary to complete an user input
    input_word = input_word.upper()
    output = [nato_dictionary[letter] for letter in input_word]

    return output