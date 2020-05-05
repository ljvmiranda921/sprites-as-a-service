# Import from standard library
from statistics import mean

# Import modules
import pytest
from fastapi.testclient import TestClient
from memory_profiler import memory_usage

# Import from package
from sprites.main import app
from sprites.main import make_sprite

client = TestClient(app)


def test_make_sprite_default_values():
    response = client.get("/api/v1/sprite")
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/png"


@pytest.mark.parametrize("n_runs", [10, 20, 30])
@pytest.mark.parametrize("tolerance", [1])
def test_memory_usage_should_not_spike_on_app(n_runs, tolerance):
    """Call the app n times and ensure that mem usage is the same"""
    kwargs = {
        "n_iters": 1,
        "extinction": 0.125,
        "survival": 0.375,
        "size": 180,
    }

    avg_mem_usage_per_run = [
        mean(memory_usage((make_sprite, [], kwargs), interval=0.2, timeout=1))
        for _ in range(n_runs)
    ]
    first_run = avg_mem_usage_per_run[0]
    last_run = avg_mem_usage_per_run[-1]
    print(f"0: {first_run}, n:{last_run}")
    assert (last_run - first_run) < tolerance
