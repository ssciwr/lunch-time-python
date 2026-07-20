import click


@click.group()
def main():
    pass


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
def stats(verbose, input):
    """Read data and calculate useful statistics"""
    if verbose:
        print("Started the CLI script")
    print(f"Calculating statistics from {input}")


@click.command()
def preprocess():
    print("Apply preprocessing")


main.add_command(stats)
main.add_command(preprocess)

if __name__ == "__main__":
    main()
