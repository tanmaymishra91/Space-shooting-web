import pygame
import os
import random
import asyncio
from player import Player
from enemy import Enemy


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

async def main():
    
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Space Shooter")
    clock = pygame.time.Clock()

    
    all_sprites = pygame.sprite.Group()
    mobs = pygame.sprite.Group()
    bullets = pygame.sprite.Group()

    
    player = Player()
    all_sprites.add(player)

    
    for i in range(8):
        m = Enemy()
        all_sprites.add(m)
        mobs.add(m)

    
    score = 0
    font_name = pygame.font.match_font('arial')
    
    def draw_text(surf, text, size, x, y):
        font = pygame.font.Font(font_name, size)
        text_surface = font.render(text, True, WHITE)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        surf.blit(text_surface, text_rect)

    
    running = True
    game_over = False

    while running:
        if game_over:

            screen.fill(BLACK)
            draw_text(screen, "GAME OVER", 64, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4)
            draw_text(screen, f"Score: {score}", 22, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
            draw_text(screen, "Press any key to restart", 18, SCREEN_WIDTH / 2, SCREEN_HEIGHT * 3 / 4)
            pygame.display.flip()
            
            waiting = True
            while waiting:
                clock.tick(FPS)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                        waiting = False
                    if event.type == pygame.KEYUP:
                        waiting = False
                        game_over = False

                        all_sprites = pygame.sprite.Group()
                        mobs = pygame.sprite.Group()
                        bullets = pygame.sprite.Group()
                        player = Player()
                        all_sprites.add(player)
                        for i in range(8):
                            m = Enemy()
                            all_sprites.add(m)
                            mobs.add(m)
                        score = 0
                await asyncio.sleep(0)


        clock.tick(FPS)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    new_bullets = player.shoot()
                    for bullet in new_bullets:
                        all_sprites.add(bullet)
                        bullets.add(bullet)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    new_bullets = player.shoot()
                    for bullet in new_bullets:
                        all_sprites.add(bullet)
                        bullets.add(bullet)


        player.power_level = min(10, (score // 30) + 1)


        all_sprites.update()


        hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
        for hit in hits:
            score += 10
            m = Enemy()
            all_sprites.add(m)
            mobs.add(m)


        hits = pygame.sprite.spritecollide(player, mobs, False)
        if hits:
            game_over = True


        screen.fill(BLACK)
        all_sprites.draw(screen)
        draw_text(screen, str(score), 18, SCREEN_WIDTH / 2, 10)
        draw_text(screen, f"Level {player.power_level}", 18, SCREEN_WIDTH - 100, 10)
        

        pygame.display.flip()
        await asyncio.sleep(0)

    pygame.quit()

if __name__ == "__main__":
    try:

        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        asyncio.run(main())
    except Exception as e:
        print(f"An error occurred: {e}")
        import traceback
        traceback.print_exc()
        input("Press Enter to exit...")
