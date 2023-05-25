# Problem Set 4C
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

import string
from ps4a import get_permutations

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    
    # print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    # print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list


### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

# you may find these constants helpful
VOWELS_LOWER = 'aeiou'
VOWELS_UPPER = 'AEIOU'
CONSONANTS_LOWER = 'bcdfghjklmnpqrstvwxyz'
CONSONANTS_UPPER = 'BCDFGHJKLMNPQRSTVWXYZ'

class SubMessage(object):
    def __init__(self, text):
        '''
        Initializes a SubMessage object
                
        text (string): the message's text

        A SubMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        # pass #delete this line and replace with your code here
        
        self.message_text = text
        self.valid_words = load_words(file_name=WORDLIST_FILENAME)
        self.word_lst = text.split()
        
    
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        # pass #delete this line and replace with your code here
    
        return self.message_text

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        
        Returns: a COPY of self.valid_words
        '''
        # pass #delete this line and replace with your code here
        return self.valid_words.copy()
    
    def get_word_lst(self):
        '''
        Used to safely access a copy of self.word_lst outside of the class.
        This helps you avoid accidentally mutating class attributes.
        
        Returns: a COPY of self.word_lst
        '''
        return self.word_lst.copy()
                
    def build_transpose_dict(self, vowels_permutation):
        '''
        vowels_permutation (string): a string containing a permutation of vowels (a, e, i, o, u)
        
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to an
        uppercase and lowercase letter, respectively. Vowels are shuffled 
        according to vowels_permutation. The first letter in vowels_permutation 
        corresponds to a, the second to e, and so on in the order a, e, i, o, u.
        The consonants remain the same. The dictionary should have 52 
        keys of all the uppercase letters and all the lowercase letters.

        Example: When input "eaiuo":
        Mapping is a->e, e->a, i->i, o->u, u->o
        and "Hello World!" maps to "Hallu Wurld!"

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        
        # pass #delete this line and replace with your code here
    
        vowels_permutation_low = vowels_permutation.lower()
        lst_perm = list(vowels_permutation_low)
        dic = {}
        
        a = 0
        for c in VOWELS_LOWER:
            dic[c] = lst_perm[a]
            a += 1
        
        b = 0
        for c in VOWELS_UPPER:
            dic[c] = lst_perm[b].upper()
            b += 1
            
        for c in CONSONANTS_LOWER:
            dic[c] = c
            
        for c in CONSONANTS_UPPER:
            dic[c] = c
            
        return dic
        

    
    def apply_transpose(self, transpose_dict):
        '''
        transpose_dict (dict): a transpose dictionary
        
        Returns: an encrypted version of the message text, based 
        on the dictionary
        '''
        
        # pass #delete this line and replace with your code here
    
                
        
        text_shifted_lst = []
        text_original_lst = self.get_word_lst()
        
        def shift_word(word):
            
            word_shifted_lst = []
            
            for c in word:
                if c.isalpha():
                    word_shifted_lst.append(transpose_dict[c])
                else:
                    word_shifted_lst.append(c)
            
            return ''.join(word_shifted_lst)
            
        
        for word in text_original_lst:
            text_shifted_lst.append(shift_word(word))
        
          
        return ' '.join(text_shifted_lst)
        
        
        
class EncryptedSubMessage(SubMessage):
    def __init__(self, text):
        '''
        Initializes an EncryptedSubMessage object

        text (string): the encrypted message text

        An EncryptedSubMessage object inherits from SubMessage and has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        # pass #delete this line and replace with your code here
    
        SubMessage.__init__(self, text)
        self.valid_words = load_words(file_name=WORDLIST_FILENAME)
        self.word_lst = text.split()

    def decrypt_message(self):
        '''
        Attempt to decrypt the encrypted message 
        
        Idea is to go through each permutation of the vowels and test it
        on the encrypted message. For each permutation, check how many
        words in the decrypted text are valid English words, and return
        the decrypted message with the most English words.
        
        If no good permutations are found (i.e. no permutations result in 
        at least 1 valid word), return the original string. If there are
        multiple permutations that yield the maximum number of words, return any
        one of them.

        Returns: the best decrypted message    
        
        Hint: use your function from Part 4A
        '''
        # pass #delete this line and replace with your code here
    
        dic = {}
        lst = get_permutations('aeiou')
        
        for perm in lst:
            perm_dic = self.build_transpose_dict(perm)
            x = SubMessage(self.apply_transpose(perm_dic))
            n = 0
            for word in x.get_word_lst():
                if is_word(self.get_valid_words(),word):
                    n += 1
            dic[perm] = n
        
        correct_perm = max(dic, key=dic.get)
        correct_dic = self.build_transpose_dict(correct_perm)
        
        t = self.apply_transpose(correct_dic)
            
        return t  
    

if __name__ == '__main__':

    # Example test case
    message = SubMessage("Hello World!")
    permutation = "eaiuo"
    enc_dict = message.build_transpose_dict(permutation)
    print("Original message:", message.get_message_text(), "Permutation:", permutation)
    print("Expected encryption:", "Hallu Wurld!")
    print("Actual encryption:", message.apply_transpose(enc_dict))
    enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
    print("Decrypted message:", enc_message.decrypt_message())
     
    #TODO: WRITE YOUR TEST CASES HERE
    
    message2 = SubMessage("I have, a life?")
    permutation2 = "oieua"
    enc_dict2 = message2.build_transpose_dict(permutation2)
    print("Original message:", message2.get_message_text(), "Permutation:", permutation2)
    print("Expected encryption:", "E hovi, o lefi?")
    print("Actual encryption:", message2.apply_transpose(enc_dict2))
    enc_message2 = EncryptedSubMessage(message2.apply_transpose(enc_dict2))
    print("Decrypted message:", enc_message2.decrypt_message())
    
    message3 = SubMessage("The BOOK, is on the (TABLE): mine")
    permutation3 = "uoiea"
    enc_dict3 = message3.build_transpose_dict(permutation3)
    print("Original message:", message3.get_message_text(), "Permutation:", permutation3)
    print("Expected encryption:", "Tho BEEK, is en tho (TUBLO): mino")
    print("Actual encryption:", message3.apply_transpose(enc_dict3))
    enc_message3 = EncryptedSubMessage(message3.apply_transpose(enc_dict3))
    print("Decrypted message:", enc_message3.decrypt_message())
