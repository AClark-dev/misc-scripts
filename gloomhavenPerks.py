from sympy.utilities.iterables import multiset_permutations
import pandas as pd

# Hardcoded available perk list, using Cragheart as an example
# Formatted as tuples: (change in number of cards, change in sum of deck)
# i.e. (delta x, delta S)
# e.g. (-4, 0) means remove four cards without changing the sum of the deck
myList = [(-4,0),
          (0, 2), (0, 2), (0, 2),
          (3, 2),
          (1, 1), (1, 1),
          (1, 2), (1, 2)]

# Initialize the storage variables
myMeansList = []
# Find the unique permutations of the multiset
# corresponding to a different ordering of perk choices
myListPermutations = list(multiset_permutations(myList))

# Loop over the permutations
for per in myListPermutations:
    # Set the state of the default deck
    myMeans = [0]
    numCards = 20
    deckSum = 0
    # Loop over the perks in the permutations in order
    for perk in per:
        # Update the sum of cards and number of cards in the deck
        numCards += perk[0]
        deckSum += perk[1]
        # Find the new mean of the deck and store it
        newMean = (deckSum)/(numCards)
        myMeans.append(newMean)
    # Store the list of means of this permutation
    myMeansList.append(myMeans)

# Convert to a dataframe for better computation
df = pd.DataFrame(myMeansList)

# Initialize storage variables
maxRowsByCol = []
# Loop over the columns
for col in df.columns:
    # Find the row indices of the rows which contain the max value
    maxRowsByCol.append(set(df.loc[df[col] == df[col].max()].index))
# Find the row(s) which have max value 
maxRows = set.intersection(*[x for x in maxRowsByCol])

# Check there exists a row which has max value for each column
assert maxRows, "No single row contains the max value for each column"
# Print the output
for x in maxRows:
    print(f"Perk choice maximising the mean average:\n{myListPermutations[x]}")