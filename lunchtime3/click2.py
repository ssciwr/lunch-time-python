import click


@click.command()
@click.option(
    "--input",
    type=click.Path(exists=True),
    default="input.txt",
    help="The data file to read from",
)
@click.option(
    "--verbose/--no-verbose", type=bool, help="Whether to output intermediate results"
)
def main(verbose, input):
    """Read data and calculate useful statistics"""
    if verbose:
        print("Started the CLI script")
    print(f"Calculating statistics from {input}")


if __name__ == "__main__":
    main()
