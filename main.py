import os
import click
import socket

SMB_SERVICE_NAME = "smbd"

@click.group()
def main():
    """Samba File Sharing Service Management Tool"""
    pass

@main.command()
def start():
    """Start the Samba File Sharing Service"""
    try:
        os.system(f"sudo service {SMB_SERVICE_NAME} start")
        click.echo("Samba File Sharing Service started.")
    except Exception as e:
        click.echo(f"Error starting Samba: {e}")

@main.command()
def stop():
    """Stop the Samba File Sharing Service"""
    try:
        os.system(f"sudo service {SMB_SERVICE_NAME} stop")
        click.echo("Samba File Sharing Service stopped.")
    except Exception as e:
        click.echo(f"Error stopping Samba: {e}")

@main.command()
def restart():
    """Restart the Samba File Sharing Service"""
    try:
        os.system(f"sudo service {SMB_SERVICE_NAME} restart")
        click.echo("Samba File Sharing Service restarted.")
    except Exception as e:
        click.echo(f"Error restarting Samba: {e}")

@main.command()
def status():
    """Check the Status of the Samba File Sharing Service"""
    try:
        status_output = os.popen(f"sudo service {SMB_SERVICE_NAME} status").read()
        click.echo(status_output)
    except Exception as e:
        click.echo(f"Error checking status: {e}")

@main.command()
def info():
    """Display User, System, and Network Information"""
    try:
    click.echo("User Information:")
    click.echo(f"  Current User: {os.getlogin()}")
    click.echo(f"  User ID: {os.getuid()}")

    click.echo("\nSystem Information:")
    click.echo(f"  Hostname: {socket.gethostname()}")
    click.echo(f"  OS: {os.uname().sysname} {os.uname().release}")

    click.echo("\nNetwork Information:")
    click.echo(f"  IP Address: {socket.gethostbyname(socket.gethostname())}")
    click.echo("  Instructions for Connecting to Other Machines:")
    click.echo("  - For Linux: Open a terminal and use 'smbclient' or 'nautilus' to connect.")
    click.echo("  - For Windows: Open File Explorer and enter '\\\\<Linux-IP>' in the address bar. Hint: type hostname -I")
    
    except Exception as e:
        click.echo(f"Error displaying information: {e}")

if __name__ == "__main__":
    main()
