from dearpygui.core import *
from dearpygui.simple import *
from nptdms import TdmsFile


def file_picker(sender, data):
    open_file_dialog(callback=apply_selected_file, extensions=".tdms")


def apply_selected_file(sender, data):
    log_debug(data)  # so we can see what is inside of data
    directory = data[0]
    file = data[1]
    filepath = directory + "/" + file
    
    set_value("directory", directory)
    set_value("file", file)
    set_value("filepath", filepath)
    
    ## Get TDMS Info

    with TdmsFile.open(filepath) as tdms:
        groups = tdms.groups()
        channels = groups[0].channels()

    log_debug(groups)
    log_debug(channels)
    # Table of
    # Groups, Channels, Length, Sample Rate, Units
    # tdms = TdmsFile.read("")


show_logger()
# show_documentation()

with window("Plot"):
    add_button("Directory Selector", callback=file_picker)
    add_text("Directory Path: ")
    add_same_line()
    add_label_text("##filedir", source="directory", color=[255, 0, 0])
    add_text("File: ")
    add_same_line()
    add_label_text("##file", source="file", color=[255, 0, 0])


start_dearpygui(primary_window="Plot")
