"""
RedPlanet-Pathfinder: Autonomous Rover Obstacle Avoidance Simulator
Author: Jolanta Antonovic
Description: An autonomous pathfinding simulation representing a Mars Rover 
             navigating grid-based terrain using Manhattan Distance-based 
             heuristics to bypass obstacles and reach a scientific target.
"""

import matplotlib.pyplot as plt
import numpy as np
import random

def manhattan_distance(point_a, point_b):
    """
    Calculates the Manhattan Distance between two points on a 2D grid.
    This acts as the heuristic for the rover's decision-making process.
    
    Parameters:
        point_a (tuple): (x, y) coordinates of the starting point.
        point_b (tuple): (x, y) coordinates of the destination point.
        
    Returns:
        int: The total grid steps required to move from point_a to point_b.
    """

    x1, y1 = point_a
    x2, y2 = point_b
    distance = abs(x1 - x2) + abs(y1 - y2)
    return distance

def main():
    # Initialize a 10x10 grid with zeros (0 represents open traversable space)
    matrix = np.zeros((10, 10))
    current_position = (0, 0)

    # Generate a random target position and ensure it does not overlap with the start point
    target_coordinate = (random.randint(0, 9), random.randint(0, 9))
    while (0, 0) == target_coordinate:
        target_coordinate = (random.randint(0, 9), random.randint(0, 9))

    # Generate 12 random obstacle (boulder) coordinates with overlap protection
    boulders = []
    for boulder in range(12):
        boulder_coordinate = (random.randint(0, 9), random.randint(0, 9))
        while boulder_coordinate == current_position or boulder_coordinate == target_coordinate or boulder_coordinate in boulders:
            boulder_coordinate = (random.randint(0, 9), random.randint(0, 9))
        boulders.append(boulder_coordinate)

    # Map the coordinates onto the NumPy grid matrix using [y, x] (Row, Column) representation
    matrix[current_position[1], current_position[0]] = 0  # Start Position (0)
    matrix[target_coordinate[1], target_coordinate[0]] = 2  # Target Zone (2)
    for boulder in boulders:
        matrix[boulder[1], boulder[0]] = 1                   # Boulder obstacles (1)

    # Initialize the plot window and turn on Matplotlib interactive mode for smooth animation
    im = plt.imshow(matrix, cmap='coolwarm') 
    plt.ion() 
    
    # Keep moving until we are at the target
    while current_position != target_coordinate:
        potential_moves = [
            (current_position[0] + 1, current_position[1]), # Move Right
            (current_position[0] - 1, current_position[1]), # Move Left
            (current_position[0], current_position[1] + 1), # Move Down
            (current_position[0], current_position[1] - 1), # Move Up
        ]

        # Filter out boundary violations, obstacles (1), and previous paths (3)
        valid_moves = []
        for move in potential_moves:
            if 0 <= move[0] < 10 and 0 <= move[1] < 10 and (matrix[move[1], move[0]] == 0 or matrix[move[1], move[0]] == 2):
                valid_moves.append(move)

        best_move = None
        best_distance = float('inf')

        # Heuristic search: Pick the valid neighboring node closest to the target
        for move in valid_moves:
            distance = manhattan_distance(move, target_coordinate)
            if distance < best_distance:
                best_distance = distance
                best_move = move

        # Exit loop if the rover gets completely boxed in by obstacles
        if best_move is None:
            print("No valid moves available.")
            break

        # Move the rover to the optimal next coordinate
        current_position = best_move

        # Only draw a path tile if we haven't reached the target yet!
        if current_position != target_coordinate:
            matrix[current_position[1], current_position[0]] = 1.5

        # Instantly update the frame data to show movement in real-time
        im.set_data(matrix) 
        plt.pause(0.2)

    # Deactivate interactive plotting so the final visual output remains frozen on-screen
    plt.ioff()
    plt.show()  # Show the final state of the matrix

if __name__ == "__main__":
    main()
