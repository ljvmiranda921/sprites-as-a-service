# Import standard library
import random
from math import sqrt
from typing import Tuple

# Import modules
import matplotlib as mpl
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import numpy as np
import seagull as sg
import seagull.lifeforms as lf
from loguru import logger
from scipy.signal import convolve2d

logger.disable("seagull")  # Do not print logs from Seagull


def generate_sprite(
    n_iters=1, ext_rate=0.125, stasis_rate=0.375, size=180, seed=None
):
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
    size : int
        Size of the generated sprite in pixels. Default is 180 for 180 x 180px.
    seed : int (optional)
        Random seed. Default is None

    Returns
    -------
    matplotlib.Figure
    """
    logger.debug("Initializing board")
    board = sg.Board(size=(8, 4))

    logger.debug("Seeding the lifeform")
    if seed:
        np.random.seed(seed)
    noise = np.random.choice([0, 1], size=(8, 4))
    custom_lf = lf.Custom(noise)
    board.add(custom_lf, loc=(0, 0))

    logger.debug("Running the simulation")
    sim = sg.Simulator(board)
    sim.run(
        _custom_rule,
        iters=n_iters,
        n_extinct=int(ext_rate * 8),
        n_stasis=int(stasis_rate * 8),
    )
    fstate = sim.get_history()[-1]

    logger.debug("Adding outline, gradient, and colors")
    sprite = np.hstack([fstate, np.fliplr(fstate)])
    sprite = np.pad(sprite, mode="constant", pad_width=1, constant_values=1)
    sprite_with_outline = _add_outline(sprite)
    sprite_gradient = _get_gradient(sprite_with_outline)
    sprite_final = _combine(sprite_with_outline, sprite_gradient)

    logger.trace("Registering a colormap")
    colors = ["black", "#f2f2f2", _color(), _color(), _color()]
    cm.register_cmap(
        cmap=mpl.colors.LinearSegmentedColormap.from_list(
            "custom", colors
        ).reversed()
    )

    logger.debug("Preparing final image")
    fig, axs = plt.subplots(1, 1, figsize=(5, 5), dpi=size)
    axs = fig.add_axes([0, 0, 1, 1], xticks=[], yticks=[], frameon=False)
    axs.imshow(sprite_final, cmap="custom_r", interpolation="nearest")
    logger.debug("Successfully generated sprite!")
    return fig


def _custom_rule(X, n_extinct=3, n_stasis=3) -> np.ndarray:
    """Custom Conway's Rule"""
    n = convolve2d(X, np.ones((3, 3)), mode="same", boundary="fill") - X
    reproduction_rule = (X == 0) & (n <= n_extinct)
    stasis_rule = (X == 1) & ((n == 2) | (n == n_stasis))
    return reproduction_rule | stasis_rule


def _color():
    """Returns a random hex code"""
    return "#{:02X}{:02X}{:02X}".format(
        random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
    )


def _add_outline(mat: np.ndarray) -> np.ndarray:
    """Create an outline given a sprite image

    It traverses the matrix and looks for the body of the sprite, as
    represented by 0 values. Once it founds one, it looks around its neighbors
    and change all background values (represented as 1) into an outline.

    Parameters
    ----------
    mat : np.ndarray
        The input sprite image

    Returns
    -------
    np.ndarray
        The sprite image with outline
    """
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

    # I need to switch some values so that I get the colors right.
    # Need to make all 0.5 (outline) as 1, and all 1 (backround)
    # as 0.5
    m[m == 1] = np.inf
    m[m == 0.5] = 1
    m[m == np.inf] = 0.5

    return m


def _get_gradient(
    mat: np.ndarray, map_range: Tuple[float, float] = (0.2, 0.25)
) -> np.ndarray:
    """Get gradient of an outline sprite

    We use gradient as a way to shade the body of the sprite. It is a crude
    approach, but it works most of the time.

    Parameters
    ----------
    mat : np.ndarray
        The input sprite with outline
    map_range : tuple of floats
        Map the gradients within a certain set of values. The default is
        between 0.2 and 0.25 because those values look better in the color map.

    Returns
    -------
    np.ndarray
        The sprite with shading
    """
    grad = np.gradient(mat)[0]

    def _remap(new_range, matrix):
        old_min, old_max = np.min(matrix), np.max(matrix)
        new_min, new_max = new_range
        old = old_max - old_min
        new = new_max - new_min
        return (((matrix - old_min) * new) / old) + new_min

    sprite_with_gradient = _remap(map_range, grad)
    return sprite_with_gradient


def _combine(mat_outline: np.ndarray, mat_gradient: np.ndarray) -> np.ndarray:
    """Combine the sprite with outline and the one with gradients

    Parameters
    ----------
    mat_outline: np.ndarray
        The sprite with outline
    mat_gradient: np.ndarray
        The sprite with gradient

    Returns
    -------
    np.ndarray
        The final black-and-white sprite image before coloring
    """
    mat_final = np.copy(mat_outline)
    mask = mat_outline == 0
    mat_final[mask] = mat_gradient[mask]
    return mat_final
