# Peg-Solitaire-Solver
A peg solitaire solver made in Python 3.6.

It uses the [DFS](https://en.wikipedia.org/wiki/Depth-first_search) search algorithm to achieve the puzzle's final state.

### Example execution result
```
Winning state achieved.
Total moves: 31

Step 1 :
--XXX--
--XOX--
XXXOXXX
XXXXXXX
XXXXXXX
--XXX--
--XXX--

Step 2 :
--XXX--
--XOX--
XOOXXXX
XXXXXXX
XXXXXXX
--XXX--
--XXX--

... // output omitted to shorten the length.

Step 30 :
--OOO--
--OOO--
OOOOOOO
OOOOOOO
OOOXOOO
--OXO--
--OOO--

Step 31 :
--OOO--
--OOO--
OOOOOOO
OOOXOOO
OOOOOOO
--OOO--
--OOO--
```
