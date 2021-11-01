import nox
import shutil
import zipfile


nox.options.sessions = ["build"]

@nox.session
def build(session: nox.Session) -> None:
    """
    Build the docs. Pass "serve" to serve.
    """

    session.install("-r", "requirements.txt")

    with zipfile.ZipFile("tipuesearch.zip", "r") as zip_obj:
        zip_obj.extractall()

    shutil.copytree("Tipue Search 7.1/tipuesearch", "pelican-themes/static/", dirs_exist_ok=True)
    session.run("pelican", "content", "-s", "pelicanconf.py", *session.posargs)


@nox.session
def serve(session: nox.Session) -> None:
    docs(session)

    session.log("Launching docs at http://localhost:8000/ - use Ctrl-C to quit")
    session.run("python", "-m", "http.server", "8000", "-d", "output")
