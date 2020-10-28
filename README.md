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

## Setup Instructions (Windows 10)

The instructions for adding HashV to the environment path variable on your system are very simple:

1. Download the .zip file and extract it anywhere you want on your computer. (It is recommended to create a new folder on your C: drive called hash-verifier and extract the .zip file there. You should then have a filepath looking like this: 'C:\hash-verifier\dist')
2. - **(a) FOR ADMINS**: Go to the Windows search box and type "Edit the system environment variables" and press Enter. Then click on the button "Environment Variables". At the "System variables" (bottom box), select the "Path" variable and click "Edit".
   - **(b) FOR NON-ADMINS**: Go to the Windows search box and just type "Edit environment variables for your account" and press Enter. At the "User variables" (top box), select the "Path" variable and click "Edit".
4. Click "New" and enter the path of the 'dist' folder wherever you extracted it. If you followed the recommended location from step-1, then here you should enter "C:\hash-verifier\dist\"
5. Reboot your computer. This is necessary for the path to register the new variable we created.

Done! You can now use hash-verifier from anywhere on your system by using the "hashv" command. Type "hashv help" in your terminal to see the usage option


## Usage Example
Let's try HashV by downloading the latest VirtualBox installer and verifying the download using the sha-256 checksum from the website. This example assumes that you successfuly followed the setup instructions and added HashV to the environment path.

**1. Download the latest VBox installer**

![image](https://i.imgur.com/5kWUEm2.png)

**2. Find the original sha-256 hash digest of the file you just downloaded**
![image](https://i.imgur.com/IX9liJm.png)
![image](https://i.imgur.com/MDAspVr.png)

**3. Go to the folder where you downloaded the file and type "cmd" in the explorer address bar**
![image](https://i.imgur.com/APs2TBV.png)

**4. Type hashv -filename- -hash- (Use tab for autocompletion in cmd) and press enter**
![image](https://i.imgur.com/lPJUyEV.png)
![image](https://i.imgur.com/baZQINp.png)

## Latest Release
You can find the latest release [here](https://github.com/soutzis/hash-verifier/releases), which includes instructions for adding hash-verifier to the 
environment path variable.

 
