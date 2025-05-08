Getting started
===============

The ``pygranta`` metapackage guarantees mutual compatibility between all PyGranta packages. The packages referenced by a
``pygranta`` metapackage version are certified to be compatibile with each other and with the corresponding Granta MI
version.

.. note::
   The ``ansys-grantami-bomanalytics`` and ``ansys-grantami-bomanalytics-openapi`` versions included in the metapackage
   are compatible with that version of *BoM Analytics Services*, included with Granta MI Restricted
   Substances and Sustainability Reports. Multiple versions of BoM Analytics Services are compatible with a single
   version of Granta MI.

Most packages require access to an installation of Ansys Granta MI. For more information on getting a licensed copy of
Ansys products, visit the `Ansys website <https://www.ansys.com/>`_.

Installing the latest version
-----------------------------

To install the latest version of the ``pygranta`` metapackage, run:

.. code:: bash

   pip install pygranta

This installs all the PyGranta packages certified to be compatible with the latest released version of Granta MI.


Installing packages compatible with a specific version of Granta MI
-------------------------------------------------------------------

To install the version of the ``pygranta`` metapackage associated with a specific version of Granta MI, provide the
version number during installation. For example, to install the version associated with Granta MI 2023 R2, specify the
``pygranta`` metapackage version ``2023.2.0``:

.. code:: bash

   pip install pygranta==2023.2.0

More detailed guidance on selecting package versions which are compatible with specific Granta MI versions is available
on the :doc:`package_versions` page. This page also includes a list of all PyGranta packages associated with each
``pygranta`` metapackage version.

See `Versioning system`_ for more details on PyGranta pacakge version numbers.


User mode installation
----------------------

Before installing the ``pygranta`` metapackage in user mode, ensure that you have the
latest version of `pip <https://pypi.org/project/pip/>`_ by running this command:

.. code:: bash

    python -m pip install -U pip

Then, install the ``pygranta`` metapackage with this command:

.. code:: bash

   python -m pip install pygranta

If you are interested in **installing a specific version**, such as ``2023.2.0``, you
can run a command like this one:

.. code:: bash

   python -m pip install pygranta==2023.2.0


Offline installation
--------------------

If you lack an internet connection on your installation machine, the
recommended way of installing the ``pygranta`` metapackage is downloading the
wheelhouse archive for your corresponding machine
architecture from the repository's `Releases
<https://github.com/ansys/pygranta/releases>`_ page.

Each wheelhouse archive contains all the Python wheels necessary to install
the ``pygranta`` metapackage from scratch on Windows and Linux for all supported
Python versions. You can install this on an isolated system with a fresh Python
installation or on a virtual environment.

For example, on Linux with Python 3.12, unzip the wheelhouse archive and install
it with these commands:

.. code:: bash

    unzip pygranta-v2023.2.0-wheelhouse-Linux-3.12-core.zip wheelhouse
    pip install pygranta -f wheelhouse --no-index --upgrade --ignore-installed

If you're on Windows with Python 3.12, unzip to a wheelhouse directory and install
using the same command as for Linux.

Consider installing using a `virtual environment <https://docs.python.org/3/library/venv.html>`_.


Versioning system
-----------------

The ``pygranta`` metapackage follows a semantic-like versioning system, though
it has been adapted to the Ansys product release mechanism. In this sense, the
following versioning system is followed:

.. code:: bash

   XXXX.Y.ZZ

Where:

- ``XXXX`` is the Ansys product release year (for example, 2024).
- ``Y`` is the Ansys product release within the same year (for example, 1,
  which relates to R1).
- ``ZZ`` is the patched versions to the ``pygranta`` metapackage, if any.

Consequently, the first ``pygranta`` metapackage compatible with the 2024 R1
release would be:

.. code:: bash

   2024.1.0

Any subsequent patched version of this package would have these versions:

.. code:: bash

   2024.1.1
   2024.1.2
   2024.1.3
   ...

When using ``pip`` to install your package, you can install a specific version with a
command like this:

.. code:: bash

   python -m pip install pygranta==2024.1.0
