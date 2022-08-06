"""CLI interface of the iso module"""
import click
from iso import Iso

iso = Iso()


@click.group()
def main():
    ...


@main.command()
@click.argument('code')
def find(code):
    """Shows a country based on a country's code"""
    print(iso.find(code))


@main.command()
@click.argument('name')
def find_name(name):
    """Shows a country based on a name"""
    print(iso.get_name(name))


@main.command()
@click.argument('code')
def check(code):
    """Checks if a provided code is correct"""
    print(iso.check(code))


@main.command()
def show_countries():
    """Shows a list of all(249) available countries"""
    for i in iso:
        print(i)


if __name__ == '__main__':
    main()
