import operator

STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]


def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    filename = input("seneca_falls.txt")
#print ("filename")

counts = dict()
bad_characters = '~`!@#$%^&*()_-+=1234567890{[}]|\\<,>.?/:;"\n'

with open("seneca_falls.txt", "r") as f:
    lines = f.readlines()
    
#print ( lines )

for line in lines:
    new_line = str()
    for character in line:
        if character not in bad_characters:
            new_line += character.lower()
            words = new_line.split(" ")
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
#print (counts)
    sort = sorted(counts.items(), key=operator.itemgetter(1))
    sort.reverse()
#print (counts)

if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)