# Game Theory Lecture Notes 1 A Brief Introduction 

Ju Hu<br>National School of Development<br>Peking University

Fall 2022

## Individual Decision Problems v.s. Strategic Interactions

- Recall from your Intermediate Microeconomics.
- Consumer's utility maximization problem:

$$
\begin{array}{rl}
\max _{x_{1}, x_{2} \geq 0} & u\left(x_{1}, x_{2}\right) \\
\text { s.t. } & p_{1} x_{1}+p_{2} x_{2} \leq w
\end{array}
$$

- Competitive firm's profit maximization problem:

$$
\max _{y \geq 0} p y-c(y)
$$

- These two problems are examples of individual decision problems: decision maker's utility/payoff is completely determined by his own choice.


## Individual Decision Problems v.s. Strategic Interactions

- In many situations, decision makers interact with each other:
- chess;
- oligopoly competition;
- auction;
- political campaign;
- In these situations, one participant's utility/payoff not only depend on his own choice but also on others'.
- We call these kinds of situations as strategic interactions.


## Individual Decision Problems v.s. Strategic Interactions

- Individual decision problems are easy to solve, e.g., first order condition, Lagrange multiplier.
- Strategic interactions are much more difficult to analyze.
- Rock-paper-scissors:
- If I predict that you will choose "Rock", I will choose "Paper".
- But if you predict my prediction, you will choose "Scissors".
- If I predict your prediction, I will choose "Rock".
- If you predict my prediction, ...
- Not a simple optimization problem.


## Individual Decision Problems v.s. Strategic Interactions

- From Theory of Games and Economic Behavior by von Neumann and Morgenstern (1944) on strategic interactions:
"[I]t is unlikely that a mere repetition of the tricks which served us so well in physics will do for the social phenomena too."
"[The] process of mathematization is not at all obvious. ... We shall find it necessary to draw upon techniques of mathematics which have not been used heretofore in mathematical economics, and ... further study may result in the future in the creation of new mathematical disciplines."
- Game theory provides a solution.


## Game Theory

- Game theory provides a language to describe a strategic interaction.
- We will learn how to write down a formal model.
- Game theory also offers a prediction about what rational players will do in a given strategic interaction.
- We will also learn how to solve the model.


## Review of Expected Utilities

- We always assume that agents are rational.
- Rational players try to maximize their utilities/payoffs.


## Review of Expected Utilities

## Definition 1.1

A simple lottery over outcomes $X=\left\{x_{1}, x_{2}, \ldots, x_{n}\right\}$ is defined as a probability distribution $p=\left(p\left(x_{1}\right), \ldots, p\left(x_{n}\right)\right)$, where $p\left(x_{k}\right) \geq 0$ is the probability that $x_{k}$ occurs and $\sum_{k=1}^{n} p\left(x_{k}\right)=1$.

- Consider literally a lottery that pays $\$ 0$ with probability $99 \%$ and $\$ 100$ with probability $1 \%$ :
- $X=\{0,100\}$;
- probability distribution $p$ with $p(0)=0.99$ and $p(100)=0.01$.
- Tomorrow's weather can be either sunny, cloudy or raining with probabilities $80 \%, 15 \%$ and $5 \%$ respectively:
- $X=\{s, c, r\}$;
- probability distribution $p$ with $p(s)=0.8, p(c)=0.15$ and $p(r)=0.05$.


## Review of Expected Utilities

## Definition 1.2

Let $u(x)$ be the player's payoff function over outcomes in $X=\left\{x_{1}, x_{2}, \ldots, x_{n}\right\}$, and let $p=\left(p_{1}, \ldots, p_{n}\right)$ be a lottery over $X$. Then we define the player 's expected payoff from the lottery $p$ as

$$
\mathbb{E}[u(x)] \equiv p_{1} u\left(x_{1}\right)+\ldots+p_{n} u\left(x_{n}\right)=\sum_{k=1}^{n} p_{k} u\left(x_{k}\right)
$$

- Expected payoff is the expectation of the payoffs from the outcomes with respect to the lottery $p$.
- In other words, it is the weighted average of the payoffs from the outcomes.


## Review of Expected Utilities

- Consider the previous weather example.
- Suppose an agent has two choices: carry an umbrella ( $u$ ) and not carry an umbrella $(n)$.
- Assume the agent's payoff is -1 if it does not rain and he carries an umbrella; 10 if it rains and he carries an umbrella; 0 if it does not rain and he does not carry an umbrella; -10 if it rains but he does not carry an umbrella.
- Then his expected payoff from carrying an umbrella is

$$
0.8 \times(-1)+0.15 \times(-1)+0.05 \times 10=-0.45
$$

and his expected payoff from not carrying an umbrella is

$$
0.8 \times 0+0.15 \times 0+0.05 \times(-10)=-0.5
$$

- Not carrying an umbrella is optimal.


# Game Theory Lecture Notes 2 

## Static Games with Complete Information

Ju Hu<br>National School of Development<br>Peking University

Fall 2022

## Motivating Examples

The prisoner's dilemma

- Two suspects are held in different rooms at the police station.
- Each of them has two choices: confess $(C)$ or deny $(D)$.
- If both of them deny, then both get 2 years in prison.
- If only one of them deny, then the suspect who denies gets 5 years in prison while the one who confesses gets 1 year.
- If both of them confess, then both get 4 years in prison.


## Motivating Examples

## The prisoner's dilemma

- We can represent this situation by the following $2 \times 2$ matrix:

$$
\text { Suspect } 2
$$

