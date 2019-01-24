This is a tmporary test repository...

The purpose of it is to provide a test python script for characters input under python curses module, aiming especially to CJK (Chinese - Japonese - Korean) characters.

The script **curses-test-input.py** has already been tested with inputing Greek characters, both in python2 and python3.

But I need help to check its behaviur with CJK characters (or any other encoding apart from utf-8). So if you can help, just clone it and give it a go.

## How to perform checks

1. Run the script and start typing characters both in english and your native language. Check the results.

2. Check its behaviour with both **pyrhon2** and **python3**.

When you run the script you will see the python version. This is the default python version for your system.

Edit the script and force the execution of **pyrhon2** or **python3**.

To do that, change the first line from

```
#!/bin/python
```
to
```
#!/bin/python2
```
or
```
#!/bin/python3
!!!
accordind to your previous version

This is the output of the script typing english, greek and "control" characters

![Output sample](sample.jpg?raw=true "Output sample")

## Feedback

When you have concluded the test, just open an **Issue** and tell me about it

