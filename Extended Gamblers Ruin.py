import random
import time
import matplotlib.pyplot as plt
import math
import re
from sympy import *

#What was done?
#Analysis with fixed value k to bet on each turn. This revealed k = 1 is optimal for p < 0.5 and maximum k for which minimal number of bets for p > 0.5, p = 0.5?
#A heuristical approach of considering the outcome graph of a strategy, knowing that less bets until winning would indicate more optimality if p < 0.5

#This function calculates the probability of winning given values for i,n, and p. The function is based on evaluating the recursive statements that are obtained when considering the gambler's possible outcomes
#at any state. These recursive statements are expanded into other recursions many times. Since the cardinality of the gambler's possible states is finite, the recursive equations eventually circle back into
#themselves, which allows for a solution. This solution can be returned as a formula in terms of n, i, and p or evaluated for specific values of these variables. In the later functions, when we want to for
#example find out the probabilites for all possible values of i given an n and p, the recursive equations depend on states whos probabilities were calculated earlier. Therefore, using a cache allows us
#to calculate these values much faster. Storing inexact evaluations instead of original formulas in the cache makes these functions even faster, but the evaluated cache, as it is currently implemented, is
#prone to numberical underflow and overflow. This probability function is based upon the (probably) optimal strategy of betting the maximal amount possible without going over the desired winning on
#each turn.
cache = {}
def P(i,n,p,evaluate=True,use_cache=True,evaluated_cache=False):
    if use_cache == False:
        org_i = i
        encountered = {}
        P,x = symbols("P x")
        expr = x
        sub1 = P * x
        sub2 = P + (1 - P) * x
        while True:
            if i == 0 or i == n:
                break
            if i <= n / 2:
                i = 2 * i
                expr = expr.subs(x,sub1)
            elif i > n / 2:
                i = 2 * i - n
                expr = expr.subs(x,sub2)
            #print(expr)
            if i in encountered:
                break
            else:
                encountered[i] =  expr
        if i == 0:
            expr = expr.subs(x,0)
        elif i == n:
            expr = expr.subs(x,1)
        elif i in encountered:
            print("Calculating without cache")
            expr = solve(Eq(expr,encountered[i]),x)[0]
            expr = encountered[i].subs(x,expr)
        if evaluate == True:
            return expr.evalf(subs={P:p})
        return expr
    elif use_cache == True:
        if evaluated_cache == False:
            org_i = i
            c = None
            encountered = {}
            P,x = symbols("P x")
            expr = x
            sub1 = P * x
            sub2 = P + (1 - P) * x
            while True:
                if i == 0 or i == n:
                    break
                if i <= n / 2:
                    i = 2 * i
                    expr = expr.subs(x,sub1)
                elif i > n / 2:
                    i = 2 * i - n
                    expr = expr.subs(x,sub2)
                if i in encountered:
                    c = False
                    break
                elif tuple([i,n]) in cache:
                    c = True
                    break
                else:
                    encountered[i] =  expr
            if i == 0:
                expr = expr.subs(x,0)
            elif i == n:
                expr = expr.subs(x,1)
            elif c == True:
                print("Getting from cache")
                expr = expr.subs(x,cache[tuple([i,n])])
            elif c == False:
                print("Calculating without cache")
                expr = solve(Eq(expr,encountered[i]),x)[0]
                expr = encountered[i].subs(x,expr)
            for k in encountered:
                if not tuple([k,n]) in cache:
                    print("Adding P(" + str(k) + ") to cache")
                    new = solve(Eq(expr,encountered[k]),x)[0]
                    cache[tuple([k,n])] = new
            if evaluate == True:
                return expr.evalf(subs={P:p})
            return expr
        elif evaluated_cache == True:
            org_i = i
            c = None
            encountered = {}
            x = symbols("x")
            expr = x
            sub1 = p * x
            sub2 = p + (1 - p) * x
            while True:
                if i == 0 or i == n:
                    break
                if i <= n / 2:
                    i = 2 * i
                    expr = expr.subs(x,sub1)
                elif i > n / 2:
                    i = 2 * i - n
                    expr = expr.subs(x,sub2)
                if i in encountered:
                    c = False
                    break
                elif tuple([i,n,p]) in cache:
                    c = True
                    break
                else:
                    encountered[i] =  expr
            if i == 0:
                expr = expr.subs(x,0)
            elif i == n:
                expr = expr.subs(x,1)
            elif c == True:
                print("Getting from cache")
                expr = expr.subs(x,cache[tuple([i,n,p])])
            elif c == False:
                print("Calculating without cache")
                expr = solve(Eq(expr,encountered[i]),x)[0]
                expr = encountered[i].subs(x,expr)
            for k in encountered:
                if not tuple([k,n,p]) in cache:
                    print("Adding P(" + str(k) + ") to cache")
                    new = solve(Eq(expr,encountered[k]),x)[0]
                    cache[tuple([k,n,p])] = new
            return expr

