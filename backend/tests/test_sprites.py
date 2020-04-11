# Import standard library
import re
from typing import List, Tuple

# Import modules
import numpy as np
import pytest
from matplotlib.figure import Figure
from matplotlib.testing.decorators import check_figures_equal

# Import from package
import sprites


def test_generate_sprite_return_type():
    fig = sprites.generate_sprite(
        n_iters=1,
        ext_rate=0.125,
        stasis_rate=0.375,
        size=180,
        sprite_seed=None,
        color_seeds=None,
    )
    assert isinstance(fig, Figure)


def test_conway_alive_cell_with_no_neighbor_dies():
    cell = (1, 1)
    state = put_cells_to_board([cell])
    next_state = sprites._custom_rule(state, n_stasis=2)
    assert next_state[cell] == 0


def test_conway_alive_cell_with_one_neighbor_dies():
    cell = (1, 1)
    state = put_cells_to_board([(1, 1), cell])
    next_state = sprites._custom_rule(state, n_stasis=2)
    assert next_state[cell] == 0


def test_conway_alive_cell_with_more_than_3_neighbors_dies():
    cell = (1, 1)
    alive_cells = [(0, 0), (1, 0), (2, 0), (2, 1)]
    state = put_cells_to_board(alive_cells + [cell])
    next_state = sprites._custom_rule(state, n_stasis=2)
    assert next_state[cell] == 0


def test_conway_alive_cell_with_2_neighbors_lives():
    cell = (1, 1)
    alive_cells = [(0, 1), (1, 0)]
    state = put_cells_to_board(alive_cells + [cell])
    next_state = sprites._custom_rule(state, n_stasis=2)
    assert next_state[cell] == 1


def test_conway_alive_cell_with_3_neighbors_lives():
    cell = (1, 1)
    alive_cells = [(0, 0), (1, 0), (2, 1)]
    state = put_cells_to_board(alive_cells + [cell])
    next_state = sprites._custom_rule(state, n_stasis=3)
    assert next_state[cell] == 1


def test_conway_dead_cell_with_three_live_neighbors_lives():
    dead_cell = (1, 1)
    alive_cells = [(2, 2), (1, 0), (2, 1)]
    state = put_cells_to_board(alive_cells)
    next_state = sprites._custom_rule(state, n_stasis=3)
    assert next_state[dead_cell] == 1


def test_conway_dead_cell_with_two_live_neighbors_stay_dead():
    dead_cell = (1, 1)
    alive_cells = [(2, 2), (1, 0)]
    state = put_cells_to_board(alive_cells)
    next_state = sprites._custom_rule(state, n_stasis=3, n_extinct=0)
    assert next_state[dead_cell] == 0


def test_color_must_return_valid_hex_code():
    hex_color = sprites._color()
    match = re.search(r"^#(?:[0-9a-fA-F]{3}){1,2}$", hex_color)
    assert match


def test_add_outline_return_value():
    test_matrix = np.array([[0, 0, 1], [1, 1, 1], [0, 0, 1]])
    expected = np.array(
        [
            [0.5, 0.5, 0.5, 0.5, 0.5],
            [0.5, 0.0, 0.0, 1.0, 0.5],
            [0.5, 1.0, 1.0, 0.5, 0.5],
            [0.5, 0.0, 0.0, 1.0, 0.5],
            [0.5, 0.5, 0.5, 0.5, 0.5],
        ]
    )

    output = sprites._add_outline(test_matrix)
    assert np.array_equal(output, expected)


def put_cells_to_board(coords: List[Tuple[int, int]]) -> np.ndarray:
    """Given a list of cells and their coords, add to board"""
    board = np.zeros((3, 3))
    for coord in coords:
        board[coord] = 1
    return board


def get_alive_cells(x: np.ndarray) -> List[Tuple[int, int]]:
    """Get alive cells given a matrix"""
    x_coords, y_coords = np.where(x == 1)
    return [(x, y) for x, y in zip(x_coords, y_coords)]


def get_dead_cells(x: np.ndarray) -> List[Tuple[int, int]]:
    """Get dead cells given a matrix"""
    x_coords, y_coords = np.where(x == 0)
    return [(x, y) for x, y in zip(x_coords, y_coords)]
