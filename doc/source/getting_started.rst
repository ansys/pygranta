Getting started
===============

The ``pygranta`` metapackage ensures compatibility between PyGranta packages and provides a convenient method for
installing packages compatible with a specific release of Ansys Granta MI.

Most packages require access to an installation of Ansys Granta MI. For more information on getting a licensed copy of
Ansys products, visit the `Ansys website <https://www.ansys.com/>`_.

************
Installation
************

There are several ways of installing PyGranta depending on your use case, but
the easiest is simply to run:

.. code:: bash

   pip install pygranta

This installs all the PyGranta libraries for the latest released
version of Granta MI, for example, v2023R2.

You can always install libraries individually by visiting the install page for
each library. For example, for RecordLists:

.. code:: bash

   pip install ansys-grantami-recordlists


User mode installation
^^^^^^^^^^^^^^^^^^^^^^

Before installing ``pygranta`` in user mode, ensure that you have the latest
version of `pip <https://pypi.org/project/pip/>`_ with:

.. code:: bash

    python -m pip install -U pip

Then, install ``pygranta`` with:

.. code:: bash

   python -m pip install pygranta

If you are interested in **installing a specific version** such as ``2023.1.0``:

.. code:: bash

   python -m pip install pygranta==2023.1.0


Offline mode installation
^^^^^^^^^^^^^^^^^^^^^^^^^

If you lack an internet connection on your installation machine, the
recommended way of installing the ``pygranta`` metapackage is downloading the
wheelhouse archive from the `Releases Page
<https://github.com/ansys/pygranta/releases>`_ for your corresponding machine
architecture.

Each wheelhouse archive contains all the Python wheels necessary to install
``pygranta`` metapackage from scratch on Windows, Linux, and MacOS from Python
3.8 to 3.11. You can install this on an isolated system with a fresh Python
installation or on a virtual environment.

For example, on Linux with Python 3.9, unzip the wheelhouse archive and install
it with the following:

.. code:: bash

    unzip pygranta-v2023.1.dev0-wheelhouse-Linux-3.9-core.zip wheelhouse
    pip install pygranta -f wheelhouse --no-index --upgrade --ignore-installed

If you're on Windows with Python 3.9, unzip to a wheelhouse directory and install using the same command as for Linux.

Consider installing using a `virtual environment <https://docs.python.org/3/library/venv.html>`_.


Versioning system
-----------------

The ``pygranta`` metapackage follows a semantic-like versioning system, though
it has been adapted to the Ansys product release mechanism. In that sense, the
following kind of versioning system is followed:

.. code:: bash

   XXXX.Y.ZZ

Where:

- ``XXXX`` is the Ansys product release year (for example, 2022)
- ``Y`` is the Ansys product release within the same year (for example, 1,
  which relates to R1)
- ``ZZ`` is the patched versions to the ``pygranta`` metapackage, if any.

Consequently, the first ``pygranta`` metapackage compatible with the 2024 R2
release would be:

.. code:: bash

   2024.2.0

And any subsequent patched version of that package would be:

.. code:: bash

   2024.2.1
   2024.2.2
   2024.2.3
   ...

You can request for a specific version install when pip installing your package:

.. code:: bash

   python -m pip install pygranta==2024.2.0