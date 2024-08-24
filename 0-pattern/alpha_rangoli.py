def print_rangoli(size):
    # your code goes here
    
    # rows = 2 * size - 1
    
    # for i in range(1, rows+1):
    #     if i <= size:
    #         print(chr(97 + size - i))
    #     else:
    #         print(chr(97 + i-size))
        
    char = [chr(i) for i in range (97, 97 + size)]
    width = (2 * size - 1) + ((size - 1) * 2)
    for i in range (1-size,size):
        second = list(char[(abs(i)):])
        first = list(reversed(second[1:]))
        total = first+second
        print('-'.join(total).center(width,'-'))
    
    

if __name__ == '__main__':
    n = int(input("Enter the size: "))
    print_rangoli(n)