#This function graphs the probability of winning for all i in the range [0,n] and fixed values for n and p.
def i_sketch(n,p,evaluate=True,use_cache=True,evaluated_cache=False):
    x_values = [x for x in range(0,n + 1)]
    y_values = []
    for x in range(0,n + 1):
        #print(cache)
        print("Working on P(" + str(x) + ")...")
        y_values.append(P(x,n,p,evaluate,use_cache,evaluated_cache))
    plt.plot(x_values,y_values,"ro")
    plt.show()

#This function graphs the probability of winning for a partioned set of possible values for p and fixed values for n and i.
def p_sketch(i,n,step=0.01):
    x_values = [x/100 for x in range(0,100,int(step*100))]
    y_values = []
    for x in x_values:
        #print(cache)
        print("Working on p = " + str(x) + "...")
        y_values.append(P(i,n,x))
    plt.plot(x_values,y_values,"ro")
    plt.show()

#This function graphs the probability of winning for variable values of n in a given range and fixed values for i and p.
def n_sketch(i,p,limit=100):
    x_values = [x for x in range(i,i+limit)]
    y_values = []
    for x in x_values:
        #print(cache)
        print("Working on n = " + str(x) + "...")
        y_values.append(P(i,x,p,True,False))
    plt.plot(x_values,y_values,"ro")
    plt.show()

#This strategy bets one unit on each turn. (probably) Optimal for p < 0.5.  
def stratone(i,n,p,t):
    track = {"w":0,"l":0}
    for j in range(t):
        initial = i
        while initial > 0 and initial < n:
            bet = 1
            if random.random() < p:
                initial += bet
            else:
                initial -= bet
            #print(initial)
            #time.sleep(0.5)
        if initial == n:
            track["w"] += 1
        else:
            track["l"] += 1
    return track

#This strategy bets the maximum possible amount that would not result in going over the winning amount on each turn. (probably) Optimal for p > 0.5
def stratmax(i,n,p,t):
    track = {"w":0,"l":0}
    for j in range(t):
        initial = i
        while initial > 0 and initial < n:
            left = n - initial
            bet = initial if left >= initial else left
            #bet = 1
            if random.random() < p:
                initial += bet
            else:
                initial -= bet
            #print(initial)
            #time.sleep(0.5)
        if initial == n:
            track["w"] += 1
        else:
            track["l"] += 1
    return track

#This strategy bets the minimum possible amount on each turn such that the number of bets required to reach n is the same as in stratmax. (probably) Optimal for p > 0.5; a second optimal strategy
def stratmin(i,n,p,t):
    track = {"w":0,"l":0}
    for j in range(t):
        initial = i
        while initial > 0 and initial < n:
            required = math.ceil(math.log((n/initial),2))
            minimum = math.ceil(n / (2 ** (required - 1)))
            bet = minimum - initial
            #bet = 250
            if random.random() < p:
                initial += bet
            else:
                initial -= bet
            #print(initial)
            #time.sleep(0.5)
        if initial == n:
            track["w"] += 1
        else:
            track["l"] += 1
    return track

#This strategy bets a random amount on each turn
def stratrand(i,n,p,t):
    track = {"w":0,"l":0}
    for j in range(t):
        initial = i
        while initial > 0 and initial < n:
            required = math.ceil(math.log((n/initial),2))
            minimum = math.ceil(n / (2 ** (required - 1)))
            left = n - initial
            minbet = minimum - initial
            maxbet = initial if left >= initial else left
            #print(minbet,maxbet)
            bet = random.randint(minbet,maxbet)
            #print(bet)
            if random.random() < p:
                initial += bet
            else:
                initial -= bet
            #print(initial)
            #time.sleep(2)
        if initial == n:
            track["w"] += 1
        else:
            track["l"] += 1
    return track

#Given values of i, n, and p, and the number of iterations t, test stratrand, stratmax, stratmin, and stratone and print out how many times each resulted in a win or a loss
def teststrats(i,n,p,t):
    print("One: " + str(stratone(i,n,p,t)))
    print("Max: " + str(stratmax(i,n,p,t)))
    print("Min: " + str(stratmin(i,n,p,t)))
    print("Random: " + str(stratrand(i,n,p,t)))

#Calculate the average winning rate of one of the strat functinos defined above over a given number of iterations
def averagestrat(i,n,p,t,strat,times):
    strategy = "strat" + strat
    s = 0
    for j in range(times):
        s += eval(strategy)(i,n,p,t)["w"]
    return s / times

#Function calls for the functions defined above
#teststrats(400,1000,0.05,1000)
#i_sketch(500,0.18)
#p_sketch(40,1000)
#n_sketch(37,0.18)
#print(P(37,107,0.18,True,False,False))

#It is interesting to think about how to calculate at what point the discontinuouties form in graphs of the i_sketch function
