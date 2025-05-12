PyGranta and Granta MI compatibility
====================================

PyGranta packages have always been compatible with the Granta MI version they were delivered against.

Starting with pygranta version ``2025.2.0`` (released with Granta MI 2025 R2), where possible, PyGranta packages are
backwards compatible with all supported Granta MI versions at the time of release. This allows access to improvements
and bug fixes without having to upgrade Granta MI.

Note: Full backwards compatibility for all supported Granta MI versions is not always guaranteed. Check the README or
"Getting Started" guide for the individual PyGranta package to confirm the minimum required Granta MI version and for
installation instructions.

If the latest PyGranta package version does not support the required Granta MI version, either:

* Use previous versions of the PyGranta package documentation to check compatibility of previous package versions, or
* Use the table in the `Package versions`_ section to identify the version of the PyGranta package released with the
  required Granta MI version.

In addition, forwards compatibility of PyGranta packages with future Granta MI releases is not guaranteed. PyGranta
packages should always be upgraded following a Granta MI server upgrade.


Package versions
----------------

These tables map a PyGranta metapackage version to the individual PyGranta package associated with it. This can be used
to determine the **minimum** PyGranta package that is compatible with a given version of Granta MI. However, due to
backwards compatibility, it may be possible to use more modern package versions.

.. note::
   The ``ansys-grantami-bomanalytics`` and ``ansys-grantami-bomanalytics-openapi`` versions included in the metapackage
   are compatible with that version of *BoM Analytics Services*, included with Granta MI Restricted Substances and
   Sustainability Reports. Multiple versions of BoM Analytics Services are compatible with a single version of Granta
   MI.

.. jinja:: package_versions_ctx

    {% for release, packages in releases.items() %}
    {{"*" * release|length}}
    {{release}}
    {{"*" * release|length}}

    .. list-table::
       :header-rows: 1

       * - Library
         - Version
         - Links
    {% for package in packages %}
       * - {{package.name}}
         - {{package.version}}
         - `PyPI <{{package.pypi}}>`__{% if package.docs %}, `Documentation <{{package.docs}}>`__{% endif %}
    {% endfor %}
    {% endfor %}
