import click


@click.command()
@click.argument("inputfile", type=click.Path(exists=True))
def stats(inputfile):
    """Read data from the given INPUTFILE and calculate useful statistics"""
    print(f"Calculating statistics from {inputfile}")


# This allows use of this Python file both for imports and for the CLI
if __name__ == "__main__":
    stats()
