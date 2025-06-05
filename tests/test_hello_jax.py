import importlib.util
import pathlib

# Load the hello-jax module from its filename
spec = importlib.util.spec_from_file_location("hello_jax", pathlib.Path(__file__).resolve().parents[1] / "hello-jax.py")
hello_jax = importlib.util.module_from_spec(spec)
spec.loader.exec_module(hello_jax)

def test_add():
    assert hello_jax.add(1, 2) == 3
