# To play the game ghost, we're going to find words that start with specific letters. 
# However, we have to be careful not to be the player that completes the spelling of a word.

# First, we'll accept user input letters:
ghost = ['b', 'l', 'a']

# To calculate whether a word will get you out, we need to input the number of players
num_of_players = 3
position = 2

# Load our dictionary of words
with open('english-words.txt') as f:
          english = f.read().splitlines()

# Start with all words that begin with the letters
possible_words = []
for word in english:
    candidate_word = word.startswith(''.join(ghost))
    # find words that start with letters and have additional letters (needed for len() staying in bounds) 
    if candidate_word and len(word) != len(ghost):
        possible_words.append(word)

# Take out words that begin with other legal words (either three letters or four letters), as the round is over once a word is spelled 
possible_legal_words = []
for word in possible_words:    
    for x in range(3, len(word)):
        if word[0:x] in english:
            break
    # we're going to use an else on the for loop!
    else:
        possible_legal_words.append(word)

# Chose words that won't end on player, depending on how many other players there are
legal_not_losing_words = [word for word in possible_legal_words if (len(word) - position) % num_of_players != 0]

# Display results by letter with corrosponding words
next_letters = [x[len(ghost)] for x in legal_not_losing_words]
for letter in sorted(set(next_letters)):
    print(letter, 
          [word for word in legal_not_losing_words if word[len(ghost)] == letter])


# Find forced wins 