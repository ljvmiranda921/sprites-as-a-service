# Import standard library
import io

# Import modules
from fastapi import FastAPI, Response, HTTPException
from loguru import logger
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.backends.backend_svg import FigureCanvasSVG

# Import from package
import sprites

app = FastAPI(
    title="Sprite as a Service",
    description="Generate 8-bit avatars from Cellular Automata!",
    version="0.1.0",
)


@app.get("/sprite")
def make_sprite(
    query: str = None,
    n_iters: int = 1,
    ext_rate: float = 0.125,
    stasis_rate: float = 0.375,
    size: int = 64,
):
    # TODO: If query exists, generate a seed and run make_sprite
    # else, then just return a random sprite
    try:
        logger.info("Generating sprite")
        fig = sprites.generate_sprite(
            n_iters=n_iters,
            ext_rate=ext_rate,
            stasis_rate=stasis_rate,
            size=size,
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
