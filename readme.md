Brief outline of the project:
    
    1. Create the simulator
        a. Generate the gameboard
        b. Initially remove all pre-made monos
        c. Reconcatenate each individual list with new randomly generated lists
        d. Develop the idea of moves
        e. Apply moves
        f. Repeat until no further moves are possible
        
    2. Test different strategies
    
    3. Compare data from different strategies
    
    4. Work out which strategy is best depending on what you're trying to optimise. 
        

            New plan for refactor:
            Mono checker becomes an abstract function - want it to return co-ords of the monos
            Generate board
            Run mono checker function
            (Update score)
            Zero out monos function
            Gravity
            Implement moves - looking like it will be a couple of nested for loops
            run mono checker function again to see if the list changes
            Revert the move in order to not change board - while still looking for other monos - this is how we will get the data


            Theory to look at: 
            Ehrenfest model - Markov Chains
