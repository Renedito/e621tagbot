from tags import tagsList
import random

if __name__ == "__main__":
    random_entry = random.choice(tagsList)      # Select a random tag from tags list
    print(random_entry)                         # DEBUG: Makes Actions print the tag on the log 