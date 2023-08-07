# Samba File Sharing Service Management CLI Tool
### This is a command-line tool for managing the Samba file sharing service on a Linux system. It provides a simple interface to start, stop, restart, and check the status of the Samba service.

## Installation
Make sure you have Python 3 installed on your system.

#### Download the main.py script from this repository.

###Make the script executable:
```
chmod +x main.py
```
## Usage
### Run the script from the command line with the following subcommands:
```
./main.py start: Start the Samba service.
./main.py stop: Stop the Samba service.
./main.py restart: Restart the Samba service.
./main.py status: Check the status of the Samba service.
```
## Examples
To start the Samba service:


```./samba_manager.py start```
To stop the Samba service:


```
./samba_manager.py stop
```
To restart the Samba service:

```
./samba_manager.py restart
```
To check the status of the Samba service:

```
./samba_manager.py status
```
## Notes
This tool assumes that you have Samba already installed and configured on your system.

Make sure to run the tool with superuser privileges (e.g., using sudo) to manage system services.

## Disclaimer
This tool is provided as-is and does not guarantee error-free operation. Use it responsibly and ensure you understand its impact on your system.

## License
This project is licensed under the MIT License.

