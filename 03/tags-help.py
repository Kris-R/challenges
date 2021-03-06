from collections import Counter
from difflib import SequenceMatcher
from itertools import product
import re
import xml.etree.ElementTree as ET

IDENTICAL = 1.0
TOP_NUMBER = 10
RSS_FEED = 'rss.xml'
SIMILAR = 0.87
TAG_HTML = re.compile(r'<category>([^<]+)</category>')

def get_tags():
    """Find all tags (TAG_HTML) in RSS_FEED.
    Replace dash with whitespace."""
    tree = ET.parse(RSS_FEED)
    allCategories = []

    for nodes in tree.iter("category"):
        if re.search(r'-', nodes.text):
            nodes.text = re.sub(r'-', ' ', nodes.text)
            allCategories.append(nodes.text)
        else:
            allCategories.append(nodes.text)
    return allCategories, tree

    # Check to see whether elements have been changed:
    #
    # for nodes in tree.iter("category"):
    #     if re.search(r'-', nodes.text):
    #         print(">>>>", nodes.text)
    #     else:
    #         print("c", nodes.text) # 'c' for correct

def get_top_tags(tags):
    """Get the TOP_NUMBER of most common tags"""
    return Counter(tags[0]).most_common(TOP_NUMBER)

def get_similarities(tags):
    """Find set of tags pairs with similarity ratio of > SIMILAR
    Hint 1: compare each tag, use for in for, or product from itertools (already imported)
    Hint 2: use SequenceMatcher (imported) to calculate the similarity ratio
    Bonus: for performance gain compare the first char of each tag in pair and continue if not the same"""
    pairs = []
    for pair in product(tags[0], tags[0]):
        if pair[0] == pair[1]:
            pass
        else:
            s = SequenceMatcher(lambda x: x == " ", pair[0], pair[1])
            # Creates an object s from the difflib.SequenceMatcher class constructor
            if s.ratio() > SIMILAR:
                pairs.append(pair)
    return pairs

if __name__ == "__main__":
    tags = get_tags()
    top_tags = get_top_tags(tags)
    print('* Top {} tags:'.format(TOP_NUMBER))
    for tag, count in top_tags:
        print('{:<20} {}'.format(tag, count))
    similar_tags = dict(get_similarities(tags))
    print()
    print('* Similar tags:')
    for singular, plural in similar_tags.items():
        print('{:<20} {}'.format(singular, plural))
