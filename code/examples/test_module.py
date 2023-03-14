def test_module_import():
    try:
        import sky_sim
    except Exception as e:
        raise AssertionError("Failed to import sky_sim")
    return

def test_get_radec():
    from sky_sim import get_radec
    result = get_radec()
    correct = (14.215420962967535, 41.26916666666666)
    if not result == correct:
        raise AssertionError(f"get_radec returns {result} but expecting {correct}")
    return