import generate
import random
import pygame
pygame.init()

def easy(fullpuzzle):
    puzzle = fullpuzzle
    for l in range(20):
        for i in range(len(puzzle)):
            for j in range(len(puzzle[i])):
                curr_box = puzzle[i][j]
                puzzle[i][j] = -1
                if len(generate.is_possible(i,j,puzzle)) == 1 and random.randint(1,20) == 1:
                    puzzle[i][j] = -1
                else:
                    puzzle[i][j] = curr_box
    return puzzle

def intermediate(fullpuzzle):
    puzzle = fullpuzzle
    for l in range(50):
        for i in range(len(puzzle)):
            for j in range(len(puzzle[i])):
                curr_box = puzzle[i][j]
                puzzle[i][j] = -1
                if len(generate.is_possible(i,j,puzzle)) == 1 and random.randint(1,20) == 1:
                    puzzle[i][j] = -1
                else:
                    puzzle[i][j] = curr_box
    return puzzle

def hard(fullpuzzle):
    puzzle = fullpuzzle
    for l in range(100):
        for i in range(len(puzzle)):
            for j in range(len(puzzle[i])):
                curr_box = puzzle[i][j]
                puzzle[i][j] = -1
                if len(generate.is_possible(i,j,puzzle)) == 1 and random.randint(1,20) == 1:
                    puzzle[i][j] = -1
                else:
                    puzzle[i][j] = curr_box
    return puzzle
