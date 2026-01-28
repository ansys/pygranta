"""Helper module to fetch dependencies of all versions of the meta-package."""
from operator import itemgetter
from packaging.version import parse as parse_version
from pathlib import Path
from typing import Dict, List, Optional
import warnings

import requests
import toml

REPOSITORY = "ansys/pygranta"
PYGRANTA_DOCS_URL = "https://grantami.docs.pyansys.com"
# Early versions of the auto-generated libraries did not include a documentation link.
# Packages without a documentation link and not in this list will emit a warning.
IGNORE_MISSING_DOCS = [
]


def list_current_dependencies(allow_prereleases: bool) -> List[Dict[str, str]]:
    """
    Inspects the pyproject.toml file to list dependencies.

    Return dictionary includes the name of the dependency, the version, a link to the version on
    PyPI, and a link to the documentation.
    """
    with open(Path(__file__).parents[1] /"pyproject.toml", "r") as f:
        pyproject = toml.load(f)

    pyansys_libraries = []
    for dependency in pyproject["project"]["dependencies"]:

        name, library_version = dependency.split(";")[0].split("==")[0:2]
        parsed_library_version = parse_version(library_version)

        if "ansys-grantami" not in name:
            continue

        pypi_link = f"https://pypi.org/project/{name}/{library_version}"
        doc_link = None
        if not parsed_library_version.is_prerelease:
            doc_link = get_documentation_link_from_pypi(name, library_version)
        if doc_link is not None:
            doc_link = pyansys_multiversion_docs_link(doc_link, library_version)

        pyansys_libraries.append(
            {
                "name": name,
                "version": library_version,
                "docs": doc_link,
                "pypi": pypi_link,
                "prerelease": parsed_library_version.is_prerelease,
            }
        )
    prereleases = [item for item in pyansys_libraries if item["prerelease"] is True]
    if prereleases and not allow_prereleases:
        raise ValueError(
            f"Pre-release versions found: {[itemgetter('name', 'version')(item) for item in prereleases]}."
        )
    return pyansys_libraries


def get_documentation_link_from_pypi(library: str, library_version: str) -> Optional[str]:
    """Get the documentation link from PyPI for a specific library and version."""
    # Get the PyPI metadata for the library
    resp = requests.get(f"https://pypi.org/pypi/{library}/{library_version}/json")
    try:
        metadata = resp.json()
    except requests.JSONDecodeError:
        metadata = {}

    try:
        doc_url = metadata["info"]["project_urls"]["Documentation"]
    except (KeyError, AttributeError, TypeError):
        if (library, library_version) not in IGNORE_MISSING_DOCS:
            warnings.warn(f"No documentation link found for {library}, version {library_version}")
        return None
    else:
        # Auto-generated packages include a link to the general PyGranta docs, filter them out
        if library.endswith("-openapi") and doc_url == PYGRANTA_DOCS_URL:
            return None
        return doc_url


def pyansys_multiversion_docs_link(docs_link: str, library_version: str) -> str:
    """Verify if the documentation link is a multi-version link.

    Notes
    -----
    Checks if the documentation link is a multi-version link. If it is, it
    tries to access the documentation for the specific version. In case of
    failure, it returns the default link. This is done on a best effort basis.
    """
    DOCS_DOMAIN = "docs.pyansys.com"

    # First, let's check it is an official PyAnsys documentation link
    if DOCS_DOMAIN in docs_link:
        # Clean the link
        tmp_link = docs_link.split(DOCS_DOMAIN)[0] + DOCS_DOMAIN
        # Get the major.minor version
        major_minor_version = ".".join(library_version.split(".")[:2])

        # Attempt to access the documentation for the specific version
        try:
            resp = requests.get(f"{tmp_link}/version/{major_minor_version}/index.html")
            if resp.status_code == 200:
                return f"{tmp_link}/version/{major_minor_version}"
        except requests.exceptions.RequestException:
            pass

    # Fall back to the default link
    return docs_link
