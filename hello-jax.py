# hello_jax.py

import jax
import jax.numpy as jnp

# A simple JAX‐compiled function that adds two numbers
@jax.jit
def add(a, b):
    return a + b

def main():
    # Call the JAX function
    result = add(1, 2)
    print(f"Hello, JAX! 1 + 2 = {result}")

if __name__ == "__main__":
    main()
