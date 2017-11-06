https://github.com/csides/SEChallenge/

Files Included:

people.txt (test file)
food.txt (test file)
drinks.txt (test file)
genTests.py (generate test files)
optimizeParty.py (decided which food and drinks to purchase given the budget)

Overall Approach:
The optimization decisions were aimed at replicating the real-life approach for choosing which items to 
purchase for a party or event. The main goal is to primarily have at least one option for food and
drink for each person. After this goal is achieved, we want to give everyone as many evenly distributed
options as possible. EG: we would rather have everyone with 2 options for food and drink, instead of one 
person with 80 options, and everyone else with 1. One caveat is we stated up front that we need to have
at least one food option and one drink option at the party. These first two choices were made simply based
off which items were the most popular among all people.


Algorithm:
The algorithm used to optimize the party choices was a slight variant on the standard knapsack algorithm. 
Our algorithm combines the standard dynamic programming approach with a constant factor reduction in order
to guarantee a true polynomial (n^2) time approach to the problem. This comes at a cost of the algorithm 
approximating the true optimal solution (according to our valuation approach), however using
an epsilon value of .05, we state that our determined solution will be above 95% of the true optimal
solution. See http://math.mit.edu/~goemans/18434S06/knapsack-katherine.pdf for more on the knapsack
approximation algorithm.

Optimization Approach:
We optimized the value of each item (and thus the likelihood of it being chosen) according to the total 
amount of people, the number of people that liked it, and the number of things that each person liked of
the people that liked it. This was done by assigning each person a 'food value' and a 'drink value'. Each
person's food/drink value would decrease based off the number of food and drinks they liked. This is a
valid approach, as people who like a lot of items, are more likely to have a favorable option selected
in the final choice of which items to buy. The result equation for the food (or drink) value for each person
was: foodValue = 1/(number of food items liked) + 1/(total number of people)^(0.3). As the value for each item
was calculated by summing the item value for each person that preferred it, this gave an advantage in terms of
preference weight (how much their preference would sway the algorithm) according to how many items they liked,
in the aims of having everyone have an item that they liked.

Assumptions Made:
The knapsack algorithm used requires integer costs (weights) of the items (drinks and food items). 
In terms of the problem, this would mean rounding each item to the nearest dollar.
Additionally, the assumption was made that each person preferred at least 1 food item 
and 1 drink, and at most n/5 items (one fifth of the total options for food or drink). The algorithm
will successfully work with any maximum value for preferences, but needs at least 1 preference. Lastly,
I assumed that our budget is large enough to purchase any 1 drink and any 1 food. This simplifies any
calculation to guaranteeing one food and one drink at the party.

Successes:
Our algorithm successfully reduced the number of people that had no food or drink options, when compared to the option where the value of each item was only how many people liked it. Additionally, our algorithm scales well with budget increases, meaning that increasing the budget significantly decreases the number of people with no food or drink options.

Failures:
Our algorithm, based off value to cost, significantly preferred drinks to food items, as drinks were generated as lower cost items, and had the same preference value per person. This resulted in more drink options being purchased, and less people having a food option they liked.

Conclusion:
The algorithm in question was a good start to solve the given problem taking into account my overall approach. However, the algorithm has notable flaws that could definitely be improved. One noted approach that could provide significant improvement is the dynamic re-weighting of items as the process goes on. This would steadily give more weight to items that satisfy more of the remaining people, aiming to achieve a solution where the most people have at least one option at the lowest cost.


