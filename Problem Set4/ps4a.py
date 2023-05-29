# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence, step = 0,lst=[]):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''

    #delete this line and replace with your code here

    
    
    if step == len(sequence):
       lst.append("".join(sequence))
    
    for i in range(step, len(sequence)):
        
        sequence_copy = [character for character in sequence]
        sequence_copy[step],sequence_copy[i] = sequence_copy[i],sequence_copy[step]
        get_permutations(sequence_copy,step + 1)
    
    
    return lst
    

if __name__ == '__main__':
   #EXAMPLE
   example_input = 'abc'
   print('Input:', example_input)
   print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
   print('Actual Output:', get_permutations(example_input))
    
   # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    # pass #delete this line and replace with your code here
   print('Input:', "abc")
   print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
   print('Actual Output:', get_permutations("abc"))
    
   print("====================================================================")
    
   print('Input:', "nop")
   print('Expected Output:', ['nop', 'npo', 'onp', 'opn', 'pon', 'pno'])
   print('Actual Output:', get_permutations("nop"))
    
   print("====================================================================")
    
   print('Input:', "jac")
   print('Expected Output:', ['jac', 'jca', 'ajc', 'acj', 'cja', 'caj'])
   print('Actual Output:', get_permutations("jac"))
