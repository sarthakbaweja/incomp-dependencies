"""Main module for incomp-depend."""

import tensorflow as tf
import protobuf
from prophet import Prophet
from PyPDF2 import PdfReader


def main():
    """Entry point for the application."""
    print("Hello from incomp-depend!")
    print(f"TensorFlow version: {tf.__version__}")
    print(f"Protobuf version: {protobuf.__version__}")
    print(f"Prophet loaded: {Prophet.__name__}")
    print(f"PyPDF2 PdfReader loaded: {PdfReader.__name__}")


if __name__ == "__main__":
    main()