![](https://cdn.mathpix.com/cropped/2024_09_09_605858d45802b61328b8g-013.jpg?height=166&width=527&top_left_y=290&top_left_x=365)

Figure 2.1: The prisoner's dilemma

- Each row represents one of suspect 1's choice.
- Each column represents one of suspect 2's choice.
- Each entry in this matrix contains two numbers. The first one is suspect 1's payoff while the second one is suspect 2's payoff.
- Because each entry contains two numbers instead of one, such matrix is sometimes called a bi-matrix.


## Motivating Examples

The prisoner's dilemma

- Adding each of the numbers by 4 , we obtain:

![](https://cdn.mathpix.com/cropped/2024_09_09_605858d45802b61328b8g-014.jpg?height=154&width=300&top_left_y=373&top_left_x=483)

Figure 2.2: The partnership game

- E represents effort while $S$ represents shirking.


## Motivating Examples

## Rock-paper-scissors

- Two players simultaneously choose among rock (R), paper $(P)$ and scissors $(S)$.
- Rock beats scissors, scissors beats paper, and paper beats rock.
- The loser pays one dollar to the winner.
- If they choose the same, it is a draw and no one pays.
- Its situation is represented by the following $3 \times 3$ matrix:

|  | $R$ | $P$ | $S$ |
| ---: | :---: | :---: | :---: |
| $R$ | 0,0 | $-1,1$ | $1,-1$ |
| $P$ | $1,-1$ | 0,0 | $-1,1$ |
| $S$ | $-1,1$ | $1,-1$ | 0,0 |
|  |  |  |  |

Figure 2.3: Rock-paper-scissors

## Motivating Examples

Voting on a new agenda

- Three voters on a committee vote on whether to remain at the status quo or adopt a new policy.
- Each can vote "yes" $(Y)$, "no" $(N)$, or "abstain" $(A)$.
- Each receives a payoff 0 from the status quo.
- Players 1 and 2 receive a payoff 1 from the new policy, while player 3 receive -1 from it.
- Majority rule: the new policy is adopted only if strictly more than half of the voting voters vote $Y$.


## Motivating Examples

Voting on a new agenda

- We can represent this situation by the following matrices:

|  | $Y$ | $N$ | $A$ |  |
| :---: | :---: | :---: | :---: | :---: |
| $Y$ | $1,1,-1$ | $1,1,-1$ | $1,1,-1$ |  |
| $N$ | $1,1,-1$ | $0,0,0$ | $0,0,0$ |  |
|  | $1,1,-1$ | $0,0,0$ | $1,1,-1$ |  |
|  | $Y$ |  |  |  |
|  | $Y$ |  |  |  |


|  | $Y$ | $N$ |  |  |  |
| :---: | :---: | :---: | :---: | :---: | :---: |
| $Y$ | $1,1,-1$ | $0,0,0$ | $0,0,0$ |  |  |
| $N$ | $0,0,0$ | $0,0,0$ | $0,0,0$ |  |  |
| $A$ | $0,0,0$ | $0,0,0$ | $0,0,0$ |  |  |
| $N$ |  |  | $N$ |  |  |


|  | $Y$ | $N$ | $A$ |
| :---: | :---: | :---: | :---: |
| $Y$ | $1,1,-1$ | $0,0,0$ | $1,1,-1$ |
| $N$ | $0,0,0$ | $0,0,0$ | $0,0,0$ |
| $A$ | $1,1,-1$ | $0,0,0$ | $0,0,0$ |
|  | $A$ |  |  |
|  | $A$ |  |  |

Figure 2.5: Voting on a new agenda

- Voter 1 chooses one of the rows, voter 2 chooses one of the columns, and voter 3 chooses one of the tables.


## Normal Form Games

- Each of the above matrix informs us of three components:
- The players;
- Each player's available choices;
- The payoff to each player as a function of all players' choices.
- In fact, these three components together define a normal form game.
- Matrix representation is very intuitive. But it has its obvious drawbacks: it can only represent simple games.
- Therefore, we need a more general and formal way to describe a game.


## Normal Form Games

## Definition

## Definition 2.1

A normal form game includes three components as follows:

1. A finite set of players, $N=\{1,, 2, \ldots, n\}$.
2. A strategy space $S_{i}$ for each player $i \in N$.
3. A payoff function $v_{i}: S_{1} \times \cdots \times S_{n} \rightarrow \mathbb{R}$ for each player $i \in N$.

In summary, a normal form game is a triple $\Gamma=\left(N,\left\{S_{i}\right\}_{i=1}^{n},\left\{v_{i}\right\}_{i=1}^{n}\right)$.

- Strategy space $S_{i}$ contains all the available strategies for player $i$.
- Each element $s_{i} \in S_{i}$ is a player $i$ 's strategy.
- A vector of strategies $s=\left(s_{1}, \ldots, s_{n}\right) \in S_{1} \times \cdots \times S_{n}$ is a strategy profile.
- A normal form game $G$ is finite if every player's strategy space contains only finitely many strategies.


## Normal Form Games

## Definition

- A short hand notation.
- Given a strategy profile $s=\left(s_{1}, \ldots, s_{n}\right) \in S_{1} \times \cdots \times S_{n}$ and a player $i$, we usually use

$$
s_{-i} \equiv\left(s_{1}, \ldots, s_{i-1}, s_{i+1}, \ldots, s_{n}\right) \in S_{1} \times \cdots \times S_{i-1} \times S_{i+1} \times \cdots \times S_{n}
$$

to denote the strategies chosen by the players who are not player $i$.

- Thus, $S_{-i} \equiv S_{1} \times \cdots \times S_{i-1} \times S_{i+1} \times \cdots \times S_{n}$ is the set of all possible combinations of player $i$ 's opponents' strategies.
- In this spirit, we write $s=\left(s_{i}, s_{-i}\right)$ to denote the whole strategy profile. For example, we usually write $v_{i}\left(s_{i}, s_{-i}\right)$. In this way, we can easily separate the strategy chosen by player $i$ and those chosen by other players.


# Normal Form Games 

Examples

- The prisoner's dilemma:
- Set of players: $N=\{1,2\}$;
- Strategy space: $S_{1}=S_{2}=\{C, D\}$;
- Payoffs:

$$
\begin{aligned}
& v_{1}(D, D)=v_{2}(D, D)=-2, \\
& v_{1}(C, C)=v_{2}(C, C)=-4, \\
& v_{1}(D, C)=v_{2}(C, D)=-5, \\
& v_{1}(C, D)=v_{2}(D, C)=-1 .
\end{aligned}
$$

## Normal Form Games

## Examples

- Rock-paper-scissors:
- Set of players: $N=\{1,2\}$;
- Strategy space: $S_{1}=S_{2}=\{R, P, S\}$;
- Payoffs:

$$
\begin{aligned}
& v_{1}(R, R)=v_{1}(P, P)=v_{1}(S, S)=0 \\
& v_{1}(R, S)=v_{1}(S, P)=v_{1}(P, R)=1 \\
& v_{1}(S, R)=v_{1}(P, S)=v_{1}(R, P)=-1 \\
& v_{2}(R, R)=v_{2}(P, P)=v_{2}(S, S)=0 \\
& v_{2}(S, R)=v_{2}(P, S)=v_{2}(R, P)=1 \\
& v_{2}(R, S)=v_{2}(S, P)=v_{2}(P, R)=-1
\end{aligned}
$$

# Normal Form Games 

Examples

- Voting on a new agenda:
- $N=\{1,2,3\}$.
- $S_{1}=S_{2}=S_{3}=\{Y, N, A\}$.
- For $i=1,2$,

$$
v_{i}\left(s_{1}, s_{2}, s_{3}\right)= \begin{cases}1, & \text { if }\left|\left\{j \mid s_{j}=Y\right\}\right|>\left|\left\{j \mid s_{j} \neq A\right\}\right| / 2 \\ 0, & \text { otherwise }\end{cases}
$$

- For $i=3$,

$$
v_{3}\left(s_{1}, s_{2}, s_{3}\right)= \begin{cases}-1, & \text { if }\left|\left\{j \mid s_{j}=Y\right\}\right|>\left|\left\{j \mid s_{j} \neq A\right\}\right| / 2 \\ 0, & \text { otherwise }\end{cases}
$$

## Normal Form Games

## Examples

- Cournot competition.
- Two firms compete in their supplies in a market with demand curve

$$
P(Q)=\max \{100-Q, 0\}
$$

where $Q$ is the total supply of the products.

- Firm $i$ 's cost is $q_{i}^{2}$ if $q_{i}$ units of the product is produced.
- Normal form game:
- $N=\{1,2\}$;
- $S_{1}=S_{2}=\mathbb{R}_{+}$;
- $v_{i}\left(q_{i}, q_{j}\right)=D\left(q_{i}+q_{j}\right) q_{i}-q_{i}^{2}$.
-What about $n>2$ firms?


## Normal Form Games

## Examples

- Bertrand competition.
- Two firms compete in price in a market.
- The market contains a continuum of consumers of total mass 1.
- If firm $i$ 's price is lower than that of firm $j \neq i$, all consumers will buy from firm $i$.
- If two firms set the same price, then half of the buyers will buy from one firm and the others will buy from the other firm.
- Firm $i$ has a constant marginal cost $c_{i}$.
- Normal form game:
- $N=\{1,2\}$
- $S_{1}=S_{2}=\mathbb{R}_{+}$;

$$
v_{i}\left(p_{i}, p_{j}\right)= \begin{cases}p_{i}-c_{i}, & \text { if } p_{i}<p_{j} \\ 0, & \text { if } p_{i}>p_{j} \\ \frac{1}{2}\left(p_{i}-c_{i}\right), & \text { if } p_{i}=p_{j}\end{cases}
$$

## Normal Form Games

## Examples

$\rightarrow$ First price auction.

- There is one good to be sold.
- There are two bidders.
- The value of the good to bidder $i$ is $v_{i} \geq 0$.
- The bidders simultaneously bid a price.
- The one with the higher price wins the good and pays his own bid.
- The loser gets nothing and does not pay.
- If there is a tie in bids, then the good is randomly allocated to the two bidders with equal probability.


# Normal Form Games 

Examples

- Normal form game:
- $N=\{1,2\}$;
- $S_{1}=S_{2}=\mathbb{R}_{+}$;

$$
v_{i}\left(p_{i}, p_{j}\right)= \begin{cases}v_{i}-p_{i}, & \text { if } p_{i}>p_{j} \\ \frac{1}{2}\left(v_{i}-p_{i}\right), & \text { if } p_{i}=p_{j} \\ 0, & \text { if } p_{i}<p_{j}\end{cases}
$$

## Normal Form Games

## Examples

- Second price auction.
- Everything is the same with the first price auction except the payment rule.
- The winning bidder pays the second highest bid.
- Normal form game:
- $N=\{1,2\}$,
- $S_{1}=S_{2}=\mathbb{R}_{+}$,

$$
v_{i}\left(p_{i}, p_{j}\right)= \begin{cases}v_{i}-p_{j}, & \text { if } p_{i}>p_{j} \\ \frac{1}{2}\left(v_{i}-p_{j}\right), & \text { if } p_{i}=p_{j} \\ 0, & \text { if } p_{i}<p_{j}\end{cases}
$$

## Dominance

## Dominated strategies

- Consider the prisoner's dilemma:

\$\$

\$\$

Figure 2.6: The prisoner's dilemma

- Focus on player 1 (row player):
- If player 2 chooses $D$, choosing $D$ is strictly worse than $C$ for player 1 ;
- If player 2 chooses $C$, choosing $D$ is strictly worse than $C$ for player 1 as well.
- In sum, choosing $D$ is strictly worse than $C$ for player 1 regardless of what player 2 chooses.
- A similar observation applies to player 2 (column player) too: choosing $D$ is strictly worse than $C$ for player 2 regardless of what player 1 chooses.


## Dominance

## Dominated strategies

## Definition 2.2

Let $s_{i} \in S_{i}$ and $s_{i}^{\prime} \in S_{i}$ be possible strategies for player $i$. We say that $s_{i}^{\prime}$ is strictly dominated by $s_{i}$ if for any possible combination of the other players' strategies $s_{-i} \in S_{-i}$, player $i$ 's payoff from $s_{i}^{\prime}$ is strictly less than that from $s_{i}$. That is,

$$
v_{i}\left(s_{i}, s_{-i}\right)>v_{i}\left(s_{i}^{\prime}, s_{-i}\right), \forall s_{-i} \in S_{-i}
$$

- In the prisoner's dilemma, $D$ is strictly dominated by $C$ for both players.


## Dominance

## Dominated strategies

- A simple observation: a rational player will (should) never play a strictly dominated strategy.
- For the prisoner's dilemma, each player will never choose $D$.
- Therefore, both players will choose $C$ since each player only has two possible strategies.
- For the prisoner's dilemma, rationality alone is enough to offer a prediction about which outcome will prevail: $(C, C)$.


## Dominance

## Dominated strategies

|  | $L$ | $M$ | $H$ |
| ---: | :---: | :---: | :---: |
| $L$ | 6,8 | 2,6 | 0,4 |
| $M$ | 8,4 | 4,2 | 1,3 |
| $H$ | 4,1 | 3,0 | 2,2 |
|  |  |  |  |

Figure 2.7: A $3 \times 3$ game

- For player $1, L$ is strictly dominated by $M$. But neither $M$ nor $H$ is strictly dominated.
- For player $2, M$ is strictly dominated by $L$. But neither $L$ nor $H$ is strictly dominated.
- For this game, rationality alone does not offer a unique prediction.


## Dominance

## Dominant strategies

- The following concept, loosely speaking, is the converse of strictly dominated strategies.


## Definition 2.3

$s_{i} \in S_{i}$ is a strictly dominant strategy for $i$ if every other strategy of $i$ is strictly dominated by it, that is, for all $s_{i}^{\prime} \in S_{i}, s_{i}^{\prime} \neq s_{i}$,

$$
v_{i}\left(s_{i}, s_{-i}\right)>v_{i}\left(s_{i}^{\prime}, s_{-i}\right), \forall s_{-i} \in S_{-i}
$$

- In the prisoner's dilemma, $C$ is a strictly dominant strategy for every player.
- In the game in Figure 2.7, no player has a strictly dominant strategy.


## Dominance

## Dominant strategies

- A simple observation: a rational player will (should) play his strictly dominant strategy if he has one.
- This observation provides us our first solution concept in this course.


## Definition 2.4

The strategy profile $s \in S$ is a strictly dominant strategy equilibrium if $s_{i} \in S_{i}$ is a strictly dominant strategy for all $i \in N$.

- $(C, C)$ is a strictly dominant strategy equilibrium for the prisoner's dilemma. In this equilibrium, every player chooses $C$. The equilibrium outcome is $(C, C)$ and the equilibrium payoff is $(-4,-4)$.


## Dominance

## Dominant strategies

- As we have seen, players may not have strictly dominant strategies.
- But if a player has a strictly dominant strategy, it must be unique.


## Lemma 2.1

If player $i$ has a strictly dominant strategy, it is unique.

- Yes?
- As a corollary, strictly dominant strategy equilibrium may not exist.
- But if it exists, it is unique.

Proposition 2.1
If the game $\Gamma=\left(N,\left\{S_{i}\right\}_{i=1}^{n},\left\{v_{i}\right\}_{i=1}^{n}\right)$ has a strictly dominant strategy equilibrium $s$, then $s$ is the unique dominant strategy equilibrium.

- Yes?


## Dominance

## Dominant strategies

- Is the equilibrium outcome of a strictly dominant strategy equilibrium always desirable?


## Definition 2.5

A strategy profile $s \in S$ Pareto dominates strategy profile $s^{\prime} \in S$ if $v_{i}(s) \geq v_{i}\left(s^{\prime}\right)$ for all $i \in N$ and $v_{i}(s)>v_{i}\left(s^{\prime}\right)$ for at least one $i \in N$ (in which case, we will also say that $s^{\prime}$ is Pareto dominated by $s$ ). A strategy profile is Pareto optimal if it is not Pareto dominated by any other strategy profile.

- A strategy profile is Pareto dominated if there is another strategy profile that makes every player at least as good as before and some player strictly better.
- Pareto optimal is sometimes called Pareto efficient.


## Dominance

## Dominant strategies

- In the prisoner's dilemma, $(C, C)$ is the unique strictly dominant strategy equilibrium.
- It is not Pareto optimal: $(D, D)$ Pareto dominates $(C, C)$.
- Compare with competitive market equilibrium outcome.


## Iterated elimination of strictly dominated strategies

An example

Player 2

|  | L | C | R |
| :---: | :---: | :---: | :---: |
| Player 1 | 4, 3 | 5,1 | 6,2 |
|  | 2,1 | 8,4 | 3, 6 |
|  | 3,0 | 9,6 | 2,8 |

Figure 2.8: An example for IESDS

- Neither player 1 nor player 2 has strictly dominant strategy.
- Player 1 has no strictly dominated strategy.
- $C$ for player 2 is strictly dominated by $R$.
- As we have noted earlier, rationality of player 2 predicts that player 2 will never play $C$.


## Iterated elimination of strictly dominated strategies

## An example

- Suppose player 1 knows that player 2 is rational.
- Then player 1 will predict that player 2 will never play $C$.
- Thus, when considering his own strategy, player 1 can effectively ignore the possibility of player 2 choosing $C$.
- In other words, player 1 essentially views the game as follows:

|  | $L$ |  |
| :---: | :---: | :---: |
| $U$ | $R$ |  |
| $M$ | 4,3 | 6,2 |
| $D$ | 2,1 | 3,6 |
|  | 3,0 | 2,8 |
|  |  |  |

- Observe that both $M$ and $D$ are strictly dominated by $U$ for player 1 in this reduced game.
- Hence, rationality of player 1 predicts that he will never play $M$ and $D$.


## Iterated elimination of strictly dominated strategies

## An example

- Let's go even further.
- Suppose player 2 knows that
- player 1 is rational; and
- player 1 knows that player 2 is rational.
- Then player 2 will predict that player 1 will never play $M$ and $D$.
- This implies that player 2 essentially view the game as follows

\$\$

\$\$
- Observe that $R$ is strictly dominated by $L$ for player 2 in this further reduced game.
- Hence, rationality of player 2 then predicts that he will never play $R$.

## Iterated elimination of strictly dominated strategies

An example

- Thus, we obtain the unique prediction of this game: $(U, L)$.
- Notice that rationality of both players alone does not lead to this prediction.
- We need additional assumptions on the two players' knowledge about rationality:
- both players are rational;
- both players know that their opponents are rational;
- player 2 knows that player 1 knows that player 2 is rational.


## Iterated elimination of strictly dominated strategies

Common knowledge

## Definition 2.6

An event $E$ is common knowledge if (1) everyone knows $E$, (2) everyone knows that everyone knows $E$, and so on ad infinitum.

- Under the assumption of common knowledge of rationality, our previous arguments work.


## Iterated elimination of strictly dominated strategies

## Common knowledge

- To get more sense of common knowledge, consider the following situation.
- A boyfriend and a girlfriend want to date on Valentine's day night.
- Unfortunately, there is a chance that the boyfriend has to work overtime, in which case they can not date.
- If the boyfriend does not need to work overtime, he will send a message to his girlfriend so that they can go out and date.
- But there is possibility that the message will be lost due to some technology problems.
- Thus, they reached the agreement that once the girlfriend receives the message, she sends back a confirmation.
- But there is also possibility that the girlfriend's message is lost.


## Iterated elimination of strictly dominated strategies

Common knowledge

- So, if the boyfriend receives the confirmation, he will send a re-confirmation.
- And it is possible that this re-confirmation is lost.
- So, if the girlfriend receives this re-confirmation, she will send a re-re-confirmation.
- ......
- Unfortunate couple: no matter how many messages they have sent and received, it is never common knowledge that they can date!


## Iterated elimination of strictly dominated strategies

IESDS

- The process of iterated elimination of strictly dominated strategies can be described inductively as follows.
- Let $S_{i}^{0}=S_{i}$.
- Suppose we have defined $\left\{S_{i}^{k}\right\}_{i=1}^{n}$. If there are players who have strictly dominated strategies in the reduced game ( $N,\left\{S_{i}^{k}\right\}_{i=1}^{n},\left\{v_{i}^{k}\right\}_{i=1}^{n}$ ), delete all of them to get $\left\{S_{i}^{k+1}\right\}_{i=1}^{n}$. If there is no strictly dominated strategy in $\left(N,\left\{S_{i}^{k}\right\}_{i=1}^{n},\left\{v_{i}^{k}\right\}_{i=1}^{n}\right)$, then stop.
- Then any strategy $s_{i} \in \cap_{k \geq 0} S_{i}^{k}=S_{i}^{*}$ is said to survive the process of iterated elimination of strictly dominated strategies.
- Any strategy profile $s \in S_{1}^{*} \times \cdots \times S_{n}^{*}$ is called an iterated-elimination equilibrium.


## Iterated elimination of strictly dominated strategies

IESDS

- For finite games, the above process must stop in finite steps. In fact, the resulting set of strategies that survive IESDS does not depend on the order of deletion. The only requirement is that some (not necessarily all) strictly dominated strategies be deleted in each round.
- For infinite games, the process may never end. Moreover, if in each round, only some strictly dominated strategies are deleted, then the result will rely on the choice of these strategies in each round. In other words, the result will depend on the order of deletion. For this reason, we always require that all strictly dominated strategies be deleted in each round.


## Iterated elimination of strictly dominated strategies

IESDS

|  | $a$ | $b$ | $c$ | $d$ |
| :---: | :---: | :---: | :---: | :---: |
| $w$ | 6,4 | 4,4 | 4,5 | 12,2 |
| $x$ | 5,9 | 8,7 | 5,8 | 10,6 |
| $y$ | 2,10 | 7,6 | 4,6 | 9,5 |
| $z$ | 4,4 | 5,9 | 4,10 | 10,9 |
|  |  |  |  |  |

- Deleting all strictly dominated strategies in each round:
- 1st round: $y$ for player 1 and $d$ for player 2;
- 2nd round: $z$ for player 1 and $b$ for player 2;
- $S_{1}^{*}=\{w, x\}$ and $S_{2}^{*}=\{a, c\}$.
- Another order of deletion:
- 1st round: $y$ for player 1;
- 2nd round: $b$ and $d$ for player 2;
- 3rd round: $z$ for player 1 ;
- $S_{1}^{*}=\{w, x\}$ and $S_{2}^{*}=\{a, c\}$.


## Iterated elimination of strictly dominated strategies

IESDS

- Note that there might be more than one strategies that survive IESDS.
- Hence IESDS may not provide a unique prediction about the outcome.
- But


## Proposition 2.2

If for a game $\Gamma=\left(N,\left\{S_{i}\right\}_{i=1}^{n},\left\{v_{i}\right\}_{i=1}^{n}\right)$, $s$ is a strict dominant strategy equilibrium, then $s_{i}$ uniquely survives IESDS for every player $i$.

- Reason: for every $s_{i}^{\prime} \neq s_{i}, s_{i}^{\prime}$ is strictly dominated by $s_{i}$. Hence in the first round, all strategies other than $s_{i}$ is deleted for player $i$. The process ends just in one round.


# Iterated elimination of strictly dominated strategies 

Example: Cournot Duopoly

- Consider Cournot duopoly with constant marginal cost.
- Demand curve $P(Q)=\max \{100-Q, 0\}$.
- Payoff function

$$
\begin{aligned}
v_{i}\left(q_{i}, q_{j}\right) & =\max \left\{100-\left(q_{i}+q_{j}\right), 0\right\} q_{i}-10 q_{i} \\
& =\max \left\{\left(90-q_{i}-q_{j}\right) q_{i},-10 q_{i}\right\}
\end{aligned}
$$

- Initial round $S_{1}^{0}=S_{2}^{0}=\mathbb{R}_{+}$.


## Iterated elimination of strictly dominated strategies

## Example: Cournot Duopoly

- Focus on firm 1.
- If $q_{2} \geq 90$, then any positive $q_{1}$ yields negative profit for firm 1 . Thus, $q_{1}=0$ is the profit maximizing quantity for firm 1 because it guarantees zero profit.
- If $q_{2}<90$, then firm 1 can earn positive profit. In fact, the profit maximizing quantity solves

$$
\max _{q_{1} \geq 0}\left(90-q_{1}-q_{2}\right) q_{1}
$$

- The first order condition yields

$$
q_{1}=\frac{90-q_{2}}{2}
$$

- In sum, the profit maximizing quantity for firm 1 as a function of firm 2's output is

$$
q_{1}=\max \left\{\frac{90-q_{2}}{2}, 0\right\}
$$

## Iterated elimination of strictly dominated strategies

## Example: Cournot Duopoly

- Observe that, as $q_{2}$ changes over $\mathbb{R}_{+}$, firm 1's profit maximizing quantity changes over $[0,45]$.
- We thus claim that any quantity $q_{1} \in[0,45]$ for firm 1 is not strictly dominated: there exists $q_{2}=90-2 q_{1} \in S_{2}^{0}$ such that

$$
v_{1}\left(q_{1}, q_{2}\right) \geq v_{1}\left(q_{1}^{\prime}, q_{2}\right), \forall q_{1}^{\prime} \in S_{1}^{0}
$$

- Therefore, in the first round, quantities in $[0,45]$ should not be deleted.


## Iterated elimination of strictly dominated strategies

## Example: Cournot Duopoly

- How about quantities above 45 ?
- We claim that any $q_{1}>45$ is strictly dominated by $q_{1}^{\prime}=45$.
- To see this, we only need to observe that for any $q_{2} \in S_{2}^{0}$, the mapping

$$
q_{1} \mapsto \max \left\{\left(90-q_{1}-q_{2}\right) q_{1},-10 q_{1}\right\}
$$

is strictly decreasing over the interval $[45,+\infty)$.

- This implies that for all $q_{1}>45$,

$$
v_{1}\left(45, q_{2}\right)>v_{1}\left(q_{1}, q_{2}\right), \forall q_{2} \in S_{2}^{0}
$$

meaning that $q_{1}$ is strictly dominated by 45 .

- Therefore, quantities in $(45, \infty)$ should be deleted in the first round.
$\rightarrow$ We obtain $S_{1}^{1}=[0,45]$.
- By symmetry, we have $S_{2}^{1}=[0,45]$, completing the first round deletion.


## Iterated elimination of strictly dominated strategies

## Example: Cournot Duopoly

- We now move the second round.
- Because $S_{1}^{1}=S_{2}^{1}=[0,45]$, we can write

$$
v_{i}\left(q_{i}, q_{j}\right)=\left(90-q_{i}-q_{j}\right) q_{i}
$$

- Focus on firm 1 again.
- For any $q_{2} \in S_{2}^{1}$, the profit maximizing quantity for firm 1 in $S_{1}^{1}$ is simply

$$
q_{1}=\frac{90-q_{2}}{2}
$$

- As $q_{2}$ changes in $S_{2}^{1}$, this profit maximizing quantity changes over $[22.5,45]$.
- Then, we know that any quantity in [22.5,45] is not strictly dominated for firm 1 in the second round and should be kept.


## Iterated elimination of strictly dominated strategies

## Example: Cournot Duopoly

- How about quantities below 22.5?
- We claim that any $q_{1}<22.5$ is strictly dominated by $q_{1}^{\prime}=22.5$.
- To see this, simply observe that for any $q_{2} \in S_{2}^{1}$, the mapping

$$
q_{1} \mapsto\left(90-q_{1}-q_{2}\right) q_{1}
$$

is strictly increasing over [0, 22.5].

- This implies for all $q_{1} \in[0,22.5)$,

$$
v\left(22.5, q_{2}\right)>v_{1}\left(q_{1}, q_{2}\right), \forall q_{2} \in S_{2}^{1}
$$

meaning that $q_{1}$ is strictly dominated by 22.5 .

- Therefore, quantities in $[0,22.5)$ should be deleted.
- We obtain $S_{1}^{2}=[22.5,45]$.
- By symmetry, we have $S_{2}^{2}=[22.5,45]$, completing the second round deletion.


## Iterated elimination of strictly dominated strategies

## Example: Cournot Duopoly

- Given $S_{1}^{2}=S_{2}^{2}=[22.5,45]$ and applying a similar argument as above, we can show that $S_{1}^{3}=S_{2}^{3}=[22.5,33.75]$, where 33.75 comes from $(90-22.5) / 2$.
Let $S_{1}^{k}=S_{2}^{k}=\left[\underline{q}^{k}, \bar{q}^{k}\right]$ for $k \geq 1$.
- We can show

$$
\underline{q}^{k}=\phi^{(k-1)}(0) \text { and } \bar{q}^{k}=\phi^{(k)}(0) \text { if } k \text { is odd, }
$$

and

$$
\underline{q}^{k}=\phi^{(k)}(0) \text { and } \bar{q}^{k}=\phi^{(k-1)}(0) \text { if } k \text { is even, }
$$

where $\phi(q)=(90-q) / 2$ and $\phi^{(k)}$ is the $k$ th composition of $\phi$ itself.

- Because $\lim _{k \rightarrow \infty} \phi^{(k)}(0)=30$, we know

$$
S_{i}^{*}=\bigcap_{k \geq 1} S_{i}^{k}=\{30\}
$$

- Therefore, $q=30$ is the unique quantity that survives IESDS for both firms. This is exactly the Cournot equilibrium outcome.


## Iterated elimination of strictly dominated strategies

Example: Cournot Duopoly

![](https://cdn.mathpix.com/cropped/2024_09_09_605858d45802b61328b8g-056.jpg?height=691&width=742&top_left_y=156&top_left_x=253)

Figure 2.9: IESDS in the Cournot game

## Best Response

- Both strictly dominant strategy equilibrium and IESDS are based on eliminating strategies that players would never play.
- An alternative approach is to ask what possible strategies might players choose to play and under what conditions?
- When we consider eliminating strategies that no rational player would play, it was by finding some strategy that is always better.
- A strategy that cannot be eliminated suggests that under some conditions this strategy is the one that the player may choose.
- When we qualify a strategy to be the best under some conditions, these conditions must be expressed in terms that are rigorous and are related to the game that is being played.


## Best Response

## The best response

![](https://cdn.mathpix.com/cropped/2024_09_09_605858d45802b61328b8g-058.jpg?height=152&width=248&top_left_y=286&top_left_x=509)

Figure 2.10: Battle of the sexes

- No one has strictly dominated strategies.
- If player 2 chooses $O, O$ is the best for player 1 .
- If, instead, player 2 chooses $F, F$ is the best for player 1 .


## Best Response

## The best response

## Definition 2.7

The strategy $s_{i} \in S_{i}$ is player $i$ 's best response to his opponents' strategies $s_{-i} \in S_{-i}$ if

$$
v_{i}\left(s_{i}, s_{-i}\right) \geq v_{i}\left(s_{i}^{\prime}, s_{-i}\right), \forall s_{i}^{\prime} \in S_{i}
$$

- This is the most central concept of game theory!
- Sometimes, it is also called a best reply.
- In the battle of the sexes:
- $O$ for player $i$ is a best response to his opponent's strategy $O$;
- $F$ for player $i$ is a best response to his opponent's strategy $F$.


## Best Response

## The best response

- Best responses may not be unique for a given opponents' strategies $s_{i} \in S_{-i}$.

|  | $L$ | $C$ | $R$ |
| :---: | :---: | :---: | :---: |
| $U$ | 3,3 | 5,1 | 6,2 |
| $M$ | 4,1 | 8,4 | 3,6 |
| $D$ | 4,0 | 9,6 | 6,8 |
|  |  |  |  |

Figure 2.11: A $3 \times 3$ game

- Both $M$ and $D$ are player 1's best responses to player 2's strategy $L$.
- $D$ is player 1's unique best response to player 2's strategy $C$.
- Both $U$ and $D$ are player 1's best responses to player 2's strategy $R$.


## Best Response

The best response

- An observation: a rational player who believes that his opponents are playing some $s_{-i} \in S_{-i}$ will always choose a best response to $s_{-i}$.


## Proposition 2.3

If $s_{i}$ is a strictly dominated strategy for player $i$, then it cannot be a best response to any $s_{-i} \in S_{-i}$.

## Proof of Proposition 2.3.

Suppose $s_{i}$ is strictly dominated by $s_{i}^{\prime}$. Then for any $s_{-i} \in S_{-i}$, we have

$$
v_{i}\left(s_{i}^{\prime}, s_{-i}\right)>v_{i}\left(s_{i}, s_{-i}\right)
$$

implying that $s_{i}$ is not a best response to $s_{-i}$.

- Contrapositive: if $s_{i}$ is a best response to some $s_{-i} \in S_{-i}$, then it is not strictly dominated.


## Best Response

## The best response

## Proposition 2.4

If $s_{i}$ is a strictly dominant strategy for player $i$, then it is the unique best response to any $s_{-i} \in S_{-i}$.

- This directly comes from the definition of strict dominance and best response.


## Best Response

The best response

## Proposition 2.5

In a finite normal-form game, if $s^{*}$ uniquely survives IESDS, then $s_{i}^{*}$ is the unique best response to $s_{-i}^{*}$ for all $i \in N$.

## Proof of Proposition 2.5.

Consider any player $i$. Suppose, by contradiction, that $s_{i}^{*}$ is not a best response to $s_{-i}^{*}$. Then there exists $s_{i}^{1} \in S_{i}$ such that
$v_{i}\left(s_{i}^{1}, s_{-i}^{*}\right)>v_{i}\left(s_{i}^{*}, s_{-i}^{*}\right)$. Because $s_{i}^{1}$ is deleted in some round of IESDS and because $s_{-i}^{*}$ survives the process, there must be $s_{i}^{2} \in S_{i}$ such that $v_{i}\left(s_{i}^{2}, s_{-i}^{*}\right)>v_{i}\left(s_{i}^{1}, s_{-i}^{*}\right)$. But because $s_{i}^{2}$ is deleted, we can find $s_{i}^{3}$ such that $v_{i}\left(s_{i}^{3}, s_{-i}^{*}\right)>v_{i}\left(s_{i}^{2}, s_{-i}^{*}\right)$. This argument continues and we can find infinitely many such strategies. This contradicts the finite game assumption.

## Best Response

## The best response

## Proof of Proposition 2.5 (Cont.)

If there is a strategy $s_{i}$ which is also a best response to $s_{-i}^{*}$, then by Proposition 2.3, $s_{i}$ is not strictly dominated in every round of the process because $s_{-i}^{*}$ survives. This proves that $s_{i}^{*}$ is the unique best response to $s_{-i}^{*}$.

- The assumption that the game is finite is indispensable. There will be a counter example in your problem set for infinite game.


## Best Response

## Best response correspondences

- When we think of player $i$ 's best responses as a function of his opponents' strategies, we obtain player $i$ 's best response correspondence.
- Think about a mapping $f: X \rightarrow Y$ that maps every element $x \in X$ into an element $f(x) \in Y$. We call this mapping a function.
- Think about a mapping $f: X \rightarrow 2^{Y}$ where $2^{Y}$ is the set of all subsets of $Y$. That is, $f$ maps every element $x \in X$ into a subset $f(x) \subseteq Y$. Of course, we can all $f$ a function from $X$ to $2^{Y}$. But more conveniently, we call $f$ a correspondence from $X$ to $Y$, and usually write $f: X \Rightarrow Y$. In words, a correspondence is just a set-valued function.
- If $f: X \Rightarrow Y$ is a correspondence and for every $x \in X, f(x)$ only contains one element, then $f$ is essentially a function: it maps every element $x \in X$ into an element in $Y$. For example, $f: X \Rightarrow X$ with $f(x)=\{x\}$. In this case, we write $f(x)=x$ for simplicity.


## Best Response

## Best response correspondences

- Player $i$ 's best response correspondence is a correspondence $B R_{i}: S_{-i} \Rightarrow S_{i}$ such that

$$
B R_{i}\left(s_{-i}\right)=\left\{s_{i} \in S_{i} \mid s_{i} \text { is a best response to } s_{-i}\right\}
$$

- Therefore, if player $i$ believes that his opponents are playing $s_{-i}$, he should play a strategy in $B R_{-i}\left(s_{i}\right)$.


## Best Response

## Best response correspondences

- In the game in Figure 2.11, we have

$$
B R_{1}\left(s_{2}\right)= \begin{cases}\{M, D\}, & \text { if } s_{2}=L \\ \{D\}, & \text { if } s_{2}=C \\ \{U, D\} & \text { if } s_{2}=R\end{cases}
$$

and

$$
B R_{2}\left(s_{1}\right)= \begin{cases}L, & \text { if } s_{1}=U \\ R, & \text { if } s_{1}=M \\ R, & \text { if } s_{1}=D\end{cases}
$$

- Note that we directly write $B R_{2}$ as a function because it is always single-valued.


## Best Response

## Best response correspondences

- Recall the Cournot duopoly with constant marginal cost:

$$
v_{i}\left(q_{i}, q_{j}\right)=\max \left\{100-q_{i}-q_{j}, 0\right\} q_{i}-10 q_{i}
$$

- In fact, we have already figured out

$$
B R_{1}\left(q_{2}\right)=\max \left\{\frac{90-q_{2}}{2}, 0\right\}
$$

and by symmetry

$$
B R_{2}\left(q_{1}\right)=\max \left\{\frac{90-q_{1}}{2}, 0\right\}
$$

## Best Response

## Best response correspondences

- Recall the Bertrand competition: $N=\{1,2\}, S_{1}=S_{2}=\mathbb{R}_{+}$, and

$$
v_{i}\left(p_{i}, p_{j}\right)= \begin{cases}p_{i}-c_{i}, & \text { if } p_{i}<p_{j} \\ \frac{1}{2}\left(p_{i}-c_{i}\right), & \text { if } p_{i}=p_{j} \\ 0, & \text { if } p_{i}>p_{j}\end{cases}
$$

- Then

$$
B R_{i}\left(p_{j}\right)= \begin{cases}\left(p_{j},+\infty\right), & \text { if } p_{j}<c_{i} \\ {\left[p_{j},+\infty\right),} & \text { if } p_{j}=c_{i} \\ \emptyset, & \text { if } p_{j}>c_{i}\end{cases}
$$

- Make sure you understand (1) why some interval is open while some is closed; (2) why there is $\emptyset$.


## Nash Equilibrium

## Definition

![](https://cdn.mathpix.com/cropped/2024_09_09_605858d45802b61328b8g-070.jpg?height=156&width=258&top_left_y=282&top_left_x=501)

Figure 2.12: Battle of the sexes

- There is no strictly dominant strategy equilibrium.
- IESDS yields "anything is possible": $S_{1}^{*}=S_{2}^{*}=\{O, F\}$.
- John Nash provided us an answer to this situation.


## Nash Equilibrium

Definition

## Definition 2.8

The strategy profile $s^{*}=\left(s_{1}^{*}, \ldots, s_{n}^{*}\right) \in S$ is a Nash equilibrium if for every $i \in N, s_{i}^{*}$ is a best response to $s_{-i}^{*}$. That is, for every $i \in N$,

$$
v_{i}\left(s_{i}^{*}, s_{-i}^{*}\right) \geq v_{i}\left(s_{i}, s_{-i}^{*}\right), \forall s_{i} \in S_{i} .
$$

- Mutual best response: every player is playing a best response given their opponents' strategies.
- In terms of the best response correspondence: $s_{i}^{*} \in B R_{i}\left(s_{-i}^{*}\right)$ for all $i$.


## Definition 2.9

Given a strategy profile $s=\left(s_{1}, \ldots, s_{n}\right) \in S$, we say player $i$ has a profitable deviation if there exists $s_{i}^{\prime}$ such that

$$
v_{i}\left(s_{i}^{\prime}, s_{-i}\right)>v_{i}\left(s_{i}, s_{-i}\right)
$$

- Nash equilibrium $\Longleftrightarrow$ no one has a profitable deviation.


## Nash Equilibrium

## Definition

John F. Nash Jr.

![](https://cdn.mathpix.com/cropped/2024_09_09_605858d45802b61328b8g-072.jpg?height=459&width=309&top_left_y=262&top_left_x=77)

The Sveriges Riksbank Prize in Economic Sciences in Memory of Alfred Nobel 1994
"for their pioneering analysis of equilibria in the theroy of non-cooperative games"

Contribution: Introduced the distinction between cooperative games, in which binding agreements can be made, and non-cooperative games, where binding agreements are not feasible. Developed an equilibrium concept for non-cooperative games that now is called Nash equilibrium.

- The movie, A Beautiful Mind, is based the true story of John Nash.


## Nash Equilibrium

## Definition

\$\$

\$\$
- $(O, O)$ is a Nash equilibrium.
- $(O, F)$ is not a Nash equilibrium.
- $(F, O)$ is not a Nash equilibrium.
- $(F, F)$ is a Nash equilibrium.
- Notice that Nash equilibrium may not be unique. The definition of Nash equilibrium is silent about which equilibrium will/should be played.

## Nash Equilibrium

## Definition

- Nash equilibrium is about players' strategies (what they will do), not about the payoffs!

|  | $O$ | $F$ |
| :---: | :---: | :---: |
| $O$ | 2,1 | 0,0 |
| $F$ | 2,1 | 1,2 |
|  |  |  |

- Nash equilibria: $(O, O)$ and $(F, F)$.
- Note that $(O, O)$ and $(F, O)$ yield the same payoffs to the players. However, $(F, O)$ is not a Nash equilibrium since player 2 wants to deviate to $F$.


## Nash Equilibrium

## Definition

|  | $L$ | $C$ | $R$ |
| ---: | :---: | :---: | :---: |
| $U$ | 7,7 | 4,2 | 1,8 |
| $M$ | 2,4 | 5,5 | 2,3 |
| $D$ | 8,1 | 3,2 | 0,0 |
|  |  |  |  |

- Is there a Nash equilibrium in which player 1 plays $U$ ?
- If yes, player 2 must play a best response to $U$. In this case, it is $R$.
- But if player 2 plays $R, U$ for player 1 is not a best response.
- Thus, the answer is no.
- Is there a Nash equilibrium in which player 1 plays $M$ ?
- If yes, player 2 must play a best response to $M$. In this case, it is $C$.
- Given player 2 plays $C, M$ for player 1 is a best response.
- Thus, $(M, C)$ is a Nash equilibrium.
- Is there a Nash equilibrium in which player 1 plays $D$ ?
- If yes, player 2 must play a best response to $D$. In this case, it is $C$.
- But if player 2 plays $C, D$ for player 1 is not a best response.
- Thus, the answer is no.


## Nash Equilibrium

## Definition

- Nash equilibrium is based on the following two principles:
- Rationality: each player is playing a best response to his belief about the opponents' strategies.
- Consistency: Players' beliefs about their opponents are correct. player 1 believes that player 2 is playing $\hat{s}_{2}$

![](https://cdn.mathpix.com/cropped/2024_09_09_605858d45802b61328b8g-076.jpg?height=146&width=854&top_left_y=486&top_left_x=277)

- An informal expression for consistency is that players know their opponents' strategies in equilibrium.


# Nash Equilibrium 

Definition

- The following proposition is a direct corollary of Propositions 2.4.


## Proposition 2.6

If the strategy profile $s^{*}=\left(s_{1}^{*}, \ldots, s_{n}^{*}\right)$ is a strict dominant strategy equilibrium, then it is the unique Nash equilibrium.

## Nash Equilibrium

## Definition

- We have a similar result for the unique survivor of IESDS.


## Proposition 2.7

If the game is finite, and the strategy profile $s^{*}=\left(s_{1}^{*}, \ldots, s_{n}^{*}\right)$ is the unique survivor of IESDS, then it is the unique Nash equilibrium.

- The result that $s^{*}$ is a Nash equilibrium is a direct corollary of Proposition 2.5.
- The uniqueness comes from the next proposition, which is a converse of Proposition 2.7.
- Note the fact that $s_{i}^{*}$ is the unique best response to $s_{-i}^{*}$ as claimed by Proposition 2.5 does not imply that $s^{*}$ is the unique Nash equilibrium. (Yes?)


## Nash Equilibrium <br> Definition

## Proposition 2.8

If $s^{*}$ is a Nash equilibrium, it survives IESDS.

- It is a direct corollary of Proposition 2.3. (Yes?)


## Applications

Two kinds of societies

| $S$ | $H$ |  |
| :---: | :---: | :---: |
| $S$ | 5,5 | 0,3 |
| $H$ | 3,0 | 3,3 |
|  |  |  |

- Two hunters can each choose to hunt a stag $(S)$ or hunt a hare $(H)$.
- Hunting stags is challenging and requires mutual cooperation.
- If either hunts a stag alone, the change of success is negligible.
- Hunting hares is an individualistic enterprise that is not done in pairs.
- A stag provides a rather large and tasty meal, while a hare is much less filling.


## Applications

## Two kinds of societies

- Two Nash equilibria: $(S, S)$ and $(H, H)$.
- $(S, S)$ Pareto dominates $(H, H)$.
- Why can $(H, H)$ happen? Self-fulfilling: if everybody anticipates that the other will not join forces, then it is better for himself to hunt a hare.
- Different societies that may look very similar in their endowments, access to technology, and physical environments have very different achievements, all because of self-fulfilling beliefs or, as they are often called, norms of behavior.


## Applications

Two kinds of societies

|  | $L$ | $R$ |
| :---: | :---: | :---: |
| $L$ | 1,1 | 0,0 |
| $L$ | 0,0 | 1,1 |
|  |  |  |

- Two Nash equilibria: $(L, L)$ and $(R, R)$.
- Social norm: some countries drive on the right while others drive on the left.


## Applications

## Cournot duopoly

- Inverse demand curve $P(Q)=\max \{a-b Q, 0\}$.
- Constant marginal cost $c_{i}\left(q_{i}\right)=c_{i} q_{i}$, where $c_{i}<a$.
- Payoff function

$$
\begin{aligned}
v_{i}\left(q_{i}, q_{j}\right) & =\max \left\{a-b\left(q_{i}+q_{j}\right), 0\right\} q_{i}-c_{i} q_{i} \\
& =\max \left\{\left(a-b q_{i}-b q_{j}-c_{i}\right) q_{i},-c_{i} q_{i}\right\}
\end{aligned}
$$

- If $q_{j}<\frac{a-c_{i}}{b}$, the unique best response for firm $i$ is

$$
B R_{i}\left(q_{j}\right)=\frac{a-b q_{j}-c_{i}}{2 b}
$$

- If $q_{j} \geq \frac{a-c_{i}}{b}$, the unique best response for firm 1 is

$$
B R_{i}\left(q_{j}\right)=0
$$

$\rightarrow$ In sum,

$$
B R_{i}\left(q_{j}\right)=\max \left\{\frac{a-b q_{j}-c_{i}}{2 b}, 0\right\}
$$

## Applications

## Cournot duopoly

- Therefore, a strategy profile $\left(q_{1}^{*}, q_{2}^{*}\right)$ is a Nash equilibrium if and only if they solve the following system of equations

$$
\begin{aligned}
& q_{1}^{*}=\max \left\{\frac{a-b q_{2}^{*}-c_{1}}{2 b}, 0\right\} \\
& q_{2}^{*}=\max \left\{\frac{a-b q_{1}^{*}-c_{2}}{2 b}, 0\right\}
\end{aligned}
$$

## Applications

Cournot duopoly

![](https://cdn.mathpix.com/cropped/2024_09_09_605858d45802b61328b8g-085.jpg?height=638&width=778&top_left_y=160&top_left_x=241)

Figure 2.13: The unique Nash equilibrium in Cournot duopoly

## Applications

## Cournot duopoly

- $s^{*}$ is a Nash equilibrium if $s_{i}^{*} \in B R_{i}\left(s_{-i}^{*}\right)$ for all $i$.
- For a two-player game, we require $s_{1}^{*} \in B R_{1}\left(s_{2}^{*}\right)$ and $s_{2}^{*} \in B R_{2}\left(s_{1}^{*}\right)$.
$\rightarrow$ Let

$$
G_{1}=\left\{\left(s_{1}, s_{2}\right) \mid s_{1} \in B R_{1}\left(s_{2}\right)\right\} \subseteq S_{1} \times S_{2}
$$

be the graph of player 1's best response correspondence. Notice that if $B R_{1}$ is always single value, $G_{1}$ is simply the graph of function $B R_{1}$.

- Similarly, let

$$
G_{2}=\left\{\left(s_{1}, s_{2}\right) \mid s_{2} \in B R_{2}\left(s_{1}\right)\right\} \subseteq S_{1} \times S_{2}
$$

be the graph of player 2's best response correspondence.

- Then $\left(s_{1}^{*}, s_{2}^{*}\right)$ is a Nash equilibrium if and only if

$$
\left(s_{1}^{*}, s_{2}^{*}\right) \in G_{1} \cap G_{2}
$$

- Thus, if we draw $G_{1}$ and $G_{2}$ in the $S_{1} \times S_{2}$ plane, their intersections give us all Nash equilibria.


## Applications

Cournot duopoly

- If $a-2 c_{1}+c_{2}>0$ and $a-2 c_{2}+c_{1}>0$ :

![](https://cdn.mathpix.com/cropped/2024_09_09_605858d45802b61328b8g-087.jpg?height=618&width=676&top_left_y=215&top_left_x=281)

Figure 2.14: Cournot: best response functions and Nash equilibrium

## Applications

## Cournot duopoly

- Notice that if $c_{1}=c_{2}=c$, then the unique Nash equilibrium is

$$
q_{1}^{*}=q_{2}^{*}=\frac{a-c}{3 b}
$$

- When $a=100, b=1$ and $c=10$, we have $q_{1}^{*}=q_{2}^{*}=30$. As we have seen, this is the unique strategy profile that survives IESDS.


## Applications

## Cournot duopoly

- If $a-2 c_{1}+c_{2}<0$ and $a-2 c_{2}+c_{1}>0$ : (the third case is symmetric)

![](https://cdn.mathpix.com/cropped/2024_09_09_605858d45802b61328b8g-089.jpg?height=618&width=684&top_left_y=218&top_left_x=282)

Figure 2.15: Cournot: best response functions and Nash equilibrium

## Applications

## Bertrand competition

- Price competition.
- Demand curve $Q(p)=\max \{a-p, 0\}$.
- Identical constant marginal cost $c$ with $a>c$.
- Consumers buy from the firm with lower price.
- If there is a tie in price, the two firms equally split the market.
- Therefore,

$$
v_{i}\left(p_{i}, p_{j}\right)= \begin{cases}Q\left(p_{i}\right)\left(p_{i}-c\right), & \text { if } p_{i}<p_{j} \\ \frac{1}{2} Q\left(p_{i}\right)\left(p_{i}-c\right), & \text { if } p_{i}=p_{j} \\ 0, & \text { if } p_{i}>p_{j}\end{cases}
$$

- Monopoly pricing: if there were only one firm,

$$
\max _{p \geq 0} Q(p)(p-c) \Longrightarrow p^{m}=\frac{a+c}{2}
$$

## Applications

## Bertrand competition

- Nash equilibrium $\left(p_{1}^{*}, p_{2}^{*}\right)$ ?
- In any equilibrium, we must have $p_{i}^{*} \geq c$ for both firms; otherwise at least one firm is earning negative profit. This firm can make zero profit by deviating to $c$.
- There is no equilibrium in which one firm charges higher than $c$. To see this, $\left(p_{1}^{*}, p_{2}^{*}\right)$ is an equilibrium and $p_{1}^{*}>c$. If $p_{1}^{*}>p^{m}$, then we must have $p_{2}^{*}=p_{m}$. But then firm 1 can deviate to any $p \in\left(c, p^{m}\right)$ to earn positive profit. If $p_{1}^{*} \leq p^{m}$, then there is no best response for firm 2 .
- We are left with $p_{1}^{*}=p_{2}^{*}=c$. This is indeed a Nash equilibrium since no firm has an incentive to deviate.
- In sum, the only Nash equilibrium of Bertrand competition is $(c, c)$, i.e., marginal cost pricing (competitive outcome?).


## Applications

## Bertrand competition

- Best response correspondence:

$$
B R_{i}\left(p_{j}\right)= \begin{cases}\left(p_{j},+\infty\right), & \text { if } p_{j}<c \\ {\left[p_{j},+\infty\right),} & \text { if } p_{j}=c \\ \emptyset, & \text { if } c<p_{j} \leq p^{m} \\ \left\{p^{m}\right\}, & \text { if } p_{j}>p^{m}\end{cases}
$$

- Again, make sure you understand why some interval is open while some is closed. Make sure you understand why some inequality is strict and some is weak.


## Applications

## Bertrand competition

![](https://cdn.mathpix.com/cropped/2024_09_09_605858d45802b61328b8g-093.jpg?height=599&width=608&top_left_y=171&top_left_x=321)

Figure 2.16: Bertrand: best response correspondences and Nash equilibrium

## Applications

## Bertrand competition

- Consider the asymmetric case: marginal cost $c_{1}<c_{2}$.
- Notice that the best response correspondences have exactly the same form as before:

$$
B R_{i}\left(p_{j}\right)= \begin{cases}\left(p_{j},+\infty\right), & \text { if } p_{j}<c_{i} \\ {\left[p_{j},+\infty\right),} & \text { if } p_{j}=c_{i} \\ \emptyset, & \text { if } c_{i}<p_{j} \leq p_{i}^{m} \\ \left\{p_{i}^{m}\right\}, & \text { if } p_{j}>p_{i}^{m}\end{cases}
$$

where $p_{i}^{m}=\left(a+c_{i}\right) / 2$.

## Applications

## Bertrand competition

![](https://cdn.mathpix.com/cropped/2024_09_09_605858d45802b61328b8g-095.jpg?height=593&width=606&top_left_y=189&top_left_x=319)

Figure 2.17: Bertrand with asymmetric marginal cost

- There is no Nash equilibrium!


## Applications

## Political ideology and electoral competition

- There are 101 political group of citizens, each labeled by $-50,-49, \ldots, 0, \ldots, 49,50$.
- The group's label also represents this group's ideal policy.
- Each group consists of a continuum of citizens of mass 1.
- There are two political candidates, each caring only about being elected.
- Each candidate $i$ chooses his platform as a policy $a_{i} \in\{-50,-49, \ldots, 0, \ldots, 49,50\}$.
- Each citizen votes for the candidate whose platform is closest to his ideal policy.
- If citizens in a group are indifferent between two platforms, half of them vote for one politician and the other half vote for the other.


## Applications

Political ideology and electoral competition

- The outcome is determined by majority rule.
- The candidate with more votes wins.
- If they receive the same number of votes, we say there is a tie.
- Candidates prefer winning to a tie, and a tie to losing.
- This is a discrete version of the Hotelling model.


## Applications

## Political ideology and electoral competition

- There is a unique Nash equilibrium $(0,0)$. Why?
- First of all, $(0,0)$ is indeed a Nash equilibrium: given $a_{j}=0$, any $a_{i}^{\prime} \neq 0$ would lose while $a_{i}=0$ gets a tie.
- There is no Nash equilibrium in which one candidate, say 1 , chooses $a_{1} \neq 0$. If there is such equilibrium, then candidate 2 must win the election in equilibrium (yes?). This means candidate 1 loses in equilibrium. But by deviating to the same platform chosen by candidate 2, candidate 1 can obtain a tie.


## Applications

## Political ideology and electoral competition

- Media voter theorem: if voters are different from one another along a single-dimensional "preference" line, as in Hotelling model, and if each prefers his own political location, with other platforms being less and less attractive the farther away they fall to either side of that location, then the political platform located at the median voter will defeat any other platform in a simple majority vote.


## Mixed Strategies and Expected Payoffs

Motivating examples

| $H$ | $T$ |  |
| :---: | :---: | :---: |
| $H$ | $1,-1$ | $-1,1$ |
| $T$ | $-1,1$ | $1,-1$ |
|  |  |  |

Figure 2.18: The matching pennies

- Players 1 and 2 each put a penny on a table simultaneously.
- If the two pennies come up the same side (heads or tails) then player 1 gets both; otherwise player 2 does.
- Easy to see: no Nash equilibrium.
- Zero-sum game.


## Mixed Strategies and Expected Payoffs

Motivating examples

|  | $R$ | $P$ | $S$ |
| :---: | :---: | :---: | :---: |
| $R$ | 0,0 | $-1,1$ | $1,-1$ |
| $P$ | $1,-1$ | 0,0 | $-1,1$ |
| $S$ | $-1,1$ | $1,-1$ | 0,0 |
|  |  |  |  |

Figure 2.19: Rock-paper-scissors

- No Nash equilibrium either.
- Remedy: allow players to randomize between several of their strategies.


## Mixed Strategies and Expected Payoffs

Mixed strategies

## Definition 2.10

Let $S_{i}=\left\{s_{i 1}, s_{i 2}, \ldots, s_{i m}\right\}$ be player $i$ 's finite set of pure strategies. Define $\Delta S_{i}$ as the simplex of $S_{i}$, which is the set of all probability distributions over $S_{i}$. A mixed strategy for player $i$ is an element $\sigma_{i} \in \Delta S_{i}$, so that $\sigma_{i}=\left(\sigma_{i}\left(s_{i 1}\right), \sigma_{i}\left(s_{i 2}\right), \ldots, \sigma_{i}\left(s_{i m}\right)\right)$ is a probability distribution over $S_{i}$, where $\sigma_{i}\left(s_{i}\right)$ is the probability that player $i$ plays $s_{i}$.

- Equivalently, a mixed strategy is a mapping $\sigma_{i}: S_{i} \rightarrow[0,1]$ with the constraint $\sum_{s_{i} \in S_{i}} \sigma_{i}\left(s_{i}\right)=1$.
$\checkmark$ In the matching pennies,

$$
\Delta S_{i}=\left\{\left(\sigma_{i}(H), \sigma_{i}(T)\right) \mid \sigma_{i}(H) \geq 0, \sigma_{i}(T) \geq 0 \text { and } \sigma_{i}(H)+\sigma_{i}(T)=1\right\}
$$

- In the rock-paper-scissors,

$$
\Delta S_{i}=\left\{\begin{array}{l|l}
\left(\sigma_{i}(R), \sigma_{i}(P), \sigma_{i}(S)\right) \left\lvert\, \begin{array}{l}
\sigma_{i}(R) \geq 0, \sigma_{i}(P) \geq 0, \sigma_{i}(S) \geq 0 \\
\sigma_{i}(R)+\sigma_{i}(P)+\sigma_{i}(S)=1
\end{array}\right.
\end{array}\right\}
$$

## Mixed Strategies and Expected Payoffs

## Mixed strategies

- In this course, we only consider mixed strategies with finite strategy spaces.
- Note that even for finite strategy space with more than two strategies, there are infinitely many mixed strategies!
- We have called each $s_{i} \in S_{i}$ as player $i$ 's strategy. To distinguish it from mixed strategies, we call it a pure strategy.
- Observe that a pure strategy is simply a spacial case of a mixed strategy. It is a mixed strategy with a degenerate distribution.
- For instance, for $s_{i} \in S_{i}$, the mixed strategy $\sigma_{i}$ with

$$
\sigma_{i}\left(s_{i}^{\prime}\right)= \begin{cases}1, & \text { if } s_{i}^{\prime}=s_{i} \\ 0, & \text { if } s_{i}^{\prime} \neq s_{i}\end{cases}
$$

is simply the pure strategy $s_{i}$, since $\sigma_{i}$ plays $s_{i}$ for sure.

## Mixed Strategies and Expected Payoffs

Mixed strategies

## Definition 2.11

Given a mixed strategy $\sigma_{i}$ for player $i$, we will say that a pure strategy $s_{i} \in S_{i}$ is in the support of $\sigma_{i}$ if and only if it occurs with positive probability, that is, $\sigma_{i}\left(s_{i}\right)>0$.

- Those pure strategies that are not in the support will not be played.
- For example, the support of the degenerate mixed strategy $\sigma_{i}$ on the previous page contains only $s_{i}$.
- For another example, consider $\sigma_{i}(R)=\sigma_{i}(P)=0.5$ and $\sigma_{i}(S)=0$ in the rock-paper-scissors. Then both $R$ and $P$ are in the support while $S$ is not.
- We use the notation $\operatorname{supp} \sigma_{i}$ to denote the support of $\sigma_{i}$.


## Mixed Strategies and Expected Payoffs

## Expected payoffs

- Consider the matching pennies.
- Suppose player 1 plays the mixed strategy $\sigma_{1}$ with $\sigma_{1}(H)=p$ and $\sigma_{1}(T)=1-p$. We also write $p \circ H+(1-p) \circ T$ to denote this strategy.
- Suppose player 2 plays the mixed strategy $\sigma_{2}=q \circ H+(1-q) \circ T$.
- We always assume that players' mixtures are independent.
- What is the outcome of this strategy profile?

![](https://cdn.mathpix.com/cropped/2024_09_09_605858d45802b61328b8g-105.jpg?height=156&width=644&top_left_y=528&top_left_x=308)

Figure 2.20: The outcome is a distribution over the strategy profiles

- Outcome $H H$ will occur with probability $p q$. Outcome $H T$ will occur with probability $p(1-q)$, and so on.


## Mixed Strategies and Expected Payoffs

## Expected payoffs

- We assume that players are expected utility maximizers.
- Thus, they evaluate their mixed strategies by their expected payoffs.
- Therefore, in this example, player $i$ 's expected utility is

$$
\begin{aligned}
v_{i}\left(\sigma_{1}, \sigma_{2}\right)= & p q v_{i}(H, H)+p(1-q) v_{i}(H, T) \\
& +(1-p) q v_{i}(T, H)+(1-p)(1-q) v_{i}(T, T)
\end{aligned}
$$

## Mixed Strategies and Expected Payoffs

Expected payoffs

- More generally, consider a $n$-player finite game.
- Consider the strategy profile $\sigma=\left(\sigma_{1}, \ldots, \sigma_{n}\right)$.
- Then, the outcome $\left(s_{1}, \ldots, s_{n}\right)$ under $\sigma$ occurs with probability

$$
\sigma_{1}\left(s_{1}\right) \times \sigma_{2}\left(s_{2}\right) \times \ldots \times \sigma_{n}\left(s_{n}\right)=\prod_{j=1}^{n} \sigma_{j}\left(s_{j}\right)
$$

- Therefore, player $i$ 's expected payoff under $\sigma$ is

$$
\begin{aligned}
v_{i}(\sigma) & =\sum_{s \in S}\left(\prod_{j=1}^{n} \sigma_{j}\left(s_{j}\right)\right) v_{i}(s) \\
& =\sum_{s_{1} \in S_{1}} \sum_{s_{2} \in S_{2}} \ldots \sum_{s_{n} \in S_{n}}\left(\prod_{j=1}^{n} \sigma_{j}\left(s_{j}\right)\right) v_{i}(s)
\end{aligned}
$$

## Mixed Strategies and Expected Payoffs

## Expected payoffs

- Rearranging terms, we can also write it as

$$
v_{i}(\sigma)=\sum_{s_{i} \in S_{i}}\left[\sigma_{i}\left(s_{i}\right) \times \sum_{s_{-i} \in S_{-i}}\left(\prod_{j \neq i} \sigma_{j}\left(s_{j}\right)\right) v_{i}\left(s_{i}, s_{-i}\right)\right]
$$

$\rightarrow$ Note that

$$
\sum_{s_{-i} \in S_{-i}}\left(\prod_{j \neq i} \sigma_{j}\left(s_{j}\right)\right) v_{i}\left(s_{i}, s_{-i}\right)=v_{i}\left(s_{i}, \sigma_{-i}\right)
$$

is $i$ 's expected payoff from playing $s_{i}$ against opponents' $\sigma_{-i}$.

- Therefore, $i$ 's expected payoff can be written as

$$
v_{i}\left(\sigma_{i}, \sigma_{-i}\right)=\sum_{s_{i} \in S_{i}} \sigma_{i}\left(s_{i}\right) v_{i}\left(s_{i}, \sigma_{-i}\right)
$$

- Player $i$ 's expected payoff from $\sigma_{i}$ against $\sigma_{-i}$ is the weighted average of his expected payoffs from playing pure strategies.


## Mixed-Strategy Nash Equilibrium

## Definition

- We are ready to extend the concept of best response and Nash equilibrium to mixed strategies.


## Definition 2.12

A mixed strategy $\sigma_{i}$ for player $i$ is a best response to the opponents' strategy $\sigma_{-i}$ if

$$
v_{i}\left(\sigma_{i}, \sigma_{-i}\right) \geq v_{i}\left(s_{i}, \sigma_{-i}\right), \forall s_{i} \in S_{i}
$$

- $\sigma_{i}$ is a best response to $\sigma_{-i}$ if it is as good as any pure strategy $s_{i} \in S_{i}$.
- In fact, if $\sigma_{i}$ is a best response to $\sigma_{-i}$, then it is as good as any mixed strategy $\sigma_{i}^{\prime} \in \Delta S_{i}$ :

$$
v_{i}\left(\sigma_{i}, \sigma_{-i}\right)=\sum_{s_{i} \in S_{i}} \sigma_{i}^{\prime}\left(s_{i}\right) v_{i}\left(\sigma_{i}, \sigma_{-i}\right) \geq \sum_{s_{i} \in S_{i}} \sigma_{i}^{\prime}\left(s_{i}\right) v_{i}\left(s_{i}, \sigma_{-i}\right)=v_{i}\left(\sigma_{i}^{\prime}, \sigma_{-i}\right)
$$

## Mixed-Strategy Nash Equilibrium

## Definition

- The following lemma is simple. But it plays an important (perhaps the most important) role in computing mixed strategy Nash equilibria.


## Lemma 2.2

A mixed strategy $\sigma_{i}$ is a best response to $\sigma_{-i}$ if and only if every pure strategy $s_{i}$ in the support of $\sigma_{i}$ is a best response to $\sigma_{-i}$. Consequently, player $i$ is indifferent between all pure strategies in the support of $\sigma_{i}$.

## Mixed-Strategy Nash Equilibrium

## Definition

## Proof of Lemma 2.2.

"if" part: suppose every pure strategy $s_{i}$ in the support of $\sigma_{i}$ is a best response to $\sigma_{-i}$ :

$$
v_{i}\left(s_{i}, \sigma_{-i}\right) \geq v_{i}\left(s_{i}^{\prime}, \sigma_{-i}\right), \forall s_{i}^{\prime} \in S_{i}
$$

Then, for any $s_{i}^{\prime} \in S_{i}$, we have

$$
\begin{aligned}
v_{i}\left(\sigma_{i}, \sigma_{-i}\right) & =\sum_{s_{i} \in \operatorname{supp} \sigma_{i}} \sigma_{i}\left(s_{i}\right) v_{i}\left(s_{i}, \sigma_{-i}\right) \\
& \geq \sum_{s_{i} \in \operatorname{supp} \sigma_{i}} \sigma_{i}\left(s_{i}\right) v_{i}\left(s_{i}^{\prime}, \sigma_{-i}\right) \\
& =v_{i}\left(s_{i}^{\prime}, \sigma_{-i}\right)
\end{aligned}
$$

This proves that $\sigma_{i}$ is a best response to $\sigma_{-i}$.

# Mixed-Strategy Nash Equilibrium 

Definition

## Proof of Lemma 2.2 (Cont.)

"only if" part: assume $\sigma_{i}$ is a best response to $\sigma_{-i}$. Suppose, by contradiction, that $s_{i}$ is in the support of $\sigma_{i}$ but it is not a best response to $\sigma_{-i}$. Let $\hat{s}_{i} \neq s_{i}$ be a best response to $\sigma_{-i}$. Then we have

$$
v_{i}\left(\hat{s}_{i}, \sigma_{-i}\right) \geq v_{i}\left(s_{i}^{\prime}, \sigma_{-i}\right), \forall s_{i}^{\prime} \in S_{i}
$$

and

$$
v_{i}\left(\hat{s}_{i}, \sigma_{-i}\right)>v_{i}\left(s_{i}, \sigma_{-i}\right)
$$

## Mixed-Strategy Nash Equilibrium

## Definition

## Proof of Lemma 2.2 (Cont.)

Therefore,

$$
\begin{aligned}
v_{i}\left(\hat{s}_{i}, \sigma_{-i}\right) & =\sum_{s_{i}^{\prime} \in \operatorname{supp} \sigma_{i}} \sigma_{i}\left(s_{i}^{\prime}\right) v_{i}\left(\hat{s}_{i}, \sigma_{-i}\right) \\
& >\sum_{s_{i}^{\prime} \in \operatorname{supp} \sigma_{i}} \sigma_{i}\left(s_{i}^{\prime}\right) v_{i}\left(s_{i}^{\prime}, \sigma_{-i}\right) \\
& =v_{i}\left(\sigma_{i}, \sigma_{-i}\right)
\end{aligned}
$$

contradicting the assumption that $\sigma_{i}$ is a best response. Hence, every pure strategy in the support of $\sigma_{i}$ must be a best response to $\sigma_{-i}$. Consequently, if $s_{i}$ is in the support of $\sigma_{i}$, we have

$$
v_{i}\left(s_{i}, \sigma_{-i}\right)=\max _{s_{i}^{\prime}} v_{i}\left(s_{i}^{\prime}, \sigma_{-i}\right)
$$

proving the indifference condition.

# Mixed-Strategy Nash Equilibrium 

Definition

## Definition 2.13

A mixed strategy profile $\sigma^{*}=\left(\sigma_{1}^{*}, \sigma_{2}^{*}, \ldots, \sigma_{n}^{*}\right)$ is a Nash equilibrium if for each player $i, \sigma_{i}^{*}$ is a best response to $\sigma_{-i}^{*}$.

- Conceptually identical to pure strategy Nash equilibrium: mutual best responses.


## Mixed-Strategy Nash Equilibrium

Example: the matching pennies

\$\$

\$\$

Figure 2.21: The matching pennies

- No pure strategy Nash equilibrium.
- Suppose $\sigma_{1}(H)=p$ and $\sigma_{2}(H)=q$.
- Then

$$
\begin{aligned}
v_{1}\left(\sigma_{1}, \sigma_{2}\right) & =p q-p(1-q)-(1-p) q+(1-p)(1-q) \\
& =2(2 q-1) p+1-2 q
\end{aligned}
$$

- Thus,

$$
B R_{1}(q)= \begin{cases}0, & \text { if } q<1 / 2 \\ {[0,1],} & \text { if } q=1 / 2 \\ 1, & \text { if } q>1 / 2\end{cases}
$$

## Mixed-Strategy Nash Equilibrium

Example: the matching pennies

- Similarly,

$$
\begin{aligned}
v_{2}\left(\sigma_{1}, \sigma 2\right) & =-p q+p(1-q)+(1-p) q-(1-p)(1-q) \\
& =2(1-2 p) q+2 p-1
\end{aligned}
$$

- Thus,

$$
B R_{2}(p)= \begin{cases}1, & \text { if } p<1 / 2 \\ {[0,1],} & \text { if } p=1 / 2 \\ 0, & \text { if } p>1 / 2\end{cases}
$$

## Mixed-Strategy Nash Equilibrium

Example: the matching pennies

![](https://cdn.mathpix.com/cropped/2024_09_09_605858d45802b61328b8g-117.jpg?height=552&width=602&top_left_y=177&top_left_x=329)

Figure 2.22: Best response correspondences in the matching pennies

- Unique Nash equilibrium: $\left(\frac{1}{2} \circ H+\frac{1}{2} \circ T, \frac{1}{2} \circ H+\frac{1}{2} \circ T\right)$.


## Mixed-Strategy Nash Equilibrium

## Example: the matching pennies

- We can also use the indifference condition to solve this game.
- Indifference condition first implies that, in this game, if one player mixes in equilibrium, the other player must mix as well. (Yes?)
- Hence, there will be no equilibrium in which only one player mixes.
- Suppose $\sigma_{1}(H)=p \in(0,1)$ and $\sigma_{2}(H)=q \in(0,1)$.
- Indifference condition for player 1 requires

$$
q-(1-q)=-q+(1-q) \Longrightarrow q=1 / 2
$$

- Indifference condition for player 2 requires

$$
-p+(1-p)=p-(1-p) \Longrightarrow q=1 / 2
$$

- We obtain the same result: $\left(\frac{1}{2} \circ H+\frac{1}{2} \circ T, \frac{1}{2} \circ H+\frac{1}{2} \circ T\right)$.


## Mixed-Strategy Nash Equilibrium

Example: rock-paper-scissors

|  | $R$ | $P$ | $S$ |
| :---: | :---: | :---: | :---: |
| $R$ | 0,0 | $-1,1$ | $1,-1$ |
| $P$ | $1,-1$ | 0,0 | $-1,1$ |
| $S$ | $-1,1$ | $1,-1$ | 0,0 |
|  |  |  |  |

Figure 2.23: Rock-paper-scissors

- No pure strategy Nash equilibrium, as we have already known.
- Nash equilibrium in mixed strategies?
- A brave guess: $(\sigma, \sigma)$ where $\sigma=\frac{1}{3} \circ R+\frac{1}{3} \circ P+\frac{1}{3} \circ S$.
- It is indeed a Nash equilibrium

$$
v_{i}(R, \sigma)=v_{i}(P, \sigma)=v_{i}(S, \sigma)=0
$$

## Mixed-Strategy Nash Equilibrium

Example: rock-paper-scissors

- It is more challenging to show that this is the unique equilibrium.
- The best response correspondence approach is not very useful, since we can not draw 4 -dimensional graphs. (why 4 -dimensional?)
- Therefore, we rely on the indifference condition with a careful discussion about the support of the equilibrium strategies.


## Mixed-Strategy Nash Equilibrium

## Example: rock-paper-scissors

- First observe that there is no equilibrium in which only one player mixes. (The same reason as that in the matching pennies.)
- Thus, we consider potential equilibrium in which both players mix.
- We claim that there is no equilibrium in which one player only mixes between two pure strategies.
- Consider an equilibrium $\left(\sigma_{1}, \sigma_{2}\right)$. Suppose, by contradiction, that $\sigma_{1}$ mixes between $R$ and $P$ only. Note that

$$
v_{2}\left(P, \sigma_{1}\right)=\sigma_{1}(R)>-\sigma_{1}(P)=v_{2}\left(R, \sigma_{1}\right)
$$

implying that $R$ is not a best response for player 2 to $\sigma_{1}$.

- Because $\sigma_{2}$ is a best response to $\sigma_{1}$, we know $\sigma_{2}(R)=0$. Hence, $\sigma_{2}$ mixes between $P$ and $S$ only.


## Mixed-Strategy Nash Equilibrium

Example: rock-paper-scissors

- But if $\sigma_{2}$ only mixes between $P$ and $S$, we know

$$
v_{1}\left(S, \sigma_{2}\right)=\sigma_{2}(P)>-\sigma_{2}(S)=v_{1}\left(P, \sigma_{2}\right)
$$

implying that $P$ is not a best response to $\sigma_{2}$.

- This contradicts our assumption that $\sigma_{1}$ is a best response to $\sigma_{2}$ and $\sigma_{1}(P)>0$.
- Therefore, there is no equilibrium in which player 1 only mixes between $R$ and $P$.
- Applying similar arguments, we can show that there is no equilibrium in which one player only mixes between two strategies.


## Mixed-Strategy Nash Equilibrium

Example: rock-paper-scissors

- We are left with the case where both players mix between all three pure strategies.
- Then, this requires that every player is indifferent between all three pure strategies given the opponent's strategy.
- Given $\sigma_{2}$, we know

$$
\begin{aligned}
& v_{1}\left(R, \sigma_{2}\right)=-\sigma_{2}(P)+\sigma_{2}(S) \\
& v_{1}\left(P, \sigma_{2}\right)=\sigma_{2}(R)-\sigma_{2}(S) \\
& v_{1}\left(S, \sigma_{2}\right)=-\sigma_{2}(R)+\sigma_{2}(P)
\end{aligned}
$$

- Indifference conditions require

$$
-\sigma_{2}(P)+\sigma_{2}(S)=\sigma_{2}(R)-\sigma_{2}(S)=-\sigma_{2}(R)+\sigma_{2}(P)
$$

- These two equations, together with $\sigma_{2}(R)+\sigma_{2}(P)+\sigma_{2}(S)=1$, yield

$$
\sigma_{2}(R)=\sigma_{2}(P)=\sigma_{2}(S)=\frac{1}{3}
$$

## Mixed-Strategy Nash Equilibrium

Example: rock-paper-scissors

- Similarly, applying player 2's indifference conditions would yield

$$
\sigma_{1}(R)=\sigma_{1}(P)=\sigma_{1}(S)=\frac{1}{3}
$$

- Therefore, both players mixing over all three pure strategies with equal probability is the unique Nash equilibrium.


## Mixed-Strategy Nash Equilibrium

Example: coexistence of pure and mixed strategy Nash equilibrium

|  | $O$ | $F$ |
| :--- | :---: | :---: |
| $O$ | 2,1 | 0,0 |
| $F$ | 0,0 | 1,2 |
|  |  |  |

Figure 2.24: Battle of the sexes

- Two pure strategy Nash equilibria: $(O, O)$ and $(F, F)$.
- Mixed strategy Nash equilibrium:
- In this game, if in equilibrium one player mixes, the other player must mix as well. Thus, we look for equilibrium in which both players mix.
- Suppose $\sigma_{1}(O)=p \in(0,1)$ and $\sigma_{2}(O)=q \in(0,1)$.
- Player 1's indifference condition requires

$$
2 \times q+0 \times(1-q)=0 \times q+1 \times(1-q) \Longrightarrow q=1 / 3
$$

- Player 2's indifference condition requires

$$
1 \times p+0 \times(1-p)=0 \times p+2 \times(1-p) \Longrightarrow p=2 / 3
$$

- Unique mixed strategy Nash equilibrium: $\left(\frac{2}{3} \circ O+\frac{1}{3} \circ F, \frac{1}{3} \circ O+\frac{2}{3} \circ F\right)$.


## Existence of Nash Equilibrium

- We have seen simple games in which there is no pure strategy Nash equilibrium, e.g., the matching pennies and rock-paper-scissors.
- We also know that these two games have Nash equilibrium in mixed strategies.
- In fact, if players are allowed to randomize, then every finite game has a Nash equilibrium.
- This is Nash's existence theorem.

Theorem 2.1
Every finite normal form game has a Nash equilibrium (possibly in mixed strategies).

## Dominance and IESDS Revisited

Dominance by a mixed strategy

## Definition 2.14

Let $\sigma_{i} \in \Delta S_{i}$ and $s_{i} \in S_{i}$ be possible strategies for player $i$. We say that $s_{i}$ is strictly dominated by $\sigma_{i}$ if

$$
v_{i}\left(\sigma_{i}, s_{-i}\right)>v_{i}\left(s_{i}, s_{-i}\right), \forall s_{-i} \in S_{-i}
$$

- That is, to consider a strategy as strictly dominated, we no longer require that some other pure strategy dominate it.
- We allow for mixed strategies to dominate it as well.


## Dominance and IESDS Revisited

Dominance by a mixed strategy

| $L$ | $C$ | $R$ |  |
| :---: | :---: | :---: | :---: |
| $U$ | 5,1 | 1,4 | 1,0 |
| $M$ | 3,2 | 0,0 | 3,5 |
| $D$ | 4,3 | 4,4 | 0,3 |
|  |  |  |  |

- No strategy is strictly dominated by another pure strategy for each player.
- However, $L$ is strictly dominated by some mixture of $C$ and $R$.
- To see this, consider the mixed strategy $\sigma_{2}$ with $\sigma_{2}(C)=\sigma_{2}(R)=1 / 2$.
- Then,

$$
\begin{array}{r}
v_{2}\left(U, \sigma_{2}\right)=2>1=v_{2}(U, L), \\
v_{2}\left(M, \sigma_{2}\right)=5 / 2>2=v_{2}(M, L), \\
v_{2}\left(D, \sigma_{2}\right)=7 / 2>3=v_{2}(D, L) .
\end{array}
$$

- Note that there are other mixed strategies that strictly dominate $L$.


## Dominance and IESDS Revisited

## Dominance by a mixed strategy

- It is worth having a more careful look at Definition 2.14.
- In this definition, we require that $\sigma_{i}$ do better than $s_{i}$ for every pure strategy $s_{-i} \in S_{-i}$ of the opponents.
- If we allow player $i$ to mix, why don't we allow the opponents to mix as well and require that $\sigma_{i}$ do better than $s_{i}$ for every $\sigma_{-i} \in \Delta S_{-i}$ ? That is, we require

$$
v_{i}\left(\sigma_{i}, \sigma_{-i}\right)>v_{i}\left(s_{i}, \sigma_{-i}\right), \forall \sigma_{-i} \in \Delta S_{-i}
$$

- This is because (2.1) and (2.2) are actually equivalent:
- On the one hand, it is obvious that (2.2) implies (2.1).
- On the other hand, if (2.1) holds, then for any $\sigma_{-i} \in \Delta S_{-i}$, we have

$$
v_{i}\left(\sigma_{i}, \sigma_{-i}\right)=\sum_{s_{-i}} \sigma_{-i}\left(s_{-i}\right) v_{i}\left(\sigma_{i}, s_{-i}\right)>\sum_{s_{-i}} \sigma_{-i}\left(s_{-i}\right) v_{i}\left(s_{i}, s_{-i}\right)=v_{i}\left(s_{i}, \sigma_{-i}\right)
$$

implying that (2.2) holds.

## Dominance and IESDS Revisited

IESDS

- The idea of IESDS still applies.
- But in each round, we also delete those strategies that are dominated by a mixed strategy.

|  | $L$ | $C$ | $R$ |
| :---: | :---: | :---: | :---: |
| $U$ | 5,1 | 1,4 | 1,0 |
| $M$ | 3,2 | 0,0 | 3,5 |
| $D$ | 4,3 | 4,4 | 0,3 |
|  |  |  |  |

- In the first round, we delete $L$.
- In the second round, we delete $U$ because it is strictly dominated by $\frac{1}{2} \circ M+\frac{1}{2} \circ R$.
- Then $S_{1}^{*}=\{M, D\}$ and $S_{2}^{*}=\{C, R\}$ survive IESDS.


## Dominance and IESDS Revisited

IESDS

- One of the significance of IESDS is stated in the following proposition.


## Proposition 2.9

Consider a finite game. Suppose $S_{1}^{*} \times \ldots \times S_{n}^{*}$ survive IESDS. Then, $\sigma^{*}$ is a Nash equilibrium of the original game if and only if it is a Nash equilibrium of the reduced game $\left(N, S_{1}^{*} \times \ldots \times S_{n}^{*},\left\{v_{i}\right\}_{i=1}^{n}\right)$.

- Note that the "only if" part implicitly asserts that every pure strategy $s_{i}$ in the support of $\sigma_{i}^{*}$ survives IESDS. This is a mixed strategy analog of Proposition 2.8.
- For games with many pure strategies, it is usually not easy to find out all the (possibly mixed) equilibria.
- Proposition 2.9 asserts that IESDS can help us in that it may narrow down the set of pure strategies we need to consider.


## Dominance and IESDS Revisited

IESDS

|  | $L$ | $C$ | $R$ |
| :---: | :---: | :---: | :---: |
| $U$ | 5,1 | 1,4 | 1,0 |
| $M$ | 3,2 | 0,0 | 3,5 |
| $D$ | 4,3 | 4,4 | 0,3 |
|  |  |  |  |

- $S_{1}^{*}=\{M, D\}$ and $S_{2}^{*}=\{C, R\}$ survive IESDS.
- To find all Nash equilibria, we only need to find all Nash in the reduced game:

|  | $C$ | $R$ |
| :---: | :---: | :---: |
| $M$ | 0,0 | 3,5 |
| $D$ | 4,4 | 0,3 |
|  |  |  |

- Nash: $(M, R),(D, C)$ and $\left(\frac{1}{6} \circ M+\frac{5}{6} \circ D, \frac{3}{7} \circ C+\frac{4}{7} \circ R\right)$.


## Dominance and IESDS Revisited

IESDS

## Proof of Proposition 2.9.

"if" part: assume $\sigma^{*}$ is a Nash equilibrium of the reduced game.
Suppose, by contradiction, that it is not a Nash equilibrium of the original game. Then in the original game, some player, say $i$, must have a profitable deviation $s_{i}^{1}: v_{i}\left(s_{i}^{1}, \sigma_{-i}^{*}\right)>v_{i}\left(\sigma^{*}\right)$. Because $\sigma^{*}$ is a Nash in the reduced game, we must have $s_{i}^{1} \notin S_{i}^{*}$, that is, $s_{i}^{1}$ must be deleted in the process of IESDS.

Because $s_{i}^{1}$ is deleted and because every pure strategy $s_{j}$ in the support of $\sigma_{j}^{*}$ always remains for $j \neq i$, there must exist some $\sigma_{i}^{1}$ such that

$$
v_{i}\left(\sigma_{i}^{1}, s_{-i}\right)>v_{i}\left(s_{i}^{1}, s_{-i}\right), \forall s_{-i} \in \operatorname{supp} \sigma_{-i}^{*} .
$$

This implies $v_{i}\left(\sigma_{i}^{1}, \sigma_{-i}^{*}\right)>v_{i}\left(s_{i}^{1}, \sigma_{-i}^{*}\right)$. Thus, there must exist $s_{i}^{2}$ such that $v_{i}\left(s_{i}^{2}, \sigma_{-i}^{*}\right)>v_{i}\left(s_{i}^{1}, \sigma_{-i}^{*}\right)$.

## Dominance and IESDS Revisited

## IESDS

## Proof of Proposition 2.9.

Similarly as $s_{i}^{1}$, we know $s_{i}^{2} \notin S_{i}^{*}$, that is, $s_{i}^{2}$ must be deleted in the process of IESDS as well. Applying the same arguments, we can actually find infinitely many strategies $s_{i}^{3}, \ldots, s_{i}^{m}, \ldots$. This contradicts our finite game assumption.

## Dominance and IESDS Revisited

## IESDS

## Proof of Proposition 2.9 (Cont.)

"only if" part: we prove the claim that if $\sigma_{i}^{*}$ is a Nash equilibrium, then no pure strategy $s_{i}$ in the support of $\sigma_{i}^{*}$ is strictly dominated. The desired result will directly follow. (Yes?)

Suppose, by contradiction, that $s_{i}$ is in the support of $\sigma_{i}^{*}$ and it is strictly dominated by some $\sigma_{i}$. Then, we have

$$
v_{i}\left(\sigma_{i}, s_{-i}\right)>v_{i}\left(s_{i}, s_{-i}\right), \forall s_{-i} \in S_{-i}
$$

This implies

$$
\sum_{s_{-i} \in S_{-i}} \sigma_{-i}^{*}\left(s_{-i}\right) v_{i}\left(\sigma_{i}, s_{-i}\right)>\sum_{s_{-i} \in S_{-i}} \sigma_{-i}^{*}\left(s_{-i}\right) v_{i}\left(s_{i}, s_{-i}\right)
$$

## Dominance and IESDS Revisited

## IESDS

## Proof of Proposition 2.9 (Cont.)

Equivalently,

$$
v_{i}\left(\sigma_{i}, \sigma_{-i}^{*}\right)>v_{i}\left(s_{i}, \sigma_{-i}^{*}\right)
$$

contradicting the assumptions that $\sigma_{i}^{*}$ is a best response to $\sigma_{-i}^{*}$ and $s_{i}$ is in the support of $\sigma_{i}^{*}$.

# Game Theory Lecture Notes 3 

## Dynamic Games with Complete Information

Ju Hu<br>National School of Development<br>Peking University

Fall 2022

## The Extensive Form Game

Introduction

- Normal form games are mostly used to capture static strategic interactions: players act only once and simultaneously.
- How about dynamic environment: players act sequentially?
- Examples of such situations:
- chess;
tennis;
- bargaining;
- chatting; etc.
- We use extensive form games to describe such situations.


## The Extensive Form Game Game Trees

- An extensive form game describes who moves when with what available actions and information, as well as players' payoffs as a function of outcomes.
- Similarly as matrix representation for normal form games, we can use a game tree to represent an extensive form game.


## The Extensive Form Game

## Game Trees

![](https://cdn.mathpix.com/cropped/2024_09_09_605858d45802b61328b8g-140.jpg?height=348&width=369&top_left_y=152&top_left_x=497)

Figure 3.1: A trust game.

- Player 1 first chooses whether to ask for the services of player 2 .
- He can trust player $2(T)$ or not trust him $(N)$.
- The latter choice gives both players a payoff of 0 .
- If player 1 plays $T$, player 2 can choose to cooperate $(C)$ or defect $(D)$.
- If player 2 cooperates, both players get 1 .
- If player 2 defects, player 1 gets -1 while player 2 gets 2 .


## The Extensive Form Game

## Game Trees

![](https://cdn.mathpix.com/cropped/2024_09_09_605858d45802b61328b8g-141.jpg?height=298&width=659&top_left_y=179&top_left_x=294)

Figure 3.2: The sequential-move Battle of the Sexes game.

- A variant of the battle of the sexes game.
- Players move sequentially.
- Player 1 chooses between $O$ or $F$ first.
- Then, after observing player 1's choice, player 2 chooses between $o$ and $f$.


## The Extensive Form Game

## Game Trees

![](https://cdn.mathpix.com/cropped/2024_09_09_605858d45802b61328b8g-142.jpg?height=459&width=430&top_left_y=219&top_left_x=460)

Figure 3.3: A three player game

## The Extensive Form Game

## Game Trees

## Definition 3.1

A game tree is a set of nodes $x \in X$ with a precedence relation $x \succ x^{\prime}$, which means " $x$ precedes $x^{\prime}$." Every node in a game tree has only one predecessor. There is a special node called the root (or initial node) of the tree. Nodes that do not precede other nodes are called terminal nodes. Terminal nodes denote the final outcomes of the game with which payoffs are associated. Every node $x$ that is not a terminal node is assigned to a player, $i(x)$, with action set $A_{i}(x)$.

- An extensive form game is finite if there are only finitely many nodes.
- How about the game tree for Tianji's horse racing?


## The Extensive Form Game

## Game Trees

![](https://cdn.mathpix.com/cropped/2024_09_09_605858d45802b61328b8g-144.jpg?height=297&width=663&top_left_y=152&top_left_x=292)

- Nodes: $X=\left\{x_{0}, x_{1}, x_{2}, x_{3}, x_{4}, x_{5}, x_{6}\right\}$
- Root (initial node): $x_{0}$
- Terminal nodes: $Z=\left\{x_{3}, x_{4}, x_{5}, x_{6}\right\}$
- Player assignment: $i\left(x_{0}\right)=1, i\left(x_{1}\right)=i\left(x_{2}\right)=2$
- Available action: $A_{1}\left(x_{0}\right)=\{O, F\}, A_{2}\left(x_{1}\right)=A_{2}\left(x_{2}\right)=\{o, f\}$
- Payoffs: $v_{1}, v_{2}: Z \rightarrow \mathbb{R}$

$$
\begin{aligned}
& v_{1}\left(x_{3}\right)=2, v_{1}\left(x_{4}\right)=0, v_{1}\left(x_{5}\right)=0, v_{1}\left(x_{6}\right)=1, \\
& v_{2}\left(x_{3}\right)=1, v_{2}\left(x_{4}\right)=0, v_{2}\left(x_{5}\right)=0, v_{2}\left(x_{6}\right)=2 .
\end{aligned}
$$

## The Extensive Form Game Game Trees

- So far, we have seen examples of game trees in which every player, when called on to move, perfectly knows where he is in the tree.
- In other words, every player perfectly observes what has occurred (or equivalently, what other players have chosen) previously.
- Can we use game tree to describe the situation where players may not be fully informed about what has happened before.
- Example: professor gives an exam; students prepare for that exam without knowing whether it is easy or difficult.


## The Extensive Form Game <br> Game Trees

## Definition 3.2

Every player $i$ has a collection of information sets $h_{i} \in H_{i}$ that partition the nodes of the games at which player $i$ moves with the following properties:

- If $h_{i}$ is a singleton that includes only $x$ when player $i$ who moves at $x$ knows that he is at $x$.
- If $x \neq x^{\prime}$ and if both $x \in h_{i}$ and $x^{\prime} \in h_{i}$, then player $i$ who moves at $x$ does not know whether he is at $x$ or $x^{\prime}$.
- If $x \neq x^{\prime}$ and if both $x \in h_{i}$ and $x^{\prime} \in h_{i}$, then $A_{i}(x)=A_{i}\left(x^{\prime}\right)$.


## The Extensive Form Game Game Trees

- The 2nd point states that player $i$ can not distinguish nodes that are contained in the same information set.
- The 3rd point is to maintain the logic of information. If both $x$ and $x^{\prime}$ are contained in the same information set, but $A_{i}(x) \neq A_{i}\left(x^{\prime}\right)$, then player $i$ can indeed distinguish $x$ and $x^{\prime}$ by observing what actions available to him.


## The Extensive Form Game

## Game Trees

![](https://cdn.mathpix.com/cropped/2024_09_09_605858d45802b61328b8g-148.jpg?height=303&width=655&top_left_y=257&top_left_x=301)

Figure 3.4: The simultaneous-move Battle of the Sexes game.

- $H_{1}=\left\{h_{1}\right\}$ where $h_{1}=\left\{x_{0}\right\}$.
- $H_{2}=\left\{h_{2}\right\}$ where $h_{2}=\left\{x_{1}, x_{2}\right\}$.


## The Extensive Form Game

## Game Trees

![](https://cdn.mathpix.com/cropped/2024_09_09_605858d45802b61328b8g-149.jpg?height=441&width=825&top_left_y=255&top_left_x=216)

Figure 3.5: Game tree of rock-paper-scissors

- Every normal form game can be represented by an extensive form game!


## The Extensive Form Game

## Game Trees

![](https://cdn.mathpix.com/cropped/2024_09_09_605858d45802b61328b8g-150.jpg?height=448&width=803&top_left_y=165&top_left_x=227)

- Player 1 has one information set: $h_{1}=\left\{x_{0}\right\}$.
- Player 2 has two information sets: $h_{2}=\left\{x_{1}\right\}$ and $h_{2}^{\prime}=\left\{x_{2}, x_{3}\right\}$.
- Player 3 has three information sets: $h_{3}=\left\{x_{4}\right\}, h_{3}^{\prime}=\left\{x_{5}, x_{6}\right\}$ and $h_{3}^{\prime \prime}=\left\{x_{7}\right\}$.


## The Extensive Form Game

## Perfect recall

- We will only consider extensive form games in which every player knows whatever he knew previously, including his own previous actions.


## Definition 3.3

A game of perfect recall in one in which no player ever forgets information that he previously knew.

## The Extensive Form Game

## Perfect recall

![](https://cdn.mathpix.com/cropped/2024_09_09_605858d45802b61328b8g-152.jpg?height=209&width=440&top_left_y=164&top_left_x=151)
(a) Player 1 forgets his previous action.

![](https://cdn.mathpix.com/cropped/2024_09_09_605858d45802b61328b8g-152.jpg?height=208&width=433&top_left_y=166&top_left_x=664)
(b) Player 1 forgets his previous action.

![](https://cdn.mathpix.com/cropped/2024_09_09_605858d45802b61328b8g-152.jpg?height=260&width=475&top_left_y=410&top_left_x=367)
(c) Player 2 forgets what he previously knew.

Figure 3.6: Examples of imperfect recall. They are beyond the scope of this course.

## The Extensive Form Game

## Perfect recall

![](https://cdn.mathpix.com/cropped/2024_09_09_605858d45802b61328b8g-153.jpg?height=324&width=932&top_left_y=256&top_left_x=161)

Figure 3.7: The absent-minded driver. It is a one-player game (decision problem) with imperfect recall.

## The Extensive Form Game

Imperfect v.s. perfect information

## Definition 3.4

An extensive form game is called a game of perfect information if every information set is a singleton. It is called a game of imperfect information if some information sets contain several nodes.

- Perfect information: every player, when called on to move, knows exactly what has happened previously.
- Imperfect information: some players do not know what some other players have chosen previously at some information sets.


## Strategies in Extensive Form Games

Pure strategies

![](https://cdn.mathpix.com/cropped/2024_09_09_605858d45802b61328b8g-155.jpg?height=298&width=658&top_left_y=277&top_left_x=293)

Figure 3.8: The sequential-move Battle of the Sexes game.

## Strategies in Extensive Form Games

## Pure strategies

- Player 1 has a single information set.
- It is then intuitive that a pure strategy for him is simply $O$ or $F$.
- Strategy space for player $1:\{O, F\}$.
- How about player 2? How does player 2 think about her situation?
- Because player 2 moves after observing player 1's choice, player 2 can make a plan for her choices:
- if player 1 chooses $O, \mathrm{I}$ am going to choose $x \in\{o, f\}$;
- if player 1 chooses $F, \mathrm{I}$ am going to choose $y \in\{o, f\}$.
- Thus, player 2's strategy is not simply $o$ or $f$.
- Rather, it should be a complete plan of play that describes which pure action she will choose at each of her information sets.
- Strategy space for player 2: $\{o o$, of, $f o, f f\}$.
- $x y$ means if player 1 chooses $O$ (the left branch), player 2 will choose $x$; if player 1 chooses $F$ (the right branch), player 2 will choose $y$.


## Strategies in Extensive Form Games

## Pure strategies

![](https://cdn.mathpix.com/cropped/2024_09_09_605858d45802b61328b8g-157.jpg?height=302&width=655&top_left_y=167&top_left_x=296)

Figure 3.9: The simultaneous-move Battle of the Sexes game.

- A pure strategy for player 1 is still either $O$ or $F$, as before, $S_{1}=\{O, F\}$.
- Now, player 2 can not observe player 1's choice when called on to move.
- Therefore, player 2 can not condition her choice on player 1's choice.
- Consequently, player 2 can only simply chooses either $o$ or $f, S_{2}=\{o, f\}$.
- Note that this is also a complete plan of play: it fully describes player 2's behavior when called upon to move.


## Strategies in Extensive Form Games

## Pure strategies

- $H_{i}$ : the collection of all information sets at which player $i$ plays.
- $h_{i} \in H_{i}$ : one of $i$ 's information sets.
- $A_{i}\left(h_{i}\right):$ the actions available to player $i$ at $h_{i}$.
- $A_{i} \equiv \cup_{h_{i} \in H_{i}} A_{i}\left(h_{i}\right)$ : the set of all actions of player $i$.


## Definition 3.5

A pure strategy for player $i$ is a mapping $s_{i}: H_{i} \rightarrow A_{i}$ that assigns an action $s_{i}\left(h_{i}\right) \in A_{i}\left(h_{i}\right)$ for every information set $h_{i} \in H_{i}$. We denote by $S_{i}$ the set of all pure strategy mappings $s_{i} \in S_{i}$.

- Usually, we also say that a strategy in an extensive form game is a complete contingent plan: a plan of actions conditional on this player's information about where he is in the game.


## Strategies in Extensive Form Games

Pure strategies

![](https://cdn.mathpix.com/cropped/2024_09_09_605858d45802b61328b8g-159.jpg?height=450&width=813&top_left_y=164&top_left_x=217)

- $S_{1}=\{L, C, R\}$;
- $S_{2}=\{\ell \ell, \ell r, r \ell, r r\}=\{\ell, r\} \times\{\ell, r\} ;$
- $S_{3}=\left\{\ell^{\prime} \ell^{\prime} \ell^{\prime}, \ell^{\prime} \ell^{\prime} r^{\prime}, \ell^{\prime} r^{\prime} \ell^{\prime}, \ell^{\prime} r^{\prime} r^{\prime}, r^{\prime} \ell^{\prime} \ell^{\prime}, r^{\prime} \ell^{\prime} r^{\prime}, r^{\prime} r^{\prime} \ell^{\prime}, r^{\prime} r^{\prime} r^{\prime}\right\}=$ $\left\{\ell^{\prime}, r^{\prime}\right\} \times\left\{\ell^{\prime}, r^{\prime}\right\} \times\left\{\ell^{\prime}, r^{\prime}\right\}$.


## Strategies in Extensive Form Games

## Pure strategies

![](https://cdn.mathpix.com/cropped/2024_09_09_605858d45802b61328b8g-160.jpg?height=444&width=805&top_left_y=151&top_left_x=226)

- Note that if player 1 plays $L$ at his first information set, then his second information set is never reached regardless of other players' choices.
- But every strategy of player 1 must still specify player 1's plan of choice at his second information set, e.g., $L \ell^{\prime}$.
- $S_{1}=\{L, C, R\} \times\left\{\ell^{\prime}, r^{\prime}\right\}$.


## Strategies in Extensive Form Games

Pure strategies

- Every pure strategy profile $s=\left(s_{1}, \ldots, s_{n}\right)$ leads to a unique terminal node, denoted by $z(s)$.
- This terminal node is the outcome of strategy profile $s$.
- Note the difference between a strategy profile and the induced outcome in extensive form games.


## Strategies in Extensive Form Games

## Mixed and behavioral strategies

- Given a pure strategy space $S_{i}$ for player $i$ in an extensive form game, it is straightforward to define mixed strategies for player $i$, as we do for normal form games.


## Definition 3.6

A mixed strategy for player $i$ is a probability distribution over his pure strategies $s_{i} \in S_{i}$.

- Interpretation: the player selects a plan randomly before the game is played and then follows a particular pure strategy.
- For example, consider $\sigma_{2}=\frac{1}{2} \circ o o+\frac{1}{2} \circ f f$ in the sequential move battle of the sexes. It can be interpreted as the following:
- player 2 randomizes with equal probability between $o o$ and ff before the game is played;
- if $o o$ is chosen, then player 2 plays $o$ regardless of player 1's choice;
- if $f f$ is chose, then player 2 plays $f$ regardless of player 1's choice.


## Strategies in Extensive Form Games

Mixed and behavioral strategies

- How about the following natural description of a "random plan":
- player 2 randomizes between $o$ with probability $1 / 3$ and $f$ with probability $2 / 3$ if player 1 plays $O$;
- she randomizes between $o$ with probability $1 / 4$ and $f$ with probability $3 / 4$ if player 1 plays $F$.
- It is a "plan" that allows players to randomize as the game unfolds.


## Definition 3.7

A behavioral strategy $\sigma_{i}$ specifies for each information set $h_{i} \in H_{i}$ an independent probability distribution $\sigma_{i}\left(h_{i}\right) \in \Delta A_{i}\left(h_{i}\right)$. Thus, for action $a_{i} \in A_{i}\left(h_{i}\right), \sigma_{i}\left(h_{i}\right)\left[a_{i}\right]$ is the probability that player $i$ plays $a_{i}$ at information set $h_{i}$.

- The above example: $\sigma_{2}(O)[o]=\frac{1}{3}, \sigma_{2}(O)[f]=\frac{2}{3}, \sigma_{2}(F)[o]=\frac{1}{4}$, and $\sigma_{2}(F)[f]=\frac{3}{4}$.


## Strategies in Extensive Form Games

Mixed and behavioral strategies

- Consider the sequential move battle of the sexes again.
- Pure strategy space for player 2: $S_{2}=\{o o, o f, f o, f f\}$.
- Mixed strategy space:

$$
\left\{\left(p_{o o}, p_{o f}, p_{f o}, p_{f f}\right) \in[0,1]^{4} \mid p_{o o}+p_{o f}+p_{f o}+p_{f f}=1\right\}
$$

This is a 3 -dimensional space. (Yes?)

- Behavior strategy space:

$$
\left\{\begin{array}{l|l}
(\sigma(O)[o], \sigma(O)[f], \sigma(F)[o], \sigma(F)[f]) \in[0,1]^{4} & \begin{array}{l}
\sigma(O)[o]+\sigma(O)[f]=1 \\
\sigma(F)[o]+\sigma(F)[f]=1
\end{array}
\end{array}\right\}
$$

This is a 2-dimensional space. (Yes?)

- Mixed v.s. behavioral strategy?


## Strategies in Extensive Form Games

## Mixed and behavioral strategies

- Every mixed/behavioral strategy profile leads to a probability distribution of the terminal nodes.
- This distribution is the outcome of this mix/behavioral strategy profile.
- Consider an arbitrary behavioral strategy $\sigma_{2}(O)[o]=q_{O}$ and $\sigma_{2}(F)[o]=q_{F}$.
- If player 1 plays $O$, the outcome is $q_{O} \circ O o+\left(1-q_{O}\right) \circ O f$.
- If player 1 plays $F$, the outcome is $q_{F} \circ F o+\left(1-q_{F}\right) \circ F f$.
- Now, consider an arbitrary mixed strategy ( $\left.p_{o o}, p_{o f}, p_{f o}, p_{f f}\right)$.
- If player 1 plays $O$, the outcome is $\left(p_{o o}+p_{o f}\right) \circ O o+\left(p_{f o}+p_{f f}\right) \circ O f$.
- If player 1 plays $F$, the outcome is $\left(p_{o o}+p_{f o}\right) \circ F o+\left(p_{o f}+p_{f f}\right) \circ F f$.


## Strategies in Extensive Form Games

Mixed and behavioral strategies

- Starting from the behavioral strategy, we can construct a mixed strategy so that it induces the same outcome regardless of player 1's play.
- To see this, consider

$$
\begin{aligned}
p_{o o} & \equiv q_{O} q_{F} \geq 0 \\
p_{o f} & \equiv q_{O}\left(1-q_{F}\right) \geq 0 \\
p_{f o} & \equiv\left(1-q_{O}\right) q_{F} \geq 0 \\
p_{f f} & \equiv\left(1-q_{O}\right)\left(1-q_{F}\right) \geq 0
\end{aligned}
$$

- It is straightforward to see $p_{o o}+p_{o f}+p_{f o}+p_{f f}=1$. So it is indeed a mixed strategy.
- Moreover, because $p_{o o}+p_{o f}=q_{O}$ and $p_{o o}+p_{f o}=q_{F}$, it induces the same outcome as the given behavioral strategy no matter whether player 1 plays $O$ or $F$.


## Strategies in Extensive Form Games

## Mixed and behavioral strategies

- Starting from the mixed strategy, we can also construct a behavioral strategy so that it induces the same outcome regardless of player 1's play.
- To see this, consider

$$
\begin{aligned}
q_{O} & \equiv p_{o o}+p_{o f} \in[0,1] \\
q_{F} & \equiv p_{o o}+p_{f o} \in[0,1]
\end{aligned}
$$

- By construction, it induces the same outcome as the given mixed strategy no matter whether player 1 plays $O$ or $F$.
- The above analysis will also work even if we consider player 1's randomization.


## Strategies in Extensive Form Games

Mixed and behavioral strategies

- In sum, mixed strategies and behavioral strategies are "equivalent".

Theorem 3.1 (Kuhn)
For finite games with perfect recall, every mixed strategy has a realization equivalent behavioral strategy.

- Any randomization over play can be represented by either mixed or behavioral strategies.
- We can choose the one that is more convenient.


## Nash Equilibrium

Normal form representation of extensive form games

- We have already known the pure strategy space $S_{i}$ for player $i$ in an extensive form game.
- We also know that every strategy profile $s$ leads an outcome $z(s)$.
- Thus, player $i$ 's payoff from this strategy profile is $v_{i}(z(s))$.
- That is, we can always transform an extensive form game into a normal form game: $\left(N,\left\{S_{i}\right\}_{i=1}^{n},\left\{v_{i}(z(\cdot))\right\}_{i=1}^{n}\right)$.
- This is called the normal form representation of an extensive form.


## Nash Equilibrium

Normal form representation of extensive form games

![](https://cdn.mathpix.com/cropped/2024_09_09_605858d45802b61328b8g-170.jpg?height=299&width=659&top_left_y=188&top_left_x=294)

Figure 3.10: The sequential-move Battle of the Sexes game.

- Its normal form representations is

|  | $o o$ | $o f$ | $f o$ | $f f$ |
| :---: | :---: | :---: | :---: | :---: |
| $O$ | 2,1 | 2,1 | 0,0 | 0,0 |
| $F$ | 0,0 | 1,2 | 0,0 | 1,2 |
|  |  |  |  |  |

## Nash Equilibrium

Normal form representation of extensive form games

![](https://cdn.mathpix.com/cropped/2024_09_09_605858d45802b61328b8g-171.jpg?height=245&width=696&top_left_y=199&top_left_x=282)

Figure 3.11: The centipede game

- Its normal form representation is:

|  | $n n$ | $n c$ | $c n$ | $c c$ |
| :--- | :--- | :--- | :--- | :--- |
| $N N$ | 1,1 | 1,1 | 1,1 | 1,1 |
| $N C$ | 1,1 | 1,1 | 1,1 | 1,1 |
| $C N$ | 0,3 | 0,3 | 2,2 | 2,2 |
| $C C$ | 0,3 | 0,3 | 1,4 | 3,3 |
|  |  |  |  |  |

## Nash Equilibrium

Nash equilibrium

- Once we transform an extensive form game into its normal form representation, we can then consider the Nash equilibria of this normal form game.
- This is indeed how we define Nash equilibrium for an extensive form game.

Definition 3.8
A strategy profile $\sigma^{*}$ is a Nash equilibrium of an extensive form game if it is a Nash equilibrium of the normal form representation.

## Nash Equilibrium

## Nash equilibrium

- Normal form representation of the sequential move battle of the sexes:

|  | $o o$ | of | fo | $f f$ |
| :---: | :---: | :---: | :---: | :---: |
| $O$ | 2,1 | 2,1 | 0,0 | 0,0 |
| $F$ | 0,0 | 1,2 | 0,0 | 1,2 |
|  |  |  |  |  |

- Three pure strategy Nash equilibria: $(O, o o),(O, o f)$ and $(F, f f)$.
- Nash equilibrium is about strategy profiles, not about the outcomes. For instance, $(F, o f)$ leads to the same outcome $F f$ as $(F, f f)$, but $(F, o f)$ is not a Nash equilibrium.
- Mixed strategy Nash equilibria?


## Nash Equilibrium

## Nash equilibrium

- Its normal form representation is:

|  | $n n$ | $n c$ | $c n$ | $c c$ |
| :---: | :---: | :---: | :---: | :---: |
| $N N$ | 1,1 | 1,1 | 1,1 | 1,1 |
| $N C$ | 1,1 | 1,1 | 1,1 | 1,1 |
| $C N$ | 0,3 | 0,3 | 2,2 | 2,2 |
| $C C$ | 0,3 | 0,3 | 1,4 | 3,3 |
|  |  |  |  |  |

- Four pure strategy Nash equilibria: $(N N, n n),(N N, n c),(N C, n n)$, $(N c, n c)$.
- Mixed strategy Nash equilibria?


## Sequential Rationality

Motivating examples

![](https://cdn.mathpix.com/cropped/2024_09_09_605858d45802b61328b8g-175.jpg?height=385&width=533&top_left_y=151&top_left_x=396)

Figure 3.12: The chain-store game.

- Nash equilibria: (Stay out, Fight) and (Enter, Accomondate).
- Intuitively, (Stay out, Fight) is not very appealing:
- The entrant stays out because he faces the threat that the incumbent will fight if he enters.
- But is it the incumbent's own interest to fight were the entrant to enter?
- The threat to fight is not credible.


## Sequential Rationality

## Motivating examples

![](https://cdn.mathpix.com/cropped/2024_09_09_605858d45802b61328b8g-176.jpg?height=301&width=659&top_left_y=171&top_left_x=294)

Figure 3.13: The sequential-move Battle of the Sexes game.

- A similar criticism applies to Nash equilibria $(O, o o)$ and $(F, f f)$.
- For example, in $(F, f f)$, player 1 plays $F$ rather than $O$ because he believes that 2 will play $f$ after $O$. But if 1 , for whatever reasons, indeed played $O$, it was not optimal for 2 to play $f$. Again, playing $f$ after $O$ is not credible.
- Similarly, playing $o$ after $F$ is not credible either, which occurs in $(O, o o)$.


## Sequential Rationality

## Motivating example

- The reason that a Nash equilibrium in an extensive form game may involve incredible threats is that its normal form representation, from which we define Nash equilibrium, ignores the dynamic nature of the game.
- As a result, Nash equilibrium only requires that players play optimally at those information sets reached under the strategy profile.
- For example, in the (Stay out, Fight) equilibrium in the chain store game, the incumbent's information set is not reached under this strategy profile. Consequently, Nash equilibrium does not require that the incumbent play Accomondate, which is the optimal action if his information set is reached.


## Sequential Rationality

## Backward induction

## Definition 3.9

Let $\sigma^{*}=\left(\sigma_{1}^{*}, \ldots, \sigma_{n}^{*}\right)$ be a Nash equilibrium profile of behavioral strategies in an extensive form game. We say that an information set is on the equilibrium path if given $\sigma^{*}$ it is reached with positive probability. We say that an information set is off the equilibrium path if given $\sigma^{*}$ it is never reached.

- Nash equilibrium only requires that players play optimally on the equilibrium path.
- Incredible threats then may occur off the equilibrium path.


## Sequential Rationality

## Backward induction

- To avoid those Nash equilibria that involve incredible threats, we should require that players play strategies that are sequentially rational.
- That is, player $i$ 's strategy is a best response to the opponents' at each of his information sets.
- The strategy Accomondate is the only sequentially rational strategy for the incumbent in the chain store game.
- The strategy of is the only sequentially rational strategy for player 2 in the sequential move battle of the sexes game.


## Sequential Rationality

## Backward induction

- For finite games of perfect information, there is an easy and very natural way to find all Nash equilibria that are sequentially rational / do not involve incredible threats.
- This method is called backward induction.
- It starts at the bottom of a game tree.
- It moves backwards $u p$ the tree, keeping at each node exactly one action.
- This action must be sequentially rational, i.e., an optimal choice conditional on
- being at that node, and
- the actions already specified at subsequent nodes.
- A backward induction solution is a strategy profile generated by this procedure.


## Sequential Rationality

## Backward induction

![](https://cdn.mathpix.com/cropped/2024_09_09_605858d45802b61328b8g-181.jpg?height=425&width=364&top_left_y=194&top_left_x=213)
(a) The first step

![](https://cdn.mathpix.com/cropped/2024_09_09_605858d45802b61328b8g-181.jpg?height=432&width=366&top_left_y=194&top_left_x=701)
(b) The second step

Figure 3.14: Backward induction in the chain store game

- The only backward induction solution is $(E, A)$.


## Sequential Rationality

## Backward induction

![](https://cdn.mathpix.com/cropped/2024_09_09_605858d45802b61328b8g-182.jpg?height=269&width=1094&top_left_y=306&top_left_x=101)
(b) The second step

Figure 3.15: Backward induction in the sequential move battle of the sexes

- The only backward induction solution is $(O, o f)$.


## Sequential Rationality

Backward induction

## Theorem 3.2

Every backward induction solution is a Nash equilibrium in pure strategies.

- This result is intuitive, but not straightforward. It is a consequence of Theorem 3.5.


## Theorem 3.3 (Kuhn)

Every finite game of perfect information has a backward induction solution (and hence a Nash equilibrium in pure strategies).

- Chess is a trivial game?

Theorem 3.4
Every finite game of perfect information has a unique backward induction solution if no player is indifferent between any two terminal nodes.

## Sequential Rationality

## Backward induction

![](https://cdn.mathpix.com/cropped/2024_09_09_605858d45802b61328b8g-184.jpg?height=239&width=695&top_left_y=303&top_left_x=281)

Figure 3.16: The centipede game

- Unique backward induction solution ( $N N, n n$ ).


## Sequential Rationality

## Backward induction

- The ultimatum game.
- Two players decide how to split $\$ 100$.
- Player 1 makes a proposal and player 2 decides whether to accept.
- A proposal is of the form $(x, 100-x)$ where $x=0,1, \ldots, 100$.
- If player 2 accepts $(x, 100-x)$, then player 1 gets $x$ and player 2 gets $100-x$.
- If player 2 rejects, both get 0 .
- There are two backward induction solutions:
- Player 1 proposes $(99,1)$; player 2 accepts all proposals but $(100,0)$.
- Player 1 proposes $(100,0)$; player 2 accepts all proposals.


## Subgame Perfect Equilibrium

## Subgames

- How to generalize backward induction so it applies to games of imperfect information?

![](https://cdn.mathpix.com/cropped/2024_09_09_605858d45802b61328b8g-186.jpg?height=419&width=445&top_left_y=292&top_left_x=406)

Figure 3.17: The voluntary battle of the sexes game

- Can not simply do backward induction since player 2's optimal choice depends on player 1's behavior.


## Subgame Perfect Equilibrium

## Subgames

## Definition 3.10

A (proper) subgame $G$ of an extensive form game $\Gamma$ consists of only a single non-terminal node and all its successors in $\Gamma$ with the property that $x \in G$ and $x^{\prime} \in h(x)$ then $x^{\prime} \in G$. The subgame $G$ is itself a game tree with its information sets and payoffs inherited from $\Gamma$.

- We "dissect" an extensive form game into a sequence of smaller games.
- The word "only" is the key in the definition: node $x$ can be the root of a subgame if and only if
- it is a singleton information set; and
- if two nodes are in the same information set and one of them is a successor of $x$, then the other one must be a successor of $x$ too.
- If the root of a subgame is node $x$, we say node $x$ induces a subgame.
- Every subgame is an extensive form in its own right.
- By definition, the game $\Gamma$ itself is a subgame.


## Subgame Perfect Equilibrium

## Subgames

- In a game of perfect information, every non-terminal node induces a subgame.

![](https://cdn.mathpix.com/cropped/2024_09_09_605858d45802b61328b8g-188.jpg?height=383&width=442&top_left_y=371&top_left_x=409)

## Subgame Perfect Equilibrium

## Subgames

![](https://cdn.mathpix.com/cropped/2024_09_09_605858d45802b61328b8g-189.jpg?height=383&width=467&top_left_y=151&top_left_x=398)

Figure 3.18: The voluntary battle of the sexes game

- Consider $x_{3}$ and all its successors, $x_{5}$ and $x_{6}$, i.e., $G=\left\{x_{3}, x_{5}, x_{6}\right\}$.
- They do not form a subgame, because $x_{3}$ and $x_{4}$ are in the same information set, but $x_{4} \notin G$.
- Thus, $x_{3}$ does not induce a subgame. Neither does $x_{4}$.
- A node can induce a subgame only if it is a singleton information set.
- $x_{0}$ induces the original game and $x_{1}$ induces $G=\left\{x_{1}, x_{3}, x_{4}, \ldots, x_{8}\right\}$.


## Subgame Perfect Equilibrium

## Subgames

![](https://cdn.mathpix.com/cropped/2024_09_09_605858d45802b61328b8g-190.jpg?height=397&width=639&top_left_y=229&top_left_x=277)

- $x_{1}$ does not induce a subgame. This is because $x_{4}$ is a successor of $x_{1}$ and $x_{4}$ and $x_{5}$ are in the same information set, but $x_{5}$ is not a successor of $x_{1}$.
- The only subgame of this game is the whole game itself.


## Subgame Perfect Equilibrium

## Subgame perfect equilibrium

- Every subgame itself is an extensive form game.
- Thus, we can talk about Nash equilibrium in every subgame.


## Definition 3.11

Let $\Gamma$ be an $n$-player extensive form game. A behavioral strategy profile $\sigma^{*}=\left(\sigma_{1}^{*}, \ldots, \sigma_{n}^{*}\right)$ is a subgame perfect equilibrium if for every subgame $G$ of $\Gamma$ the restriction of $\sigma^{*}$ to $G$ is a Nash equilibrium in $G$.

- A subgame perfect equilibrium (SPE) is a Nash equilibrium. (Yes?)
- "every subgame $G$ " includes those subgames reached and not reached in equilibrium.
- SPE requires that the strategy profile consists of mutual best responses both on and off the equilibrium path.


## Subgame Perfect Equilibrium

Subgame perfect equilibrium
Reinhard Selten
The Sveriges Riksbank Prize in Economic
Sciences in Memory of Alfred Nobel 1994
"for their pioneering analysis of equilibria in the
theroy of non-cooperative games"
Contribution: Refined the Nash equilibrium
concept for analyzing dynamic strategic
interaction by getting rid of unlikely equilibria. He
also applied the refined concept to analyses of
oligopolistic competition.
Reinhard Selten

The Sveriges Riksbank Prize in Economic Sciences in Memory of Alfred Nobel 1994
"for their pioneering analysis of equilibria in the theroy of non-cooperative games"

Contribution: Refined the Nash equilibrium concept for analyzing dynamic strategic interaction by getting rid of unlikely equilibria. He also applied the refined concept to analyses of oligopolistic competition.

## Subgame Perfect Equilibrium

## Subgame perfect equilibrium

![](https://cdn.mathpix.com/cropped/2024_09_09_605858d45802b61328b8g-193.jpg?height=300&width=652&top_left_y=152&top_left_x=304)

Figure 3.19: The sequential-move Battle of the Sexes game.

- Recall three Nash: $(O, o o),(F, f f),(O, o f)$.
- $(O, o o)$ is not subgame perfect: it is not a Nash equilibrium when restricted to the subgame following player 1 choosing $F$.
- $(F, f f)$ is not subgame perfect neither: it is not a Nash equilibrium when restricted to the subgame following player 1 choosing $O$.
- $(O$, of $)$ is the only SPE, which is also the unique backward induction solution.
$\rightarrow$ Any mixed strategy SPE?


## Subgame Perfect Equilibrium

## Subgame perfect equilibrium

- Restrict attention to finite game of perfect information for now.
- What is the difference between backward induction solution and SPE?


## Theorem 3.5

For finite game of perfect information, the set of pure strategy subgame perfect equilibria coincides with the set of backward induction solutions.

- The algorithm of backward induction requires that at each node, the player's action at this node be optimal, given the opponents' and this player's own future play.
- A SPE requires that at each node, the player's strategy in this subgame be optimal given the opponents' future play.
- Thus, a SPE must be a backward induction solution.


## Subgame Perfect Equilibrium

Subgame perfect equilibrium

- But why is a backward induction solution a SPE?


## Definition 3.12

Consider strategy $s_{i}$ for player $i$. We call a strategy $s_{i}^{\prime}$ is a one-shot deviation of $s_{i}$, if $s_{i}^{\prime}$ differs from $s_{i}$ at one and only one node in $H_{i}$ : there exists a unique $h_{i} \in H_{i}$ such that $s_{i}^{\prime}\left(h_{i}\right) \neq s_{i}\left(h_{i}\right)$ and $s_{i}^{\prime}\left(h_{i}^{\prime}\right)=s_{i}\left(h_{i}^{\prime}\right)$ for all $h_{i}^{\prime} \neq h_{i}$.

- $s_{i}^{\prime}$ is a one-shot deviation of $s_{i}$ if $s_{i}^{\prime}$ deviates from $s_{i}^{\prime}$ only once.
- Other names: one-step deviation / one-stage deviation.


## Subgame Perfect Equilibrium

Subgame perfect equilibrium

## Definition 3.13

Consider a strategy profile $s$. We say a strategy $s_{i}^{\prime}$ is a profitable one-shot deviation if (i) $s_{i}^{\prime}$ is a one-shot deviation of $s_{i}$ at node $h_{i}$, and (ii) $s_{i}^{\prime}$ is a profitable deviation from $s_{i}$ in the subgame induced by $h_{i}$, given $s_{-i}$.

- The following theorem is usually referred to as the one-shot deviation principle for finite game of perfect information.


## Theorem 3.6

Consider a finite game of perfect information. The strategy profile $s$ is a subgame perfect equilibrium if and only if no one has profitable one-shot deviation.

- Theorem $3.6 \Longrightarrow$ Theorem $3.5 \Longrightarrow$ Theorem 3.2 .


## Subgame Perfect Equilibrium

Subgame perfect equilibrium

- In fact, the one-shot deviation principle holds for many other classes of extensive form games.
- In particular, its variations holds in all games we consider in this course.


## Subgame Perfect Equilibrium

## Subgame perfect equilibrium

![](https://cdn.mathpix.com/cropped/2024_09_09_605858d45802b61328b8g-198.jpg?height=419&width=451&top_left_y=236&top_left_x=409)

Figure 3.20: The voluntary battle of the sexes

## Subgame Perfect Equilibrium

## Subgame perfect equilibrium

- Its normal form representation:

|  | $o$ | $f$ |
| :---: | :---: | :---: |
| $Y O$ | 2,1 | 0,0 |
| $Y F$ | 0,0 | 1,2 |
| $N O$ | $1.5,1.5$ | $1.5,1.5$ |
| $N F$ | $1.5,1.5$ | $1.5,1.5$ |
|  |  |  |

- Three pure strategy Nash: $(Y O, o),(N O, f)$ and $(N F, f)$.
- $(Y O, o)$ and $(N F, f)$ are SPE's, while $(N O, f)$ is not.
- Many mixed strategy Nash: $(\alpha \circ N O+(1-\alpha) \circ N F, \beta \circ o+(1-\beta) \circ f)$ for $\alpha \in[0,1]$ and $\beta \in\left[0, \frac{3}{4}\right]$.
- The mixed strategy $\alpha \circ N O+(1-\alpha) \circ N F$ is equivalent to the behavioral strategy that player 1 plays $N$ for sure at his first information set and then mixes between $O$ and $F$ with probability $\alpha$ and $1-\alpha$ at his second information set.
- Only when $\alpha=\frac{2}{3}$ and $\beta=\frac{1}{3}$, it is a SPE.


## Subgame Perfect Equilibrium

## Subgame perfect equilibrium

- One-shot deviation principle also holds for this game.
- Applying one-shot deviation principle, we can find out the SPE's similarly as backward induction.
- In the subgame following player 1 choosing $Y$, there are three Nash: $(O, o),(F, f)$ and $\left(\frac{2}{3} \circ O+\frac{1}{3} \circ F, \frac{1}{3} \circ o+\frac{2}{3} \circ f\right)$.
- Consider any behavioral strategy profile $\sigma^{*}$.
- If it is a SPE, it must play one of the three equilibria in this subgame.
- If $(O, o)$ is played, then it is optimal for player 1 to choose $Y$ in the first information set. This leads to $(Y O, o)$.
- If $(F, f)$ or $\left(\frac{2}{3} \circ O+\frac{1}{3} \circ F, \frac{1}{3} \circ o+\frac{2}{3} \circ f\right)$ is played, then it is optimal for player 1 to choose $N$ in the first information set. This leads to either $(N F, f)$ or $\left(\frac{2}{3} \circ N O+\frac{1}{3} \circ N F, \frac{1}{3} \circ o+\frac{2}{3} \circ f\right)$.
- Note that these three strategy profiles are just the SPE's we found earlier.


## SPE Examples

## Stackelberg competition

- Stackelberg game: sequential move variation on the Cournot duopoly.
- Demand $P=100-Q$.
- Firm 1 chooses $q_{1} \geq 0$ first.
- Firm 2 then chooses $q_{2} \geq 0$ after observing firm 1's choice.
- Market supply $Q=q_{1}+q_{2}$.
- Constant marginal cost $c_{i}\left(q_{i}\right)=10 q_{i}$.
- Payoff $\left(100-q_{1}-q_{2}\right) q_{i}-10 q_{i}$.
- Infinite game of perfect information.


## SPE Examples

## Stackelberg competition

![](https://cdn.mathpix.com/cropped/2024_09_09_605858d45802b61328b8g-202.jpg?height=623&width=424&top_left_y=159&top_left_x=436)

Figure 3.21: Stackelberg competition

## SPE Examples

## Stackelberg competition

- We restrict attention to pure strategies.
- Firm 1 only has one information set.
- Thus, a strategy for firm 1 is simply a quantity $q_{1} \in \mathbb{R}_{+}$.
- Firm 2 has infinitely many information sets; every action $q_{1}$ of firm 1 leads to an information set for firm 2.
- Thus, a strategy for firm 2 is a function $q_{2}: \mathbb{R}_{+} \rightarrow \mathbb{R}_{+}$, where $q_{2}\left(q_{1}\right)$ means firm 2's quantity choice if firm 1 chooses $q_{1}$.


## SPE Examples

## Stackelberg competition

- Since it is a game of perfect information, every non-terminal node induces a subgame.
- There are infinitely many subgames.
- We can also do backward induction in this game to find out SPE.
- In the subgame after firm 1 choosing $q_{1} \geq 0$, we know firm 2 's optimal choice $q_{2}^{*}\left(q_{1}\right)$ solves

$$
\max _{q_{2} \geq 0}\left(100-q_{1}-q_{2}\right) q_{2}-10 q_{2}
$$

and thus

$$
q_{2}^{*}\left(q_{1}\right)=\frac{90-q_{1}}{2}
$$

- Here, we assume $q_{1} \leq 90$.


## SPE Examples

## Stackelberg competition

- Inducting backwardly, at the initial node, firm 1's problem is

$$
\max _{q_{1} \geq 0}\left(100-q_{1}-q_{2}^{*}\left(q_{1}\right)\right) q_{1}-10 q_{1} .(\text { Yes? })
$$

- Plugging in the expression for $q_{2}^{*}$, we have

$$
\max _{q_{1} \geq 0}\left(100-q_{1}-\frac{90-q_{1}}{2}\right) q_{1}-10 q_{1}
$$

- FOC yields

$$
q_{1}^{*}=45 .
$$

- Then, firm 2's equilibrium quantity choice is

$$
q_{2}^{*}\left(q_{1}^{*}\right)=22.5
$$

- Profits are $\pi_{1}^{*}=1012.5$ and $\pi_{2}^{*}=506.25$.


## SPE Examples

## Stackelberg competition

- Cournot (simultaneous move) equilibrium $q_{1}^{*}=q_{2}^{*}=30$ with profits $\pi_{1}^{*}=\pi_{2}^{*}=900$.
- When firm 1 moves first, it earns more.
- This is usually called the first mover advantage.

Why?

## SPE Examples

## Stackelberg competition

- Nash equilibria?
- Consider $\hat{q}_{1} \geq 0$ such that

$$
\left(100-\hat{q}_{1}-q_{2}^{*}\left(\hat{q}_{1}\right)\right) \hat{q}_{1}-10 \hat{q}_{1} \geq 0
$$

- Suppose

$$
\hat{q}_{2}\left(q_{1}\right)= \begin{cases}q_{2}^{*}\left(q_{1}\right), & \text { if } q_{1}=\hat{q}_{1} \\ 90, & \text { if } q_{1} \neq \hat{q}_{1}\end{cases}
$$

- Then the strategy profile $\left(\hat{q}_{1}, \hat{q}_{2}(\cdot)\right)$ is a Nash equilbrium. (Yes?)
- Incredible threat. (Yes?)


## SPE Examples

## Mutually assured destruction

- Cuba missile crisis of 1962.
- The US (player 1) discovered Soviet (player 2) nuclear missiles in Cuba.
- Player 1 decides whether to ignore the incident $(I)$, resulting in payoffs $(0,0)$, or escalate the situation $(E)$.
- Following escalation by player 1, player 2 can back down $(B)$, causing it to lose face and resulting in payoffs of $(10,-10)$, or it can choose to proceed to a nuclear confrontation $(N)$.
- Upon choice of $N$, the players play a simultaneous move game in which they can either retreat ( $R$ for player 1 and $r$ for player 2 ) or choose Doomsday ( $D$ for player 1 and $d$ for player 2 ), in which the world is all but destroyed.
- If both retreat then they suffer a small loss due to the mobilization process and payoffs are $(-5,-5)$, while if either party chooses Doomsday then the world destructs and payoffs are $(-100,-100)$.


## SPE Examples

Mutually assured destruction

![](https://cdn.mathpix.com/cropped/2024_09_09_605858d45802b61328b8g-209.jpg?height=520&width=508&top_left_y=196&top_left_x=384)

Figure 3.22: Mutually assured destruction

## SPE Examples

## Mutually assured destruction

- Pure strategy SPE?
- One-shot deviation principle.
- Consider the subgame after player 1 choosing $E$ and player 2 choosing $N$.
- There are two Nash: $(R, r)$ and $(D, d)$.
- If $\sigma^{*}$ is a SPE, it must play either $(R, r)$ or $(D, d)$ in this subgame.
- If it is $(R, r)$,
- then player 2's optimal choice at its first information set is $N$;
- player 1's optimal choice at its first information is $I$.
- Thus, a SPE $(I R, N r)$.
- If it is $(D, d)$,
- then player 2's optimal choice at its first information set is $B$;
- player 1's optimal choice at its first information set is $E$.
- Thus, another SPE $(E D, B d)$.


## Topics I: Repeated Games

Motivating examples

- Consider the partnership game (the prisoners' dilemma):

|  | $E$ | $S$ |
| :---: | :---: | :---: |
| $E$ | 2,2 | $-1,3$ |
| $S$ | $3,-1$ | 0,0 |
|  |  |  |

Figure 3.23: The partnership game

- $E$ stands for effort; $S$ stands for shirking.
- Unique Nash equilibrium: $(S, S)$.
- Cooperation can not arise in equilibrium.
- Why can we observe cooperation behavior in reality?


## Topics I: Repeated Games

## Motivating examples

- Consider the Cournot duopoly: $P(Q)=\max \{100-Q, 0\}, c_{1}=c_{2}=10$.
- Instead of operating independently, imagine the firms choose quantities jointly so as to maximize the industry profits and then divide up the profits among them. In other words, they form a cartel and collude:

$$
\max _{Q} P(Q) Q-10 Q
$$

- $Q^{*}=45$.
- If each firm produces 22.5 , each earns profits $45 \times 22.5=1012.5$.
- But we know this is not a Nash equilibrium. In the unique Nash equilibrium, $q_{1}^{*}=q_{2}^{*}=30$ and equilibrium profits are $30 * 30=900$ for each firm.
- Forming a cartel can make both firms strictly better and we do observe collusion behavior in reality.


## Topics I: Repeated Games

## Motivating examples

- One possible reason that what we observe in reality is not equilibrium behavior in the previous two examples is that the simultaneous move game only captures one-shot interaction.
- Intuitively, agents in reality do not interact only once. Instead, they interact through a long-run relationship.
- In such a relationship, agents not only care about their today's payoffs but also their future payoffs.
- Moreover, agents can condition their behavior on what has happened in the past.
- Thus, it is intuitive to expect different behavior than that predicted by the one-shot interaction.
- Repeated games provide us a useful tool to analyze agents' long-run interactions.


## Topics I: Repeated Games

## Repeated games

- Consider a normal form game $G$.
- Suppose this game is repeatedly played for $T$ times.
- In period $t=1$, players simultaneously choose actions in $G$.
- In period $t=2$, they observe all players' choices in period $t=1$ and then simultaneously choose actions in $G$ again.
- In period $t=3$, they again observe all players' choices in period $t=2$, (they also know the choices in period $t=1$ by perfect recall), and then simultaneously choose actions again.
- This repeated play lasts for $T$ periods. $T$ can be either finite or infinite in which case the repeated play lasts forever.
- This dynamic game is called a repeated game (payoffs to be specified later). The game $G$ is called the stage game of this repeated game.
- If $T$ is finite, it is a finitely repeated game. If $T=\infty$, it is an infinitely repeated game.


## Topics I: Repeated Games

Repeated games

![](https://cdn.mathpix.com/cropped/2024_09_09_605858d45802b61328b8g-215.jpg?height=456&width=1190&top_left_y=177&top_left_x=24)

Figure 3.24: The game tree for the twice repeated partnership game

- Note that every repeated game is an extensive form game of imperfect information.


## Topics I: Repeated Games

## Repeated games

- In each round, players obtain payoffs from the play of the stage game.
- Player $i$ 's total payoff from the repeated game is the discounted sum of his stage game payoffs.
- Suppose $T$ is finite. Let $\delta \in(0,1]$ be the discount factor. If player $i$ obtains payoffs $v_{i}^{1}, \ldots, v_{i}^{T}$ in each period throughout the play, his discounted sum is

$$
v_{i} \equiv v_{i}^{1}+\delta v_{i}^{2}+\ldots+\delta^{T-1} v_{i}^{T}=\sum_{t=1}^{T} \delta^{t-1} v_{i}^{t}
$$

- Suppose $T=\infty$. Let $\delta \in(0,1)$ be the discount factor. If player $i$ obtains payoffs $v_{i}^{1}, v_{i}^{2}, v_{i}^{3}, \ldots$ in each period throughout the play, his discounted sum is

$$
v_{i} \equiv v_{i}^{1}+\delta v_{i}^{2}+\delta^{2} v_{i}^{3}+\ldots=\sum_{t=1}^{\infty} \delta^{t-1} v_{i}^{t}
$$

We require $\delta<1$ in this case; otherwise the infinite sum may not be well defined.

## Topics I: Repeated Games

Repeated games

![](https://cdn.mathpix.com/cropped/2024_09_09_605858d45802b61328b8g-217.jpg?height=528&width=1198&top_left_y=178&top_left_x=23)

Figure 3.25: The twice repeated partnership game with some payoffs

# Topics I: Repeated Games 

Repeated games

- Two usual interpretations of $\delta$ :
- it measures how impatient the players are (this is why we call it the discount factor).
- it measures the probability that the players will meet and interact tomorrow.


# Topics I: Repeated Games 

Repeated games

- How about strategies?
- Consider the twice repeated partnership game.
- Each player has 5 information sets.
- Clearly, a strategy for player $i$ should specify an action for each of these 5 information sets.
- Is there a convenient way to express each strategy?


## Topics I: Repeated Games

## Repeated games

- Let $A=A_{1} \times \ldots \times A_{n}$ denote the set of all action profiles in the stage game.
- Suppose the players have finished the play in the first period and are at the beginning of period $t=2$.
- Note that an action profile $a \in A$ can fully describe what has happened in the first period.
- For example, in the twice repeated partnership game, the action profile $E E$ can be used to describe that both players have chosen $E$ in the first period.
- Thus, every action profile $a \in A$ can be considered as a possible history up to period $t=1$.
- We can define $H_{1}=A$ to denote the set of all possible histories up to period $t=1$.


## Topics I: Repeated Games

## Repeated games

- More generally, for $t \geq 1$, we can define $H_{t}=A^{t}$ be the set of all possible histories up to period $t$.
- Every element $h_{t} \in H_{t}$ fully describes what has happened in the first $t$ periods, and vice versa.
- For example, consider the $T \geq 5$ times repeated partnership game.
- The history ( $E E, S S, S S, S S, S S$ ) means that both players played $E$ in the first period, but then they played $S$ in periods 2 to 5 .
- We also use $\emptyset$ to denote the "empty" history (initial node), which means "nothing has happened". Let $H_{0}=\{\emptyset\}$.


## Topics I: Repeated Games

## Repeated games

- The nice property of histories is that every player's every information set can be uniquely identified by a history.
- Thus, a strategy $s_{i}$ for player $i$ in the $T$ times repeated game is simply a mapping

$$
s_{i}: \bigcup_{t=0}^{T-1} H_{t} \rightarrow A_{i}
$$

- If $T$ is finite, we can explicitly write a strategy $s_{i}$ as $T$ mappings $\left(s_{i}^{1}, s_{i}^{2}, \ldots, s_{i}^{T}\right)$ such that $s_{i}^{t}$ is a mapping $s_{i}^{t}: H_{t-1} \rightarrow A_{i}$ specifying player $i$ 's behavior in period $t$.
- It has a very natural interpretation: in period $t=1, \ldots, T$, if $h \in H_{t-1}$ has happened in the past $t-1$ periods, player $i$ is going to choose $s_{i}^{t}(h)$ in period $t$.
- If $T=\infty$, then a strategy $s_{i}$ is in fact an infinite sequence of mappings $\left(s_{i}^{1}, s_{i}^{2}, \ldots\right)$ such that $s_{i}^{t}$ is a mapping $s_{i}^{t}: H_{t-1} \rightarrow A_{i}$ specifying player $i$ 's behavior in period $t$.


## Topics I: Repeated Games

## Repeated games

- Consider the twice repeated partnership game.
- Consider the strategy

$$
s_{1}^{1}=E \text { and } s_{1}^{2}(a)= \begin{cases}E, & \text { if } a=E E \\ S, & \text { if } a \neq E E\end{cases}
$$

- In words,
- player 1 plays $E$ in the first period;
- he continues to player $E$ in the first period if both players play $E$ in the first period;
- otherwise, he plays $S$ in the second period.
- Consider another strategy: player 1 plays $S$ in the first period; in the second period, he imitates player 2's behavior in the first period. How to write down this strategy?


## Topics I: Repeated Games

## Repeated games

- Consider the infinitely repeated partnership game.
- Consider the strategy $s_{1}$ :

$$
s_{1}^{1}=E \text { and for all } t \geq 2, s_{1}^{t}(h)= \begin{cases}E, & \text { if } h=(E E, \ldots, E E) \in H_{t-1} \\ S, & \text { otherwise }\end{cases}
$$

- In words,
- player 1 plays $E$ in the first period;
- in any period $t \geq 2$, if both players have played $E$ in all previous periods, then he plays $E$ again;
- otherwise, he plays $S$.
- Cooperation if they have cooperated in the past; otherwise, never cooperate in the future.
- Consider another strategy $s_{1}$ : player 1 plays $E$ in the first period; in any period $t \geq 2$, if player 2 has played $S$ in the past for at least twice, he switches to $S$; otherwise, he continues to play $E$. (Forgiving once).


## Topics I: Repeated Games

## Finitely repeated games

- We first consider finitely repeated games.
- We focus on SPE's.
- Every non-terminal history $h \in H_{t}$ for $t=0, \ldots, T-1$ induces a subgame.
- One-shot deviation principle holds for these games.


## Topics I: Repeated Games

## Finitely repeated games

- Consider the twice repeated partnership game.
- If $s$ is a SPE, what would it play in the second period after history $h \in H_{1}=\{E E, E S, S E, S S\} ?$
- The subgame after $h$ has the following matrix representation:

\$\$

\$\$
- Observe that when player 1 compares his payoff from $E$ and $S$ (given player 2's action in this subgame), player 1 only needs to compare his payoff from the second period. The same observation also applies to player 2 .

## Topics I: Repeated Games

## Finitely repeated games

- Therefore, the subgame after $h$ is equivalent to the following game

|  | $E$ | $S$ |
| :---: | :---: | :---: |
| $E$ | 2,2 | $-1,3$ |
| $S$ | $3,-1$ | 0,0 |
|  |  |  |

which is just the partnership game (the stage game) itself.

- We know there is a unique Nash equilibrium $S S$ in this game.
- Since $s$ is a SPE, we know $s_{1}^{2}(h)=s_{2}^{2}(h)=S$ for all $h \in H_{1}$.


## Topics I: Repeated Games

## Finitely repeated games

- We now move on to the first period play. By the one-shot deviation principle, we only need to focus on their play in the first period, given their behavior in the second period which we have known.
- They again face a simultaneously move game whose matrix is

\$\$

$$
- Observe again that this game is equivalent to
$$

\$\$
which is again the stage game itself.
- This is true because their second period play (which we have figured out) is independent of their first period play, i.e., $s(h)=S S$ for all $h \in H_{1}$.
- Since $s$ is a SPE, we know $s_{1}^{1}=s_{2}^{1}=S$.

## Topics I: Repeated Games

## Finitely repeated games

- Therefore, there is a unique SPE in the twice repeated partnership game. In this SPE, players play $S$ after every history. The associated outcome path is $(S S, S S)$.
- It is disappointing! Even if the game is repeatedly played, the only equilibrium is simply a repetition of the one-shot game.
- How about $T \geq 3$ ?


## Topics I: Repeated Games

## Finitely repeated games

- In the previous example, we show two results:
- repeated play of a stage Nash equilibrium after every history is a SPE;
- in this particular example, it is the unique SPE.
- In fact, these two results can be generalized.


## Theorem 3.7

Consider a finitely repeated game. Suppose action profile $a^{*}=\left(a_{1}^{*}, \ldots, a_{n}^{*}\right)$ is a Nash equilibrium of the stage game. Then the strategy profile $s$ which plays $a^{*}$ after every history is a subgame perfect equilibrium of the repeated game, for any $\delta \in(0,1]$. If, in addition, $a^{*}$ is the unique Nash equilibrium in the stage game, then this strategy profile is the unique SPE in the repeated game.

## Topics I: Repeated Games

## Finitely repeated games

- The first part of Theorem 3.7 is encouraging.
- It states the existence of SPE in finitely repeated games.
- The second part is discouraging.
- We can expect nothing but the repetition of the stage Nash in any finitely repeated games if the stage game has only one Nash equilibrium.
- Even if $T$ is very large, cooperation can not arise in equilibrium in the repeated partnership game.


## Topics I: Repeated Games

## Finitely repeated games

## Proof of Theorem 3.7.

Consider the strategy profile $s$ which plays $a^{*}$ after every history. We can directly verify that $s$ is a SPE without invoking the one-shot deviation principle.

Consider any history $h=\left(\tilde{a}^{1}, \ldots, \tilde{a}^{t-1}\right)$ at the beginning of period $t=1, \ldots T-1$. In the subgame following $h$, given the opponents' strategy, player $i$ 's payoff from any strategy can be written as

$$
\sum_{\tau=1}^{t-1} \delta^{\tau-1} v_{i}\left(\tilde{a}^{\tau}\right)+\sum_{\tau=t}^{T} \delta^{\tau-1} v_{i}\left(a_{i}^{\tau}, a_{-i}^{*}\right)
$$

Because $a_{i}^{*}$ maximizes player $i$ 's stage game payoff if the opponents play $a_{-i}^{*}$, it is obvious that playing $s_{i}$ is optimal for player $i$ in this subgame.

This proves that $s$ is a SPE.

## Topics I: Repeated Games

## Finitely repeated games

## Proof of Theorem 3.7.

Now, assume $a$ is the unique Nash equilibrium of the stage game. We show that $s$ is the unique SPE of the repeated game.

Consider any SPE $\tilde{s}$. Consider any history $h=\left(\tilde{a}^{1}, \ldots, \tilde{a}^{T-1}\right)$ at the beginning of the last period. The subgame following $h$ is a simultaneous move game with strategy space $A_{i}$ for player $i$ and payoff function $\hat{v}_{i}(a)=\sum_{\tau=1}^{T-1} \delta^{\tau-1} v_{i}\left(\tilde{a}^{\tau}\right)+\delta^{T-1} v_{i}(a)$. Because $\tilde{s}$ is a SPE, it must play a Nash equilibrium in this subgame. Because this subgame is equivalent to the stage game itself, $\tilde{s}$ in this subgame must play $a^{*}$, which is the unique stage Nash equilibrium. Thus, we have shown that $\tilde{s}_{i}^{T}(h)=a_{i}^{*}$ for all $i$ and $h \in H_{T-1}$.

## Topics I: Repeated Games

## Finitely repeated games

## Proof of Theorem 3.7.

Suppose we have shown that $\tilde{s}$ play $a^{*}$ in periods
$t=k, k+1, \ldots, T-1, T$ after any history. We now show that $\tilde{s}$ must also play $a^{*}$ in period $t=k-1$ after any history. Pick any $h=\left(\tilde{a}^{1}, \ldots, \tilde{a}^{t-1}\right) \in H_{t-1}$. Because $\tilde{s}$ is a SPE, no one has a profitable deviation after $h$. This means that for all $i, \tilde{s}_{i}^{t}(h)$ solves

$$
\max _{a_{i} \in A_{i}} \sum_{\tau=1}^{t-1} \delta^{\tau-1} v_{i}\left(\tilde{a}^{\tau}\right)+\delta^{t-1} v_{i}\left(a_{i}, \tilde{s}_{-i}^{t}(h)\right)+\sum_{\tau=t+1}^{T} \delta^{\tau-1} v_{i}\left(a^{*}\right)
$$

Equivalently, $\tilde{s}_{i}^{t}(h)$ solves

$$
\max _{a_{i} \in A_{i}} v_{i}\left(a_{i}, \tilde{s}_{-i}^{t}(h)\right)
$$

which implies that $\tilde{s}^{t}(h)$ is a Nash equilibrium of the stage game.
Therefore, $\tilde{s}^{t}(h)=a^{*}$ since $a^{*}$ is the unique stage Nash equilibrium.

## Topics I: Repeated Games

## Finitely repeated games

- In the previous proof, we proved a result which is worth stating of itself.


## Lemma 3.1

Suppose $s$ is a subgame perfect equilibrium of a finitely repeated game. In the last period, after any history, s must play a stage Nash equilibrium.

- Note that after different histories, different Nash equilibria can be played.


## Topics I: Repeated Games

## Finitely repeated games

|  | $E$ | $S$ | $P$ |
| :---: | :---: | :---: | :---: |
| $E$ | 2,2 | $-1,3$ | $-3,-3$ |
| $S$ | $3,-1$ | 0,0 | $-3,-3$ |
| $P$ | $-3,-3$ | $-3,-3$ | $-2,-2$ |
|  |  |  |  |

Figure 3.26: The augmented partnership game

- There are two stage Nash equilibria: $S S$ and $P P$.
- Can $E E$ be played in the first period in a SPE? ( $E E$ can not be played in the second period after any history. Yes?)


## Topics I: Repeated Games

## Finitely repeated games

- Consider the following strategy profile:

$$
s_{i}^{1}=E \text { and } s_{i}^{2}(h)= \begin{cases}S, & \text { if } h=E E \\ P, & \text { if } h \neq E E\end{cases}
$$

- In words,
- both players play $E$ in the first period;
- in the second period, if both players have played $E$ in the first period, they play $S$;
- if at least one player played an action different from $E$ in the first period, they play $P$.


## Topics I: Repeated Games

## Finitely repeated games

- Is this strategy profile a SPE?
- Their play in the second period is consistent with a SPE, by construction. (Yes?)
- So we only need to worry about their play in the first period.
- Consider player 1. Given player 2's strategy and player 1's own strategy in the second period, player 1's payoff from choosing $E$ in the first period is

$$
v_{1}(E E)+\delta v_{1}(S S)=2
$$

that from choosing $S$ is

$$
v_{1}(S E)+\delta v_{1}(P P)=3-2 \delta
$$

and that from choosing $P$ is

$$
v_{1}(P E)+\delta v_{1}(P P)=-3-2 \delta
$$

## Topics I: Repeated Games

## Finitely repeated games

- As long as $2 \geq 3-2 \delta$, or equivalently $\delta \geq 1 / 2$, choosing $E$ in the first period is optimal.
- By symmetry, it is also optimal for player 2 to play $E$ in the first period provided $\delta \geq 1 / 2$.
- Therefore, when $\delta \geq 1 / 2$, the above strategy profile is indeed a SPE!
- Cooperation EE, which is non stage equilibrium behavior, appears in a SPE.


## Topics I: Repeated Games

## Finitely repeated games

- There are some general messages we can learn from the above example.
- First, when the stage game has more than one Nash equilibrium, it is possible that players play non stage Nash equilibrium in early periods of a finitely repeated game in a SPE. In other words, it is possible that players are willing to sacrifice their myopic interests in order to obtain higher long-run payoffs.


## Topics I: Repeated Games

## Finitely repeated games

- Second, the key mechanism is the conditional play of different Nash equilibria in the second period, which promise different continuation payoffs to the players. This serves as the "stick and carrot" policy:
- $S S$ is the "carrot": if no player has deviated in the first period, they play SS then and obtain 0 in the second period;
- $P P$ is the "stick": if someone has deviated in the first period, they punish each other by playing $P$ and obtain only $-2<0$ in the second period. ( $P$ for punishment)
It is this "stick and carrot" behavior that gives players the intertemporal incentive to choosing $E$ in the first period. (Their myopic best response in the first period is $S$.)


## Topics I: Repeated Games

## Finitely repeated games

- Third, for this mechanism to work, we require that the discount factor be sufficiently large, e.g., $\delta \geq 1 / 2$ in the above example. This is very intuitive since $\delta$ measures how much the players care about their future payoffs. The larger $\delta$ is, the more the players care about their future payoffs. If $\delta$ is too small, it is not possible to induce a player to play a non myopic best response by promising him a high payoff in the future, since he does not care about his future payoff.


## Topics I: Repeated Games

Infinitely repeated games

- We now move on to the infinitely repeated games.
- We have defined previously players' payoffs from the repeated game to be the discounted sum of stage game payoffs.
- When infinitely repeated game is considered, it is usually conventional to use the average discounted sum of stage game payoffs as players' payoffs:

$$
v_{i} \equiv(1-\delta) \sum_{t=1}^{\infty} \delta^{t-1} v_{i}^{t}
$$

- It is simply a normalization of the discounted sum.
- For example, if the same action profile $a$ is infinitely repeatedly played, then player $i$ 's payoff is

$$
(1-\delta) \sum_{t=1}^{\infty} \delta^{t-1} v_{i}(a)=v_{i}(a)
$$

## Topics I: Repeated Games

Infinitely repeated games

- We can not do backward induction now since there is no terminal node.
- But one-shot deviation principle still applies.
- However, because there are infinitely many subgames, it seems very difficult to check whether a given strategy profile is a SPE even if we apply the one-shot deviation principle.


## Topics I: Repeated Games

Infinitely repeated games

- Consider an history $h=\left(a^{1}, \ldots, a^{t}\right)$ and the subgame following it.
- If some strategy is played in this subgame which leads to the outcome path $\left(a^{t+1}, a^{t+2}, \ldots\right)$, the player $i$ 's payoff is

$$
\begin{aligned}
v_{i} & =(1-\delta) \sum_{\tau=1}^{\infty} \delta^{\tau-1} v_{i}\left(a^{\tau}\right) \\
& =(1-\delta) \sum_{\tau=1}^{t} \delta^{\tau-1} v_{i}\left(a^{\tau}\right)+(1-\delta) \sum_{\tau=t+1}^{\infty} \delta^{\tau-1} v_{i}\left(a^{\tau}\right) \\
& =(1-\delta) \sum_{\tau=1}^{t} \delta^{\tau-1} v_{i}\left(a^{\tau}\right)+\delta^{t}(1-\delta) \sum_{\tau=1}^{\infty} \delta^{\tau-1} v_{i}\left(a^{\tau+t}\right)
\end{aligned}
$$

- Thus, this subgame is in fact equivalent to the original repeated game! (This is the key difference between the finitely and infinitely repeated games.)


## Topics I: Repeated Games

Infinitely repeated games

- Consider a strategy profile $s$.
- Given any history $h, s$ specifies players' play in the subgame following $h$.
- We call this part of strategy as the continuation play of $s$ in the subgame following $h$.
- Note that this continuation play can also be considered as a strategy of the original repeated game.
- We therefore have


## Lemma 3.2

Consider a strategy profile $s$ in an infinitely repeated game. $s$ is a subgame perfect equilibrium if and only if the continuation play of $s$ after any history $h$ is a Nash equilibrium of the original repeated game.

## Topics I: Repeated Games

Infinitely repeated games

- The following theorem is analogous to Theorem 3.7.

Theorem 3.8
Consider an infinitely repeated game. Suppose action profile $a=\left(a_{1}, \ldots, a_{n}\right)$ is a Nash equilibrium of the stage game. Then the strategy profile $s$ which plays $a$ after every history is a subgame perfect equilibrium of the repeated game, for any $\delta \in(0,1)$.

## Proof.

By Lemma 3.2, we only need to show that this strategy profile is a Nash equilibrium of the repeated game. Given $s_{-i}$, which always plays $a_{-i}$ after any history, always playing $a_{i}$ is clearly optimal for player $i$ since it maximizes player $i$ 's stage payoff in every period. Note also that this argument is independent of $\delta$.

## Topics I: Repeated Games

Infinitely repeated games

- Other SPE?
- Consider the partnership game.
- Consider the following strategy profile:

$$
\forall t \geq 1, s_{i}^{t}(h)= \begin{cases}E, & \text { if } h=\emptyset \text { or } h=(E E, \ldots, E E) \in H_{t-1} \\ S, & \text { otherwise }\end{cases}
$$

- In words,
- players play $E$ in the first period;
- in any period after any history, if no one has deviated from $E$, they continue to play $E$;
- otherwise, they play $S$.
- Cooperating if they all have cooperated in the past.


## Topics I: Repeated Games

Infinitely repeated games

- Consider history $h=\emptyset$ (or equivalently period $t=1$ ).
- Given player 2's strategy and player 1's own strategy from period $t=2$ on, player 1's payoff from playing $E$ in this period is

$$
v_{i}(E E)=2(\text { Yes? })
$$

and that from playing $S$ is

$$
(1-\delta) v_{i}(S E)+\delta v_{i}(S S)=3(1-\delta)(\mathrm{Yes} ?)
$$

- Thus, player 1 does not have a profitable one-shot deviation in period $t=1$ if $2 \geq 3(1-\delta)$, or equivalently $\delta \geq 1 / 3$.


## Topics I: Repeated Games

Infinitely repeated games

- Now, consider any history of the form $h=(E E, \ldots, E E)$.
- Because the continuation play of $s$ in the subgame following $h$ is identical to $s$, we have already known that no one has a profitable one-shot deviation at $h$ provided $\delta \geq 1 / 3$.
- Finally, consider any history $h$ in which $S$ is played at least once.
- Because the continuation play of $s$ in the subgame following $h$ is simply the repeated play of the stage Nash equilibrium after all continuation histories, we know it is a SPE in the subgame for all $\delta$. Thus no one has profitable one-shot deviation at $h$ for all $\delta$.
- In sum, when $\delta \geq 1 / 3$, no one has profitable one-shot deviation after every history.
- Therefore, $s$ is a SPE provided $\delta \geq 1 / 3$.
- The same idea of "stick and carrot" behavior.


## Topics I: Repeated Games

Infinitely repeated games

- Even if the stage game has a unique Nash equilibrium, there is a SPE whose outcome path involves repeated play of non stage Nash equilibrium, provided $\delta$ is large enough.
- This kind of strategy is usually referred to as a grim trigger strategy: deviating from $E$ is a trigger that causes the players to revert to a bad stage Nash equilibrium, resulting in a very grim future.
- This kind of strategy profile is widely used to support non stage Nash equilibrium behavior as a SPE in the infinitely repeated game.


## Topics I: Repeated Games

Infinitely repeated games

## Theorem 3.9

Consider an infinitely repeated game. Suppose $a^{*}=\left(a_{1}^{*}, \ldots, a_{n}^{*}\right)$ is a stage Nash equilibrium. Assume that there is an action profile $a=\left(a_{1}, \ldots, a_{n}\right)$ in the stage game that gives every player strictly higher stage game payoff than $a^{*}$. Then there exists $\underline{\delta} \in(0,1)$ such that when $\delta \geq \underline{\delta}$, there is a subgame perfect equilibrium in which the outcome path is repeated play of $a$.

## Topics I: Repeated Games

Infinitely repeated games

## Proof of Theorem 3.9.

Define $M \equiv \max _{i, a} u_{i}(a)$ to be the largest stage game payoff across all players and all action profiles. Consider the trigger strategy profile

$$
\forall t \geq 1, s_{i}^{t}(h)= \begin{cases}a_{i}, & \text { if } h=\emptyset \text { or } h=(a, \ldots, a) \in H_{t-1} \\ a_{i}^{*} & \text { otherwise }\end{cases}
$$

In the firs period, if player $i$ plays $a_{i}$, given his opponents' strategy and his own future play, his payoff is $v_{i}(a)$. If player $i$ plays an action $a_{i}^{\prime}$ different from $a_{i}$, his payoff is

$$
(1-\delta) v_{i}\left(a_{i}^{\prime}, a_{-i}\right)+\delta v_{i}\left(a^{*}\right) \leq(1-\delta) M+\delta v_{i}\left(a^{*}\right)
$$

## Topics I: Repeated Games

Infinitely repeated games

## Proof of Theorem 3.9 (Cont.)

Thus, player $i$ does not have a profitable one-shot deviation in period $t=1$ if

$$
v_{i}(a) \geq(1-\delta) M+\delta v_{i}\left(a^{*}\right)
$$

or equivalently

$$
\delta \geq \delta_{i}=\frac{M-v_{i}(a)}{M-v_{i}\left(a^{*}\right)} \in[0,1)
$$

Let $\underline{\delta} \equiv \max _{i} \delta_{i}$. Then, when $\delta \in[\underline{d}, 1)$, no one has a profitable one-shot deviation in the first period.

Consider any history $h=(a, \ldots, a)$. Since players' continuation play after history $h$ is identical to $s$ itself, we know that no one has a profitable one-shot deviation provided $\delta \in[\underline{\delta}, 1)$.

## Topics I: Repeated Games

Infinitely repeated games

## Proof of Theorem 3.9 (Cont.)

Finally, consider any history $h \neq(a, \ldots, a)$. Because the continuation play of $s$ is simply the repeated play of the stage Nash equilibrium $a^{*}$ after every history, we know the continuation play is a SPE in the subgame. Thus no one has a profitable one-shot deviation at $h$. In sum, as long as $\delta \in[\underline{\delta}, 1)$, no one has a profitable one-shot deviation, implying it is a SPE.

## Topics I: Repeated Games

Infinitely repeated games

- Let's go back to the Cournot duopoly example.
- Suppose now that the two firms involve in a long-run relationship instead of a one-shot competition.
- They compete in every period $t=1,2, \ldots$, with discount factor $\delta \in(0,1)$.
- Can they collude without entering an explicit contract, which is forbidden in most countries?


## Topics I: Repeated Games

Infinitely repeated games

- Let $q_{1}^{c}=q_{2}^{c}=22.5$ and $q_{1}^{e}=q_{2}^{e}=30$.
- We have calculated that each firm's collusive payoff is 1012.5 and equilibrium payoff is 900 .
- Consider the trigger strategy profile

$$
\forall t \geq 1, s_{i}^{t}(h)= \begin{cases}q_{i}^{c}, & \text { if } h=\emptyset \text { and } h=\left(q^{c}, \ldots, q^{c}\right) \\ q_{i}^{e}, & \text { otherwise. }\end{cases}
$$

- If $s$ is played, then the firms collude all the time.
- But the question is whether $s$ is a SPE.


## Topics I: Repeated Games

Infinitely repeated games

- After any history in which at least one firm has deviated from the collusive quantity, the two firms play a stage Nash equilibrium independent of histories. Thus, $s$ is a Nash in such subgames for any $\delta$.
- Consider period $t=1$.
- Given the opponent's strategy and firm $i$ 's own strategy from period $t=2$ on, firm $i$ 's total payoff from choosing $q_{i}=q_{i}^{c}$ in period $t=1$ is 1012.5 and that from choosing $q_{i} \neq q_{i}^{c}$ is

$$
\left.(1-\delta)\left[P\left(q_{i}+q_{-i}^{c}\right)-10\right)\right] q_{i}+\delta \times 900
$$

## Topics I: Repeated Games

Infinitely repeated games

Thus, if

$$
1012.5 \geq \max _{q_{i} \geq 0}(1-\delta)\left[P\left(q_{i}+q_{-i}^{c}\right)-10\right] q_{i}+\delta \times 900
$$

then firm $i$ does not have a profitable one-shot deviation in the first period.

- Easy calculation shows that the above inequality is equivalent to

$$
1012.5 \geq(1-\delta) \times 1139.0625+\delta \times 900
$$

- Thus, when

$$
\delta \geq \underline{\delta} \equiv 0.53
$$

firm $i$ has no profitable one-shot deviation in the first period.

## Topics I: Repeated Games

Infinitely repeated games

- In any period after the history in which firms have colluded previously, the continuation play of $s$ is identical to $s$ itself. Thus, no fir has a profitable one-shot deviation at such history, provided $\delta \geq \underline{\delta}$.
- Therefore, as long as $\delta \in[\underline{\delta}, 1), s$ is a SPE. In this SPE, the firms collude all the time.


## Topics II: Strategic Bargaining

## The alternating offer bargaining game

- Two players bargain over a pie of size 1.
- In the fist round:
- Player 1 offers shares $(x, 1-x)$ for $x \in[0,1]$.
- Player 2 decides to accept, causing the game to end with payoffs $v_{1}=x$ and $v_{2}=1-x$, or reject, causing the game to move to the second round.
$\rightarrow$ In the second round:
- Player 2 offers shares $(x, 1-x)$ for $x \in[0,1]$.
- Player 1 decides to accept, causing the game to end with payoffs $v_{1}=\delta x$ and $v_{2}=\delta(1-x)$, or reject, causing the game to move to the next round.
- $\delta \in(0,1)$ is the discount factor: players are impatient / time is money.
- In the third round and beyond:
- The game continues in the same way, where players alternate to offer following a rejection.
- Each period has further discounting, so that if agreement $(x, 1-x)$ is reached in round $t$, payoffs are $v_{1}=\delta^{t-1} x$ and $v_{2}=\delta^{t-1}(1-x)$.


## Topics II: Strategic Bargaining

## The alternating offer bargaining game

- Assume the bargaining process can not go beyond $T$ rounds.
- $T$ can be finite, $T=1,2,3, \ldots$. In this case, $T$ is a "hard deadline". If an agreement is not reached in the first $T$ rounds, the pie is destroyed and each player obtains 0 .
- $T$ can be infinite, $T=\infty$. In this case, the bargaining process can last indefinitely. If an agreement is never reached, the pie is destroyed and each player obtains 0 .
- This is a game of perfect information.


## Topics II: Strategic Bargaining

The alternating offer bargaining game

![](https://cdn.mathpix.com/cropped/2024_09_09_605858d45802b61328b8g-263.jpg?height=641&width=321&top_left_y=149&top_left_x=482)

Figure 3.27: The alternating offer bargaining.

## Topics II: Strategic Bargaining

## One round of bargaining: the ultimatum game

- Assume $T=1$, so there is only one round of bargaining.
- That is, if player 2 rejects player 1's offer, the game ends and each obtains 0 .
- SPE by backward induction.
- If player 1 proposes $(x, 1-x)$ for $x \in[0,1)$, the unique optimal choice for player 2 is to accept.
- If player 1 proposes $(1,0)$, player 2 is indifferent between accepting and rejecting.
- Thus, two possibilities:
- Player 2 accepts every proposal. The player 1's best response is to propose $(1,0)$. This is a SPE.
- Player 2 accepts all but $(1,0)$ in which case he rejects. Player 1 has not best response. (Yes?)
- Unique SPE: player 1 proposes $(1,0)$ and player 2 accepts every proposal.


## Topics II: Strategic Bargaining

One round of bargaining: the ultimatum game

- How about Nash? Many.
- Consider any $x \in[0,1]$.
- Suppose
- player 1 proposes $(x, 1-x)$;
- player 2 accepts $(x, 1-x)$ and rejects every other proposal.

It is a Nash. (Yes?)

- Incredible threat is involved.


## Topics II: Strategic Bargaining

Finitely many rounds of bargaining

- Assume $T>1$ but is finite.
- As an example, consider $T=2$.

![](https://cdn.mathpix.com/cropped/2024_09_09_605858d45802b61328b8g-266.jpg?height=586&width=289&top_left_y=242&top_left_x=508)

Figure 3.28: The alternating offer bargaining.

## Topics II: Strategic Bargaining

## Finitely many rounds of bargaining

- Backward induction for SPE.
- We have already known that if player 2 rejects player 1's proposal, then 2 will get the whole pie in the second round, with payoff $\delta$ (because of discounting).
- In the first round, if player 1 proposes $(x, 1-x)$, then player 2
- strictly prefers accepting if $1-x>\delta$;
- strictly prefers rejecting if $1-x<\delta$;
- is indifferent between accepting and rejecting if $1-x=\delta$.


## Topics II: Strategic Bargaining

## Finitely many rounds of bargaining

- There are two possibilities again.
- Consider first player 2 in the first round accepts any $(x, 1-x)$ such that $1-x>\delta$ and rejects others.
- If player 1 proposes $(x, 1-x)$ in the first round, then
- the offer will be accepted and resulting a payoff $x$ to player 1 if $x<1-\delta$;
- the offer will be rejected and resulting a payoff 0 to player 1 (in the second round) if $x \geq 1-\delta$.
- Obviously, player 1 has no optimal choice.
- So this player 2's behavior can not be part of a SPE.


## Topics II: Strategic Bargaining

## Finitely many rounds of bargaining

- Consider then player 2 in the first round accepts any $(x, 1-x)$ such that $1-x \geq \delta$ and rejects others.
- If player 1 proposes $(x, 1-x)$ in the first round, then
- the offer will be accepted and resulting a payoff $x$ to player 1 if $x \leq 1-\delta$;
- the offer will be rejected and resulting a payoff 0 to player 1 (in the second round) if $x>1-\delta$.
- Thus player 1's optimal choice in the first round is $(1-\delta, \delta)$.
- Unique SPE:
- player 1 in the first round proposes $(1-\delta, \delta)$ and accepts every proposal in the second round;
- player 2 accepts $(x, 1-x)$ if $x \leq 1-\delta$ and rejects others in the first round. He always proposes $(0,1)$ in the second round.
- Equilibrium payoff $(1-\delta, \delta)$. Agreement is reached in the first round.
- As $\delta \uparrow 1$, player 2 gets larger fraction of the pie.


## Topics II: Strategic Bargaining

## Finitely many rounds of bargaining

- How about $T=3$ ?
- In the first round, player 1 proposes.
- If player 2 rejects, then they will play the unique SPE for the two-round bargaining game that we have just figured out.
- In that equilibrium, the payoffs are $\left(\delta^{2}, \delta(1-\delta)\right.$ ) (one more round of discounting).
- Therefore, in the first round, player 2 must accept any proposal $(x, 1-x)$ with $1-x \geq \delta(1-\delta)$ (can not reject when being indifferent by the same reason as above).
- Then, in the first round, player 1 proposes $(1-\delta(1-\delta), \delta(1-\delta))$.
- Unique SPE (how to describe it?)


## Topics II: Strategic Bargaining

Finitely many rounds of bargaining

- If $T=4$, there is also a unique SPE.
- In this equilibrium, player 1 proposes
$(1-\delta(1-\delta(1-\delta)), \delta(1-\delta(1-\delta)))$.
- If $T=5, \ldots$


## Topics II: Strategic Bargaining

Rubinstein bargaining: the inifinite horizon bargaining

- How about $T=\infty$ ?
- This is usually referred to as Rubintein bargaining model.
- Backward induction does not apply due to infinite horizon.
- SPE?


## Topics II: Strategic Bargaining

## Rubinstein bargaining: the inifinite horizon bargaining

- The key step to derive a SPE is to observe the stationary structure of this game.
- Think about the whole game and a subgame starting in the 3rd round following player 1's rejection in the 2nd round.
- A simple examination reveals that these two games are the same (up to $\delta^{2}$ discounting).
- More importantly, all subgames starting in odd periods following player 1 's rejection in the previous round are the same.
- Similarly, all subgames starting in even periods following player 2's rejection in the previous round are the same.


## Topics II: Strategic Bargaining

## Rubinstein bargaining: the inifinite horizon bargaining

- With this observation, let's guess a stationary equilibrium.
- player 1 always proposes $\left(x^{*}, 1-x^{*}\right)$ and 2 always proposes $\left(y^{*}, 1-y^{*}\right)$.;
- player 1 always accepts an offer $x \geq y^{*}$ and rejects others;
- player 2 always accepts an offer $1-x \geq 1-x^{*}$ and rejects others.


## Topics II: Strategic Bargaining

Rubinstein bargaining: the inifinite horizon bargaining

- For 2 to accept $1-x^{*}, 1-x^{*} \geq \delta\left(1-y^{*}\right)$.
- For 2 to reject any offer $1-x<1-x^{*}, 1-x \leq \delta\left(1-y^{*}\right)$.
- Hence 2 must be indifferent between accepting and rejecting $1-x^{*}$ :

$$
1-x^{*}=\delta\left(1-y^{*}\right)
$$

- For 1 to accept $y^{*}, y^{*} \geq \delta x^{*}$.
- For 1 to reject any offer $x<y^{*}, x \leq \delta x^{*}$.
- Hence 1 must be indifferent between accepting and rejecting $y^{*}$ :

$$
y^{*}=\delta x^{*}
$$

- Therefore, we have

$$
x^{*}=\frac{1}{1+\delta} \text { and } y^{*}=\frac{\delta}{1+\delta}
$$

- This strategy profile is a SPE.


## Topics II: Strategic Bargaining

## Rubinstein bargaining: the inifinite horizon bargaining

- Any other SPE?
- Let $G_{1}$ be the set of all SPE payoffs in the subgames in which player 1 makes the initial proposal.
- Let $M_{1}=\sup G_{1}$ and $m_{1}=\inf G_{1}$.
- In words, $M_{1}\left(m_{1}\right)$ is the highest (lowest) SPE payoff to player 1 in the subgames in which player 1 makes the initial proposal.
- Similarly, let $G_{2}$ be the set of all SPE payoffs in the subgames in which player 2 makes the initial proposal.
- Let $M_{2}=\sup G_{2}$ and $m_{2}=\inf G_{2}$.


## Topics II: Strategic Bargaining

Rubinstein bargaining: the inifinite horizon bargaining

- We now claim that $m_{i} \geq 1-\delta M_{j}$ for $i \neq j$.
- For example, assume $i=1$ and $j=2$.
- Consider the subgame in which player 1 makes the initial proposal (e.g. the whole game).
- Observe that if player 2 rejects 1's proposal, then 2 can obtain at most $\delta M_{2}$.
- Thus, player 2 must be willing to accept any $1-x>\delta M_{2}$.
- This implies that player 1 can get $1-\delta M_{2}-\varepsilon$ for $\varepsilon>0$.
- Therefore, $m_{1} \geq 1-\delta M_{2}$.


## Topics II: Strategic Bargaining

Rubinstein bargaining: the inifinite horizon bargaining

- We also claim that $M_{i} \leq 1-\delta_{j} m_{j}$ for $i \neq j$.
- For example, assume $i=1$ and $j=2$ again.
- Consider again the subgame in which player 1 makes the initial proposal.
- Observe that if player 2 rejects 1's proposal, then 2 can obtain at least $\delta m_{2}$.
- Thus player 2 must reject any $1-x<\delta m_{2}$.
- If player 1 's offer is accepted, 1 can at most get $1-\delta m_{2}$.
- If player 1's offer is rejected, 1 can at most get $\delta\left(1-m_{2}\right) \leq 1-\delta m_{2}$.
- Therefore, $M_{1} \leq 1-\delta m_{2}$.


## Topics II: Strategic Bargaining

Rubinstein bargaining: the inifinite horizon bargaining

- Now,

$$
\begin{aligned}
& m_{i} \geq 1-\delta M_{j} \geq 1-\delta\left(1-\delta m_{i}\right) \Rightarrow m_{i} \geq \frac{1}{1+\delta} \\
& M_{i} \leq 1-\delta m_{j} \leq 1-\delta\left(1-\delta M_{i}\right) \Rightarrow M_{i} \leq \frac{1}{1+\delta}
\end{aligned}
$$

- Because $m_{i} \leq M_{i}$ by construction, we have

$$
M_{i}=m_{i}=\frac{1}{1+\delta}
$$

- Up to this point, we have shown that in the subgame in which player $i$ makes the initial proposal, the unique SPE payoff to player $i$ is $1 /(1+\delta)$.
- Note this is just the stationary SPE payoff (it must be).


## Topics II: Strategic Bargaining

Rubinstein bargaining: the inifinite horizon bargaining

- It remains to show that the stationary SPE is the unique SPE.
- Consider the subgame in which 1 makes the initial proposal.
- In any SPE, if an agreement is not reached in the first round, 1 can get at most $1-M_{2}=\delta M_{1}<M_{1}$.
- This implies that for 1 to get $M_{1}$, an agreement must be reached in the first round.
- Thus, 1 must propose ( $M_{1}, 1-M_{1}$ ) in the first round and 2 accepts this proposal.
- For this behavior to be part of a SPE, 2 must reject any proposal that gives her a strictly lower payoff that $1-M_{1}$; otherwise 1 can make a lower offer to 2 .
- Moreover, if 1 makes a proposal that gives 2 a strictly higher payoff than $1-M_{1}=\delta M_{2}, 2$ must accept.


## Topics II: Strategic Bargaining

## Rubinstein bargaining: the inifinite horizon bargaining

- The above arguments show that in any subgame in which 1 makes the initial proposal, any SPE prescribes that, in the initial round, 1 makes proposal $\left(M_{1}, 1-M_{1}\right)$ and 2 accepts any offer higher than or equal to $1-M_{1}$ and rejects others.
- Similar arguments apply to any SPE in the subgame in which 2 makes the initial proposal.
- We can show that 2 makes the proposal $\left(1-M_{2}, M_{2}\right)$ and 1 accepts any offer higher than or equal to $1-M_{2}$ and rejects others.
- Therefore, the stationary SPE is the unique SPE.


## Topics II: Strategic Bargaining

## Bonus: the pirate game

- $n$ pirates, named $i=1, \ldots, n$, decide how to split 100 coins.
- In the first round, $i=1$ makes a proposal and all pirates vote about this proposal.
- If at least half of the pirates vote for this proposal, then it is accepted and the coins are split accordingly.
- Otherwise, the proposal is rejected and $i=1$ is thrown into the sea. In this case, they move to the second round and it is $i=2$ 's turn to make a proposal.
- The game then proceed in a similar fashion until an agreement is achieved.
- A pirate's payoff is equal to the number of coins he obtains, or -1 if he is thrown into the sea.
- SPE?


# Game Theory Lecture Notes 4 

Static Games with Incomplete Information

Ju Hu<br>National School of Development<br>Peking University

Fall 2022

## Motivating Example

## Game of chicken with incomplete information

- Two teenagers drive toward each other.
- Just before impact, they must simultaneously choose whether to be chicken and swerve to the right, or continue driving head on.
- They want to show they are brave and gain the respect from their friends.
- But they also suffer a loss if a collision occurs (e.g., parents reprimand, if seriously injured).
- If everything is common knowledge, it is a complete information game that we have learned.

![](https://cdn.mathpix.com/cropped/2024_09_09_605858d45802b61328b8g-284.jpg?height=155&width=537&top_left_y=633&top_left_x=355)
where $R>0, k \geq 0$.

## Motivating Example

Game of chicken with incomplete information

- Now, assume the punishment $k$ is each player's private information.
- For instance, every teenage knows whether his own parents are harsh or lenient, but does not know others' parents.
- If $i$ 's parents are harsh, then $k_{i}=H$ is high.
- If $i$ 's parents are lenient, then $k_{i}=L$ is low.
- Assume every player's parents can be harsh or lenient with equal probabilities.


## Motivating Example

Game of chicken with incomplete information

- We have described a situation where not everything is common knowledge among the players.
- In particular, players have uncertainty over some characteristics of their opponents.
- In this example, each player is uncertain over the preferences of his opponent.
- This is an example of games of incomplete information.


## Motivating Example

## Game of chicken with incomplete information

- Consider player 1 who knows that his own parents are harsh.
- This means that player 1 knows if a collision happens, he will face a large punishment $k_{1}=H$ from his parents.
- He does not know whether player 2's parents are harsh or lenient. Should he care about that?
- Although $k_{2}$ does not directly determine 1's payoff if a collision occurs, but it will affect 2's behavior which in turn will affect 1's own payoff too.
- Thus, when considering his own action, 1 should takes into account the fact that it is equally likely $k_{2}=H$ or $k_{2}=L$.
- The same intuition also applies to player 1 with $k_{1}=L$ and player 2.
- But then, when considering his own actions, $i$ should also takes into account the fact that $j$ takes into account the fact that $k_{i}=H$ or $k_{i}=L$ equally likely.
- But then, $i$ should also takes into account that $j$ takes into account that $i$ takes into account that ...


## Motivating Example

## Game of chicken with incomplete information

- It sounds like a very difficult and intractable situation.
- It was John Harsanyi who first realized that this difficult game of incomplete information can be transformed into an extensive form game of imperfect information which we have developed and fully understood.
- The trick is to introduce a special player, Nature, into an extensive form game, who "chooses" each player's characteristics.


## Motivating Example

## Game of chicken with incomplete information

## John C. Harsanyi

![](https://cdn.mathpix.com/cropped/2024_09_09_605858d45802b61328b8g-289.jpg?height=466&width=315&top_left_y=278&top_left_x=74)

The Sveriges Riksbank Prize in Economic Sciences in Memory of Alfred Nobel 1994
"for their pioneering analysis of equilibria in the theory of non-cooperative games."

Contribution: Showed how games of incomplete information can be analyzed, thereby providing a theoretical foundation for a lively field of research - the economics of information - which focuses on strategic situations where different agents do not know each others' objectives.

## Motivating Example

## Game of chicken with incomplete information

- Consider the following extensive form game.
- There are three players: Nature (player 0), players 1 and 2.
- Nature moves first. Available actions are $L L, L H, H L$ and $H H$. Choosing $L L$ means $k_{1}=L$ and $k_{2}=L$, and so on.
- Moreover, Nature's strategy is a fixed behavior strategy: it chooses of the four actions with probability $1 / 4$.
- Next, player 1 moves, observing Nature's choice $k_{1}$ but not $k_{2}$ and choosing between $C$ and $D$.
- Lastly, player 2 moves, observing only Nature's choice $k_{2}$ but neither $k_{1}$ nor player 1's choice, and choosing between $c$ and $d$.
- The payoff at each terminal node is properly specified.


## Motivating Example

## Game of chicken with incomplete information

![](https://cdn.mathpix.com/cropped/2024_09_09_605858d45802b61328b8g-291.jpg?height=671&width=1113&top_left_y=153&top_left_x=88)

Figure 4.1: The extensive form for game of chicken with private punishment

## Motivating Example

## Game of chicken with incomplete information

- When player 2 chooses, he does not observe 1's choice, implying this is a simultaneous move game between players 1 and 2 .
- When either player 1 or 2 chooses, he only knows his own $k$ but not his opponent's, implying that $k_{i}$ is $i$ 's private information.
- Thus, this extensive form game characterizes exactly the same strategic situation that we have described by a game of incomplete information.
- And, we know how to analyze it!


## Motivating Example

## Game of chicken with incomplete information

- Player 1 has two information sets. Thus, $S_{1}=\{C C, C D, D C, D D\}$.
- For example, $C D$ specifies that player 1 chooses $C$ at his first information set and $D$ at the second.
- In other words, $C D$ represents the strategy that 1 chooses
- $C$ when $k_{1}=L$ (his parents are lenient in our story), and
- $D$ when $k_{1}=H$ (his parents are harsh).
- Similarly, player 2 has two information sets. Thus $S_{2}=\{c c, c d, d c, d d\}$.
- For example, $d c$ represents the strategy that 2 chooses
- $d$ when $k_{2}=L$ (his parents are lenient), and
- $c$ when $k_{2}=H$ (his parents are harsh).


## Motivating Example

## Game of chicken with incomplete information

- For any strategy profile $\left(A_{L} A_{H}, a_{L} a_{H}\right)$, the outcome is the distribution

$$
\frac{1}{4} \circ\left(L L, A_{L}, a_{L}\right)+\frac{1}{4} \circ\left(L H, A_{L}, a_{H}\right)+\frac{1}{4} \circ\left(H L, A_{H}, a_{L}\right)+\frac{1}{4} \circ\left(H H, A_{H}, a_{H}\right)
$$

- Player 1's payoff thus is

$$
\begin{aligned}
\tilde{v}_{1}\left(A_{L} A_{H}, a_{L} a_{H}\right) \equiv & \frac{1}{4} v_{1}\left(A_{L}, a_{L} ; k_{1}=L\right)+\frac{1}{4} v_{1}\left(A_{L}, a_{H} ; k_{1}=L\right) \\
& +\frac{1}{4} v_{1}\left(A_{H}, a_{L} ; k_{1}=H\right)+\frac{1}{4} v_{1}\left(A_{H}, a_{H} ; k_{1}=H\right) \\
\tilde{v}_{2}\left(A_{L} A_{H}, a_{L} a_{H}\right) \equiv & \frac{1}{4} v_{2}\left(A_{L}, a_{L} ; k_{2}=L\right)+\frac{1}{4} v_{2}\left(A_{L}, a_{H} ; k_{2}=H\right) \\
& +\frac{1}{4} v_{2}\left(A_{H}, a_{L} ; k_{2}=L\right)+\frac{1}{4} v_{2}\left(A_{H}, a_{H} ; k_{2}=H\right)
\end{aligned}
$$

## Motivating Example

## Game of chicken with incomplete information

- Assume $R=8, H=16$, and $L=0$.
- The matrix representation is as follows:

|  | cc | cd | $d c$ | $d d$ |
| :---: | :---: | :---: | :---: | :---: |
| $C C$ | 0,0 | 0,4 | 0,4 | 0,8 |
| $C D$ | 4, 0 | $-1,-1$ | $-1,3$ | $-6,2$ |
| $D C$ | 4, 0 | $3,-1$ | 3, 3 | 2,2 |
| DD | 8,0 | $2,-6$ | 2,2 | $-4,-4$ |

- Unique pure strategy Nash equilibrium: $(D C, d c)$.
- Meaning: in this symmetric equilibrium, a teenager with harsh parents chooses to be chicken and a teenager with lenient parents choose to drive head on.
- By transforming it into a game of imperfect information, we have done analyzing a game of incomplete information without learning any new knowledge.


## Bayesian Games

Players, actions, information and preferences

- To model the situation of incomplete information generally, we introduce types for each player.
- Each type of player $i$ summarizes his characteristics.
- The set of all player $i$ 's possible types is his type space.
- For example, in the previous game of chichen, $k_{1}=H$ is one of player 1's types. It summarizes player 1's preference characteristics: if a collision occurs, this type is subject to a large reprimand $H$.
- $k_{1}=L$ is another possible type of player 1. It also summarizes player 1 's preference characteristics: if a collision occurs, this type is subject to a small reprimand $L$.
- Hence, player 1's type space is $\{H, L\}$. So is player 2's type space.


## Bayesian Games

Players, actions, information and preferences

- Uncertainty over types is described by/imagined as Nature choosing types for the different players.
- Importantly, there is common knowledge about the way in which Nature chooses between profiles of types of players.
- This is represented by a common prior, which is a probability distribution over type profiles that is common knowledge among the players.
- For example, in the previous game of chicken, the common prior is

$$
\frac{1}{4} \circ L L+\frac{1}{4} \circ L H+\frac{1}{4} \circ H L+\frac{1}{4} \circ H H
$$

## Bayesian Games

Players, actions, information and preferences

## Definition 4.1

The normal-form representation of an $n$-player Bayesian game or static game of incomplete information is

$$
\left(N,\left\{A_{i}\right\}_{i=1}^{n},\left\{\Theta_{i}\right\}_{i=1}^{n},\left\{v_{i}\right\}_{i=1}^{n}, \mathbb{P}\right)
$$

where

- $N=\{1,2, \ldots, n\}$ is the set of players;
- $A_{i}$ is player $i$ 's action space;
- $\Theta_{i}$ is player $i$ 's type space and every element $\theta_{i} \in \Theta_{i}$ is a type;
- $v_{i}: A \times \Theta \rightarrow \mathbb{R}$ is $i$ 's payoff function; where $A=A_{1} \times \ldots \times A_{n}$ is the set of action profiles and $\Theta=\Theta_{1} \times \ldots \times \Theta_{n}$ is the set of type profiles;
- $\mathbb{P}$ is the common prior: a probability distribution over $\Theta$.
- $v_{i}(a ; \theta)$ is $i$ 's payoff if the action profile is $a$ and the type profile is $\theta$.


## Bayesian Games

Deriving posteriors from a common prior: a player's beliefs

- Recall from your probability course.
- Suppose $\mathbb{P}$ is a probability distribution over some space $X$.
- The conditional probability of an event $B \subset X$ given event $A \subset X$ is

$$
\mathbb{P}(B \mid A) \equiv \frac{\mathbb{P}(B \cap A)}{\mathbb{P}(A)}
$$

provided the denominator is positive.

- This formula is called the Bayes' rule.


## Bayesian Games

Deriving posteriors from a common prior: a player's beliefs

- In a Bayesian game, the common prior $\mathbb{P}$ is a probability distribution over $\Theta=\Theta_{1} \times \ldots \times \Theta_{n}$.
- Suppose $i$ knows that his type is $\theta_{i} \in \Theta_{i}$.
- How does he think about his opponents' types?
- In particular, how likely does player $i$ thinks that his opponents' type is $\theta_{-i} \in \Theta_{-i}$ ?
- This is precisely the conditional probability of $\theta_{-i}$ given $\theta_{i}$ :

$$
\phi_{i}\left(\theta_{-i} \mid \theta_{i}\right)=\frac{\mathbb{P}\left(\theta_{i}, \theta_{-i}\right)}{\mathbb{P}\left(\theta_{i}\right)}
$$

where $\mathbb{P}\left(\theta_{i}\right)=\sum_{\theta_{-i}^{\prime} \in \Theta_{-i}} \mathbb{P}\left(\theta_{i}, \theta_{-i}^{\prime}\right)$ is the marginal distribution of player $i$ 's types.

- $\phi_{i}\left(\cdot \mid \theta_{i}\right)$ is called player $i$ 's posterior belief about his opponents' types given his own type $\theta_{i}$.


## Bayesian Games

Deriving posteriors from a common prior: a player's beliefs

- Consider the previous game of chicken example.
- The common prior can be represented by

| $L$ | $H$ |  |
| :---: | :---: | :---: |
| $L$ | $1 / 4$ | $1 / 4$ |
| $H$ | $1 / 4$ | $1 / 4$ |
|  |  |  |

where each row (column) represents one of player 1's (2's) types.

- Thus, $\phi_{i}\left(H \mid \theta_{i}\right)=\phi_{i}\left(L \mid \theta_{i}\right)=\frac{1}{2}$ for $i=1,2$ and $\theta_{i} \in\{H, L\}$. This is so because we have assumed that the two players' types are independently distributed.


## Bayesian Games

Deriving posteriors from a common prior: a player's beliefs

- If, instead, the common prior is

|  | $L$ | $H$ |
| :---: | :---: | :---: |
| $L$ | $1 / 3$ | $1 / 6$ |
| $H$ | $1 / 6$ | $1 / 3$ |
|  |  |  |

then for $i=1,2$,

$$
\phi_{i}(L \mid L)=\frac{2}{3}, \phi_{i}(H \mid L)=\frac{1}{3}
$$

and

$$
\phi_{i}(L \mid H)=\frac{1}{3}, \phi_{i}(H \mid H)=\frac{2}{3}
$$

- Different types have different posterior beliefs.
- In particular, every type thinks that it is more likely that the opponent is of the same type.


## Bayesian Games

## Strategies and Bayesian Nash equilibrium

## Definition 4.2

Consider a Bayesian game

$$
\left(N,\left\{A_{i}\right\}_{i=1}^{n},\left\{\Theta_{i}\right\}_{i=1}^{n},\left\{v_{i}\right\}_{i=1}^{n}, \mathbb{P}\right)
$$

A pure strategy for player $i$ is a function $s_{i}: \Theta_{i} \rightarrow A_{i}$ that specifies a pure action $s_{i}\left(\theta_{i}\right)$ that player $i$ will choose when his type is $\theta_{i}$. A mixed strategy is a function $\sigma_{i}: \Theta_{i} \rightarrow \Delta\left(A_{i}\right)$ that specifies a mixed action $\sigma_{i}\left(\theta_{i}\right)$ for each type $\theta_{i}$.

- A strategy is a complete type-contingent plan.
- Easy to understand if we think about its equivalent extensive form representation: a pure strategy is a mapping from information sets (types) to actions. A mixed strategy in the Bayesian game corresponds to a behavioral strategy in the extensive form representation.


## Bayesian Games

## Strategies and Bayesian Nash equilibrium

- Given a strategy profile $s_{-i}$ of $i$ 's opponents, the expected payoff for player $i$ if his type is $\theta_{i}$ and he chooses action $a_{i} \in A_{i}$ is

$$
\sum_{\theta_{-i} \in \Theta_{-i}} \phi_{i}\left(\theta_{-i} \mid \theta_{i}\right) v_{i}\left(a_{i}, s_{-i}\left(\theta_{-i}\right) ; \theta_{i}, \theta_{-i}\right)
$$

- Player $i$ of type $\theta_{i}$ thinks that $\theta_{-i}$ is realized with probability $\phi_{i}\left(\theta_{-i} \mid \theta_{i}\right)$, in which case the opponents choose $s_{-i}\left(\theta_{-i}\right)$ and the resulting payoff is $v_{i}\left(a_{i}, s_{-i}\left(\theta_{-i}\right) ; \theta_{i}, \theta_{-i}\right)$


## Bayesian Games

## Strategies and Bayesian Nash equilibrium

## Definition 4.3

In the Bayesian game

$$
\left(N,\left\{A_{i}\right\}_{i=1}^{n},\left\{\Theta_{i}\right\}_{i=1}^{n},\left\{v_{i}\right\}_{i=1}^{n}, \mathbb{P}\right)
$$

a strategy profile $s^{*}=\left(s_{1}^{*}, s_{2}^{*}, \ldots, s_{n}^{*}\right)$ is a pure strategy Bayesian
Nash equilibrium if, for every player $i$, for each of player $i$ 's type $\theta_{i} \in \Theta_{i}$, we have

$$
\begin{aligned}
& \sum_{\theta_{-i} \in \Theta_{-i}} \phi_{i}\left(\theta_{-i} \mid \theta_{i}\right) v_{i}\left(s_{i}^{*}\left(\theta_{i}\right), s_{-i}^{*}\left(\theta_{-i}\right) ; \theta_{i}, \theta_{-i}\right) \\
\geq & \sum_{\theta_{-i} \in \Theta_{-i}} \phi_{i}\left(\theta_{-i} \mid \theta_{i}\right) v_{i}\left(a_{i}, s_{-i}^{*}\left(\theta_{-i}\right) ; \theta_{i}, \theta_{-i}\right), \forall a_{i} \in A_{i}
\end{aligned}
$$

- No type of any player wants to deviate.
- Mixed strategy equilibrium is similarly defined.


## Bayesian Games

## Strategies and Bayesian Nash equilibrium

- In any Bayesian game, a strategy profile is a Bayesian Nash equilibrium if and only if it is a Nash equilibrium of the equivalent extensive form game.
- To see the "only if" direction, consider the extensive form game and any strategy $s_{i}$ of player $i$.
- (4.1) implies that for each type $\theta_{i} \in \Theta_{i}$, we have

$$
\begin{aligned}
& \sum_{\theta_{-i} \in \Theta_{-i}} \phi_{i}\left(\theta_{-i} \mid \theta_{i}\right) v_{i}\left(s_{i}^{*}\left(\theta_{i}\right), s_{-i}^{*}\left(\theta_{-i}\right) ; \theta_{i}, \theta_{-i}\right) \\
\geq & \sum_{\theta_{-i} \in \Theta_{-i}} \phi_{i}\left(\theta_{-i} \mid \theta_{i}\right) v_{i}\left(s_{i}\left(\theta_{i}\right), s_{-i}^{*}\left(\theta_{-i}\right) ; \theta_{i}, \theta_{-i}\right)
\end{aligned}
$$

## Bayesian Games

## Strategies and Bayesian Nash equilibrium

- Multiplying both side by $\mathbb{P}\left(\theta_{i}\right)$ and summing up all these inequalities over $\theta_{i} \in \Theta_{-i}$ yields

$$
\begin{aligned}
& \sum_{\theta_{i} \in \Theta_{i}} \mathbb{P}\left(\theta_{i}\right) \sum_{\theta_{-i} \in \Theta_{-i}} \phi_{i}\left(\theta_{-i} \mid \theta_{i}\right) v_{i}\left(s_{i}^{*}\left(\theta_{i}\right), s_{-i}^{*}\left(\theta_{-i}\right) ; \theta_{i}, \theta_{-i}\right) \\
\geq & \sum_{\theta_{i} \in \Theta_{i}} \mathbb{P}\left(\theta_{i}\right) \sum_{\theta_{-i} \in \Theta_{-i}} \phi_{i}\left(\theta_{-i} \mid \theta_{i}\right) v_{i}\left(s_{i}\left(\theta_{i}\right), s_{-i}^{*}\left(\theta_{-i}\right) ; \theta_{i}, \theta_{-i}\right)
\end{aligned}
$$

- Equivalently,

$$
\begin{aligned}
& \sum_{\theta \in \Theta} \mathbb{P}(\theta) v_{i}\left(s_{i}^{*}\left(\theta_{i}\right), s_{-i}^{*}\left(\theta_{-i}\right) ; \theta_{i}, \theta_{-i}\right) \\
\geq & \sum_{\theta \in \Theta} \mathbb{P}(\theta) v_{i}\left(s_{i}\left(\theta_{i}\right), s_{-i}^{*}\left(\theta_{-i}\right) ; \theta_{i}, \theta_{-i}\right)
\end{aligned}
$$

- The LHS is $i$ 's expected payoff in the extensive form game from the strategy profile $\left(s_{i}^{*}, s_{-i^{*}}\right)$, while the RHS is that from the strategy profile $\left(s_{i}, s_{-i}^{*}\right)$. Thus, $s^{*}$ is a Nash equilibrium of the extensive form game.


## Bayesian Games

## Strategies and Bayesian Nash equilibrium

- To see the "if" direction, suppose (4.1) is violated for some player $i$ of some type $\hat{\theta}_{i}$.
- That is, there exists $\hat{a}_{i}$ such that

$$
\begin{aligned}
& \sum_{\theta_{-i} \in \Theta_{-i}} \phi_{i}\left(\theta_{-i} \mid \hat{\theta}_{i}\right) v_{i}\left(\hat{a}_{i}, s_{-i}^{*}\left(\theta_{-i}\right) ; \hat{\theta}_{i}, \theta_{-i}\right) \\
> & \sum_{\theta_{-i} \in \Theta_{-i}} \phi_{i}\left(\theta_{-i} \mid \hat{\theta}_{i}\right) v_{i}\left(s_{i}^{*}\left(\hat{\theta}_{i}\right), s_{-i}^{*}\left(\theta_{-i}\right) ; \hat{\theta}_{i}, \theta_{-i}\right)
\end{aligned}
$$

Define

$$
s_{i}\left(\theta_{i}\right)= \begin{cases}\hat{a}_{i}, & \text { if } \theta_{i}=\hat{\theta}_{i} \\ s_{i}^{*}\left(\theta_{i}\right), & \text { if } \theta_{i} \neq \hat{\theta}_{i}\end{cases}
$$

- Note that $s_{i}$ differs from $s_{i}^{*}$ only at $\hat{\theta}_{i}$.


## Bayesian Games

## Strategies and Bayesian Nash equilibrium

- Performing a similar analysis as before, we can show that

$$
\begin{aligned}
& \sum_{\theta \in \Theta} \mathbb{P}(\theta) v_{i}\left(s_{i}\left(\theta_{i}\right), s_{-i}^{*}\left(\theta_{-i}\right) ; \theta_{i}, \theta_{-i}\right) \\
> & \sum_{\theta \in \Theta} \mathbb{P}(\theta) v_{i}\left(s_{i}^{*}\left(\theta_{i}\right), s_{-i}^{*}\left(\theta_{-i}\right) ; \theta_{i}, \theta_{-i}\right)
\end{aligned}
$$

- This shows that $s_{i}^{*}$ is not a best response to $s_{-i}^{*}$ in the extensive form.


## Bayesian Games

## Strategies and Bayesian Nash equilibrium

- A final comment about the common prior $\mathbb{P}$.
- From Definition 4.3, the common prior $\mathbb{P}$ enters the analysis only through the induced players' posterior beliefs $\left\{\phi_{i}\right\}_{i}$.
- Therefore, when writing down a Bayesian game, we sometimes directly write down the system of posterior belief $\left\{\phi_{i}\right\}_{i}$ instead of the common prior $\mathbb{P}$.
- Doing so effectively enlarges the scope of Bayesian games because it also incorporates the possibility of models without a common prior.
- Though it is conceptually/philosophically not easy to think about a environment where players do not share a common prior, the definition of Bayesian Nash equilibrium still applies. (But now it is impossible to transform it into an equivalent extensive form game with Nature. Yes?)


## Bayesian Games

## Strategies and Bayesian Nash equilibrium

- The following is a simple example of system of beliefs which does not admit a common prior:

![](https://cdn.mathpix.com/cropped/2024_09_09_605858d45802b61328b8g-311.jpg?height=257&width=266&top_left_y=283&top_left_x=314)

![](https://cdn.mathpix.com/cropped/2024_09_09_605858d45802b61328b8g-311.jpg?height=259&width=265&top_left_y=282&top_left_x=679)

- Suppose, by contradiction, that a common prior $\mathbb{P}$ exists.
- $\phi_{1}$ implies

$$
\mathbb{P}\left(\theta_{1}=H, \theta_{2}=L\right)=0
$$

while $\phi_{2}$ implies

$$
\mathbb{P}\left(\theta_{1}=H, \theta_{2}=L\right)>0
$$

A contradiction.

## Examples

Cournot duopoly with private information

- Cournot duopoly in which firm 1's marginal cost is its private information.
- In particular, firm 1's marginal cost can be either high $c_{h}$ with probability $\theta \in(0,1)$ or low $c_{\ell}$ with probability $1-\theta$.
- Only firm 1 knows its marginal cost.
- Firm 2's marginal cost, $c_{2}$, is commonly known.
- The two firms then choose quantities simultaneously.
- Market demand is $P(q)=\max \{a-q, 0\}$.


## Examples

Cournot duopoly with private information

- Firm 1 has two types $c_{h}$ and $c_{\ell}$. Thus, firm 1's strategy is a pair $\left(q_{h}, q_{\ell}\right) \in \mathbb{R}_{+}^{2}$, where $q_{h}$ is its supply when its marginal cost is high and $q_{\ell}$ is its supply when its marginal cost is low.
- Firm 2's strategy is $q_{2} \in \mathbb{R}_{+}$.
- The strategy profile $\left(q_{h}^{*}, q_{\ell}^{*}, q_{2}\right)$ is a Bayesian Nash equilibrium if

$$
\begin{aligned}
& q_{h}^{*} \in \underset{q_{h} \geq 0}{\arg \max }\left[P\left(q_{h}+q_{2}^{*}\right)-c_{h}\right] q_{h}, \\
& q_{\ell}^{*} \in \underset{q_{\ell} \geq 0}{\arg \max }\left[P\left(q_{\ell}+q_{2}^{*}\right)-c_{\ell}\right] q_{\ell},
\end{aligned}
$$

and

$$
q_{2}^{*} \in \underset{q_{2} \geq 0}{\arg \max } \theta\left[P\left(q_{h}^{*}+q_{2}\right)-c_{2}\right] q_{2}+(1-\theta)\left[P\left(q_{\ell}^{*}+q_{2}\right)-c_{2}\right] q_{2} .
$$

- The first two conditions state that each type of firm 1 maximizes its profit given firm 2's supply. The last condition states that firm 2 maximizes its profit given firm 1's strategy.


## Examples

Cournot duopoly with private information

- Assume interior solution, i.e. $a$ is large enough

$$
\begin{aligned}
& q_{h}^{*} \in \underset{q_{h} \geq 0}{\arg \max }\left[a-q_{h}-q_{2}^{*}-c_{h}\right] q_{h} \\
& q_{\ell}^{*} \in \underset{q_{\ell} \geq 0}{\arg \max }\left[a-q_{\ell}-q_{2}^{*}-c_{\ell}\right] q_{\ell} \\
& q_{2}^{*} \in \underset{q_{2} \geq 0}{\arg \max } \theta\left[a-q_{h}^{*}-q_{2}-c_{2}\right] q_{2}+(1-\theta)\left[a-q_{\ell}^{*}-q_{2}-c_{2}\right] q_{2}
\end{aligned}
$$

- We have

$$
\begin{aligned}
q_{h}^{*} & =\frac{a-q_{2}^{*}-c_{h}}{2} \\
q_{l}^{*} & =\frac{a-q_{2}^{*}-c_{l}}{2} \\
q_{2}^{*} & =\frac{a-\theta q_{h}^{*}-(1-\theta) q_{l}^{*}-c_{2}}{2}
\end{aligned}
$$

## Examples

Cournot duopoly with private information

Finally

$$
\begin{aligned}
q_{h}^{*} & =\frac{a-2 c_{h}+c_{2}}{3}+\frac{1-\theta}{6}\left(c_{h}-c_{\ell}\right) \\
q_{l}^{*} & =\frac{a-2 c_{l}+c_{2}}{3}-\frac{\theta}{6}\left(c_{h}-c_{\ell}\right) \\
q_{2}^{*} & =\frac{a-2 c_{2}+\theta c_{h}+(1-\theta) c_{\ell}}{3}
\end{aligned}
$$

## Examples

## Study groups

- Two students, who have to hand in a joint lab assignment, form a study group.
- Each student $i$ can either put in the effort $\left(e_{i}=1\right)$ or shirk $\left(e_{i}=0\right)$.
- The cost of exerting effort is $0<c<1$, while shirking involves no cost.
- If either one or both of the students put in the effort, then the lab assignment is success.
- While if both shirk, then it is a failure.
- The value of a failure to both students is 0 .
- The value of a success to player $i$ is $\theta_{i}^{2}$, where $\theta_{i}$ is player $i$ 's private information.
- Assume $\theta_{1}$ and $\theta_{2}$ are uniformly and independently distributed over $[0,1]$.
- A game of voluntary contribution to public good.


## Examples

## Study groups

- A strategy for player $i$ is a mapping $\sigma_{i}:[0,1] \rightarrow[0,1]$, where $\sigma_{i}\left(\theta_{i}\right)$ is the probability that $i$ of type $\theta_{i}$ exerts effort.
- Consider an arbitrary $\sigma_{i}$. From student $j$ 's point view, the probability that player $i$ exerts effort is

$$
p^{\sigma_{i}}=\int_{0}^{1} \sigma_{i}\left(\theta_{i}\right) f\left(\theta_{i}\right) \mathrm{d} \theta_{i}=\int_{0}^{1} \sigma_{i}\left(\theta_{i}\right) \mathrm{d} \theta_{i}
$$

where $f\left(\theta_{i}\right)=1$ is the density of uniform distribution.

## Examples

## Study groups

- Given an arbitrary $\sigma_{2}$, consider student 1 of type $\theta_{1}$.
- If he exerts effort, the payoff is

$$
\theta_{1}^{2}-c
$$

- If he shirks, the payoff is

$$
p^{\sigma_{2}} \theta_{1}^{2}
$$

- Therefore, if $\sigma_{1}$ is a best reponse to $\sigma_{2}$, we must have

$$
\sigma_{1}\left(\theta_{1}\right)= \begin{cases}1, & \text { if } \theta_{1}^{2}>c /\left(1-p^{\sigma_{2}}\right) \\ 0, & \text { if } \theta_{1}^{2}<c /\left(1-p^{\sigma_{2}}\right)\end{cases}
$$

- This is an example of a cut-off strategy (or threshold strategy): there exists a cut-off type $\hat{\theta}_{1}=\sqrt{c /\left(1-p^{\sigma_{2}}\right)}$ such that student 1 exerts effort if his type is above this cut-off and shirks if his type is below this cut-off.


## Examples

## Study groups

- Symmetrically, given an arbitrary $\sigma_{1}$, if $\sigma_{2}$ is a best response for player 2, then we must have

$$
\sigma_{2}\left(\theta_{2}\right)= \begin{cases}1, & \text { if } \theta_{2}^{2}>c /\left(1-p^{\sigma_{1}}\right) \\ 0, & \text { if } \theta_{2}^{2}<c /\left(1-p^{\sigma_{1}}\right)\end{cases}
$$

- Now, suppose $\left(\sigma_{1}, \sigma_{2}\right)$ is a Bayesian Nash equilibrium. From (4.2), we know

$$
p^{\sigma_{1}}=\int_{\min \left\{1, \sqrt{c /\left(1-p^{\sigma_{2}}\right)}\right\}} \mathrm{d} \theta_{1}=1-\min \left\{1, \sqrt{c /\left(1-p^{\sigma_{2}}\right)}\right\}
$$

- Similarly, from (4.3), we know

$$
p^{\sigma_{2}}=1-\min \left\{1, \sqrt{c /\left(1-p^{\sigma_{1}}\right)}\right\}
$$

## Examples

## Study groups

- For $0<c<1$, (4.4) and (4.5) have a unique solution

$$
p^{\sigma_{1}}=p^{\sigma_{2}}=1-c^{\frac{1}{3}}
$$

- This implies the game has an essentially unique Bayesian Nash equilibrium $\left(\sigma_{1}^{*}, \sigma_{2}^{*}\right)$, where

$$
\sigma_{i}^{*}\left(\theta_{i}\right)= \begin{cases}1, & \text { if } \theta_{i}>c^{\frac{1}{3}} \\ 0, & \text { if } \theta_{i}<c^{\frac{1}{3}}\end{cases}
$$

- The word "essentially" means that when $\theta_{i}=c^{\frac{1}{3}}$, any $\sigma_{i}\left(\theta_{i}\right) \in[0,1]$ is fine.


## Applications

## Adverse selection

- Player 1 owns a car which he has been driving for some years and which he considers to sell.
- Player 2 is a potential buyer.
- The mechanical condition of the car is player 1's private information.
- Player 2 thinks that the condition can be poor $(P)$, fair $(F)$ or good $(G)$, with equal probabilities.


## Applications

## Adverse selection

- Player 1's reservation value for this car is

$$
v_{1}(\theta)= \begin{cases}10, & \text { if } \theta=P \\ 20, & \text { if } \theta=F \\ 30, & \text { if } \theta=G\end{cases}
$$

- Player 2's willingness to pay for this car is

$$
v_{2}(\theta)= \begin{cases}14, & \text { if } \theta=P \\ 24, & \text { if } \theta=F \\ 34, & \text { if } \theta=G\end{cases}
$$

## Applications

## Adverse selection

- As a benchmark, assume now that the mechanical condition is commonly known.
- The game between 1 and 2 is an ultimatum game.
- Player 2 first announces a price $p$ that he is willing to pay for that car.
- After observing $p$, player 1 decides whether to accept or not.
- If player 1 accepts, they trade at price $p$; otherwise, they do not trade.


## Applications

Adverse selection

- If $\theta=P$, they trade at $p=10$ in the unique SPE.
- If $\theta=F$, they trade at $p=20$ in the unique SPE.
- If $\theta=G$, they trade at $p=30$ in the unique SPE.
- In all cases, trade occurs and is efficient.


## Applications

## Adverse selection

- Now, we return to the case where the mechanical condition is player 1's private information.
- To model this situation as a Bayesian game (simultaneous move), we assume that player 1 chooses an acceptance plan which specifies for each price whether he accepts or not.
- Thus, a strategy for player 1 of type $\theta \in\{P, F, G\}$ is a mapping $s_{1}^{\theta}: \mathbb{R} \rightarrow\{a, r\}$.
- Bayesian Nash equilibria?


## Applications

## Adverse selection

- There is no equilibrium in which $G$ accepts the equilibrium price.
- To see this, suppose by contradiction that $G$ accepts the equilibrium price $p$ in an equilibrium, i.e., $s_{1}^{G}(p)=a$.
- This implies $p \geq 30$, which in turn implies $s_{1}^{P}(p)=s_{1}^{F}(p)=a$.
- But then, player 2's expected payoff from $p$ is

$$
\frac{1}{3} v_{2}(P)+\frac{1}{3} v_{2}(F)+\frac{1}{3} v_{2}(G)-p=24-p<0
$$

- By deviating to $p^{\prime}=0$, player 2 can obtain at least 0 .
- A contradiction.


## Applications

## Adverse selection

- There is no equilibrium in which $F$ accepts the equilibrium price $p$, i.e., $s_{1}^{F}(p)=a$, either.
- The argument is similar to the above one.
- If, by contradiction, $s_{1}^{F}(p)=a$, we know $p \geq 20$, which in turn implies $s_{1}^{P}(p)=a$.
- So, player 2's expected payoff from $p$ is (we know $s_{1}^{G}(p)=r$ from previous analysis):

$$
\frac{1}{2} v_{2}(P)+\frac{1}{2} v_{2}(F)-p=19-20<0
$$

- Again, by deviating to $p^{\prime}=0$, player 2 can at least obtain 0 .
- A contradiction.


## Applications

## Adverse selection

- In sum, in any Bayesian Nash equilibrium, player 1 of fair or good condition will not sell!
- There is a Bayesian Nash equilibrium in which player 1 of poor condition sells: $p=10$ and for $\theta \in\{P, F, G\}$,

$$
s_{1}^{\theta}(p)= \begin{cases}a, & \text { if } p \geq v_{1}(\theta) \\ r, & \text { if } p<v_{1}(\theta)\end{cases}
$$

- The market consists of only the sellers with the lowest quality due to asymmetric information.
- Consequently, trade is not efficient!


## Applications

## Adverse selection

- This observation is first made by George Akerlof who won the Nobel Prize because of this contribution.
- The phenomenon in this example is called adverse selection.
- Good sellers are out of the market and bad sellers stay.
- Asymmetric information selects those sellers that are adverse to the buyer.
- More generally, in an environment with asymmetric information, the informed party usually behaves adversely to the uniformed party.


## Applications

## Adverse selection

George A. Akerlof

The Sveriges Riksbank Prize in Economic

![](https://cdn.mathpix.com/cropped/2024_09_09_605858d45802b61328b8g-330.jpg?height=457&width=308&top_left_y=286&top_left_x=77)
Sciences in Memory of Alfred Nobel 2001
"for their analyses of markets with asymmetric information"

Contribution: Studied markets where sellers of products have more information than buyers about product quality. He showed that low-quality products may squeeze out high-quality products in such markets, and that prices of high-quality products may suffer as a result.

## Applications

## Committee voting

- A jury is made up of two players (jurors) who must collectively decide whether to acquit $(A)$ or to convict $(C)$ a defendant.
- The process calls for each player to cast a sealed vote, and the defendant is convicted only if both vote $C$.
- There is uncertainty about whether the defendant is guilty $(G)$ or innocent $(I)$.
- The prior probability that the defendant is guilty is given by $q>\frac{1}{2}$.
- Each player cares about making the right decision:

| $G$ | $A$ | $C$ |
| :---: | :---: | :---: |
| $A$ | 0,0 | 0,0 |
| $C$ | 0,0 | 1,1 |
|  |  |  |


|  | $A$ | $C$ |
| :---: | :---: | :---: |
| $A$ | 1,1 | 1,1 |
| $C$ | 1,1 | 0,0 |
|  |  |  |

## Applications

## Committee voting

- If the only information available to the players is the prior probability, then it is a game with symmetric incomplete information and can be conveniently thought of as a game of complete information:

\$\$

\$\$
- Two Nash equilibria: $(A, A)$ and $(C, C)$.

## Applications

## Committee voting

- Now assume each player $i$ receives a private signal $\theta_{i} \in\left\{\theta_{G}, \theta_{I}\right\}$ distributed according to

$$
\mathbb{P}\left(\theta_{i}=\theta_{G} \mid G\right)=\mathbb{P}\left(\theta_{i}=\theta_{I} \mid I\right)=p>\frac{1}{2}
$$

and

$$
\mathbb{P}\left(\theta_{i}=\theta_{I} \mid G\right)=\mathbb{P}\left(\theta_{i}=\theta_{G} \mid I\right)=1-p
$$

- So signal $\theta_{x}$ is more likely in state $x \in\{G, I\}$.
- The larger $p$ is, the more informative is the signal.
- Assume also that the players' signals are conditionally independent:

$$
\mathbb{P}\left(\theta_{1}=\theta_{x}, \theta_{2}=\theta_{y} \mid z\right)=\mathbb{P}\left(\theta_{1}=\theta_{x} \mid z\right) \mathbb{P}\left(\theta_{2}=\theta_{y} \mid z\right)
$$

for $x, y, z \in\{G, I\}$.

- This defines a Bayesian game.


## Applications

Committee voting

- What would player 1 do if there is no player 2?
- After observing signal $\theta_{1}=\theta_{G}$, player 1's posterior belief that the defendant is guilty is

$$
\mathbb{P}\left(G \mid \theta_{1}=\theta_{G}\right)=\frac{q p}{q p+(1-q)(1-p)}>q>\frac{1}{2}
$$

- Thus, player 1 is even more convinced that the defendant is guilty and hence will choose to convict him.


## Applications

## Committee voting

- After observing signal $\theta_{1}=\theta_{I}$, player 1 's posterior belief becomes

$$
\mathbb{P}\left(G \mid \theta_{1}=\theta_{I}\right)=\frac{q(1-p)}{q(1-p)+(1-q) p}<q
$$

- Thus, player 1 is less confident that the defendant is guilty.
- In particular,
- if $p>q$, player 1 acquit the defendant;
- if $p<q$, player 1 convict the defendant.
- Intuition: when $p$ is large, the signal is very informative. Hence, player 1 is convinced that the defendant is not guilty after observing signal $\theta_{1}=\theta_{I}$.


## Applications

Committee voting

- Is voting according to one's own signal a Bayesian Nash equilibrium?
- Assume $\sigma_{2}\left(\theta_{G}\right)=c$ and $\sigma_{2}\left(\theta_{I}\right)=a$.
- Assume player 1 receives signal $\theta_{1}=\theta_{I}$. His posterior belief is given by

|  | $\theta_{2}=\theta_{G}$ | $\theta_{2}=\theta_{I}$ |
| :---: | :---: | :---: |
| G | $\frac{q(1-p) p}{\mathbb{P}\left(\theta_{1}=\theta_{I}\right)}$ | $\frac{q(1-p)^{2}}{\mathbb{P}\left(\theta_{1}=\theta_{I}\right)}$ |
| I | $\frac{(1-q) p(1-p)}{\operatorname{N}(0}$ | $\frac{(1-q) p^{2}}{\mathbb{P}\left(\theta_{1}=\theta_{I}\right)}$ |

where $\mathbb{P}\left(\theta_{1}=\theta_{I}\right)=q p^{2}+q p(1-p)+(1-q)(1-p)^{2}+(1-q)(1-p) p$.

## Applications

## Committee voting

- If player 1 chooses to acquit, his payoff is

$$
\frac{(1-q) p(1-p)+(1-q) p^{2}}{\mathbb{P}\left(\theta_{1}=\theta_{I}\right)}
$$

- If instead, he convicts, then his payoff is

$$
\frac{q(1-p) p+(1-q) p^{2}}{\mathbb{P}\left(\theta_{1}=\theta_{I}\right)}
$$

- Therefore, player 1 should convict, not acquit!
- Voting according to one's own signal is NOT a Bayesian Nash equilibrium.


## Applications

Committee voting

- Given $\sigma_{2}$, player 1 is pivotal only if $\theta_{2}=\theta_{G}$.
- Therefore, when comparing $a$ and $c$, player 1 only needs to compare

$$
\mathbb{P}\left(G, \theta_{2}=\theta_{G} \mid \theta_{1}=\theta_{I}\right)
$$

and

$$
\mathbb{P}\left(I, \theta_{2}=\theta_{G} \mid \theta_{1}=\theta_{I}\right)
$$

- Although it is possible $\mathbb{P}\left(G \mid \theta_{1}=\theta_{I}\right)<\mathbb{P}\left(I \mid \theta_{1}=\theta_{I}\right)$ (when $\left.p>q\right)$, but we always have

$$
\mathbb{P}\left(G, \theta_{2}=\theta_{G} \mid \theta_{1}=\theta_{I}\right)>\mathbb{P}\left(I, \theta_{2}=\theta_{G} \mid \theta_{1}=\theta_{I}\right)
$$

## Applications

Committee voting

- Another way to see the above inequality is

$$
\begin{aligned}
& \frac{\mathbb{P}\left(G, \theta_{2}=\theta_{G} \mid \theta_{1}=\theta_{I}\right)}{\mathbb{P}\left(I, \theta_{2}=\theta_{G} \mid \theta_{1}=\theta_{I}\right)} \\
= & \frac{\mathbb{P}\left(G \mid \theta_{1}=\theta_{I}, \theta_{2}=\theta_{G}\right)}{\mathbb{P}\left(I \mid \theta_{1}=\theta_{I}, \theta_{2}=\theta_{G}\right)} \\
= & \frac{\mathbb{P}\left(G, \theta_{1}=\theta_{I}, \theta_{2}=\theta_{G}\right)}{\mathbb{P}\left(I, \theta_{1}=\theta_{I}, \theta_{2}=\theta_{G}\right)} \\
= & \frac{q(1-p) p}{(1-q) p(1-p)}>1 .
\end{aligned}
$$

- That is, given both $\theta_{1}=\theta_{I}$ and $\theta_{2}=\theta_{G}$, player 1 thinks $G$ is more likely.


## Applications

## Purification: Harsanyi's interpretation of mixed strategies

- Consider the game of Matching Pennies:

\$\$

\$\$

Figure 4.2: The Matching Pennies

- Unique Nash equilibrium: $\sigma_{1}=\sigma_{2}=\frac{1}{2} \circ H+\frac{1}{2} \circ T$.
- In equilibrium, every player is indifferent between $H$ and $T$.
- Yet, they are prescribed to randomize between these strategies in a unique, particular, and precise way, i.e., half-half, for this to be a Nash.
- Does it make sense to expect such precision when a player is indifferent?


## Applications

## Purification: Harsanyi's interpretation of mixed strategies

- Harsanyi's solution: players may not mix. In fact, they may always have some slight preference for choosing $H$ over $T$ or choosing $T$ over $H$. We, as an observer, think that players are mixing because we do not have precise information about the players' preferences.


## Applications

## Purification: Harsanyi's interpretation of mixed strategies

- Consider the following "perturbed " Matching Pennies:

|  | $H$ | $T$ |
| :---: | :---: | :---: |
| $H$ | $1+\varepsilon_{1},-1+\varepsilon_{2}$ | $-1+\varepsilon_{1}, 1$ |
| $T$ | $-1,1+\varepsilon_{2}$ | $1,-1$ |
|  |  |  |

Figure 4.3: The perturbed Matching Pennies

- Imagine that $\varepsilon_{1}$ and $\varepsilon_{2}$ are random variables that are independently and uniformly distributed on the interval $[-\varepsilon, \varepsilon]$ for some small $\varepsilon>0$.
- For an example, suppose player 2 plays $H$ with probability $1 / 2$.
- If player 1 plays $H$, his payoff is $\varepsilon_{1}$. If he plays $T$, his payoff is 0 .
- Thus, player 1 strictly prefers $H$ when $\varepsilon_{1}>0$, while he strictly prefers $T$ when $\varepsilon_{1}<0$.


## Applications

## Purification: Harsanyi's interpretation of mixed strategies

- Suppose now that $\varepsilon_{i}$ is player $i$ 's private information.
- This defines a Bayesian game.
- A strategy for player $i$ is a mapping $\sigma_{i}:[-\varepsilon, \varepsilon] \rightarrow[0,1]$, where $\sigma_{i}\left(\varepsilon_{i}\right)$ is the probability of choosing $H$ when $i$ 's type is $\varepsilon_{i}$.
- Consider an arbitrary $\sigma_{i}$. From player $j$ 's point of view, the probability that player $i$ plays $H$ is

$$
p^{\sigma_{i}} \equiv \int_{-\varepsilon}^{\varepsilon} \sigma_{i}\left(\varepsilon_{i}\right) f\left(\varepsilon_{i}\right) \mathrm{d} \varepsilon_{i}=\frac{1}{2 \varepsilon} \int_{-\varepsilon}^{\varepsilon} \sigma_{2}\left(\varepsilon_{2}\right) \mathrm{d} \varepsilon_{i}
$$

where $f\left(\varepsilon_{i}\right)=\frac{1}{2 \varepsilon}$ is the density of uniform distribution.

## Applications

Purification: Harsanyi's interpretation of mixed strategies

- Consider player 1 of type $\varepsilon_{1}$.
- If he plays $H$, his payoff is

$$
\left(1+\varepsilon_{1}\right) p^{\sigma_{2}}+\left(-1+\varepsilon_{1}\right)\left(1-p^{\sigma_{2}}\right)=2 p^{\sigma_{2}}-1+\varepsilon_{1}
$$

- If he plays $T$, his payoff is

$$
-p^{\sigma_{2}}+\left(1-p^{\sigma_{2}}\right)=-2 p^{\sigma_{2}}+1
$$

- Therefore, if $\sigma_{1}$ is a best reply, we must have

$$
\sigma_{1}\left(\varepsilon_{1}\right)= \begin{cases}1, & \text { if } \varepsilon_{1}>2-4 p^{\sigma_{2}} \\ 0, & \text { if } \varepsilon_{1}<2-4 p^{\sigma_{2}}\end{cases}
$$

- Then, we can calculate

$$
p^{\sigma_{1}}= \begin{cases}1, & \text { if } 2-4 p^{\sigma_{2}} \leq-\varepsilon \\ \frac{\varepsilon-2+4 p^{\sigma_{2}}}{2 \varepsilon}, & \text { if }-\varepsilon<2-4 p^{\sigma_{2}}<\varepsilon \\ 0, & \text { if } 2-4 p^{\sigma_{2}} \geq \varepsilon\end{cases}
$$

## Applications

Purification: Harsanyi's interpretation of mixed strategies

- Similarly, if $\sigma_{2}$ is a best reply to $\sigma_{1}$, we must have

$$
\sigma_{2}\left(\varepsilon_{2}\right)= \begin{cases}1, & \text { if } \varepsilon_{2}>4 p^{\sigma_{1}}-2 \\ 0, & \text { if } \varepsilon_{2}<4 p^{\sigma_{1}}-2\end{cases}
$$

- Then, we can calculate

$$
p^{\sigma_{2}}= \begin{cases}1, & \text { if } 4 p^{\sigma_{1}}-2 \leq-\varepsilon \\ \frac{\varepsilon+2-4 p^{\sigma_{1}}}{2 \varepsilon}, & \text { if }-\varepsilon<4 p^{\sigma_{1}}-2<\varepsilon \\ 0, & \text { if } 4 p^{\sigma_{1}}-2 \geq \varepsilon\end{cases}
$$

## Applications

## Purification: Harsanyi's interpretation of mixed strategies

- Thus, if $\left(\sigma_{1}, \sigma_{2}\right)$ is a Bayesian Nash equilibrium, $p^{\sigma_{1}}$ and $p^{\sigma_{2}}$ must simultaneously solve equations (4.6) and (4.7).
- When $\varepsilon<2$, the unique solution is

$$
p^{\sigma_{1}}=p^{\sigma_{2}}=\frac{1}{2}
$$

- Therefore, there is a (essentially) unique Bayesian Nash equilibrium $\left(\sigma_{1}^{*}, \sigma_{2}^{*}\right)$ of this perturbed matching pennies:

$$
\sigma_{i}^{*}\left(\varepsilon_{i}\right)= \begin{cases}H, & \text { if } \varepsilon_{i}>0 \\ T, & \text { if } \varepsilon_{i}<0\end{cases}
$$

- The word "essentially" means the fact that any arbitrary specification of $\sigma_{i}^{*}(0)$ is fine.


## Applications

## Purification: Harsanyi's interpretation of mixed strategies

- Notice that, in this unique equilibrium, every player "always" has strictly preference between $H$ and $T$, and consequently plays a pure strategy.
- The only situation where a player is indifferent between $H$ and $T$ is when his type is 0 . But this event occurs with probability 0 .
- Moreover, since $p^{\sigma_{1}}=p^{\sigma_{2}}=1 / 2$, each player plays $H$ half of the time.
- In other words, their behavior looks as though they are mixing between $H$ and $T$ with equal probabilities, from an outside observer's point view who does not observe players' private information.
- Purification: mixed strategy Nash equilibrium of a complete information game can be purified by a nearby incomplete information game.


## Auctions

Common auction formats

- English auction: open ascending price auction
- Dutch auction: open descending price auction
- First-price sealed-bid auction
- Second-price sealed bid auction
- William Vickrey was the first to analyze auctions using formal game theory tools.


## Auctions

## Common auction formats

William Vickrey
The Sveriges Riksbank Prize in Economic
Sciences in Memory of Alfred Nobel 1996
"for their fundamental contributions to the
economic theory of incentives under asymmetric
information."
Contribution: Developed methods of analyzing
the problems of incomplete, or asymmetrical,
information. Specialized in auction theory.
William Vickrey
The Sveriges Riksbank Prize in Economic Sciences in Memory of Alfred Nobel 1996
"for their fundamental contributions to the economic theory of incentives under asymmetric information."

Contribution: Developed methods of analyzing the problems of incomplete, or asymmetrical, information. Specialized in auction theory.

## Auctions

Auctions with independent private values

- We will model auctions as Bayesian games, as Vickrey did.
- In a Bayesian game of auction, if bidders' types are distributed independently, we say it is an independent type environment; otherwise, we say it is a correlated type environment.
- Moreover, if each bidder's own type completely determines his willingness to pay, we say it is a private value environment; otherwise it is an interdependent value environment.
- We will mainly focus on the independent private value (IPV) environment in what follows, until the last subsection in which we consider independent common value auction which is a special case of independent interdependent value environment.


## Auctions

## Second-price sealed-bid auctions and English auctions

- There are $n$ bidders.
- Each bidder has a valuation $\theta_{i}$ (willingness to pay) about the object being sold.
- Bidder $i$ 's valuation is his private information.
- Thus, each valuation is a type of bidder $i$.
- Assume $\theta_{i}$ is drawn from the interval $\left[\underline{\theta}_{i}, \bar{\theta}_{i}\right]$ with $\operatorname{cdf} F_{i}$ and density $f_{i}$.
- Valuations among the bidders are drawn independently.
- Thus we are in the IPV setting.


## Auctions

## Second-price sealed-bid auctions and English auctions

- In a second-price sealed-bid auction, the winning bidder pays his the second highest bid.
- Thus, the payoff for bidder $i$ is

$$
v_{i}\left(b_{i}, b_{-i} ; \theta_{i}\right)= \begin{cases}\frac{\theta_{i}-\text { max }_{j i j} b_{j}}{\left\{k k i b_{k}=\max _{j} b_{j}\right\}}, & \text { if } b_{i}=\max _{j} b_{j} \\ 0 & \text { if } b_{i}<\max _{j} b_{j}\end{cases}
$$

- In the case where several bidders bid the same highest price, the object is randomly allocated to each of them with equal probabilities.


## Auctions

## Second-price sealed-bid auctions and English auctions

- The second price auction has a very appealing feature, as we see now.
- Consider bidder $i$ of type $\theta_{i}$.
- For any $b_{i} \neq \theta_{i}$, we have

$$
v_{i}\left(\theta_{i}, b_{-i} ; \theta_{i}\right) \geq v_{i}\left(b_{i}, b_{-i} ; \theta_{i}\right), \forall b_{-i}
$$

and there exists $b_{-i}$ such that

$$
v_{i}\left(\theta_{i}, b_{-i} ; \theta_{i}\right)>v_{i}\left(b_{i}, b_{-i} ; \theta_{i}\right)
$$

- Condition (4.8) says that bidding one own valuation is always as least as good as any other bid.
- Condition (4.9) says that for any other bid, bidding one's own valuation is sometimes strictly better.


## Auctions

## Second-price sealed-bid auctions and English auctions

- To see why (4.8) and (4.9) hold, consider any $b_{i}<\theta_{i}$ first.
- Then, it is easy to see that for $b_{-i}$ such that $\max _{j \neq i} b_{j}<b_{i}$ or $\max _{j \neq i} b_{j} \geq \theta_{i}$,

$$
v_{i}\left(b_{i}, b_{-i} ; \theta_{i}\right)=v_{i}\left(\theta_{i}, b_{-i} ; \theta_{i}\right)
$$

- For $b_{-i}$ such that $b_{i} \leq \max _{j \neq i} b_{j}<\theta_{i}$,

$$
v_{i}\left(b_{i}, b_{-i} ; \theta_{i}\right)<v_{i}\left(\theta_{i}, b_{-i} ; \theta_{i}\right)
$$

## Auctions

## Second-price sealed-bid auctions and English auctions

- Now, consider $b_{i}>\theta_{i}$.
- Then, for $b_{-i}$ such that $\max _{j \neq i} b_{j} \leq \theta_{i}$ or $\max _{j \neq i} b_{j}>b_{i}$, we have

$$
v_{i}\left(b_{i}, b_{-i} ; \theta_{i}\right)=v_{i}\left(\theta_{i}, b_{-i} ; \theta_{i}\right)
$$

- For $b_{-i}$ such that $\theta_{i}<\max _{j \neq i} b_{j} \leq b_{i}$,

$$
v_{i}\left(b_{i}, b_{-i} ; \theta_{i}\right)<v_{i}\left(\theta_{i}, b_{-i} ; \theta_{i}\right)
$$

- Therefore, (4.8 and (4.9) hold.
- We say that bidding one's own valuation is a weakly dominant strategy.


## Auctions

## Second-price sealed-bid auctions and English auctions

- It should then be easy to understand that in the Bayesian game of second price auction, every bidder biding his own valuation is a Bayesian Nash equilibrium.
- This is because $s_{i}\left(\theta_{i}\right)=\theta_{i}$ is a best response to any $s_{-i}$ : for $\theta_{i}$,

$$
\mathbb{E}_{\theta_{-i}}\left(v_{i}\left(\theta_{i}, s_{-i}\left(\theta_{-i}\right) ; \theta_{i}\right)\right) \geq \mathbb{E}_{\theta-i}\left(v_{i}\left(b_{i}, s_{-i}\left(\theta_{-i}\right) ; \theta_{i}\right)\right), \forall b_{i}
$$

## Auctions

## Second-price sealed-bid auctions and English auctions

- Three properties:
- Bidders in a second price auction do not care about the probability distribution over their opponents' types. Thus, the result holds even if bidders have no idea about their opponents' valuations.
- In the private value setting, the same result still applies even if types among bidders are correlated.
- The equilibrium outcome is efficient: the one with the highest value wins and obtains the object.


## Auctions

## Second-price sealed-bid auctions and English auctions

- English auction seems more difficult to analyze.
- But we can think about it in the following way.
- At the beginning of the auction, all the bidders raise their hands.
- Then the auctioneer continuously increasing the price, starting at $p=0$.
- If a bidder thinks the current price is too high that he is not willing to pay for the object, he simply put down his hand.
- This means "I drop out."
- As long as there are more than one bidders who still keep their hands up in the air, the auctioneer keeps raising the price.
- Once the penultimate bidder drops out, the auctioneer stops and the auction ends.
- The only bidder who still raise his hand wins the auction and pays the current price.


## Auctions

## Second-price sealed-bid auctions and English auctions

- The only possible difference between English auction in reality and this "hands-up" game is that in English auction there might be a minimum incremental requirement while in this game, the auction immediately ends if there is only one bidder left.
- It is also easy to see that this "hands-up" game is equivalent to the second-price auction.
- Thus, biding one's own valuation is a Bayesian Nash equilibrium.


## Auctions

## First-price sealed-bid auctions and Dutch auctions

- In a first-price sealed-bid auction, the winning bidder pays his own bid.
- Thus, the payoff for bidder $i$ is

$$
v_{i}\left(b_{i}, b_{-i} ; \theta_{i}\right)= \begin{cases}\frac{\theta_{i}-b_{i}}{\left|\left\{k \mid b_{k}=\max _{j} b_{j}\right\}\right|}, & \text { if } b_{i}=\max _{j} b_{j} \\ 0, & \text { if } b_{i}<\max _{j} b_{j}\end{cases}
$$

- As before, if there is a tie in the winning bid, the object is randomly allocated to all the winning bidders with equal probabilities.


## Auctions

## First-price sealed-bid auctions and Dutch auctions

- In this first price auction, bidding one's own valuation is not a dominant strategy.
- Always bidding one's own valuation yields payoff 0 .
- However, if bidder bids slightly lower than his own valuation, then intuitively, there is positive probability that he would obtain this object, in which case he can get positive payoff.
- Then, can we find a Bayesian Nash equilibrium?


## Auctions

## First-price sealed-bid auctions and Dutch auctions

- Since higher type means higher willingness to pay, it is intuitive that bidder with a higher type will bid a higher price.
- Thus, let's guess that there is a Bayesian Nash equilibrium in which every bidder's strategy is strictly increasing.
- That is, in this Bayesian Nash equilibrium $\left(s_{1}, \ldots, s_{n}\right)$, for all $i$,

$$
s_{i}\left(\theta_{i}\right)<s_{i}\left(\theta_{i}^{\prime}\right), \forall \theta_{i}<\theta_{i}^{\prime}
$$

## Auctions

## First-price sealed-bid auctions and Dutch auctions

- Let's now consider the best response of bidder $i$ of type $\theta_{i}$, given $s_{-i}$.
- If $\theta_{i}$ bids $b_{i}$, he is the only winner if and only if

$$
s_{j}\left(\theta_{j}\right)<b_{i}, \forall j \neq i
$$

- Since $s_{j}$ is strictly increasing for all $j$, the above condition is equivalent to

$$
\theta_{j}<s_{j}^{-1}\left(b_{i}\right), \quad \forall j \neq i
$$

where $s_{j}^{-1}$ is the inverse of $s_{j}$.

- Thus, the probability that $\theta_{i}$ with bid $b_{i}$ is the only winner is

$$
\mathbb{P}\left(\theta_{j}<s_{j}^{-1}\left(b_{i}\right), \quad \forall j \neq i\right)=\prod_{j \neq i} \mathbb{P}\left(\theta_{j}<s_{j}^{-1}\left(b_{i}\right)\right)=\prod_{j \neq i} F_{j}\left(s_{j}^{-1}\left(b_{i}\right)\right)
$$

where the first equality comes from independence of valuations among the bidders.

## Auctions

## First-price sealed-bid auctions and Dutch auctions

- Given $s_{j}$ is strictly increasing for all $j$, the probability that bidder $i$ wins but is not the only winner is zero.
- Therefore, the expected payoff of $\theta_{i}$ with bid $b_{i}$ is

$$
\prod_{j \neq i} F_{j}\left(s_{j}^{-1}\left(b_{i}\right)\right) \times\left(\theta_{i}-b_{i}\right)
$$

- Trade-off: higher bid leads to higher probability of winning but at the same time to higher price.
- To go further, let's assume that $s_{j}$ is differentiable.
- Since $b_{i}=s_{i}\left(\theta_{i}\right)$ maximizes this expected payoff, if it is interior, it must satisfy the first order condition:
$-\prod_{j \neq i} F_{j}\left(s_{j}^{-1}\left(b_{i}\right)\right)+\left.\left(\theta_{i}-b_{i}\right) \sum_{j \neq i}\left[\frac{f_{j}\left(s_{j}^{-1}\left(b_{i}\right)\right)}{s_{j}^{\prime}\left(s_{j}^{-1}\left(b_{i}\right)\right)} \prod_{k \neq i, j} F_{k}\left(s_{k}^{-1}\left(b_{i}\right)\right)\right]\right|_{b_{i}=s_{i}\left(\theta_{i}\right)}=0$.


## Auctions

## First-price sealed-bid auctions and Dutch auctions

- Assume that the value distribution $F_{j}$ is the same for all bidders.
- In particular, assume $F_{j}=F$ and $f_{j}=f$ for some cdf $F$ and its density $f$ over $[\underline{\theta}, \bar{\theta}]$.
- Then, it is intuitive that we should have a symmetric equilibrium:

$$
s_{1}=s_{2}=\ldots=s_{n}=s
$$

for some $s$.

- Under this assumption, $s_{j}^{-1}\left(s_{i}\left(\theta_{i}\right)\right)=\theta_{i}$.
- Then, the above first order condition is simplified to (we drop subscript $i$ on $\theta_{i}$ )

$$
-F^{n-1}(\theta)+(n-1)(\theta-s(\theta)) \frac{f(\theta) F^{n-2}(\theta)}{s^{\prime}(\theta)}=0
$$

## Auctions

## First-price sealed-bid auctions and Dutch auctions

- The above formula gives us a differential equation

$$
F^{n-1}(\theta) s^{\prime}(\theta)+(n-1) f(\theta) F^{n-2}(\theta) s(\theta)=(n-1) \theta f(\theta) F^{n-2}(\theta)
$$

- Integrating on both sides yields

$$
\begin{aligned}
F^{n-1}(\theta) s(\theta) & =\int_{\underline{\theta}}^{\theta}(n-1) x f(x) F^{n-2}(x) \mathrm{d} x+k \\
& =\left.x F^{n-1}(x)\right|_{x=\underline{\theta}} ^{\theta}-\int_{\underline{\theta}}^{\theta} F^{n-1}(x) \mathrm{d} x+k \\
& =\theta F^{n-1}(\theta)-\int_{\underline{\theta}}^{\theta} F^{n-1}(x) \mathrm{d} x+k
\end{aligned}
$$

where the second equality comes from integration by parts and $k$ is some constant.

- Since $F(\underline{\theta})=0$, evaluating both sides at $\theta=\underline{\theta}$, we obtain $k=0$.


## Auctions

## First-price sealed-bid auctions and Dutch auctions

- Therefore,

$$
s(\theta)=\theta-\frac{\int_{\theta}^{\theta} F^{n-1}(x) \mathrm{d} x}{F^{n-1}(\theta)}
$$

- Notice that it is easy to see that $s$ is strictly increasing and differentiable.
- Thus, we found a symmetric Bayesian Nash equilibrium in this symmetric first price auction.
- Each bidder of any valuation bids strictly lower than his valuation.
- Note also that this equilibrium is also efficient: the one with the highest valuation obtains the object. This is because we focused on equilibrium with increasing strategies.


## Auctions

## First-price sealed-bid auctions and Dutch auctions

- For example, if $F$ is uniform distribution over $[0,1]$, then

$$
s(\theta)=\theta-\frac{\theta^{n}}{n \theta^{n-1}}=\frac{n-1}{n} \theta .
$$

- We can also directly verify that this is a Bayesian Nash equilibrium.
- Given $s_{2}=\ldots=s_{n}=s$, bidder 1 with valuation $\theta_{1}$ 's expected payoff can be written as

$$
\begin{cases}0, & \text { if } b_{1} \leq 0 \\ \left(\frac{n b_{1}}{n-1}\right)^{n-1}\left(\theta_{1}-b_{1}\right), & \text { if } b_{1} \in\left(0, \frac{n-1}{n}\right) \\ \theta_{1}-b_{1}, & \text { if } b_{1} \geq \frac{n-1}{n}\end{cases}
$$

- Then, it is optimal for $\theta_{1}$ to bid $(n-1) \theta_{1} / n$.


## Auctions

## First-price sealed-bid auctions and Dutch auctions

- The Dutch and first price auctions are closely related in the same way that the English and second price auctions are.
- Each bidder in a Dutch auction thinks about at what price he will jump in and announce that he will buy, as in a first price auction each bidder considers a bid.
- Lower price leads to higher gain conditional on winning.
- But at the same time, lower price faces the risk of someone else jumping in, which reduces the probability of winning.
- Thus, the Dutch and the first price auctions are strategically equivalent. They have the same normal form and as a consequence have the same set of Bayesian Nash equilibria.


## Auctions

## Revenue Equivalence

- We have analyzed both first price and second price auctions from the bidder's point of view, i.e., Bayesian Nash equilibrium.
- But from the seller/auctioneer's point of view, which of these two auction formats bring higher revenue?
- To illustrate the idea, let's assume the symmetric environment where $F$ is a uniform distribution over $[0,1]$.


## Auctions

## Revenue Equivalence

- Consider the second price auction first.
- In the Bayesian Nash equilibrium, every bidder bids his own valuation and pays the second highest valuation.
- Given $\left(\theta_{1}, \ldots, \theta_{n}\right) \in[0,1]^{n}$, let $\theta^{[2]}$ be the second highest value among them.
- Since $\theta_{1}, \ldots, \theta_{n}$ are random variables taking values in $[0,1]$, so is $\theta_{n}^{[2]}$.
- It is called the second-order statistic of the $n$ random variables $\theta_{1}, \ldots, \theta_{n}$.
- Note that $\theta_{n}^{[2]}$ is the just the seller's revenue in the second price auction.


## Auctions

## Revenue Equivalence

- For any $x \in[0,1]$,

$$
\begin{aligned}
F_{n}^{[2]}(x) & =\mathbb{P}\left(\theta_{n}^{[2]} \leq x\right) \\
& =\mathbb{P}\left(\bigcup_{i=1}^{n}\left(\theta_{i}>x, \theta_{j} \leq x, \forall j \neq i\right)\right)+\mathbb{P}\left(x_{i} \leq x, \forall i\right) \\
& =\sum_{i=1}^{n} \mathbb{P}\left(\theta_{i}>x, \theta_{j} \leq x, \forall j \neq i\right)+\mathbb{P}\left(x_{i} \leq x, \forall i\right) \\
& =\sum_{i=1}^{n}(1-F(x)) F(x)^{n-1}+F(x)^{n} \\
& =n F^{n-1}(x)-(n-1) F^{n}(x)
\end{aligned}
$$

- This is the cdf of $\theta_{n}^{[2]}$.


## Auctions

## Revenue Equivalence

- The corresponding density is

$$
f_{n}^{[2]}(x)=n(n-1) F^{n-2}(x) f(x)-n(n-1) F^{n-1}(x) f(x)
$$

- For uniform distribution, we have

$$
F_{n}^{[2]}(x)=n x^{n-1}-(n-1) x^{n}
$$

and

$$
f_{n}^{[2]}(x)=n(n-1) x^{n-2}-n(n-1) x^{n-1}
$$

- Then, the seller's expected revenue is

$$
\mathbb{E}\left(\theta_{n}^{[2]}\right)=\int_{0}^{1} x f_{n}^{[2]}(x) \mathrm{d} x=(n-1)-\frac{n(n-1)}{n+1}=\frac{n-1}{n+1}
$$

## Auctions

## Revenue Equivalence

- We now turn to the first price auction.
- In the symmetric equilibrium, each bidder bids according $s(\theta)=\frac{n-1}{n} \theta$.
- Note that each $s$ is a random variable with uniform distribution over $\left[0, \frac{n-1}{n}\right]$.
- For $\left(b_{1}, \ldots, b_{n}\right) \in\left[0, \frac{n-1}{n}\right]^{n}$, let $b_{n}^{[1]}$ be the highest bid among them

$$
b_{n}^{[1]}=\max \left\{b_{1}, \ldots, b_{n}\right\}
$$

- Note that $b_{n}^{[1]}$ is the seller's revenue in the first price auction.


## Auctions

## Revenue Equivalence

- For any $x \in\left[0, \frac{n-1}{n}\right]$,

$$
\begin{aligned}
F_{n}^{[1]}(x) & =\mathbb{P}\left(b_{n}^{[1]} \leq x\right) \\
& =\mathbb{P}\left(b_{i} \leq x, \forall i\right) \\
& =\left(\frac{n x}{n-1}\right)^{n}
\end{aligned}
$$

- This is the cdf of $b_{n}^{[1]}$.
- The corresponding density is

$$
f_{n}^{[1]}(x)=\frac{n^{2}}{n-1}\left(\frac{n x}{n-1}\right)^{n-1}
$$

## Auctions

## Revenue Equivalence

- Then, the seller's expected revenue from the first price auction is

$$
\mathbb{E}\left(b_{n}^{[1]}\right)=\int_{0}^{\frac{n-1}{n}} x f_{n}^{[1]}(x) \mathrm{d} x=\frac{n-1}{n+1}
$$

- This is exactly the same as that in the second price auction!


## Auctions

## Revenue Equivalence

- We have demonstrated one of the fundamental results in auction theory: the revenue equivalence theorem.
- In the IPV setting, any auction game that satisfies the following four conditions will yield the seller the same expected revenue:
- each bidder's type is drawn from a "well-behaved" distribution;
- bidders are risk neutral;
- the bidder with the highest type wins; and
- the bidder with the lowest possible type has an expected payoff of zero.
- It was first found by Vikerey and then generalized by Roger Myerson.


## Auctions

## Revenue Equivalence

Roger B. Myerson

The Sveriges Riksbank Prize in Economic Sciences in Memory of Alfred Nobel 2007
"for having laid the foundations of mechanism design theory."

Contribution: In the 1970s, the formulation of the "revelation principle" (a way of simplifying the search for a feasible mechanism) and implementation theory led to great advances of mechanism design. He developed this principle to perfection and pioneered its application to economic problems such as auctions and regulations.

## Auctions

## Common value auction

- Two bidders in a first price auction.
- The object has the same value to both of them.
- However, neither of them knows the precise value.
- In fact, each of them receives a signal about the true value.
- The signals are uniformly and independently distributed over $[0,1]$.
- Each bidder's signal is his private information.
- The value of the object to each of the bidder is

$$
v=t_{1}+t_{2}
$$

where $t_{i}$ is $i$ 's signal (type).

- This is an independent common value setting.


## Auctions

## Common value auction

- Each bidder's strategy is a mapping from types to bids, as always.
- Again, we look for Bayesian Nash equilibrium in which both bidders' strategies are strictly increasing.
- Given $s_{j}$, consider bidder $i$ of type $t_{i}$.
- If $i$ bids $b_{i}$, he wins if $j$ 's type satisfies $s_{j}\left(t_{j}\right)<b_{i}$
- Or equivalently, if $t_{j}<s_{j}^{-1}\left(b_{i}\right)$, in which case $i$ 's value is $t_{i}+t_{j}$.
- Thus, $i$ 's expected payoff is

$$
\int_{0}^{s_{j}^{-1}\left(b_{i}\right)}\left(t_{i}+t_{j}-b_{i}\right) \mathrm{d} t_{j}
$$

where we have used the uniform distribution assumption.

## Auctions

## Common value auction

- It is then easy to calculate

$$
\int_{0}^{s_{j}^{-1}\left(b_{i}\right)}\left(t_{i}+t_{j}-b_{i}\right) \mathrm{d} t_{j}=\left(t_{i}-b_{i}\right) s_{j}^{-1}\left(b_{i}\right)+\frac{1}{2}\left[s_{j}^{-1}\left(b_{i}\right)\right]^{2}
$$

- Assume $s_{j}$ is differentiable.
- If $s_{i}\left(t_{i}\right)$ is a best response, it must satisfy the first order condition:

$$
-s_{j}^{-1}\left(b_{i}\right)+\frac{t_{i}-b_{i}}{s_{j}^{\prime}\left(s_{j}^{-1}\left(b_{i}\right)\right)}+\left.\frac{s_{j}^{-1}\left(b_{i}\right)}{s_{j}^{\prime}\left(s_{j}^{-1}\left(b_{i}\right)\right)}\right|_{b_{i}=s_{i}\left(t_{i}\right)}=0
$$

- If it is a symmetric equilibrium, i.e., $s_{i}=s_{j}=s$, we have

$$
-t+\frac{t-s(t)}{s^{\prime}(t)}+\frac{t}{s^{\prime}(t)}=0
$$

or equivalently

$$
t s^{\prime}(t)+s(t)=2 t
$$

## Auctions

## Common value auction

- Integrating on both sides yields

$$
t s(t)=t^{2}+k
$$

where $k$ is a constant.

- Evaluating both sides at $t=0$ implies $k=0$.
- Therefore, we have found a symmetric Bayesian Nash equilibrium:

$$
s_{1}(t)=s_{2}(t)=t
$$

## Auctions

## Common value auction

- In this equilibrium, bidder 1 of type $t_{1}$ estimates that the value of the object is

$$
t_{1}+\mathbb{E} t_{2}=t_{1}+\frac{1}{2}
$$

and bids $t_{1}$.

- Now suppose this bidder indeed wins the auction.
- Then, he should understand that he wins the auction because his opponent's type is lower than $t_{1}$.
- With this additional information, he should revise his estimate about the value

$$
t_{1}+\mathbb{E}\left(t_{2} \mid t_{2}<t_{1}\right)=t_{1}+\frac{\int_{0}^{t_{1}} t_{2} \mathrm{~d} t_{2}}{\mathbb{P}\left(t_{2}<t_{1}\right)}=t_{1}+\frac{t_{1}}{2}<t_{1}+\frac{1}{2}!
$$

## Auctions

## Common value auction

- Winning is "bad news"!
- The fact that one wins tells himself that he has overestimated the value of the object.
- This phenomenon, which occurs in common-value settings, is known as the winner's curse.


## Auctions

Common value auction
Paul R. Milgrom

The Sveriges Riksbank Prize in Economic Sciences in Memory of Alfred Nobel 2020
"for improvements to auction theory and inventions of new auction formats."

Work: Robert Wilson and Paul Milgrom have studied how auctions work. They have also translated their theories into practice and created new auctions for goods and services that are difficult to sell through traditional means, such as radio frequencies. Their discoveries have benefited sellers, buyers and taxpayers around the world.

## Auctions

Common value auction
Robert B. Wilson

The Sveriges Riksbank Prize in Economic Sciences in Memory of Alfred Nobel 2020
"for improvements to auction theory and inventions of new auction formats."

Work: Robert Wilson and Paul Milgrom have studied how auctions work. They have also translated their theories into practice and created new auctions for goods and services that are difficult to sell through traditional means, such as radio frequencies. Their discoveries have benefited sellers, buyers and taxpayers around the world.

# Game Theory Lecture Notes 5 

## Dynamic Games with Incomplete Information

Ju Hu<br>National School of Development<br>Peking University

Fall 2022

## A Motivating Example

The chain store game with complete information

![](https://cdn.mathpix.com/cropped/2024_09_09_605858d45802b61328b8g-388.jpg?height=387&width=331&top_left_y=155&top_left_x=458)

Figure 5.1: The chain-store game with complete information

- Nash equilibria: $(S, F)$ and $(E, A)$; only $(E, A)$ is subgame perfect.
- $(S, F)$ involves non-credible threat: the incumbent is not sequentially rational off the equilibrium path.
- Subgame perfection requires sequential rationality both on and off the equilibrium path; Nash does not.


## A Motivating Example

The chain store game with incomplete information

- Consider an incomplete variant of the above chain store game.
- The entrant may be a competent one $(C)$ or a weak one $(W)$.
- The probability of a competent entrant is $p$.
- The competent entrant's payoffs are the same as before.
- The weak entrant's payoffs are reduced (specified in Figure 5.2).
- Only the entrant knows its own type; the incumbent does not know.
- The entrant moves first as before; the incumbent moves after the entrant enters.
- Game tree?


## A Motivating Example

The chain store game with incomplete information

![](https://cdn.mathpix.com/cropped/2024_09_09_605858d45802b61328b8g-390.jpg?height=600&width=902&top_left_y=166&top_left_x=203)

Figure 5.2: The chain-store game with incomplete information

## A Motivating Example

The chain store game with incomplete information

- The entrant has two information sets.
- Every strategy of the entrant specifies an action for each of the information sets.
- Therefore, $S_{1}=\{S S, S E, E S, E E\}$.
- For instance, $E S$ is the strategy where the competent entrant enters and the weak entrant stays out.
- The incumbent has only one information set.
- Therefore, $S_{2}=\{F, A\}$.


## A Motivating Example

The chain store game with incomplete information

- The normal form representation:

|  | $F$ | $A$ |
| ---: | :---: | :---: |
| $S S$ | 0,2 | 0,2 |
| $S E$ | $-2(1-p), 2 p$ | $-(1-p), 2 p+(1-p)$ |
| $E S$ | $-p,-p+2(1-p)$ | $p, p+2(1-p)$ |
| $E E$ | $-p-2(1-p),-p$ | $p-(1-p), p+(1-p)$ |
|  |  |  |

- Make sure you understand how it is written down.


## A Motivating Example

The chain store game with incomplete information

- Consider the special case where $p=\frac{1}{2}$ :

|  | $F$ | $A$ |
| :---: | :---: | :---: |
| $S S$ | 0,2 | 0,2 |
| $S E$ | $-1,1$ | $-\frac{1}{2}, \frac{3}{2}$ |
| $E S$ | $-\frac{1}{2}, \frac{1}{2}$ | $\frac{1}{2}, \frac{3}{2}$ |
| $E E$ | $-\frac{3}{2},-\frac{1}{2}$ | 0,1 |
|  |  |  |

- Two pure strategy Nash equilibria: $(S S, F)$ and $(E S, A)$.
- Note that we can also formulate this extensive form game as a Bayesian game, and the above Nash equilibria are just the Bayesian Nash equilibria of this Bayesian game.
- Both equilibria are subgame perfect, but $(S S, F)$ involves non-credible behavior: $A$ is better than $F$ regardless of the entrant's type.


## A Motivating Example

The problem of SPE for games with incomplete information

- Subgame perfection has no bite in this game, because there are too few subgames.
- Only the whole game is a subgame. Thus, Nash is equivalent to SPE.
- This is due to the fact that although the incumbent observes the entrant's action, but it does not know the entrant's type.
- This is a common property of dynamic games with incomplete information.
- We want to find a way to extend the idea of sequential rationality to these games.


## Perfect Bayesian Equilibrium

## System of beliefs

- Recall the notion of on and off the equilibrium path.


## Definition 5.1

Let $\sigma^{*}=\left(\sigma_{1}^{*}, \ldots, \sigma_{n}^{*}\right)$ be a Bayesian Nash equilibrium profile of strategies in a game of incomplete information. We say that an information set is on the equilibrium path if given $\sigma^{*}$ and given the distribution of types, it is reached with positive probability. We say that an information set if off the equilibrium path if given $\sigma^{*}$ and the distribution of types, it is reached with zero probability.

- Every information set is on the path of play under $(E S, A)$.
- The incumbent's information set is off the path of play under $(S S, A)$.


## Perfect Bayesian Equilibrium

## System of beliefs

- Recall notation:
- $H$ the set of all information sets;
- $h \in H$ is one information set;
- $x \in h$ is a node in information set $h$.
- We now introduce the core notion: beliefs.


## Definition 5.2

A system of beliefs $\mu$ of an extensive-form game assigns a probability distribution over decision nodes to every information set. That is, for every information set $h \in H$ and every decision node $x \in h, \mu(x) \in[0,1]$ is the probability that player $i$ who moves in information set $h$ assigns to his being at $x$, where $\sum_{x \in h} \mu(x)=1$ for every $h \in H$.

- What is a system of beliefs for a game of perfect information?


## Perfect Bayesian Equilibrium

Four requirements for a Bayesian Nash equilibrium to be perfect

## Requirement 1

Every player will have a well-defined belief over where he is in each of his information sets. That is, the game will have a system of beliefs.

- Then, what kind of system of beliefs is reasonable?


## Perfect Bayesian Equilibrium

Four requirements for a Bayesian Nash equilibrium to be perfect

## Requirement 2 (Consistency)

Let $\sigma^{*}=\left(\sigma_{1}^{*}, \sigma_{2}^{*}, \ldots, \sigma_{n}^{*}\right)$ be a Bayesian Nash equilibrium profile of strategies. We require that in all information sets beliefs that are on the equilibrium path be consistent with Bayes' rule.

- Given $\sigma^{*}$ and the nature's move (type distribution), let $\mathbb{P}^{\sigma^{*}}(x)$ be the probability that node $x$ is reached.
- An information set $h$ is on the equilibrium path if and only if

$$
\mathbb{P}^{\sigma^{*}}(h) \equiv \sum_{x \in h} \mathbb{P}^{\sigma^{*}}(x)>0
$$

- In this case, Requirement 2 requires

$$
\mu(x)=\frac{\mathbb{P}^{\sigma^{*}}(x)}{\mathbb{P} \sigma^{*}(h)}, \forall x \in h
$$

## Perfect Bayesian Equilibrium

Four requirements for a Bayesian Nash equilibrium to be perfect

- What happens if $h$ is off the equilibrium path?
- This is equivalent to $\mathbb{P}^{\sigma^{*}}(h)=0$.
- Then, Bayes' rule does not apply. (Yes?)


## Requirement 3

At information sets that are off the equilibrium path, to which Bayes' rule does not apply, any belief can be assigned.

- That is, no requirement at all is imposed on the off path beliefs.


## Perfect Bayesian Equilibrium

Four requirements for a Bayesian Nash equilibrium to be perfect

- The last requirement is sequential rationality: best response to beliefs.


## Requirement 4 (Sequential Rationality)

Given their beliefs, players' strategies must be sequentially rational. That is, in every information set players will play a best response to their beliefs.

- Suppose $h$ is $i$ 's information set. Player $i$ 's strategy $\sigma_{i}$ is sequentially rational at $h$ given $\sigma_{-i}$ and $\mu$ if

$$
\mathbb{E}\left[v_{i}\left(\sigma_{i}, \sigma_{-i}, \theta\right) \mid h, \mu\right] \geq \mathbb{E}\left[v_{i}\left(s_{i}, \sigma_{-i}, \theta\right) \mid h, \mu\right], \forall s_{i}
$$

- In words, conditional on $h$ being reached, playing $\sigma_{i}$ is at least as good as every other strategy given $\sigma_{-i}$ and $\mu$.
- $(S S, F)$ in the previous example is not sequentially rational given any belief.


## Perfect Bayesian Equilibrium

Four requirements for a Bayesian Nash equilibrium to be perfect

- Imagine an information set in an extensive form game.

![](https://cdn.mathpix.com/cropped/2024_09_09_605858d45802b61328b8g-401.jpg?height=318&width=845&top_left_y=272&top_left_x=201)

Figure 5.3: Illustration of sequential rationality; payoffs are for player 2

- Regardless of $\mu \in[0,1], b$ is not optimal.
- Thus, $b$ at this information set is not sequentially rational to any belief.


# Perfect Bayesian Equilibrium 

Perfect Bayesian equilibrium

- Putting consistency and sequential rationality together leads to perfect Bayesian equilibrium.


## Definition 5.3

A Bayesian Nash equilibrium profile $\sigma^{*}=\left(\sigma_{1}^{*}, \ldots, \sigma_{n}^{*}\right)$ together with a system of beliefs $\mu$ constitutes a perfect Bayesian equilibrium for an n-player game if they satisfy requirements 1 - 4.

## Perfect Bayesian Equilibrium

## Perfect Bayesian equilibrium

- If all the information sets are on the path of play under a strategy profile, then this strategy profile is a perfect Bayesian equilibrium (given some belief system) if and only if it is a Bayesian Nash equilibrium.


## Proposition 5.1

If a profile of strategies $\sigma^{*}=\left(\sigma_{1}^{*}, \ldots, \sigma_{n}^{*}\right)$ is a Bayesian Nash equilibrium of a Bayesian game $\Gamma$, and if $\sigma^{*}$ induces all the information sets to be reached with positive probability, then $\sigma^{*}$, together with the belief system $\mu^{*}$ uniquely derived from $\sigma^{*}$ and the distribution of types, constitutes a perfect Bayesian equilibrium for $\Gamma$.

- Make sure you understand: if all information sets are on the path, there is only one consistent belief system.


## Signaling Games

## General idea

- An informed player interacts with an uninformed player.
- In some instances, it may be the informed player's interest to reveal his private information to the uninformed player.
- Can the informed player credibly signal his type and make the uninformed player believe him?
- Examples include:
- firm with high quality product signal its quality by providing long-term warranty;
- the owner of a company keeps control of a significant percentage of the company when going public;
- rich people show they are rich by buying luxury goods;
- workers signal their intrinsic productivity to the job market by taking education.


## Signaling Games

## A. Michael Spence

The Sveriges Riksbank Prize in Economic Sciences in Memory of Alfred Nobel 2001

![](https://cdn.mathpix.com/cropped/2024_09_09_605858d45802b61328b8g-405.jpg?height=458&width=311&top_left_y=295&top_left_x=74)
"for their analyses of markets with asymmetric information."

Contribution: Showed how the able agents may improve the market outcome by taking costly action to signal information to poorly informed recipients. An important example is education as a signal of high individual productivity in the labor market. It is not necessary for education to have intrinsic value. Costly investment in education as such signals high ability.

## Education Signaling

## Setup

- Nature chooses player 1's (his) skill (productivity at work), which can be high $H$ or low $L$. Only player 1 knows his own type. The probability of $H$ is $p \in(0,1)$, which is common knowledge.
- Player 1 can choose whether to get an MBA degree $D$ or be content with his undergraduate degree $U$. The cost of getting an MBA degree is $c_{H}$ for $H$ type and $c_{L}$ for $L$ type, $c_{H}<c_{L}$. There is no cost if he chooses $U$.
- Player 2 (she) is an employer. She does not know player 1's type, but observes whether he owns an MBA degree or not. Then, she decides whether to assign him to be a manager $M$ or a blue-collar worker $B$. At the same time, she must pay him the market wage: $w_{M}$ for a manager and $w_{B}$ for a blue-collar worker. Assume $w_{M}>w_{B}$.


## Education Signaling

## Setup

- Once employed, player 1 works and produces value to player 2 . The net profit (output minus wage) to player 2 depends on player 1's skill and the job assignment:

Assignment

| Skill ${ }_{L}^{H}$ | M | B |
| :---: | :---: | :---: |
|  | 10 | 5 |
|  | 0 | 3 |

- High skilled worker is always more productive than the low skilled one.
- High skilled worker is better at managing, while low skilled one is better at blue-collar work.
- Note: we have assumed that education is completely valueless. The productivity of player 1 only depends on his own intrinsic ability and the job assignment, but is independent of whether he owns an MBA degree or not.


## Education Signaling

## Setup

- Player 1's payoff is the wage he obtains minus his education cost (if any).
- Player 2's payoff is the net profit.

![](https://cdn.mathpix.com/cropped/2024_09_09_605858d45802b61328b8g-408.jpg?height=554&width=1117&top_left_y=266&top_left_x=57)

Figure 5.4: $c_{H}=2, c_{L}=5, w_{M}=10$ and $w_{B}=6$

## Education Signaling

## Setup

- Another, but equivalent, way to draw the game tree.

![](https://cdn.mathpix.com/cropped/2024_09_09_605858d45802b61328b8g-409.jpg?height=426&width=708&top_left_y=290&top_left_x=268)

Figure 5.5: An equivalent game tree for the education signaling

## Education Signaling

## PBE

- Assume $p=\frac{1}{4}$. We look for PBE's.
- Pure strategies for player 1: $U U, U D, D U, D D$. For instance, $U D$ means that player 1 chooses $U$ if his type is $H$ and chooses $D$ if his type is $L$.
- Pure strategies for player 2: $M M, M B, B M, B B$. For instance, $M B$ means that player 2 chooses $M$ after observing $U$ and chooses $B$ after observing $D$.
- $\mu_{U}$ : player 2's belief that player 1's type is $H$ after observing $U$.
- $\mu_{D}$ : player 2's belief that player 1's type is $H$ after observing $D$.


## Education Signaling

## PBE

- Is there a PBE in which player 1's strategy is UD?
- If $\left(\mu_{U}, \mu_{D}\right)$ is consistent, it must be $\mu_{U}=1$ and $\mu_{D}=0$. (Yes?)
- If player 2's strategy is sequentially rational given belief, it must that she chooses $M$ after $U$ and $B$ after $D$. That is, player 2's strategy must be $M B$.
- Given player 2's strategy $M B, L$ type wants to deviate to $U$.
- Therefore, there is no PBE in which player 1's strategy is $U D$.


## Education Signaling

## PBE

- Is there a PBE in which player 1's strategy is $D U$ ?
- If $\left(\mu_{U}, \mu_{D}\right)$ is consistent, it must be $\mu_{U}=0$ and $\mu_{D}=1$.
- If player 2's strategy is sequentially rational given belief, she must play BM.
- Given player 2's strategy, no type of player 1 has an incentive to deviate.
- Therefore, $(D U, B M)$ together with the belief system $\left(\mu_{U}=0, \mu_{D}=1\right)$ constitutes a PBE.
- We call this equilibrium a separating equilibrium: each type of player 1 chooses a different action, thus fully revealing his type to player 2 .
- Although player 2 does not know player 1's type initially, but she can perfectly infer in equilibrium: after observing $U$, she knows it is $L$ and after observing $D$, she knows it is $L$.


## Education Signaling

## PBE

- Is there a PBE in which player 1's strategy is UU?
- Consistency requires $\mu_{U}=p=\frac{1}{4}$. (Yes?)
- Given $\mu_{U}$, player 2 's best response after $U$ is $B$.
- Then, for no type of player 1 to deviate, player 2 must choose $B$ after observing $D$.
- Choosing $B$ after $D$ can be supported by the belief $\mu_{D}=0$.
- Recall that, since player 2's information set after $D$ is off the path, we have freedom in specifying $\mu_{D}$. Note also that $\mu_{D}=0$ is not the only belief that can support $B$ after $D$. For instance, $\mu_{D}=0.01$ works too.
- Therefor, $(U U, B B)$ together with the belief $\left(\mu_{U}=\frac{1}{4}, \mu_{D}=0\right)$ constitutes a PBE.
- This is called a pooling equilibrium: all types of player 1 choose the same action. Therefore, no information about player 1's type is revealed in equilibrium.


## Education Signaling

## PBE

- Is there a PBE in which player 1's strategy is $D D$ ?
- Consistency requires $\mu_{D}=\frac{1}{4}$.
- Given $\mu_{D}$, player 2's best response after $D$ is $B$.
- Then, $L$ type has an incentive to deviate to $U$ regardless of player 2's behavior after $U$.
- Therefore, there is no such PBE.


## Education Signaling

## PBE

- Other PBE?
- Observe that, in any PBE, $L$ must play $U$.
- Suppose that $H$ mixes between $U$ and $D$, with probability $q \in(0,1)$ on $U$.
- Consistency implies that $\mu_{D}=1$ and

$$
\mu_{U}=\frac{p q}{p q+(1-p) \times 1}<p=\frac{1}{4}
$$

- Given such $\mu_{U}$, it is optimal for player 2 to play $B$.
- But then $H$ is not indifferent between $U$ and $D$.
- Therefore, there is no other PBE. Especially, there is no PBE in mixed strategies.


## Education Signaling

## PBE

- In the above separating equilibrium $(D U, B M)$ with beliefs $\mu_{U}=0$ and $\mu_{D}=1$, education is used by the $H$ type to signal that he is $H$, even if education itself is completely not productive.
- $H$ can credibly do so, because $L$ type does not want to imitate $H$ type in equilibrium.
- The reason that $L$ type does not want to imitate is not because $L$ does not want to be a manager. Recall $w_{M}=10>6=w_{B}$. Rather, it is because education is too costly for him. Recall $c_{L}=5>2=c_{H}$.


## Education Signaling

## PBE

- As an exercise, let's consider whether there exists a PBE in mixed strategies if $p=\frac{1}{2}$ ?
- Following in the previous analysis, we still know that $L$ must play $U$.
- Suppose again that $H$ chooses $U$ with probability $q \in(0,1)$.
- Similarly as above, consistency implies that $\mu_{D}=1$ and $\mu_{U}=\frac{p q}{p q+(1-p)}=\frac{q}{q+1}$.
- For player 1 to be indifferent between $U$ and $D$, player 2 must mix between $M$ and $B$ with equal probability after $U$.
- But for she to mix, she must be indifferent between $M$ and $B$ after $U$. That is,

$$
10 \mu_{U}=5 \mu_{U}+3\left(1-\mu_{U}\right) \Longrightarrow \mu_{U}=\frac{3}{8}
$$

- Therefore, $\frac{q}{q+1}=\frac{3}{8}$ implying $q=\frac{3}{5}$.


## Education Signaling

## PBE

- To practice PBE in mixed strategies, consider the following signaling game.

![](https://cdn.mathpix.com/cropped/2024_09_09_605858d45802b61328b8g-418.jpg?height=437&width=763&top_left_y=312&top_left_x=252)

Figure 5.6: A finite signaling game.

## Education Signaling

## PBE

- We look for PBE in which both types mix.
- Let $\sigma\left(t_{1}\right) \in(0,1)$ be type $t_{1}$ 's probability of choosing $b$.
- Similarly, let $\sigma\left(t_{2}\right) \in(0,1)$ be type $t_{2}$ 's probability of choosing $b$.
- Let $\tau(b)$ be player 2's probability of chooosing $f$ after $b$.
- Similarly, let $\tau(q)$ be player 2's probability of choosing $f$ after $q$.
- For $t_{1}$ to be indifferent between $b$ and $q$, we must have

$$
\tau(b)-(1-\tau(b))=-2 \tau(q)
$$

- For $t_{2}$ to be indifferent between $b$ and $q$, we must have

$$
-2 \tau(b)=-3 \tau(q)-(1-\tau(q))
$$

- These two equations together imply

$$
\tau(b)=\frac{1}{2} \text { and } \tau(q)=0
$$

## Education Signaling

## PBE

- Let $\mu_{b}$ be player 2 's belief about $t_{1}$ after $b$.
- Let $\mu_{q}$ be player 2's belief about $t_{1}$ after $q$.
- For player 2 to be indifferent after $b$, we must have

$$
\mu_{b}-\left(1-\mu_{b}\right)=0 \Longrightarrow \mu_{b}=\frac{1}{2}
$$

- Consistency then requires

$$
\frac{\frac{1}{2} \sigma\left(t_{1}\right)}{\frac{1}{2} \sigma\left(t_{1}\right)+\frac{1}{2} \sigma\left(t_{2}\right)}=\frac{1}{2} \Longrightarrow \sigma\left(t_{1}\right)=\sigma\left(t_{2}\right)
$$

- This and consistency together then imply

$$
\mu_{q}=\frac{\frac{1}{2}\left(1-\sigma\left(t_{1}\right)\right)}{\frac{1}{2}\left(1-\sigma\left(t_{1}\right)\right)+\frac{1}{2}\left(1-\sigma\left(t_{2}\right)\right)}=\frac{1}{2}
$$

- Given $\mu_{q}=\frac{1}{2}$, player 2 is indeed optimal to play $r$ after $q$.


## Education Signaling

PBE

- We find a continuum of PBE:

$$
\sigma\left(t_{1}\right)=\sigma\left(t_{2}\right) \in(0,1), \tau(b)=\frac{1}{2}, \text { and } \tau(q)=0
$$

with beliefs

$$
\mu_{b}=\frac{1}{2} \text { and } \mu_{q}=\frac{1}{2}
$$

## Refinement

## Intuitive criterion

- There are still many equilibria in signaling games even though we impose sequential rationality by $P B E$.
- Part of the reason is that there is no restriction at all for off path beliefs.
- Any way to further rule out some PBEs' that are less "plausible?"
- In other words, can we refine PBE further, as we refine Nash to SPE / PBE?


## Refinement

## Intuitive criterion

- Reconsider the education signaling.

![](https://cdn.mathpix.com/cropped/2024_09_09_605858d45802b61328b8g-423.jpg?height=432&width=710&top_left_y=268&top_left_x=256)

Figure 5.7: Education signaling

- A pooling equilibrium: $(U U, B B)$. Any belief to support this behavior requires that 2 places sufficiently high probability on $L$ type after $D$.


## Refinement

## Intuitive criterion

- Let's intuitively imagine the following hypothetical situation.
- Suppose $H$ deviates to $D$ and 2 observes this off path behavior.
- Before, 2 chooses, $H$ tries to convince 2 that he is $H$ instead of $L$.
- $H$ says: "Look! If I were $L$ type and deviated to $D$, then regardless of how you would think of me, I could at most obtain 5. But If I did not deviate, I could have obtained 6. Do you think it is reasonable for me to deviate?"
- $H$ continues: "No, right? Therefore, now you believe that I am $H$. The reason I deviate to $D$ is because I know I can convince you. Then, you would choose $M$ instead of $B$, in which case this deviation is profitable for me."
- In this sense, we say $(U U, B B)$ fails the intuitive criterion.


## Refinement

## Intuitive criterion

- Let $\Theta$ be the set of all possible types of player 1 .
- For any subset $\hat{\Theta} \subset \Theta$ and $a_{1} \in A_{1}$, let $B R_{2}\left(\hat{\Theta}, a_{1}\right) \subset A_{2}$ be the set of all possible player 2's best responses if player 1 has chosen $a_{1}$ and the belief $\mu$ of player 2 puts positive probability only on types in $\hat{\Theta}$. That is

$$
B R_{2}\left(\hat{\Theta}, a_{1}\right) \equiv \bigcup_{\mu \in \Delta(\hat{\Theta})} \underset{a_{2} \in A_{2}}{\arg \max } \sum_{\theta \in \hat{\Theta}} \mu(\theta) v_{2}\left(a_{1}, a_{2}, \theta\right)
$$

- For instance, $B R_{2}(\{H, L\}, D)=\{M, B\}, B R_{2}(\{H\}, D)=\{M\}$ and $B R_{2}(\{L\}, D)=\{L\}$ in the education signaling example.


## Refinement

## Intuitive criterion

- Consider a PBE $\sigma^{*}$. Let $U(\theta)$ be type $\theta$ of player 1's equilibrium payoff.
- For any $a_{1} \in A_{1}$, define

$$
D\left(a_{1}\right) \equiv\left\{\theta \in \Theta \mid U(\theta)>\max _{a_{2} \in B R_{2}\left(\Theta, a_{1}\right)} v_{1}\left(a_{1}, a_{2}, \theta\right)\right\}
$$

- $D\left(a_{1}\right)$ contains those types who, in the given equilibrium, have no incentive at all to deviate to $a_{1}$. That is, regardless of what player 2's belief is after $a_{1}$ and regardless of which best response 2 chooses, this type's payoff is strictly lower than what he would have obtained if he did not deviate.
- For instance, $D(D)=\{L\}$ in ( $U U, B B$ ) in the above education signaling.
- Intuitively, player 2's belief after $a_{1}$ should rule out those types in $D\left(a_{1}\right)$. In other words, 2's action after $a_{1}$ should be in the set $B R_{2}\left(\Theta \backslash D\left(a_{1}\right), a_{1}\right)$.


## Refinement

## Intuitive criterion

## Definition 5.4

Consider a PBE $\sigma$ of a signaling game. We say that $\sigma$ fails the intuitive criterion if there exists a type $\theta$ and an (off path) action $a_{1}$ such that

$$
U(\theta)<\min _{a_{2} \in B R_{2}\left(\Theta \backslash D\left(a_{1}\right), a_{1}\right)} v_{1}\left(a_{1}, a_{2}, \theta\right)
$$

- Story: $\theta$ deviates to $a_{1}$ and convinces 2 that I am one of $\Theta \backslash D\left(a_{1}\right)$. Being convinced, 2 then chooses on action in $B R_{2}\left(\Theta \backslash D\left(a_{1}\right)\right)$. Type $\theta$ finds it profitable regardless of which action in $B R_{2}\left(\Theta \backslash D\left(a_{1}\right)\right)$ is actually chosen.
- If such $\theta$ and $a_{1}$ exist, we know $\theta \notin D\left(a_{1}\right)$ and $a_{1}$ is off-path.


## Refinement

## Intuitive criterion

- In the $(U U, B B)$ equilibrium of the education signaling game,

$$
U(H)=6<8=\min _{a_{2} \in B R_{2}(\Theta \backslash D(D), D)} v_{1}\left(D, a_{2}, H\right)
$$

where the second equality comes from

$$
B R_{2}(\Theta \backslash D(D), D)=B R_{2}(\{H\}, D)=\{M\}
$$

