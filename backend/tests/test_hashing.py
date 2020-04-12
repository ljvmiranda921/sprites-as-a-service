from sprites import hashing


def test_seed_is_always_the_same_after_consecutive_runs():
    run1 = hashing.get_seeds(hashing.hasher("ljvmiranda921"))
    sprite_seed1, color_seeds1 = run1
    run2 = hashing.get_seeds(hashing.hasher("ljvmiranda921"))
    sprite_seed2, color_seeds2 = run2
    assert sprite_seed1 == sprite_seed2
    assert set(color_seeds1) == set(color_seeds2)
