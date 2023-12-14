import numpy as np


class GameState:
    def __init__(self, n_cells_x, n_cells_y):
        self.n_cells_x = n_cells_x
        self.n_cells_y = n_cells_y
        self.current_state = np.random.choice([0, 1], size=(self.n_cells_x, self.n_cells_y), p=[0.8, 0.2])
        self.isPaused = False

    def change_state(self):
        new_state = np.copy(self.current_state)

        for y in range(self.n_cells_y):
            for x in range(self.n_cells_x):
                n_neighbors = (
                        self.current_state[(x - 1) % self.n_cells_x, (y - 1) % self.n_cells_y]
                        + self.current_state[(x) % self.n_cells_x, (y - 1) % self.n_cells_y]
                        + self.current_state[(x + 1) % self.n_cells_x, (y - 1) % self.n_cells_y]
                        + self.current_state[(x - 1) % self.n_cells_x, (y) % self.n_cells_y]
                        + self.current_state[(x + 1) % self.n_cells_x, (y) % self.n_cells_y]
                        + self.current_state[(x - 1) % self.n_cells_x, (y + 1) % self.n_cells_y]
                        + self.current_state[(x) % self.n_cells_x, (y + 1) % self.n_cells_y]
                        + self.current_state[(x + 1) % self.n_cells_x, (y + 1) % self.n_cells_y]
                )

                if self.current_state[x, y] == 1 and (n_neighbors < 2 or n_neighbors > 3):
                    new_state[x, y] = 0
                elif self.current_state[x, y] == 0 and n_neighbors == 3:
                    new_state[x, y] = 1

        self.current_state = new_state

    def pause_resume(self):
        self.isPaused = not self.isPaused

    def save(self):
        np.save("game_state.npy", self.current_state)

    def load(self):
        try:
            self.current_state = np.load("game_state.npy")
            self.isPaused = True
        except FileNotFoundError:
            print("Save file not found.")
