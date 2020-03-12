Modelling Candy Crush with Stochastic Processes


The Python file Gameboard3.py defines the main simulator for the Candy Crush type game. The simulator generates a Gameboard, searches for potential moves, and then allows a strategy to pick between these moves to play the game. Every time a move is made, the 'mono' disappears, allowing new pieces to be generated from the top and fall down in a gravity like fashion to replace them.

The simulator models the 2D board as a list of lists, with the 'top' in the imagined game actually being the most rightward element in the list.

There are 3 strategies encoded in the simulator, one which plays the moves closest to the 'top' (most right) in the game, one which plays the moves closest to the 'bottom' (most left) and one which implements moves randomly.

The strategies were each ran for 15000 iterations, that is, the game was played using the same strategy 15000 times.
It was found in the project that the strategy of playing near the top of the board was much better than that the other strategies. The strategy of playing near the top was 2.67x better than playing near the bottom of the board, and twice as good as playing randomly. The simulator writes the game length data to a .txt file, the raw data is available on this repo. The histogram plotter program takes this data and generates the histograms used thorughout the written project.

The main simulator also collects data regarding delta move transitions. For example, it tracks whenever the game has one move remaining and then observes the amount of moves available at the next time step. This data is then plotted at the end of the simulator and makes the figures used in Chapter 6 of the written project. It was found that, if there is only one move remaining in the game, then it is more likely that there will be more moves available at the next time step. Similarly, if there are a large number of moves available in the game. For example if there are 16 moves available, it is more likely that there will be fewer moves available at the next time step.

This behaviour is similar to that of the Ehrenfest Model, a model derived to model the diffusion of gas particles between 2 containers/urns. The similarity between the Candy Crush game and this model is critically evaluated throughout the written project.

The project also explores discrete phase-type distributions, the distributions for the expected time to absorption in an absorbing state, which in the Candy Crush game, would be the number of time-steps until there are no more moves remaining. The discrete phase distribution of a slightly modified Ehrenfest model is considered and compared to the data collected from the simulator. The program used to generate such distributions is discretephase.py.

Overall, the project shows that the general concept of the Ehrenfest model is similar to the Candy Crush game, however the model could be further improved and make suggestions for ways to make this model even more similar to the game.





