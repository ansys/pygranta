Package versions
================

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