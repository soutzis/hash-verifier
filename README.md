# Hash-Verifier (HashV)
**HashV** is a simple command-line tool, used to verify the hash digest of a file. Currently, it supports the algorithms MD5, SHA-256 and SHA-512.
The tool was written in python and uses [py2exe](https://www.py2exe.org) in order to be packaged as an executable.

## Why HashV?
Tools such as this are essential when you need to ensure the integrity of a file that was downloaded over the network. Nowadays, the advancements being made 
in the area of cloud computing are massive. Therefore, downloading files from a remote location has become an inevitable task, especially in businesses. However, 
there are attacks (e.g. variants of [Man-in-the-Middle (MITM)](https://en.wikipedia.org/wiki/Man-in-the-middle_attack) attacks) that could replace the original file
a user intented to download with a malicious one. A more common attack, is when adversaries allegedly provide popular files/programs (that normally require payment) 
for free and thus tricking users into downloading malicious alternatives.
With HashV, a user could download something from a 3rd party website and then use the **original digest, provided by the original distributor** to verify the integrity 
of the file they downloaded. 

*Note: Keep in mind that MD5 is a deprecated cryptographic hash function and has been broken many times. It is vulnerable and allows for collision within its domain 
to be discovered in mere seconds. It is advised to use either SHA-256 or SHA-512.*

## Latest Release
You can find the latest release [here](https://github.com/soutzis/hash-verifier/releases), which includes instructions for adding hash-verifier to the 
environment path variable.


