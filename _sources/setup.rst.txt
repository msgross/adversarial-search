Setup
============

Installation
-------------

Poetry Installation (**Preferred**)
^^^^^^^^^^^^^^^^^^^^^
This assumes that poetry is already installed and configured on your machine.

You can add this project to a poetry installation via:

.. code-block:: console
    poetry add git+https://github.com/msgross/adversarial-search.git

or:

.. code-block:: console
    poetry add git+git@github.com:msgross/adversarial-search.git

if ssh is configured. 

Docker Installation 
We include a Dockerfile that handles building the package into a .whl file and installing it with pip, 
you can invoke it by cloning the project down and running :code:`docker run`   

Pip Installation (**In Work**)
^^^^^^^^^^^^^^^^^^^^^^^
This isn't officially supported, but if you clone the project down,

.. code-block:: console
    git clone https://github.com/msgross/adversarial-search.git

you can then run:

.. code-block:: console
    poetry update
    poetry build 
    pip install <path_to_dist>/*.whl

to install it in your environment.


Run Tests
---------------
This project uses :code:`pytest`` to define test cases--to run with poetry:

.. code-block:: console
    poetry run pytest 

