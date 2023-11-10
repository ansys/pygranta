PyGranta metapackage
====================
|pyansys| |python| |pypi| |GH-CI| |MIT| |black| |pre-commit|

.. |pyansys| image:: https://img.shields.io/badge/Py-Ansys-ffc107.svg?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAIAAACQkWg2AAABDklEQVQ4jWNgoDfg5mD8vE7q/3bpVyskbW0sMRUwofHD7Dh5OBkZGBgW7/3W2tZpa2tLQEOyOzeEsfumlK2tbVpaGj4N6jIs1lpsDAwMJ278sveMY2BgCA0NFRISwqkhyQ1q/Nyd3zg4OBgYGNjZ2ePi4rB5loGBhZnhxTLJ/9ulv26Q4uVk1NXV/f///////69du4Zdg78lx//t0v+3S88rFISInD59GqIH2esIJ8G9O2/XVwhjzpw5EAam1xkkBJn/bJX+v1365hxxuCAfH9+3b9/+////48cPuNehNsS7cDEzMTAwMMzb+Q2u4dOnT2vWrMHu9ZtzxP9vl/69RVpCkBlZ3N7enoDXBwEAAA+YYitOilMVAAAAAElFTkSuQmCC
   :target: https://docs.pyansys.com/
   :alt: PyAnsys

.. |python| image:: https://img.shields.io/pypi/pyversions/pygranta?logo=pypi
   :target: https://pypi.org/project/pygranta/
   :alt: Python

.. |pypi| image:: https://img.shields.io/pypi/v/pygranta.svg?logo=python&logoColor=white
   :target: https://pypi.org/project/pygranta/
   :alt: PyPI

.. |GH-CI| image:: https://github.com/ansys/pygranta/actions/workflows/ci-build.yml/badge.svg
   :target: https://github.com/ansys/pygranta/actions/workflows/ci-build.yml
   :alt: GH-CI

.. |MIT| image:: https://img.shields.io/badge/License-MIT-yellow.svg
   :target: https://opensource.org/licenses/MIT
   :alt: MIT

.. |black| image:: https://img.shields.io/badge/code%20style-black-000000.svg?style=flat
   :target: https://github.com/psf/black
   :alt: Black

.. |pre-commit| image:: https://results.pre-commit.ci/badge/github/pyansys/pygranta/main.svg
   :target: https://results.pre-commit.ci/latest/github/pyansys/pygranta/main
   :alt: pre-commit.ci status

Welcome to the PyGranta metapackage repository. The ``pygranta`` metapackage
provides a single package of collected PyGranta packages that ensures compatibility
of these packages amongst themselves and the Granta MI release that they are linked to.

The ``pygranta`` metapackage ensures compatibility between these PyGranta packages:

- `BoM Analytics <https://bomanalytics.grantami.docs.pyansys.com/>`_: Pythonic interface to Ansys Granta MI BoM Analytics services.
- `RecordLists <https://recordlists.grantami.docs.pyansys.com/>`_: Pythonic interface to Ansys Granta MI Lists API.
- `serverapi-openapi <https://shared.docs.pyansys.com/>`_: Shared Ansys software components to enable package interoperability and minimize maintenance.

The PyGranta metapackage installs these core modules:

- `BoM Analytics`_
- `RecordLists`_
- `serverapi-openapi`_

Package installation
--------------------

Two installation modes are provided: user and offline.

User mode installation
^^^^^^^^^^^^^^^^^^^^^^

Before installing the ``pygranta`` metapackage in user mode, ensure that you have
the latest version of `pip <https://pypi.org/project/pip/>`_ with this command:

.. code:: bash

    python -m pip install -U pip

Then, install the ``pygranta`` metapackage with this command:

.. code:: bash

   python -m pip install pygranta

If you are interested in **installing a specific version** such as ``2023.1.0``,
you use a command like this:

.. code:: bash

   python -m pip install pygranta==2023.1.0

Offline mode installation
^^^^^^^^^^^^^^^^^^^^^^^^^

If you lack an internet connection on your installation machine, the recommended way of installing
the ``pygranta`` metapackage is downloading the wheelhouse archive from the
`Releases Page <https://github.com/ansys/pygranta/releases>`_ for your corresponding machine architecture.

Each wheelhouse archive contains all the Python wheels necessary to install the ``pygranta`` metapackage from
scratch on Windows, Linux, and MacOS from Python 3.8 to 3.11. You can install this on an isolated system with
a fresh Python installation or on a virtual environment.

For example, on Linux with Python 3.8, unzip the wheelhouse archive and install it with the following
commands:

.. code:: bash

    unzip pygranta-v2023.1.dev0-wheelhouse-Linux-3.8-core.zip wheelhouse
    pip install pygranta -f wheelhouse --no-index --upgrade --ignore-installed

If you're on Windows with Python 3.9, unzip to a wheelhouse directory and then install using
the same ``pip`` command as in the previous example.

Consider installing using a `virtual environment <https://docs.python.org/3/library/venv.html>`_.

Versioning system
-----------------

The ``pygranta`` metapackage follows a semantic-like versioning system, though it has been adapted to the
Ansys product release mechanism. Thus, this kind of versioning system is followed:

.. code:: bash

   XXXX.Y.ZZ

Where:

- ``XXXX`` is the Ansys product release year (for example, 2022).
- ``Y`` is the Ansys product release within the same year (for example, 1, which relates to R1).
- ``ZZ`` is a patched version to the ``pygranta`` metapackage, if any.

Consequently, the first ``pygranta`` metapackage compatible with the 2024 R2 release would be:

.. code:: bash

   2024.2.0

Any subsequent patched version of this package would be:

.. code:: bash

   2024.2.1
   2024.2.2
   2024.2.3
   ...

You can request a specific version install when using ``pip`` to install
your package:

.. code:: bash

   python -m pip install pygranta==2024.2.0

License and acknowledgments
---------------------------
All PyGranta libraries are licensed under the MIT license.

PyGranta libraries make no commercial claim over Ansys whatsoever.
These libraries extend the functionality of Ansys products by
adding Python interfaces to legally obtained software products
without changing the core behaviors or licenses of the original
software.

For more information on Ansys products, visit the `Ansys web site <https://www.ansys.com/>`_.
