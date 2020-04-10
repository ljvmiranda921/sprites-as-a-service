# Import standard library
import random
from math import sqrt
from typing import Tuple

# Import modules
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib as mpl
import numpy as np
import seagull as sg
import seagull.lifeforms as lf
from loguru import logger
from scipy.signal import convolve2d


def generate_sprite(n_iters=1, ext_rate=0.125, stasis_rate=0.375, seed=None):
    """Generate a sprite given various parameters

    Parameters
    ----------
    n_iters : int
        Number of iterations to run Conway's Game of Life.
    ext_rate : float (0.0 to 1.0)
        Controls how many dead cells will stay dead on the next iteration
        Default is 0.125 (around 1 cell)
    stasis_rate: float (0.0 to 1.0)
        Controls how many live cells will stay alive on the next iteration.
        Default is 0.375 (around 3 cells)
    seed : int (optional)
        Random seed. Default is None

    Returns
    -------
    matplotlib.Figure
    """
    logger.debug("Initializing board")
    board = sg.Board(size=(8, 4))

    noise = np.random.choice([0, 1], size=(8, 4))
    custom_lf = lf.Custom(noise)
    board.add(custom_lf, loc=(0, 0))
    sim = sg.Simulator(board)
    logger.debug("Running the simulation")
    sim.run(
        _custom_rule,
        iters=n_iters,
        n_extinct=int(ext_rate * 8),
        n_stasis=int(stasis_rate * 8),
    )
    fstate = sim.get_history()[-1]

    logger.debug("Adding outline, gradient, and colors")
    sprator = np.hstack([fstate, np.fliplr(fstate)])
    sprator = np.pad(sprator, mode="constant", pad_width=1, constant_values=1)
    sprator_with_outline = _add_outline(sprator)
    sprator_gradient = _get_gradient(sprator_with_outline)
    sprator_final = _combine(sprator_with_outline, sprator_gradient)

    # Generate random colors as cmap
    r = lambda: "#%02X%02X%02X" % (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
    )
    colors = ["black", "#f2f2f2", r(), r(), r()]
    cm.register_cmap(
        cmap=mpl.colors.LinearSegmentedColormap.from_list(
            "custom", colors
        ).reversed()
    )

    logger.debug("Preparing final image")
    fig, axs = plt.subplots(1, 1, figsize=(5, 5))
    axs = fig.add_axes([0, 0, 1, 1], xticks=[], yticks=[], frameon=False)
    axs.imshow(sprator_final, cmap="custom_r", interpolation="nearest")
    logger.success("Successfully generated sprite")

    return fig


def _custom_rule(X, n_extinct=3, n_stasis=3) -> np.ndarray:
    """Custom Conway's Rule"""
    n = convolve2d(X, np.ones((3, 3)), mode="same", boundary="fill") - X
    reproduction_rule = (X == 0) & (n <= n_extinct)
    stasis_rule = (X == 1) & ((n == 2) | (n == n_stasis))
    return reproduction_rule | stasis_rule


def _add_outline(mat: np.ndarray) -> np.ndarray:
    """Pad the matrix"""
    m = np.ones(mat.shape)
    for idx, orig_val in np.ndenumerate(mat):
        x, y = idx
        neighbors = [(x, y + 1), (x + 1, y), (x, y - 1), (x - 1, y)]
        if orig_val == 0:
            m[idx] = 0  # Set the coordinate in the new matrix as 0
            for n_coord in neighbors:
                try:
                    m[n_coord] = 0.5 if mat[n_coord] == 1 else 0
                except IndexError:
                    pass

    m = np.pad(m, mode="constant", pad_width=1, constant_values=1)
    # Let's do a switcheroo, I know this isn't elegant but please feel free to
    # do a PR to make this more efficient!
    m[m == 1] = np.inf
    m[m == 0.5] = 1
    m[m == np.inf] = 0.5

    return m


def _get_gradient(mat: np.ndarray) -> np.ndarray:
    """Get gradient of an outline sprator"""
    grad = np.gradient(mat)[0]

    def _remap(new_range, matrix):
        old_min, old_max = np.min(matrix), np.max(matrix)
        new_min, new_max = new_range
        old = old_max - old_min
        new = new_max - new_min
        return (((matrix - old_min) * new) / old) + new_min

    return _remap((0.2, 0.25), grad)


def _combine(mat_outline: np.ndarray, mat_gradient: np.ndarray):
    """Combine the matrix with outline and the one with grads"""
    mat_final = np.copy(mat_outline)
    mask = mat_outline == 0
    mat_final[mask] = mat_gradient[mask]
    return mat_final
