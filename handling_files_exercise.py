import string
from collections import Counter
import heapq

# Read the file and process the text
with open("test.txt", "r") as f:
    text = f.read()
    
    # Remove punctuation and convert to lowercase
    text = "".join([x for x in text if x not in string.punctuation or x in string.whitespace]).lower()
    
    # Split text into words
    words = text.split()
    
    # Count the frequency of each word
    word_counts = Counter(words)
    
    # Get words that are repeated
    repeated_words = [word for word, count in word_counts.items() if count > 1]
    
    # Get the counts of all words
    values_ = list(word_counts.values())

    # Find the top 20 largest counts
    top_20_maiores = heapq.nlargest(20, values_)

    # Map counts to words
    count_to_words = {}
    for word, count in word_counts.items():
        if count in top_20_maiores:
            if count not in count_to_words:
                count_to_words[count] = []
            count_to_words[count].append(word)
    
    # Get the words corresponding to the top 20 largest counts
    chaves_maiores = [word for count in top_20_maiores for word in count_to_words.get(count, [])]
    
    # Print results
    
    print("Count to words mapping:", count_to_words)
    print("Words with top 20 counts:", chaves_maiores)
