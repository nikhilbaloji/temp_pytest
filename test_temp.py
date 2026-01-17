from temperature import temperature

def test_cold():
    assert temperature(10) == "cold"
