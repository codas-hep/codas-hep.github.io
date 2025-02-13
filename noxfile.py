import nox
import shutil
import zipfile

nox.needs_version = ">=2025.02.09"
nox.options.default_venv_backend = "uv|virtualenv"

@nox.session(default=False)
def update(session: nox.Session) -> None:
    """
    Update the lockfile
    """
    if session.venv_backend != "uv":
        session.install("uv")

    session.run("uv", "pip", "compile", "requirements.in", "--output-file=requirements.txt")

@nox.session
def build(session: nox.Session) -> None:
    """
    Build the docs
    """

    session.install("-r", "requirements.txt")

    with zipfile.ZipFile("tipuesearch.zip", "r") as zip_obj:
        zip_obj.extractall()

    shutil.copytree("Tipue Search 7.1/tipuesearch", "pelican-themes/static/", dirs_exist_ok=True)
    session.run("pelican", "--fatal=errors", "content", "-s", "pelicanconf.py", *session.posargs)


@nox.session(default=False, requires=["build"])
def serve(session: nox.Session) -> None:
    """
    Serve the docs. Builds first.
    """

    session.log("Launching docs at http://localhost:8000/ - use Ctrl-C to quit")
    session.run("python", "-m", "http.server", "8000", "-d", "output")
