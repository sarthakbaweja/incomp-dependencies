"""Main module for incomp-depend."""

import tensorflow as tf
import protobuf


def main():
    """Entry point for the application."""
    print("Hello from incomp-depend!")
    print(f"TensorFlow version: {tf.__version__}")
    print(f"Protobuf version: {protobuf.__version__}")


if __name__ == "__main__":
    main()
