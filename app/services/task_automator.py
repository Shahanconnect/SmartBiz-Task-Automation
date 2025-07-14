import os
import subprocess
import webbrowser
import platform
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def run_notepad_task():
    subprocess.Popen(['notepad.exe'])

def open_calculator():
    subprocess.Popen(['calc.exe'])

def open_webpage(url):
    webbrowser.open(url, new=2)

def open_file_explorer():
    subprocess.Popen(['explorer'])

def open_command_prompt():
    subprocess.Popen(['cmd'], creationflags=subprocess.CREATE_NEW_CONSOLE)

def open_system_information():
    if platform.system() == "Windows":
        subprocess.Popen(['msinfo32'])

def restart_computer():
    if platform.system() == "Windows":
        subprocess.call(['shutdown', '/r', '/t', '0'])

def shutdown_computer():
    if platform.system() == "Windows":
        subprocess.call(['shutdown', '/s', '/t', '0'])

