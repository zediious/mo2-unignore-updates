# Mod Organizer 2 - Un-ignore downloads

This script will make all mods in a Mod Organizer list no longer ignore updates, after they have been told to do so via the context menu.

If you have done this to a lot of mods, this can help you quickly fix that up.

## Instructions to run

1) Download Python ([https://www.python.org/downloads/]

2) Download the [LATEST RELEASE](https://github.com/zediious/mo2-unignore-updates/releases) and place the `.py` file inside your Mod Organizer 2 `mods` directory.

3) Open your terminal of choice, and move to your `mods` directory. Run `python unignore.py` once you are in the `mods` directory.

This will replace any instances of `ignoredVersion=` that are followed by any non-whitespace characters within a `meta.ini` file for any mod, with only `ignoredVersion=`. It will only affect files that are not already un-ignored. A log will be printed to the terminal of all affected mods, and that log will be saved in the `mods` directory.
