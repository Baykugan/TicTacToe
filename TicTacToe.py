import pygame


class Board():

    def __init__(self):
        #self.size = int(input(f'How big of a board do you want?'))
        self.size = 4
        self.index = [[(' ') for j in range(self.size)] for i in range(self.size)]
        

    def threeInRow(self):
        diag1 = []
        diag2 = []
        diag1Ind = [(i, i) for i in range(self.size)]
        diag2Ind = [(i, -i - 1) for i in range(self.size)]

        for i in range(board.size):
            row = []
            col = []
            rowInd = []
            colInd = []

            for j in range(board.size):
                row.append(self.index[i][j])
                col.append(self.index[j][i])
                rowInd.append((i, j))
                colInd.append((j, i))

                
            if all(i == 'X' for i in row) or all(i == 'O' for i in row):
                return True, rowInd, row[0]
            if all(i == 'X' for i in col) or all(i == 'O' for i in col):
                return True, colInd, col[0]
            
            diag1.append(self.index[i][i])
            diag2.append(self.index[-i - 1][i])


            
        if all(i == 'X' for i in diag1) or all(i == 'O' for i in diag1):
            return True, diag1Ind, diag1[0]
        if all(i == 'X' for i in diag2) or all(i == 'O' for i in diag2):
            return True, diag2Ind, diag2[0]

        return False
    
    def draw(self):
        diag1 = []
        diag2 = []
        unwinnable = True

        for i in range(board.size):
            row = []
            col = []
            rowInd = []
            colInd = []

            for j in range(board.size):
                row.append(self.index[i][j])
                col.append(self.index[j][i])
                rowInd.append((i, j))
                colInd.append((j, i))

                
            if not any(i == 'X' for i in row) or not any(i == 'O' for i in row):
                unwinnable = False
            if not any(i == 'X' for i in col) or not any(i == 'O' for i in col):
                unwinnable = False
            
            diag1.append(self.index[i][i])
            diag2.append(self.index[-i - 1][i])


            
        if not any(i == 'X' for i in diag1) or not any(i == 'O' for i in diag1):
            unwinnable = False
        if  not any(i == 'X' for i in diag2) or not any(i == 'O' for i in diag2):
            unwinnable = False

        return unwinnable
    
    

def DRAW_BOARD(SCREEN, SIZE, TILE_SIZE):
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255) 
    BLUE = (0, 0, 200)
    GOLD = (218, 165, 20)
 

    for i in range(0, SIZE, TILE_SIZE):
        for j in range(0, SIZE, TILE_SIZE):
            rect = pygame.Rect(i, j, TILE_SIZE, TILE_SIZE)
            pygame.draw.rect(SCREEN, WHITE, rect)
            if (j / TILE_SIZE, i / TILE_SIZE) in winningSquares:
                pygame.draw.rect(SCREEN, GOLD, rect)
            pygame.draw.rect(SCREEN, BLACK, rect, 1)


def DRAW_PIECES(SCREEN, TILE_SIZE):
    X = pygame.image.load('TicTacToe_Images/X.png')
    O = pygame.image.load('TicTacToe_Images/O.png')

    X = pygame.transform.scale(X, (TILE_SIZE, TILE_SIZE))
    O = pygame.transform.scale(O, (TILE_SIZE, TILE_SIZE))
    
    for row in range(board.size):
        for col in range(board.size):
                
            if board.index[row][col] == 'X':
                SCREEN.blit(X, (col * TILE_SIZE, row * TILE_SIZE))
            elif board.index[row][col] == 'O':
                SCREEN.blit(O, (col * TILE_SIZE, row * TILE_SIZE))


def main():
    global board
    global turn
    global running
    global winningSquares
    global prevMoves 


    board = Board()
    turn = 1
    winningSquares = ()
    someoneWon = False
    unwinnable = False
    windowTitle = 'TicTacToe'
    prevMoves = [] 


    windowIcon = pygame.image.load('TicTacToe_Images/Thumbnail.png')
    pygame.display.set_icon(windowIcon)
    pygame.display.set_caption(windowTitle)
    if board.size > 6:
        SIZE = 650
        TILE_SIZE = int(SIZE / board.size)
    else:
        TILE_SIZE = 100
    SIZE = TILE_SIZE * board.size
    SCREEN = pygame.display.set_mode((SIZE, SIZE)) 
    
    running = True
    while running:  
        DRAW_BOARD(SCREEN, SIZE, TILE_SIZE)
        DRAW_PIECES(SCREEN, TILE_SIZE)
        pygame.display.flip() 
        pygame.display.set_caption(windowTitle)

        if turn % 2 == 1:
            windowTitle = 'X\'s turn'
        else:
            windowTitle = 'O\'s turn'
            

        for event in pygame.event.get():      
            if event.type == pygame.QUIT: 
                running = False

            elif event.type == pygame.MOUSEBUTTONUP:

                pos = pygame.mouse.get_pos()
                col, row = pos
                
                row = row // TILE_SIZE
                col = col // TILE_SIZE
                prevMoves.append((row * 3) + col)
                
                if board.index[row][col] == ' ' and not someoneWon and not unwinnable:
                    if turn % 2 == 1:
                        board.index[row][col] = 'X'
                    else:
                        board.index[row][col] = 'O'
                else:
                    continue
                turn += 1
                
                someoneWon = board.threeInRow()
                unwinnable = board.draw()

                if someoneWon:
                    winningSquares = someoneWon[1]
                
                
        if someoneWon:
            windowTitle = f'{someoneWon[2]} won'
        elif unwinnable:
            windowTitle = f'The game ended in a draw'
            
main()