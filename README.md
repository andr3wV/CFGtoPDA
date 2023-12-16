# Project Overview
This project converts text into a Pushdown Automaton (PDA). The assignment comprises writing a program with three key functionalities:

- Input Grammar Rules: The code accepts grammar input from users. This grammar should align with a specific format. Here is an example of a 2 rule grammer:

  `S -> aSb | aSbb | A`
  `A -> aA | λ`

  More grammer examples can be found in the examples.md file. 

- Grammar Analysis: The program analyzes the input grammar, deconstructs it into components, and generates PDA transition functions based on the grammar.

- PDA Creation via Transition Functions: A PDA is constructed that corresponds to the language defined by the grammar, using the transition functions. This involves designing a state class that outlines the transitions and flags whether a state is the start or end.

The program also evaluates language strings, running them through the PDA, and find if they are accepted or rejected by the PDA. 

# Execution Instructions
To run the program:
1. Execute `python3 main.py`.
2. Input the number of grammar rules you wish to include.
3. Enter the grammar rules.
4. Input a string to test against the grammar.