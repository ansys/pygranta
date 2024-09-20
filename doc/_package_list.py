import os
import github
import requests
import toml
import warnings

REPOSITORY = "ansys/pygranta"


def list_dependencies(branch):
    resp = requests.get(f"https://raw.githubusercontent.com/{REPOSITORY}/{branch}/pyproject.toml")
    pyproject = toml.loads(resp.text)
    # Assume poetry
    pyansys_libraries = []
    for name, raw_library_version in pyproject["tool"]["poetry"]["dependencies"].items():
        if "ansys-grantami" not in name:
            continue
        # Check if the version is a string or a dictionary...
        if (
                isinstance(raw_library_version, dict)
                and isinstance(raw_library_version["version"], str)
        ):
            library_version = raw_library_version["version"]
        elif isinstance(raw_library_version, str):
            library_version = raw_library_version
        else:
            warnings.warn(f"Unknown version format {type(raw_library_version)}, {raw_library_version}")
            continue

        library_version = library_version.split("==")[0]

        pypi_link = f"https://pypi.org/project/{name}/{library_version}"
        doc_link = get_documentation_link_from_pypi(name, library_version)
        doc_link = pyansys_multiversion_docs_link(doc_link, library_version)

        pyansys_libraries.append({
            "name": name,
            "version": library_version,
            "docs": doc_link,
            "pypi": pypi_link,
        })
    return pyansys_libraries


def get_release_branches_in_metapackage():
    """Retrieve the release branches in the PyAnsys metapackage."""
    # Get the PyAnsys metapackage repository
    g = github.Github(os.getenv("GITHUB_TOKEN", None))
    github_repo = g.get_repo(REPOSITORY)

    # Get the branches
    branches = github_repo.get_branches()

    # Get the branches that are release branches + main
    release_branches = []
    versions = []
    for branch in branches:
        if branch.name.startswith("release"):
            release_branches.append(branch.name)
            versions.append(branch.name.split("/")[-1])

    # Sort the release branches and versions: from newest to oldest
    release_branches.reverse()
    versions.reverse()

    return release_branches, versions


def get_documentation_link_from_pypi(library: str, library_version: str) -> str:
    """Get the documentation link from PyPI for a specific library and version."""
    # Get the PyPI metadata for the library
    resp = requests.get(f"https://pypi.org/pypi/{library}/{library_version}/json")
    metadata = resp.json()

    # Get the documentation URL
    default_url = f"https://pypi.org/project/{library}/{library_version}"
    try:
        project_urls = metadata["info"]["project_urls"]
        url = project_urls.get("Documentation")
        return url if url else default_url
    except (KeyError, AttributeError):
        return default_url


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
