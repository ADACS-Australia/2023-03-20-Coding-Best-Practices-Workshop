def test_module_import():
    try:
        import sky_sim
    except Exception as e:
        raise AssertionError("Failed to import sky_sim")
    return