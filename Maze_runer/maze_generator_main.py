# Simple maze generator:

import pygame, sys
import turtle


class Maze:
    def __init__(self, num_rows, num_columns, node_size):
        self.m_num_rows = num_rows
        self.m_num_columns = num_columns
        self.m_node_size = node_size
        # List of lists of nodes which build up maze
        # each list represents a row, and this each list is list of
        # nodes in column, 2 dimensional array of nodes
        self.m_nodes = [[Node(i,j,self.m_node_size) for j in range(self.m_num_columns)] for i in range(self.m_num_rows)]

    def iter_node(self):
        for i in range(self.m_num_rows):
            for j in range(self.m_num_columns):
                yield self.m_nodes[i][j]

    def get_node(self, row, col):
        if row >= 0 and row < self.m_num_rows and col >= 0 and col < self.m_num_columns:
            return self.m_nodes[row][col]
        else:
            return None

    def nodes_starting_connection(self):
        # Basically we want to iterate by each Node and create a wall between all nodes to make them
        # connect, after this step we can destroy certain walls to make passages
        for node in self.iter_node(): # iter_node is generator
            node.nod_walls['N'] = self.get_node(node.nod_row - 1, node.nod_column)
            node.nod_walls['S'] = self.get_node(node.nod_row + 1, node.nod_column)
            node.nod_walls['W'] = self.get_node(node.nod_row, node.nod_column - 1)
            node.nod_walls['E'] = self.get_node(node.nod_row, node.nod_column + 1)

    def print_maze(self):
        for node in self.iter_node():
            print(node.nod_row, node.nod_column, node.connections())

    def draw(self, screen):



class Node:  # It's square in maze (NxM structure)
    def __init__(self, row, column, size):
        self.nod_row = row
        self.nod_column = column
        self.nod_size = size
        # Dictionary storing information about each square walls corresponding to N S W E
        # Keys: N S W E, value is information of adjacent Node which wall we are using (deleted or save)
        self.nod_walls = {}

    def connections(self):
        nod_list = []
        # This loop will append only keys which consider connection with another node, so for first node
        # in 0x0 we should see only E and S key appended to the loop
        for key, val in self.nod_walls.items():
            if val != None:
                nod_list.append(key)
        return nod_list


def main():
    # Initiation of window screen
    pygame.init()
    screen = pygame.display.set_mode((900, 900), 0, 32)
    # This RGB has to be a tuple
    screen.fill((255, 255, 255))

    # Setting the size of maze displayed in window:
    num_rows = 6
    num_columns = 6
    # Each node is square of the n pixel size
    node_size = 30
    # Creating object of class maze: and defining its property
    maze = Maze(num_rows, num_columns, node_size)
    # We need information about connection of each node with adjacent node so we make method:
    maze.nodes_starting_connection()  # Connecting means there is existing wall in dictionary
    # maze.print_maze()
    maze.draw(screen)

    # Making game loop for visual features of pygame
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.update()
    pygame.quit()
    sys.exit()


# Main rutine:
main()




