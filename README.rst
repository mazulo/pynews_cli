==========
pynews-cli
==========

A Python CLI to browse news from Hacker News (and others, in the near future). Also is a Python implementation of the awesome `hn-cli <https://github.com/rafaelrinaldi/hn-cli>`_.

Installing
----------

Via pip

.. code-block:: bash

    $ pip install pynews

You can also clone this project and install via setup.py

.. code-block:: bash

    $ git clone git@github.com:mazulo/pynews_cli.git
    $ cd pynews_cli/
    $ python setup.py install


Usage Example
-------------

- Get Top Stories:

.. code-block:: bash

    $ pynews -t 10 # or
    $ pynews --top-stories 10
    # This will show the 10 first *top* stories from the list of 500.

- Get New Stories:

.. code-block:: bash

    $ pynews -n 10 # or
    $ pynews --news-stories
    # This will show the 10 first *new* stories from the list of 500.

See it in action
----------------

.. image:: http://wstaw.org/m/2016/02/16/GIFrecord_2016-02-16_014532.gif
   :height: 552px
   :width: 610px
   :alt: Usage
   :align: center
