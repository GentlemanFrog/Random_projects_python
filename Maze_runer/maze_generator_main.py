# Simple maze generator:

import pygame, sys
import random
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
        self.draw_outer_boundary(screen)
        for node in self.iter_node():
            node.draw_node_walls(screen)

    def draw_outer_boundary(self, screen):
        # Function drawing line around the all maze:
        # We're getting the information about corners and then we simply
        # draw lines connecting corners, to make it we have to use the size of nodes
        # to get pixel values to know where on the screen this node should be:
        topleft = (self.m_node_size, self.m_node_size)
        topright = (self.m_node_size + self.m_node_size*self.m_num_columns, self.m_node_size)
        bottomleft = (self.m_node_size, self.m_node_size + self.m_node_size*self.m_num_rows)
        bottomright = (self.m_node_size + self.m_node_size*self.m_num_columns, self.m_node_size +
                       self.m_node_size*self.m_num_rows)

        # Drawing lines connecting corners
        pygame.draw.line(screen, (0, 0, 0), topleft, topright, 5)
        pygame.draw.line(screen, (0, 0, 0), topleft, bottomleft, 5)
        pygame.draw.line(screen, (0, 0, 0), bottomright, topright, 5)
        pygame.draw.line(screen, (0, 0, 0), bottomleft, bottomright, 5)

    def make_maze(self):
        disconect_node = None
        for node in self.iter_node():
            disconect_node_N = self.get_node(node.nod_row-1, node.nod_column)
            disconect_node_E = self.get_node(node.nod_row, node.nod_column+1)
            if  disconect_node_N==None and disconect_node_E == None:
                disconect_node = None
            elif disconect_node_N != None and disconect_node_E == None:
                disconect_node = disconect_node_N
            elif disconect_node_N == None and disconect_node_E != None:
                disconect_node = disconect_node_E
            else:
                rand_number = random.randint(0,1)
                if rand_number:
                    disconect_node = disconect_node_E
                else:
                    disconect_node = disconect_node_N

            if disconect_node != None:
                node.destroy_wall(disconect_node)


class Node:  # It's square in maze (NxM structure)
    def __init__(self, row, column, size):
        self.nod_row = row
        self.nod_column = column
        self.nod_size = size
        # Dictionary storing information about each square walls corresponding to N S W E
        # Keys: N S W E, value is information of adjacent Node which wall we are using (deleted or save)
        self.nod_walls = {}
        # x,y is top left corner of the node
        self.node_x = self.nod_size*self.nod_column + self.nod_size
        self.node_y = self.nod_size*self.nod_row + self.nod_size

    def connections(self):
        nod_list = []
        # This loop will append only keys which consider connection with another node, so for first node
        # in 0x0 we should see only E and S key appended to the loop
        for key, val in self.nod_walls.items():
            if val != None:
                nod_list.append(key)
        return nod_list

    def draw_node_walls(self, screen):
        # We are drawing line for each of the walls
        # If there is valid wall we draw line from starting position to ending position we give
        # So we're starting from point 0.0 of the current node we're drawing. X and Y are the same position
        # on start (0.0). To draw the line on N we manipulate the ending position of x to be at the right
        # top corner of a node, while the y position stay the same because we want to achieve straight line.
        if self.nod_walls['N'] != None:
            starting_pos = (self.node_x, self.node_y)
            ending_pos = (self.node_x+self.nod_size, self.node_y)
            pygame.draw.line(screen, (0,0,0), starting_pos, ending_pos, 1)

        if self.nod_walls['S'] != None:
            starting_pos = (self.node_x, self.node_y + self.nod_size)
            ending_pos = (self.node_x + self.nod_size, self.node_y + self.nod_size)
            pygame.draw.line(screen, (0,0,0), starting_pos, ending_pos, 1)

        if self.nod_walls['W'] != None:
            starting_pos = (self.node_x, self.node_y)
            ending_pos = (self.node_x, self.node_y+self.nod_size)
            pygame.draw.line(screen, (0,0,0), starting_pos, ending_pos, 1)

        if self.nod_walls['E'] != None:
            starting_pos = (self.node_x +self.nod_size, self.node_y)
            ending_pos = (self.node_x+self.nod_size, self.node_y + self.nod_size)
            pygame.draw.line(screen, (0,0,0), starting_pos, ending_pos, 1)

    def destroy_wall(self, node, flag = True):
        for key, val in self.nod_walls.items():
            if val != None and val.nod_row == node.nod_row and val.nod_column == node.nod_column:
                self.nod_walls[key] = None
            else:
                #print("Node which you want destroy is not found.")
                pass
        # it's also have to brake its own directions but without a flag it will make infinite recursion
        # so we have to use the flag to stop this proces
        if flag:
            node.destroy_wall(self, False)


def main():
    # Initiation of window screen
    pygame.init()
    screen = pygame.display.set_mode((900, 900), 0, 32)
    # This RGB has to be a tuple
    screen.fill((255, 255, 255))

    # Setting the size of maze displayed in window:
    num_rows = 32
    num_columns = 32
    # Each node is square of the n pixel size
    node_size = 27
    # Creating object of class maze: and defining its property
    maze = Maze(num_rows, num_columns, node_size)
    # We need information about connection of each node with adjacent node so we make method:
    maze.nodes_starting_connection()  # Connecting means there is existing wall in dictionary
    # maze.print_maze()
    maze.make_maze()
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




