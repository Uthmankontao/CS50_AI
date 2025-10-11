# Knights & Knaves AI

This project implements a logical reasoning system to solve the famous "Knights & Knaves" puzzles published by Raymond Smullyan in 1978.

## Background

In these puzzles:  
- Each character is either a **Knight**, who always tells the truth,  
- Or a **Knave**, who always lies.  

The goal is to determine each character's role based on their statements.

## Project Structure

- `logic.py`: Implements logical connectives (AND, OR, NOT, Implication, Biconditional) and the `model_check` function to verify if a knowledge base entails a query.  
- `puzzle.py`: Defines the puzzles, encodes initial knowledge in propositional logic, and solves them using the logical reasoning engine.

## Included Puzzles

1. **Puzzle 0**: A says "I am both a knight and a knave."  
2. **Puzzle 1**: A says "We are both knaves." B says nothing.  
3. **Puzzle 2**: A says "We are of the same kind." B says "We are of different kinds."  
4. **Puzzle 3**: A says either "I am a knight" or "I am a knave" (unknown which).  
   B says "A said 'I am a knave'" and then "C is a knave."  
   C says "A is a knight."

## How It Works

1. Propositional symbols are defined for each character and role (`AKnight`, `AKnave`, `BKnight`, etc.).  
2. Knowledge bases are encoded using logical connectives to represent both puzzle structure and character statements.  
3. The `model_check` function is used to infer each character's role from the encoded knowledge.

## Running the Project

To solve the puzzles, run:

```bash
python puzzle.py
