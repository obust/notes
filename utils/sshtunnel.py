#!/usr/bin/env python
"""
This script helps set up a sshtunnel to a remote server.

SETUP
- Make sure that this file is executable :
    chmod +x $HOME/path/to/this/script
- Set an alias in ~/.bashrc :
    alias sshtunnel=$HOME/path/to/this/script

USAGE
sshtunnel --remote 8888 --local 8080
"""
import argparse
import subprocess


def main(remote, local):
    host = 'romain@scyfer.cloudportaal.net'
    command = ('ssh -L {local}:localhost:{remote} {host}'
               .format(local=local, remote=remote, host=host))
    print(command)
    subprocess.call(command, shell=True)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-r', '--remote', type=str, required=True,
                        help="Remote port")
    parser.add_argument('-l', '--local', type=str, default=8080,
                        help="Local port")
    main(**vars(parser.parse_args()))
