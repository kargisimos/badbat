# badbat
malicious .bat file generator written in python3.

Usage: python3 badbat.py

 Menu options:
 
        [*] list :                    list all available malicious .bat payloads.
        [*] describe <id> :           get a long description about the specified id.
        [*] outfile <outfile> :       the file which will store the generated payload.
        [*] generate <id> :           generate the .bat file with the specified id.
        [*] help :                    show this help menu
        [*] exit :                    close the program
  
 Available payloads:
         
        id  name                       description
         
        [1] fork bomb :             overload CPU, crash system
        [2] user bomb :             create infinite system users
        [3] folder bomb :           create infinite folders in desktop
        [4] C: destroyer :          delete everything in the C: drive
        [5] dns poisoner :          deny internet access to famous websites
        [6] persistent rebooter :   reboot upon every logon
        [7] time changer :          change time to random value
        [8] mouse swapper :         swap left-click with right-click
        [9] fork bomb v2 :          overload CPU,crash system, spawn notepad, cmd, powershell
