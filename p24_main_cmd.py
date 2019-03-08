""" To demonstrate main functions and command line arguments
    Command line arguments are accessible through sys.argv

    sample url = 'http://sixty-north.com/c/t.txt'
    to import -  from p22_main_cmd import *
    to execute -  main["http://sixty-north.com/c/t.txt']"""

import sys
from urllib.request import urlopen

def fetch_words(url):
    with urlopen(url) as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)
    return story_words


def print_items(items):
    for item in items:
        print(item)


def main(url):
    words = fetch_words(url)
    print_items(words)

if __name__ =='__main__':
    main(sys.argv[1])
