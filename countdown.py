import pygame
import time

# Constants
UNIX_TIMESTAMP = 1730490130  # Reference Unix timestamp
SECONDS_SINCE_UNIVERSE_BEGAN = 435252000000000000  # Total seconds since the beginning of the universe
REMAINING_TIME_UNIVERSE = 315400000000000000000  # Projected remaining time until the end of the universe
BITS_ROWS = 2
BITS_COLUMNS = 35

# Initialize Pygame
pygame.init()
window_width = 700
window_height = 160
screen = pygame.display.set_mode((window_width, window_height), pygame.RESIZABLE)
pygame.display.set_caption("Time To The End")
clock = pygame.time.Clock()

# Function to draw bits
def draw_bits(remaining_bits, bit_size):
    for row in range(BITS_ROWS):
        for col in range(BITS_COLUMNS):
            # Calculate the index for the current bit
            index = row * BITS_COLUMNS + col
            
            if index < len(remaining_bits):  # Check if the index is valid
                bit_value = remaining_bits[index]
                # Corrected color assignment: 1 is green and 0 is dark gray
                color = (0, 255, 0) if bit_value == 1 else (40, 40, 40)  # Green for 1, dark gray for 0
                # Calculate position: start from top left and fill left to right
                x = col * bit_size  # Column index for left to right
                y = row * bit_size  # Row index for top to bottom
                pygame.draw.rect(screen, color, (x, y, bit_size, bit_size))

def main():
    global screen, window_width, window_height  # Declare as global to modify in main
    running = True

    while running:
        current_time = int(time.time())
        elapsed_time = current_time - UNIX_TIMESTAMP
        remaining_time = max(0, REMAINING_TIME_UNIVERSE - elapsed_time)  # Remaining time until the end of the universe

        # Prepare bits for display: use the binary representation of remaining time
        # Inverted representation to display directly
        remaining_bits = [(1 if remaining_time & (1 << i) else 0) for i in range(BITS_ROWS * BITS_COLUMNS - 1, -1, -1)]

        # Debugging: print the remaining time and its binary representation

        # print(f"Current Unix Time: {current_time}")
        # print(f"Elapsed Time Since Reference: {elapsed_time}")
        # print(f"Remaining Time: {remaining_time}")
        # print(f"Binary Representation of Remaining Time: {bin(remaining_time)}")
        # print(f"Remaining Bits: {remaining_bits}")

        # Clear screen
        screen.fill((0, 0, 0))

        # Calculate bit size based on the window dimensions
        bit_size = min(window_width // BITS_COLUMNS, window_height // BITS_ROWS)

        # Ensure remaining_bits is of length 70
        while len(remaining_bits) < BITS_ROWS * BITS_COLUMNS:
            remaining_bits.append(0)  # Fill with zeros if there are fewer than 70 bits

        # Draw bits
        draw_bits(remaining_bits, bit_size)

        # Update display
        pygame.display.flip()
        
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.VIDEORESIZE:
                window_width, window_height = event.w, event.h
                screen = pygame.display.set_mode((window_width, window_height), pygame.RESIZABLE)

        # Control frame rate
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
