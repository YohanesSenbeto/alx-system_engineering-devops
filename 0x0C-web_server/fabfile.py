#!/usr/bin/env python3
# Fabfile defining is functions to pack, deploy, and clean the
# current directory to remote server.
from fabric import task


@task
def pack(c):
    """Create the tar gzipped archive of the current directory."""
    c.run("touch holbertonwebapp.tar.gz")
    c.run("tar --exclude='*.tar.gz' -cvzf holbertonwebapp.tar.gz .")


@task
def deploy(c):
    """Upload a archive to the remote server in the /tmp/ directory."""
    c.user = "ubuntu"
    c.put("holbertonwebapp.tar.gz", "/tmp")
    c.run("mkdir /tmp/holbertonwebapp")
    c.run("tar -C /tmp/holbertonwebapp -xzvf /tmp/holbertonwebapp.tar.gz")


@task
def clean(c):
    """Deletes the holbertonwebapp.tar.gz on the local machine."""
    c.run("rm holbertonwebapp.tar.gz")
