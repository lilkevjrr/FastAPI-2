
import typer
import requests

app = typer.Typer()

BASE_URL = "http://localhost:8000"


@app.command()
def lookup(isbn: str):
    response = requests.get(f"{BASE_URL}/book/{isbn}")

    if response.status_code == 200:
        book = response.json()
        typer.echo(book)
    else:
        typer.echo(response.json())


if __name__ == "__main__":
    app()
