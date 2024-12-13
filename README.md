# LinkedIn-Queens-Solver
Backtracking Algorithm to Solve the LinkedIn spin on the Queens game

## Overview
Welcome! I have been enjoying playing the LinkedIn puzzle games lately, and it has become a daily routine of mine to solve each one as quickly as I can. They have been really addictive and a great way to connect with friends, but I couldn't help but wonder if I could apply some CS concepts to solve it *even* quicker.

'Queens' is LinkedIn's spin on the classic n-Queens Puzzle, one of many famous constraint satisfaction problems(CSP). In the original version, the goal was to assign n queens onto a nxn grid such that none of the queens threatened each other per chess rules (none on the same row, column or diagonal). A popular example is the 8-queens puzzle, which features an 8x8 chessboard, which features precisely 92 solutions.

LinkedIn's version has a few twists, however, which makes it an excellent opportunity to create a fun implementation of a backtracking search function tailored to its specific constraints.

## How it works
The n-queens puzzle is, as stated earlier, a CSP. These are problems whose solutions must satisfy specific conditions. The LinkedIn Queens game has similar constraints to the original, notably:

- No two queens can share a row
- No two queens can share a column

But the caveats are as follows:

- No two queens can touch, even diagonally. Queens can share a diagonal, just not directly next to each other
- No two queens can exist in the same color grid. This was a fun new addition to the puzzle. For example, there cannot be two queens on blue cells, even if they satisfy the first three conditions.

Now that we have our constraints, we can get into the backtracker. This is a recursive, depth-first search function that tests cells as possible queens and recursively calls itself to look for possible solutions. 

The logic I used for this is based on the knowledge that, if there are n queens to be assigned, n rows, n columns and n colors, then there **must** be a queen in every row and column. In my backtracker, if at any point it can't find a viable queen by the end of the row, it backtracks to the last one to try something different.

## To Run
At present, I have the file containing the backtracking solver, all its helper functions and I test four sample boards, three with solutions and one without. To run, use any python IDE and run the file.

## To expand
Currently, you would have to initialize the grid you would like to test, and it can be a lengthy, time-consuming process. I plan to implement some sort of GUI, perhaps with pygame, or maybe even show colored text in the terminal by use or Colorama or ANSI escape sequences.

I also would like to implement some way to read/scan images of the puzzle and produce the solution on said image. This way, the user wouldn't have to manually input the puzzle.

## Topics
- Recursion
- Constraint Satisfation
- Backtracking
