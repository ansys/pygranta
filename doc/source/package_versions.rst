PyGranta and Granta MI compatibility
====================================

PyGranta backwards compatibility
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Starting with ``pygranta`` version 2025.2.0, PyGranta packages aim to be backwards compatible with all Granta MI
versions supported at the time of release. Installing a more modern PyGranta package that has backwards compatibility
with your Granta MI version allows access to improvements and bug fixes.

Full backwards compatibility for all supported Granta MI versions is not guaranteed. Backwards compatibility may end
earlier than the Granta MI support window, and new packages may not support older versions of Granta MI. Check the
"Getting Started" guide for the individual PyGranta package to confirm the minimum required Granta MI version and for
installation instructions.

PyGranta forwards compatibility
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Forwards compatibility of PyGranta packages with future Granta MI releases is not guaranteed. PyGranta packages should
be upgraded following a Granta MI server upgrade.


Package versions
~~~~~~~~~~~~~~~~

These tables map a PyGranta metapackage version to the individual PyGranta package associated with it. This can be used
to determine the **minimum** PyGranta package that is compatible with a given version of Granta MI. However, due to
backwards compatibility, it may be possible to use more modern package versions. See `PyGranta backwards compatibility`_
for more details.

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
