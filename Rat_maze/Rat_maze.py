import random
from queue import Queue
from colorama import Fore, Back, Style, init

init(autoreset=True)  # Initialize colorama

# Maze Generation Function
def generate_maze(size, wall_density):
    maze = [['◌' for _ in range(size)] for _ in range(size)]

    maze[0][0] = 'S'
    maze[size - 1][size - 1] = 'E'
    if(wall_density<3):
        num_walls = int(wall_density * size * size)
    else:
        num_walls = int(wall_density * size)
    

    for _ in range(num_walls):
        while True:
            x, y = random.randint(0, size - 1), random.randint(0, size - 1)
            if maze[x][y] == '◌':
                maze[x][y] = '▓'  # Representing walls
                break

    return maze

# Function to add path from start to end using BFS
def add_path(maze, start, end):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited = set()

    q = Queue()
    q.put(start)
    visited.add(start)

    while not q.empty():
        current = q.get()

        if current == end:
            break

        for dx, dy in directions:
            new_x, new_y = current[0] + dx, current[1] + dy
            if 0 <= new_x < len(maze) and 0 <= new_y < len(maze) and maze[new_x][new_y] == '◌' and (new_x, new_y) not in visited:
                q.put((new_x, new_y))
                visited.add((new_x, new_y))
                maze[new_x][new_y] = '◍'  # Mark the path

    if end not in visited:
        return None

    return maze

# Maze Printing Function
def print_maze(maze):
    for row in maze:
        for cell in row:
            if cell == 'S':
                print(Fore.BLUE + 'S', end=' ')
            elif cell == 'E':
                print(Fore.BLUE + 'E', end=' ')
            elif cell == '▓':
                print(Fore.RED + '▓', end=' ')
            elif cell == '◌':
                print(Fore.BLUE + '◌', end=' ')
            else:
                print(Fore.GREEN + '◍', end=' ')
        print()

# Pathfinding Function (BFS)
def find_path(maze):
    start = (0, 0)
    end = (len(maze) - 1, len(maze) - 1)

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited = set()
    path = {}

    q = Queue()
    q.put(start)
    visited.add(start)

    while not q.empty():
        current = q.get()

        if current == end:
            break

        for dx, dy in directions:
            new_x, new_y = current[0] + dx, current[1] + dy
            if 0 <= new_x < len(maze) and 0 <= new_y < len(maze) and maze[new_x][new_y] != '▓' and (new_x, new_y) not in visited:
                q.put((new_x, new_y))
                visited.add((new_x, new_y))
                path[(new_x, new_y)] = current

    if end not in visited:
        return None

    # Reconstruct the path
    path_list = []
    current = end
    while current != start:
        path_list.append(current)
        current = path[current]
    path_list.append(start)

    return path_list[::-1]

# Path Printing Function
def print_path(maze, path):
    for cell in path:
        maze[cell[0]][cell[1]] = '◍'



# Path Marking Function
def mark_path(maze, path):
    for cell in path:
        maze[cell[0]][cell[1]] = '◍'

# Main function
def main():
    size = int(input("Enter the size of the maze: "))
    wall_density = float(input("Enter Difficulty level you need (1 to 3): "))/10.0

    maze = generate_maze(size, wall_density)
    print("\nGenerated Maze:")
    print_maze(maze)

    while True:
        choice = int(input("\nDo you want to \n1.print the path. \n2.Generate another puzzle!! \n3.Want to Go to Next Level ?? \n4.Exit the Game? \nEnter Your Choice (1/2/3/4): "))

        if choice == 1:
            path = find_path(maze)
            if path:
                print("\nPath:")
                mark_path(maze, path)
                print_maze(maze)
            else:
                print("No path exists!")
                print("Sorry for Inconvience Try New Puzzle By Clicking 2")

        elif choice == 2:
            maze = generate_maze(size, wall_density)
            print("\nGenerated Maze:")
            print_maze(maze)

        elif choice == 3:
            size = int(input("Enter the size of the maze: "))
            wall_density = float(input("Enter Difficulty level you need (1 to 3): "))/10.0

            maze = generate_maze(size, wall_density)
            print("\nGenerated Maze:")
            print_maze(maze)

        elif choice == 4:
            break
        else:
            print("Invalid choice. Please enter 'path', 'puzzle', or 'exit'.")

if __name__ == "__main__":
    main()
