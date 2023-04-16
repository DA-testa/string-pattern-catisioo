# python3

def read_input():
    
    info = input()
    if "I" in info:
        pattern = input().strip()
        text = input().strip()
    elif "F" in info:
        with open(f"tests/06") as f:
            info = f.read().split("\n")
            pattern = info[0].strip()
            text = info[1].strip()
    
    return (pattern, text)

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm 
    len_pat = len(pattern)
    len_tex = len(text)

    occurrences = []

    for i in range(len_tex-len_pat+1):
        temp = text[i:i+len_pat]
        if hash(temp) == hash(pattern):
            occurrences.append(i)
    # and return an iterable variable
    
    return [0]


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

