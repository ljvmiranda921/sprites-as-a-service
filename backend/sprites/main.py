"""Web API entrypoint"""

# Import standard library
import io

# Import modules
from fastapi import FastAPI, Response, HTTPException
from loguru import logger
import matplotlib
matplotlib.use('Agg')
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.backends.backend_svg import FigureCanvasSVG

# Import from package
from .sprites import generate_sprite
from .hashing import get_seeds, hash

app = FastAPI(
    title="Sprite as a Service",
    description="Generate 8-bit avatars from Cellular Automata!",
    version="0.1.0",
)


@app.get("/sprite")
def make_sprite(
    q: str = None,
    n_iters: int = 1,
    ext_rate: float = 0.125,
    stasis_rate: float = 0.375,
    size: int = 180,
):
    try:
        seeds = hashing.get_seeds(hashing.hash(q)) if q else (None, None)
        sprite_seed, color_seeds = seeds

        logger.info("Generating sprite")
        fig = generate_sprite(
            n_iters=n_iters,
            ext_rate=ext_rate,
            stasis_rate=stasis_rate,
            size=size,
            sprite_seed=sprite_seed,
            color_seeds=color_seeds,
        )
    except Exception as e:
        logger.error(f"Error encountered: {e}")
        raise HTTPException(status_code=400, detail=str(e))

    logger.info("Processing image into PNG")
    output = io.BytesIO()
    metadata = {
        "Title": "Sprite as a Service",
        "Author": "@ljvmiranda921",
        "Description": "Generated 8-bit sprite from Cellular Automata",
        "Copyright": "MIT License",
        "Software": "https://github.com/ljvmiranda921/sprite-as-a-service",
    }
    FigureCanvasAgg(fig).print_png(output, metadata=metadata)

    logger.success("Done!")
    return Response(output.getvalue(), media_type="image/png")
