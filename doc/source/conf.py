"""Sphinx documentation configuration file."""

from datetime import datetime
import os

from ansys_sphinx_theme import ansys_favicon, get_version_match

from pygranta import __version__

# Project information
project = "PyGranta Documentation"
copyright = f"(c) {datetime.now().year} ANSYS, Inc. All rights reserved"
author = "ANSYS, Inc."
release = version = __version__

# Select desired logo, theme, and declare the html title
html_theme = "ansys_sphinx_theme"
html_short_title = html_title = "PyGranta"
html_favicon = ansys_favicon

cname = os.getenv("DOCUMENTATION_CNAME", "grantami.docs.pyansys.com")

# specify the location of your github repo
html_theme_options = {
    "github_url": "https://github.com/ansys/pygranta",
    "show_prev_next": False,
    "show_breadcrumbs": True,
    "additional_breadcrumbs": [
        ("PyAnsys", "https://docs.pyansys.com/"),
    ],
    "switcher": {
        "json_url": f"https://{cname}/versions.json",
        "version_match": get_version_match(__version__),
    },
    "check_switcher": False,
    "logo": "ansys",
}

# Sphinx extensions
extensions = [
    "sphinx_design",
    "sphinx_copybutton",
    "sphinx_jinja",
    "sphinx.ext.extlinks",
]

# Intersphinx mapping
intersphinx_mapping = {
    "python": ("https://docs.python.org/dev", None),
}

# numpydoc configuration
numpydoc_show_class_members = False
numpydoc_xref_param_type = True

# Consider enabling numpydoc validation. See:
# https://numpydoc.readthedocs.io/en/latest/validation.html#
numpydoc_validate = True
numpydoc_validation_checks = {
    "GL06",  # Found unknown section
    "GL07",  # Sections are in the wrong order.
    "GL08",  # The object does not have a docstring
    "GL09",  # Deprecation warning should precede extended summary
    "GL10",  # reST directives {directives} must be followed by two colons
    "SS01",  # No summary found
    "SS02",  # Summary does not start with a capital letter
    # "SS03", # Summary does not end with a period
    "SS04",  # Summary contains heading whitespaces
    # "SS05", # Summary must start with infinitive verb, not third person
    "RT02",  # The first line of the Returns section should contain only the
    # type, unless multiple values are being returned"
}

extlinks = {
    "MI_docs": (
        "https://ansyshelp.ansys.com/account/secured?returnurl=/Views/Secured/Granta/v251/en/%s",
        None,
    ),
}

# static path
html_static_path = ["_static"]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix(es) of source filenames.
source_suffix = ".rst"

# The master toctree document.
master_doc = "index"

# Set a custom user agent for linkcheck purposes
user_agent = (
    "(Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/123.0.0.0 Safari/537.36 Edg/123.0.2420.81"
)

# Ignore ansys links for linkcheck
linkcheck_ignore = ["https://www.ansys.com/", "https://ansyshelp.ansys.com"]

# sphinx-jinja configuration
jinja_contexts = {"package_versions_ctx": {}}

########
# Fetch dependencies versions
########
packages = []
allow_prereleases = {"true": True, "false": False}[os.getenv("ALLOW_DEPENDENCY_PRERELEASES", "false")]

if not tags.has("list_packages"):  # noqa: F821
    print("'list_packages' tag not provided. Skipping package list generation.")
else:
    print("'list_packages' tag provided. Generating package list.")

    import sys

    sys.path.insert(0, os.path.abspath("../"))
    from list_dependencies import list_current_dependencies

    packages = list_current_dependencies(allow_prereleases=allow_prereleases)


jinja_contexts["package_versions_ctx"]["packages"] = packages
