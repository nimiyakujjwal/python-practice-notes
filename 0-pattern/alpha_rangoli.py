""" HackerRank Question: Alpha Rangoli
The center of the rangoli has the first alphabet letter a, and the boundary has the  alphabet letter (in alphabetical order).

Function Description
    Complete the rangoli function in the editor below.

rangoli has the following parameters:
    int size: the size of the rangoli

Returns:
    string: a single string made up of each of the lines of the rangoli separated by a newline character (\n)

Input Format:
    Only one line of input containing , the size of the rangoli.

Constraints:
    0 < size < 27

"""

def print_rangoli(size):
    char = [chr(i) for i in range(97, 97 + size)]  # list of lower-case alphabets.
    width = (2 * size - 1) + ((size - 1) * 2)   # alphabets + no. of '-'
    for i in range(1-size, size):
        second = list(char[(abs(i)):])
        first = list(reversed(second[1:]))
        total = first + second
        print('-'.join(total).center(width, '-'))
    
    
if __name__ == '__main__':
    n = int(input("Enter the size: "))
    print_rangoli(n)

