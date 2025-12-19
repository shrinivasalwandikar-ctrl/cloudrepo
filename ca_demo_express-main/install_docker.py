#!/usr/bin/env python3
"""
install_docker.py

Installs Docker Engine on Debian/Ubuntu following Docker's official repo instructions,
and optionally installs Nginx. Run with `--nginx` to install Nginx as well.

Note: This script runs commands that require root. It uses `sudo` when not run as root.
Use `--yes` to run non-interactively.
"""

import argparse
import os
import subprocess
import sys


def run(cmd, shell=False, check=True):
    print(f"> {cmd if shell else ' '.join(cmd)}")
    subprocess.run(cmd, shell=shell, check=check)


def is_root():
    return hasattr(os, "geteuid") and os.geteuid() == 0


def sudo_prefix():
    return [] if is_root() else ["sudo"]


def detect_debian_like():
    try:
        with open('/etc/os-release') as f:
            text = f.read()
        return 'ID_LIKE=debian' in text or 'ID=ubuntu' in text or 'ID=debian' in text
    except Exception:
        return False


def install_docker_official(non_interactive=False):
    if not detect_debian_like():
        print('This installer currently supports Debian/Ubuntu only. Aborting.')
        sys.exit(1)

    s = sudo_prefix()
    try:
        print('Removing old Docker versions (if any)...')
        run(s + ['apt-get', 'remove', '-y', 'docker', 'docker-engine', 'docker.io', 'containerd', 'runc'])

        print('Updating package index...')
        run(s + ['apt-get', 'update'])

        print('Installing packages to allow apt to use a repository over HTTPS...')
        run(s + ['apt-get', 'install', '-y', 'ca-certificates', 'curl', 'gnupg', 'lsb-release'])

        print('Adding Docker’s official GPG key...')
        # Use the recommended keyring location
        run("curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg", shell=True)

        print('Setting up the Docker repository...')
        run("echo \"deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable\" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null", shell=True)

        print('Updating package index again...')
        run(s + ['apt-get', 'update'])

        print('Installing Docker Engine and components...')
        run(s + ['apt-get', 'install', '-y', 'docker-ce', 'docker-ce-cli', 'containerd.io', 'docker-compose-plugin'])

        print('Enabling and starting Docker...')
        run(s + ['systemctl', 'enable', 'docker'])
        run(s + ['systemctl', 'start', 'docker'])

        username = os.environ.get('SUDO_USER') or os.environ.get('USER') or os.getlogin()
        print(f'Adding user {username} to docker group...')
        run(s + ['usermod', '-aG', 'docker', username])

        print('Docker installation completed.')
    except subprocess.CalledProcessError as e:
        print('Error during installation:', e)
        sys.exit(1)


def install_nginx(non_interactive=False):
    s = sudo_prefix()
    try:
        print('Updating package index...')
        run(s + ['apt-get', 'update'])
        print('Installing Nginx...')
        run(s + ['apt-get', 'install', '-y', 'nginx'])
        print('Enabling and starting Nginx...')
        run(s + ['systemctl', 'enable', 'nginx'])
        run(s + ['systemctl', 'start', 'nginx'])
        print('Nginx installation completed.')
    except subprocess.CalledProcessError as e:
        print('Error during Nginx installation:', e)
        sys.exit(1)


def parse_args():
    p = argparse.ArgumentParser(description='Install Docker (official method) and optionally Nginx.')
    p.add_argument('--nginx', action='store_true', help='Also install Nginx')
    p.add_argument('--yes', action='store_true', help='Run non-interactively (auto-yes)')
    return p.parse_args()


def main():
    args = parse_args()
    print('Starting installer')
    install_docker_official(non_interactive=args.yes)
    if args.nginx:
        install_nginx(non_interactive=args.yes)
    print('All requested tasks finished. You may need to log out and back in for docker group changes to take effect.')


if __name__ == '__main__':
    main()