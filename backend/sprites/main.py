"""Web API entrypoint"""

# Import standard library
import io
import base64

# Import modules
from fastapi import FastAPI, Response, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from loguru import logger
import matplotlib

matplotlib.use("Agg")
from matplotlib.backends.backend_agg import FigureCanvasAgg

# Import from package
from .sprites import generate_sprite
from .hashing import get_seeds, hasher

app = FastAPI(
    title="Sprite as a Service",
    description="Generate 8-bit avatars from Cellular Automata!",
    version="0.3.2",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost", "*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/v1/sprite")
def make_sprite(
    q: str = None,
    n_iters: int = 1,
    extinction: float = 0.125,
    survival: float = 0.375,
    size: int = 180,
):
    try:
        seeds = get_seeds(hasher(q)) if q else (None, None)
        sprite_seed, color_seeds = seeds

        logger.info("Generating sprite")
        fig = generate_sprite(
            n_iters=n_iters,
            extinction=extinction,
            survival=survival,
            size=size,
            sprite_seed=sprite_seed,
            color_seeds=color_seeds,
        )
    except Exception as e:
        logger.error(f"Error encountered: {e}")
        raise HTTPException(status_code=400, detail=str(e))

    logger.info("Processing image into base64 image/png")
    binary_output = io.BytesIO()

    metadata = {
        "Title": "Sprite as a Service",
        "Author": "@ljvmiranda921",
        "Description": "Generated 8-bit sprite from Cellular Automata",
        "Copyright": "MIT License",
        "Software": "https://github.com/ljvmiranda921/sprites-as-a-service",
    }
    FigureCanvasAgg(fig).print_png(binary_output, metadata=metadata)
    base64_output = base64.b64encode(binary_output.getvalue())
    logger.success("Done!")
    return Response(base64_output, media_type="image/png")
