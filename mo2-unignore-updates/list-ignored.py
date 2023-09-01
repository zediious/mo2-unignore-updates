from os import chdir, listdir
from re import compile, sub

ignored_regex = compile('ignoredVersion=\S+')

# Open the log file to write changes to as the script runs
with open('mo2-ignored.log', 'w') as log_file:

    log_file.write("List of mods that will no longer ignore updates;\n")

    # Iterate through mod directories
    for mod_dir in listdir():
        
        # Check for separators and files related to this program, and skip them
        if (str(mod_dir).__contains__('_separator')
        or str(mod_dir).__contains__('mo2-ignored.log')
        or str(mod_dir).__contains__('list-ignored.py')):
            continue
        
        # Move into mod directory
        chdir(str(mod_dir))
        
        # Read the mod's meta.ini file to memory
        file_data: str
        changed_file_data: str
        try:
            with open('meta.ini', "r") as read_file:
                file_data = read_file.read()
                changed_file_data = sub(ignored_regex, 'ignoredVersion=', file_data)
        except FileNotFoundError:
            print(f'The mod "{mod_dir}" did not have a meta.ini file')
        
        # Log mod if the data changed
        if file_data != changed_file_data:
            # Log the changed mod
            log_file.write(f"{str(mod_dir)}\n")
        
        # Move back up to main mods directory    
        chdir('..')

# Print the log
with open('mo2-ignored.log', 'r') as log_file:

    print(" ")
    for line in log_file:

        print(line.strip())
