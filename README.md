# Extended-Gamblers-Ruin-Problem
A computational exploration of an extended version of the classic Gambler's Ruin problem.

### The Problem
The Gambler's Ruin Problem is a classic probability problem. The original problem statement is as follows: suppose you are gambler making a series of bets. On each bet, you bet one coin, and there is a probability p that you win and receive two coins back (thus increasing your total wealth by one) and a probability 1-p that you lose the coin that you just bet (thus decreasing your total wealth by one). Being a stubborn gambler, you will not leave the casino until either your total wealth has reached some number of coins N or you have lost all of your money. Now, given values of 0 <= p <= 1, N, and the amount of money you start with, i, with 0 <= i <= N, what is the probability that you will go broke (or equivalently the probability that your wealth reaches N)?

This version of the problem is very stimulating in itself, and has a relatively simple but enlightening solution. To the readers that have not seen it before, I encourage you to try and find its solution, being very careful not to spoil the reward by consulting outside sources. If a hint must be given, it is that this is a probability problem, and probability problems often have nice connections to recursive structures.

But now we shift our attention to another version of the problem. Several generalizations exist, but the one that we are interested is as follows: suppose that as the gambler you could now bet any number of coins that you desire on each turn (provided of course that you have those coins). Everything else is as before; you will still not leave the casino until either your wealth runs out or reaches N, you start with i coins, and on each bet, there is probability p of winning and 1-p loosing. Notice however that now on each bet, if you win, your net wealth increases by k coins, and if you lose, your net wealth decreases by k coins, where 1 <= k <= current wealth is the amount that you chose to bet. Also notice that it is now possible to do things such as bet all of your money at once, or bet so much on a turn that if you win your wealth would surpass N (say if you have 8 coins and N is 10, if you bet all 8 coins and win then your wealth would be 16 coins, at which point you would just exit the casino).

Now what is the probability of winning? You should notice that since you now have potentially many choices on each bet, there is a notion of an optimal strategy such that given values of p, N, and current wealth, there is an optimal amount of coins k that you can bet that maximizes your chances of getting to N. Finding this optimal strategy (or strategies) is half the battle, and finding the overall probability of winning using this optimal strategy is the other half.

### The Optimal Strategy

Only look at this section and the rest once you have exhausted all possible energy on the problem. A complex problem like this should be contemplated over the span of weeks and months, which will yield results slowly but steadily. It is very likely that you will get stuck on dead ends for long periods of time. Do not give up when this happens, as this is the part that makes the reward worth it.

First on figuring out the optimal strategy. Basically, the intuition is as follows: if p > 0.5, then on each bet you are more likely to win than you are too lose. Furthermore, as the number of bets increases, it becomes exponentially less likely that the number of times you have lost exceeds the number of times you have won. As such, you can rely on a net increase in wealth over the long run. But how much do you bet on each turn? The minimum possible amount; one coin. This is because by betting a small amount of money, you can expect your wealth to fluctuate up and down by tiny amounts on each turn, but likely steadily climb as you bet more. In contrast, if you bet a lot, say all of your money, you stand a large chance of losing it all (1 - p), whereas by betting tiny amounts this is far less likely since the large number of turns means that we will be dealing with powers of (1 - p), which quickly deteriorate, much faster than the powers of p, which indicate the probabilities of our winning streaks.

If p < 0.5. You can't expect to win more times than lose over the long run. In fact, the more times you bet, the more significant the impact of loss will be on your wealth. Therefore, the optimal strategy for any circumstance is one that minimizes the number of bets required in that circumstance. This means that from a particular starting point i, such a strategy should optimally minimize the amount of bets required to reach N, and also minimize the number of bets in any branching path that will result from betting according to this strategy. It seems like betting the maximum possible amount on each turn, but in such a way that we never bet with the possibility of increasing our wealth beyond N, is the optimal strategy. However, note that it is important to consider not only the least number of bets we require to win from our current starting point, but also the least number of bets required to win if we inccur a loss at any point, which will yield a new starting point, and so we must do an analysis for that new starting point, which will again yield new hypothetical starting points, and so on. As you can see, the situation is more complicated than we thought. This looks like never ending recursion.

This complexity is why it is hard to come up with a rigorously optimal answer to this problem. However, progress can still be made. We can do a theoritical analysis where we set up the equations representing the original gambler's ruin problem, but now instead of betting one on each turn, we have a fixed variable k representing the amount we bet on each turn. After solving the equations through a process analogous to the original gambler's ruin problem, we obtain an expression representing the overall probability of winning given i, N, p, and k. It turns out that if p < 0.5, this expression is maximized when k is maximized, and if p > 0.5, the expression is minimized when k is as small as possible (so one, given the constraints) (as for p = 0.5?? To be honest, I don't remember... The reader is encouraged to carry out the analysis on their own) So this gives some support to the above hypotheses. Note however that this is incomplete because in the full problem we are not limited to betting a fixed amount on each turn.

Furthermore, we can test these strategies out by

<!-- Problem statement, (discoveries, derivations, function derivations, observations), how to use, unexplored avenues -->
<!-- Incomplete -->
