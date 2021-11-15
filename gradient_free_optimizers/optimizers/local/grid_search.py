# Author: Simon Blanke
# Email: simon.blanke@yahoo.com
# License: MIT License


from ..base_optimizer import BaseOptimizer
from ...search import Search


class GridSearchOptimizer(BaseOptimizer, Search):
    def __init__(
        self,
        search_space,
        initialize={"grid": 5},
    ):
        super().__init__(search_space, initialize)

    def move_in_grid(self):
        print(self.conv.search_space_positions)
        pos = []
        for search_space_pos in self.conv.search_space_positions:
            pos.append(search_space_pos[0])
        print(pos)
        print(self.conv.position2value(pos))

    @BaseOptimizer.track_nth_iter
    def iterate(self):
        print(self.n_inits)
        print(self.nth_iter)
        print(self.conv.position2value(self.pos_current))
        print(self.move_in_grid())

