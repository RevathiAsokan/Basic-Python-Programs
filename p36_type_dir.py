""" In Python everything is object
    dir() - to see the attributes of an object
    type() - to see the type of object
    type(module.attribute) - type of any attribute"""

from urllib.request import urlopen
import p22_import_type1 as words # to demonstrate type and dir

def fetch_words():
    with urlopen('http://sixty-north.com/c/t.txt') as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)
    return story_words


def print_words(story_words):
    for word in story_words:
        print(word)

def main():
    words = fetch_words()
    print_words(words)

if __name__ =='__main__':
    main()

print("type(words) is ", type(words))
print("dir(words) is ", dir(words))
print("type(fetch_words) is ", type(words.fetch_words))
print("dir(fetch_words) is ", dir(words.fetch_words))
