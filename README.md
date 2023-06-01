# FARMER - dice game
A game for two players. On his turn a player may roll two twelve-sided 
dice with animals or exchange animals. To win player have to collect one horse, 
cow, pig, sheep and rabbit each.

App created in Python 3.8.
## Roll the dice
If both dice show the same animal, the player gets that animal from the main 
herd. Once the player has any animals, then after throw, he receives as many 
animals of the discarded species from the herd as he has full pairs
of that species (including those rolled on the dice).

ATTENTION! If a player rolls a fox, they lose all of their rabbits except one.
If he rolls a wolf, he loses all animals he owns except a horse, rabbits and 
a small dog (if he has it). A small dog protects from a fox attack (the rabbits
stay safe, but the player loses the little dog) and the big dog protects from 
the wolf's attack (the animals stay safe, but the player loses the big dog).

## Animal exchange
The player may make one of the following exchanges:

A) Trade 6 rabbits for 1 sheep.

B) Trade 2 sheep for 1 pig.

C) Trade 3 pigs for 1 cow.

D) Trade 2 cows for 1 horse.

E) Trade 1 sheep for 1 small dog.

F) Trade 1 cow for 1 large dog.
