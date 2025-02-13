# Mod Organizer 2 - Un-ignore downloads

This plugin will make all mods in a Mod Organizer list no longer ignore updates, after they have been told to do so via the context menu.

If you have done this to a lot of mods, this can help you quickly fix that up.

This exists as a Mod Organizer 2 plugin.

1) Download the [latest release](https://github.com/zediious/mo2-unignore-updates/releases).

2) Extract `UnignoreModUpdates.py` to the `plugins` directory in your Mod Organizer 2 instance. Restart Mod Organizer if it is not already closed.

3) Use the "Unignore Mod Updates" option under the puzzle piece icon at the top panel in Mod Organizer.

4) Any mods who have had their updates ignored will no longer ignore them. You may need to press F5 to refresh Mod Organizer to see this..

The standalone script is to be placed directly in your `mods` directory and ran by command line. It will print a log of unignored mods. An optional script exists to only list the mods, without making the changes.

## Instructions to run the standalone scripts

1) Download Python ([https://www.python.org/downloads/]

2) Download the [LATEST RELEASE](https://github.com/zediious/mo2-unignore-updates/releases) and place the `.py` file inside your Mod Organizer 2 `mods` directory.

3) Open your terminal of choice, and move to your `mods` directory. Run `python unignore.py` once you are in the `mods` directory.

This will replace any instances of `ignoredVersion=` that are followed by any non-whitespace characters within a `meta.ini` file for any mod, with only `ignoredVersion=`. It will only affect files that are not already un-ignored. A log will be printed to the terminal of all affected mods, and that log will be saved in the `mods` directory.
