from os import chdir, listdir
from re import compile, sub

from PyQt6.QtGui import QIcon
from PyQt6 import QtWidgets
import mobase


def traverse_and_unignore(modsPath: str):
    """
    Mark all mods that have their updates ignored as no longer ignored
    and return them in a list
    """
    ignored_regex = compile("ignoredVersion=\S+")
    unignored_mods = []

    # Iterate through mod directories
    for mod_dir in listdir(modsPath):
        
        # Check for separators and files related to this program, and skip them
        if (str(mod_dir).__contains__('_separator')
        or str(mod_dir).__contains__('mo2-unignore.log')
        or str(mod_dir).__contains__('unignore.py')):
            continue

        file_data: str
        changed_file_data: str
        try:
            with open(f"{modsPath}\\{mod_dir}\\meta.ini", "r", encoding='UTF-8') as read_file:
                file_data = read_file.read()
                changed_file_data = sub(
                    ignored_regex, 'ignoredVersion=', file_data)

        except FileNotFoundError:
            continue
        
        # Write changed data from memory to meta.ini file if the data changed
        if file_data != changed_file_data:
            try:
                with open(f"{modsPath}\\{mod_dir}\\meta.ini", 'w', encoding="utf-8") as write_file:
                    write_file.write(changed_file_data)
                    unignored_mods.append(mod_dir)
            except FileNotFoundError:
                continue

    return unignored_mods


class UnignoreUpdates(mobase.IPluginTool):
    organizer: mobase.IOrganizer

    def __init__(self):
        super().__init__()

    def init(self, newOrganizer: mobase.IOrganizer):
        self.organizer = newOrganizer
        return True

    def name(self) -> str:
        return "Unignore Mod Updates"

    def author(self) -> str:
        return "Zediious"

    def description(self) -> str:
        return "Un-ignore updates for all mods in the list."

    def version(self) -> mobase.VersionInfo:
        return mobase.VersionInfo(1, 2, mobase.ReleaseType.FINAL)

    def isActive(self) -> bool:
        return self.organizer.pluginSetting(self.name(), "enabled")

    def settings(self):
        return [mobase.PluginSetting("Enabled", "Enable this plugin", True)]

    def displayName(self) -> str:
        return "Unignore Mod Updates"

    def tooltip(self) -> str:
        return "Un-ignore updates for all mods in the list."

    def icon(self):
        return QIcon('null')

    def display(self):
        """
        Function called when tool is used in GUI
        """
        updating_mods = traverse_and_unignore(self.organizer.modsPath())
        updating_mods_string = ""
        if updating_mods != []:
            for mod in updating_mods:
                updating_mods_string += f"{mod}\n"
        else:
            updating_mods_string = "No mods had their updates ignored."

        QtWidgets.QMessageBox.information(
            self._parentWidget(), 'Mods who are now checking for updates', updating_mods_string)


def createPlugin() -> mobase.IPlugin:
    return UnignoreUpdates()
