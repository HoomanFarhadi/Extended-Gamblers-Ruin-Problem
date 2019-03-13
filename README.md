# Extended-Gamblers-Ruin-Problem
A computational exploration of an extended version of the classic Gambler's Ruin problem.

### The Problem
The Gambler's Ruin Problem is a classic probability problem. The original problem statement is as follows: suppose you are gambler making a series of bets. On each bet, you bet one coin, and there is a probability p that you win and receive two coins back (thus increasing your total wealth by one) and a probability 1-p that you lose the coin that you just bet (thus decreasing your total wealth by one). Being a stubborn gambler, you will not leave the casino until either your total wealth has reached some number of coins N or you have lost all of your money. Now, given values of 0 <= p <= 1, N, and the amount of money you start with, i, with 0 <= i <= N, what is the probability that you will go broke (or equivalently the probability that your wealth reaches N)?

This version of the problem is very stimulating in itself, and has a relatively simple but enlightening solution. To the readers that have not seen it before, I encourage you to try and find its solution, being very careful not to spoil the reward by consulting outside sources. If a hint must be given, it is that this is a probability problem, and probability problems often have nice connections to recursive structures.

But now we shift our attention to another version of the problem. Several generalizations exist, but the one that we are interested is as follows: suppose that as the gambler you could now bet any number of coins that you desire on each turn (provided of course that you have those coins). Everything else is as before; you will still not leave the casino until either your wealth runs out or reaches N, you start with i coins, and on each bet, there is probability p of winning and 1-p loosing. Notice however that now on each bet, if you win, your net wealth increases by k coins, and if you lose, your net wealth decreases by k coins, where 1 <= k <= current wealth is the amount that you chose to bet. Also notice that it is now possible to do things such as bet all of your money at once, or bet so much on a turn that if you win your wealth would surpass N (say if you have 8 coins and N is 10, if you bet all 8 coins and win then your wealth would be 16 coins, at which point you would just exit the casino).

Now what is the probability of winning? You should notice that since you now have potentially many choices on each bet, there is a notion of an optimal strategy such that given values of p, N, and current wealth, there is an optimal amount of coins k that you can bet that maximizes your chances of getting to N. Finding this optimal strategy (or strategies) is half the battle, and finding the overall probability of winning using this optimal strategy is the other half.

Only proceed to the rest of the sections once you have exhausted all possible energy on the problem. A complex problem like this should be contemplated over the span of weeks and months, which will yield results slowly but steadily. It is very likely that you will get stuck on dead ends for long periods of time. Do not give up when this happens, as this is the part that makes the reward worth it.

### The Optimal Strategy
Basically, the intuition is as follows: if p > 0.5, then on each bet you are more likely to win than you are too lose. Furthermore, as the number of bets increases, it becomes exponentially less likely that the number of times you have lost exceeds the number of times you have won. As such, you can rely on a net increase in wealth over the long run. But how much do you bet on each turn? The minimum possible amount; one coin. This is because by betting a small amount of money, you can expect your wealth to fluctuate up and down by tiny amounts on each turn, but likely steadily climb as you bet more. In contrast, if you bet a lot, say all of your money, you stand a large chance of losing it all (1 - p), whereas by betting tiny amounts this is far less likely since the large number of turns means that we will be dealing with powers of (1 - p), which quickly deteriorate, much faster than the powers of p, which indicate the probabilities of our winning streaks.

If p < 0.5. You can't expect to win more times than lose over the long run. In fact, the more times you bet, the more significant the impact of loss will be on your wealth. Therefore, the optimal strategy for any circumstance is one that minimizes the number of bets required in that circumstance. This means that from a particular starting point i, such a strategy should optimally minimize the amount of bets required to reach N, and also minimize the number of bets in any branching path that will result from betting according to this strategy. It seems like betting the maximum possible amount on each turn, but in such a way that we never bet with the possibility of increasing our wealth beyond N, is the optimal strategy. However, note that it is important to consider not only the least number of bets we require to win from our current starting point, but also the least number of bets required to win if we incur a loss at any point, which will yield a new starting point, and so we must do an analysis for that new starting point, which will again yield new hypothetical starting points, and so on. As you can see, the situation is more complicated than we thought. This looks like never ending recursion.

