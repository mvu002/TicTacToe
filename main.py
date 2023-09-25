import pygame
import engine

pygame.init()
WIDTH = 636
HEIGHT = 636
DIMENSION = 3
SQ_SIZE = HEIGHT // DIMENSION
IMAGES = {}


def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    screen.fill(pygame.Color("white"))
    game_state = engine.GameState()
    print(game_state.board)
    load_images()
    target_square = ()
        
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                location = pygame.mouse.get_pos()
                col = location[0] // SQ_SIZE
                row = location[1] // SQ_SIZE
                target_square = (row, col)
                move = engine.Move(target_square, game_state.board)
                game_state.make_move(move)
                target_square = ()

        draw_game_state(screen, game_state)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

def load_images():
    symbols = ["x", "o"]
    for symbol in symbols:
        IMAGES[symbol] = pygame.transform.scale(pygame.image.load("images/" + symbol + ".png"), (SQ_SIZE, SQ_SIZE))

def draw_game_state(screen, game_state):
    #draw_board(screen)
    draw_symbols(screen, game_state.board)
    draw_board(screen)

def draw_board(screen):
    color = pygame.Color("black")
    for row in range(DIMENSION):
        for col in range(DIMENSION):
            pygame.draw.rect(screen, color, pygame.Rect(col * SQ_SIZE, row * SQ_SIZE, SQ_SIZE, SQ_SIZE), width = 5)

def draw_symbols(screen, board):
    for row in range(DIMENSION):
        for col in range(DIMENSION):
            symbol = board[row][col]
            if symbol != "--":
                screen.blit(IMAGES[symbol], pygame.Rect(col * SQ_SIZE, row * (SQ_SIZE + 10), SQ_SIZE, SQ_SIZE))


main()