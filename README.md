# Ghost game helper

 This code generates letters for a player playing the game "ghost" (see [Wikipedia](https://en.wikipedia.org/wiki/Ghost_(game)) for the rules of the game).

The code `ghost.py` will search for words in `english-words.txt` that can be played. It will filter out words that cannot legally be played in the game (e.g. if the beginning of the word already spells another word), as well as words that will end on the player, which would cause the player to lose.

### Inputs: 

- `ghost` are the letters that have already been played
- `num_of_players` is how many players there are
- `position` is the position of the player's turn for the round (whether player went first, second, etc.)



Sample input:
> ghost = ['b', 'l', 'a']   

> num_of_players = 3     

> position = 2         


Sample output:

| letter |words|
| ------------- |:-------------:|
|  b  |  ['blab']  | 
|  d  |  ['blad']  | 
|  e  |  ['blae']  | 
|  g  |  ['blag']  | 
|  h  |  ['blah']  | 
|  i  |  ['blaise', 'blaize']  | 
|  m  |  ['blaming']  | 
|  n  |  ['blanquette']  | 
|  r  |  ['blaring', 'blarney']  | 
|  s  |  ['blaspheme', 'blasphemy']  | 
|  t  |  ['blat']  | 
|  u  |  ['blaubok']  | 
|  w  |  ['blawort']  | 
|  y  |  ['blay']  | 
|  z  |  ['blazing', 'blazon']  | 