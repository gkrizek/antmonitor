
antmonitor
==========

.. image:: https://img.shields.io/pypi/v/antmonitor.svg
    :target: https://pypi.python.org/pypi/antmonitor

.. image:: https://img.shields.io/circleci/project/github/gkrizek/antmonitor.svg
    :target: https://circleci.com/gh/gkrizek/antmonitor

.. image:: https://img.shields.io/pypi/l/antmonitor.svg
    :target: https://opensource.org/licenses/MIT

About
-----

**Antminer Monitor**

Antmonitor is a system monitoring tool for your Antminer devices. This CLI tool can be used to
check things like temperature, fan speed, GH/s, ASIC status, and more. Antmonitor also has the
ability to notify you via Email, SMS, or Webhook (via AWS SNS) if any of these metrics leaves a given threshold.
You can easily setup continuous monitoring by creating a cron job to execute this CLI tool.

*This was written specifically for the Antminer S9, but should work with most other Antminers.*

Installation
------------

Antmonitor can be installed using the pip distribution system for Python by
issuing:

::

    $ pip install antmonitor

Alternatively, you can run use ``setup.py`` to install by cloning this
repository and issuing:

::

    $ python setup.py install  # you may need sudo depending on your python installation

Usage
-----

::

    Usage: antmonitor [OPTIONS] COMMAND

      Antmonitor - Monitor your Antminer devices

    Options:
      -a, --alert  Send an alert if threshold is passed
      -c, --cron   Only log if a threshold is passed
      -q, --quiet  Don't log anything
      --help       Show this message and exit.

    Commands:
      all     Run all checks
      asic    Checks the ASIC status if any `o` are `x`
      config  Creates a ~/.antmonitor.cfg file
      hashes  Check if number of GH/s is below certain number
      memory  Check if free memory is below certain percentage
      pool    Check if Active Pool is what you expect it to be
      temp    Check the temperature is above given temp


After each check, you can either specify the threshold value or it will attempt to read it from your ``.antmonitor.cfg`` file.

Configuration
-------------

Antmonitor looks for a configuration file in your home directory called ``.antmonitor.cfg``.
This file is where you will set up which miners to monitor, whether to alert, your credentials, and much more.
The options include:
::

    miners:

      - antminers: List of Antminer's IPs or hostnames to monitor

    credentials

      - aws:

        - key: AWS Access Key ID for SNS Publishing

        - secret: AWS Access Secret Key for SNS Publishing

      - antminer:

        - username: Username to the Antminer's UI

        - password: Password to the Antminer's UI

    alert:

      - notify: Boolean for whether to notify on alert

      - snstopic: SNS Topic ARN to send an alert to

    threshold:

      - temp: Notify if it reaches this temperature [default is 90]

      - memory: Notify if Free Memory is less than this percent [default is 10]

      - pool: Enable or disable Dead pool notification

      - hashes: Notify if the GH/s is less than this integer

      - fan: Notify if the r/min drops below speed [default is 2000]


*Example Configuration:*

::

  {
    "miners": {
      "antminers": [
        "192.168.1.5",
        "192.168.1.6",
        "192.168.1.7"
      ]
    },
    "credentials": {
      "aws": {
        "key": "AKIAIOSFODNN7EXAMPLE",
        "secret": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
      },
      "antminer": {
        "username": "root",
        "password": "root"
      }
    },
    "alert": {
      "notify": true,
      "snstopic": "arn:aws:sns:us-west-2:800101111111:antminer-email"
    },
    "threshold": {
      "temp": "85",
      "memory": "5",
      "pool": true
      "hashes": "12000",
      "fan": "2000"
    }
  }


------------

`Example Commands <./EXAMPLE.md>`__

Notes
-----

- Currently, all antminer UI password must be the same.

- You must setup your SNS topic subscribers before you can get notified.
