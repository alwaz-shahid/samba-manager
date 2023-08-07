import os
import click

SMB_SERVICE_NAME = "smbd"

@click.group()
def main():
    """Samba File Sharing Service Management Tool"""
    pass

@main.command()
def start():
    """Start the Samba File Sharing Service"""
    click.echo("Starting Samba File Sharing Service...")
    os.system(f"sudo service {SMB_SERVICE_NAME} start")
    click.echo("Samba File Sharing Service started.")

@main.command()
def stop():
    """Stop the Samba File Sharing Service"""
    click.echo("Stopping Samba File Sharing Service...")
    os.system(f"sudo service {SMB_SERVICE_NAME} stop")
    click.echo("Samba File Sharing Service stopped.")

@main.command()
def restart():
    """Restart the Samba File Sharing Service"""
    click.echo("Restarting Samba File Sharing Service...")
    os.system(f"sudo service {SMB_SERVICE_NAME} restart")
    click.echo("Samba File Sharing Service restarted.")

@main.command()
def status():
    """Check the Status of the Samba File Sharing Service"""
    status_output = os.popen(f"sudo service {SMB_SERVICE_NAME} status").read()
    click.echo(status_output)

if __name__ == "__main__":
    main()
