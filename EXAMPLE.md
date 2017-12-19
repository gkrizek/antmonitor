# Examples

Configuration File
------------------

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
          "username": "admin",
          "password": "password"
        }
      },
      "alert": {
        "notify": true,
        "snstopic": "arn:aws:sns:us-west-2:800101111111:antminer-email"
      },
      "threshold": {
        "temp": "85",
        "memory": "5",
        "pool": "youpoolurl",
        "hashes": "12000"
      }
    }


Cron
----

::

    * * * * * antmonitor all --cron >> /var/log/antmonitor.cron 2>&1
