Files Included:

people.txt (test file)
food.txt (test file)
drinks.txt (test file)
genTests.py (generate test files)
optimizeParty.py (decided which food and drinks to purchase given the budget)

Overall Approach:
The optimization decisions were aimed at replicating the real life approach for choosing which items to 
purchase for a party or event. The main goal is to primarily have at least one option for food and
drink for each person. After this goal is acheived, we want to give everyone as many evenly distributed
options as possible. EG: we would rather have everyone with 2 options for food and drink, instead of one 
person with 80 options, and everyone else with 1. One caveat is we stated up front that we need to have
at least one food option and one drink option at the party. These first two choices were made simply based
off which items were the most popular among all people.


Algorithm:


Optimization Approach:


Assumptions Made:
The knapsack algorithm used requires integer costs (weights) of the items (drinks and food items). 
In terms of the problem, this would mean rounding each item to the nearst dollar.
Additionally, the assumption was made that each person had a preference for at least 1 food item 
and 1 drink, and at most n/5 items (one fifth of the total options for food or drink). The algorithm
will successfully work with any maximum value for preferences, but needs at least 1 preference. Lastly,
I assumed that our budget is large enough to purchase any 1 drink and any 1 food. This simplifies any
calculation to garunteeing one food and one drink at the party.

Successes:

Failures:
