.. highlight:: bash

Troubleshooting
===============

nohup
-----

When you use ``nohup`` in your scripts,
don't forget to redirect the output and stderr to ``/dev/null``
and to run the operation in the background using ``&``.
For example::

    nohup python -m SimpleHTTPServer > /dev/null 2>&1 &


File not found error
--------------------

Different linux distributions use different default interpreters.
Thus one might use bash, while the other uses sh.
Hence while bash will noramlly return an informative message
in regards to the shebang line,
the sh message might look something like this::

    /bin/sh: 1: <tmp_path>/...<script_name>: not found

This basically means that the specified path in the
shebang line is invalid
(might be a syntax error or the path specified doesn't lead anywhere).
