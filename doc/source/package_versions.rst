Package versions
================

These tables map a PyGranta metapackage version to the individual PyGranta package included within it. In most cases,
this can be used to determine which PyGranta package is compatible with a given version of Granta MI.

.. note::
   The PyGranta metapackage version for ansys-grantami-bomanalytics and ansys-grantami-bomanalytics-openapi refers to
   the required version of BoM Analytics Services, included with Granta MI Restricted Substances and Sustainability
   Reports.

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