"""
Runtime tracking utilities.
"""
import time
import os
from datetime import datetime
from src.utils.validators import validate_directory_exists


def initialize_runtime_file(output_path):
    """
    Initialize runtime file with header.

    Args:
        output_path: Path to runtime file
    """
    validate_directory_exists(os.path.dirname(output_path))

    with open(output_path, "w") as f:
        f.write("=" * 50 + "\n")
        f.write("DIMENSION REDUCTION VISUALIZER - RUNTIME LOG\n")
        f.write("=" * 50 + "\n")
        f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")


def save_runtime(runtime, operation_name, output_path, append=True):
    """
    Save runtime to file.

    Args:
        runtime: Runtime in seconds
        operation_name: Name of the operation
        output_path: Path to save runtime file
        append: If True, append to file; if False, overwrite
    """
    validate_directory_exists(os.path.dirname(output_path))

    mode = "a" if append else "w"
    with open(output_path, mode) as f:
        f.write(f"\n{operation_name}\n")
        f.write("-" * 50 + "\n")
        f.write(f"Time: {runtime:.4f} seconds\n")
        f.write(f"Time: {runtime/60:.4f} minutes\n")

    print(f"{operation_name} runtime: {runtime:.4f} seconds")
    if not append:
        print(f"Runtime saved to: {output_path}")


class Timer:
    """Context manager for timing operations."""

    def __init__(self):
        self.start_time = None
        self.end_time = None

    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, *args):
        self.end_time = time.time()

    def elapsed(self):
        """Get elapsed time in seconds."""
        if self.start_time and self.end_time:
            return self.end_time - self.start_time
        return 0
