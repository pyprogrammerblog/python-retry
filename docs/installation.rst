Installation
============


Windows (pip)
-------------

The following recipe is still a work in progress:

1. `Install Python>=3.6 (stable) <https://www.python.org/downloads/windows/>`_
2. Start the command prompt
3. Install python-retry::

    pip install python-retry


.. note::

   You might need to setup your C++ compiler according to
   `this <https://wiki.python.org/moin/WindowsCompilers>`_.


Advanced: local setup with system Python (Ubuntu)
-------------------------------------------------

These instructions make use of the system-wide Python 3 interpreter::

    $ sudo apt install python3-pip

Install python-retry::

    $ pip install --user python-retry


Advanced: local setup for development (Ubuntu)
----------------------------------------------

These instructions assume that ``git``, ``python3``, ``pip``, and
``virtualenv`` are installed on your host machine.

Clone the python-retry repository::

    $ git clone https://github.com/pyprogrammerblog/python-retry

Create and activate a virtualenv::

    $ cd python-retry
    $ virtualenv --python=python3 .venv
    $ source .venv/bin/activate

Run the tests::

    (.venv) $ pytest