This complexity is why it is hard to come up with a rigorously optimal answer to this problem. However, progress can still be made. We can do a theoretical analysis where we set up the equations representing the original gambler's ruin problem, but now instead of betting one on each turn, we have a fixed variable k representing the amount we bet on each turn. After solving the equations through a process analogous to the original gambler's ruin problem, we obtain an expression representing the overall probability of winning given i, N, p, and k. It turns out that if p < 0.5, this expression is maximized when k is maximized, and if p > 0.5, the expression is minimized when k is as small as possible (so one, given the constraints) (as for p = 0.5?? To be honest, I don't remember... The reader is encouraged to carry out the analysis on their own). So this gives some support to the above hypotheses. Note however that this is incomplete because in the full problem we are not limited to betting a fixed amount on each turn.

Furthermore, we can test these strategies out by running simulations. In the module, four sample strategies are defined:
 * stratmax: Bet the maximum amount of money that does not result in wealth going above N on each turn.
 * startmin: Bet the minimum amount of money on each turn in such a way that the number of bets required to reach N from the starting is still minimal.
 * stratrand: Bet a random amount (that is within our wealth) on each turn.
 * stratone: Bet 1 on each turn.
 
 stratrand is a self-explanatory control, and stratmax and stratone are the optimal strategies discussed above for the p < 0.5 and the p > 0.5 case, respectively. stratmin is a second strategy which seems optimal for the p < 0.5 case. This strategy is less intuitive than stratmax, but the basic idea to minimize bets over the long run is still the same. On each turn, stratmin bets the least amount possible so that the minimal number of bets required to reach N if the bet were to succeed would be the same as if stratmax had been used instead of stratmin on that first bet.
 
The function teststrats runs a randomized simulation of these four strategies for a specified number of iterations, recording the proportion of wins (the gambler reaches N) to the total iteration count. Running this simulation does indeed support our hypotheses, with stratmin and stratmax performing similarly and better than all other strategies for the p < 0.5 case, and stratone performing better than all other strategies for the p > 0.5 case.

The analysis is obviously not complete, and the optimal strategy for each case of i, N, and p is still not rigorously proven. The reader is encouraged to try to solve this problem further.

We now shift our attention to how the probabilities of winning for the "optimal" strategies can be calculated.

### Computational Approach and Recursion
We are trying to find P(i) for any i given p and N, where P(i) is the probability of eventually reaching a wealth of N. One way we can do this (there were numerous attempts to find more elegant ways to no avail) is through recursion. Specifically, because the number of possible i is finite, the tree obtained through enumerating the set of possible outcomes from starting point i must eventually end at 0 or N, for which we know the values of, or reset to i, at which we can use recursion (actually, the recursion can happen with a different i, but in that case we just start our calculations with that value instead) For example, suppose N = 10, i = 3, and p < 0.5. The enumerating the possibilities of using startmax yields the following tree:

          0    0    6
          ^    ^    ^        
          |    |    |        //At each node, we bet according to stratmax, and branch out according to the possible outcomes.
     0    2 -> 4 -> 8 -> 10  //For example, at node with i = 4, we bet all our wealth, either losing it all, which would bring our
     ^    ^                  //wealth to 0, or gaining an additional 4, which brings our wealth to 8.
     |    |
     3 -> 6 -> 10                            
     
We stop when we arrive at 6 for the second time because now we can solve the recursion. Note that i = 6 is what we will be solving, because that is where the recursion occurred.

However, this methodology allows us to calculate all the probabilities of all i that we pass over by simply keeping track of how different P(i) are related to each other. For example, in the above scenario, we have:

P(3) = P(3)

P(6) = (1/p) P(3)

P(2) = (P(6) - p) / (1 - p) = ((1/p) P(3) - p) / (1 - p)

...And so on.

Through a similar manner, we can write all the probabilities for different values of i in terms of an arbitrary P(i), and upon solving the recursion we can simply substitute the value found into all the previous terms to find P(i) for all i that occur in the tree. Note however that some values of i do not occur in the tree. That means that there might be more than one recursive tree to solve to find P(i) for all values of i between 0 and N. (It is an interesting theoretical problem to think about these trees and their properties. Questions we might ask are: for a given N, how many different recursive trees exist? What do the structures of these trees look like? (For example, we might characterize the tree above as DIID (D for decrease and I for increase), because the recursive pattern (starting at 6) decreases once, then increases twice, then decreases once more, than repeats) Characterizing the tree sequences this way, what is the length of the longest/shortest sequence that we can get?)

But anyhow, this method is how the P(i,n,p) function calculates P(i) for i from 0 to n given n and p. It starts from i = 1 and works its way up to i = n - 1, storing the results of solved recursions in a cache in case they are used again as discussed above. Using the symbolic manipulation module sympy, this function can be made to return either a closed form expression in terms of p for P(i) or an evaluated approximation (which would make further calculations faster)  

### Figures

In addition to the P(i,n,p) function, several other functions are defined which visualize the probability data with the help of matplotlib.py:
* i_sketch: Graphs P(i) vs i for all i between 0 and n, given n and p.
* p_sketch: Graphs P(i) for different values of p (these values are taken from a partition decided beforehand), given n and i.
* n_sketch: Graphs P(i) for different values of n (these values are defined beforehand), given p and i.

These function were used to produce all the png figures produced in the repository. The name of each figure indicates the function and parameters that were used in producing. For example, n = 51 i = 37.png indicates that n and i were the constant independent variables used, with their values given as parameters to the p_sketch function.

Some of these graphs are straightforward and expected, but others are interesting and complex. For example, running i_sketch with n = 500 and p = 0.18 (the figure n = 500 p = 0.18.png) produces a graph similar to that of an exponential function, but with discontinuities at particular points (Question: are the locations of those discontinuities special in any way?). Marvellously, the region of the graph between two consecutive discontinuities is a scaled transformation of the entire graph: the function is self-similar (Why!? there has to be a deep connection between this geometric property and the problem). See the figure n=500 p=0.18 3rd segment zoom.png (which is the third of the segments between the discontinuities, counting from left to right) to observe this.

<!-- Problem statement, (discoveries, derivations, function derivations, observations), how to use, unexplored avenues (so much more to be done) -->
<!-- Connecting self similarity of figures with self similarity of strategies, isomorphisms of the recursion, GEB -->
<!-- Incomplete -->
