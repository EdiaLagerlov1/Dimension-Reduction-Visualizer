"""
CLI entry point for Dimension Reduction Visualizer.
"""
import argparse
from src.workflows.prepare import prepare_data
from src.workflows.pca_workflow import run_pca
from src.workflows.tsne_workflow import run_tsne_visualization


def main():
    """Main CLI function."""
    parser = argparse.ArgumentParser(
        description="Dimension Reduction Visualizer"
    )
    parser.add_argument("--prepare", action="store_true", help="Prepare data")
    parser.add_argument("--pca", action="store_true", help="Run PCA")
    parser.add_argument("--tsne", action="store_true", help="Run t-SNE")
    parser.add_argument("--all", action="store_true", help="Run all steps")

    args = parser.parse_args()

    if args.all:
        prepare_data()
        run_pca()
        run_tsne_visualization()
    else:
        if args.prepare:
            prepare_data()
        if args.pca:
            run_pca()
        if args.tsne:
            run_tsne_visualization()

    if not any([args.prepare, args.pca, args.tsne, args.all]):
        parser.print_help()


if __name__ == "__main__":
    main()
