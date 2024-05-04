#!/usr/bin/env bash
set -eu

# ANSI color codes
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No color

# Function to print colored messages
print_info() {
    echo -e "${GREEN}[INFO] $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}[WARN] $1${NC}"
}

print_error() {
    echo -e "${RED}[ERROR] $1${NC}"
}

check_and_install() {
    for tool in "$@"; do
        if command -v "$tool" >/dev/null 2>&1; then
            print_info "$tool is already installed."
        else
            print_warning "$tool is not installed, installing it..."
            sudo pacman -Sy "$tool" --noconfirm
            if command -v "$tool" >/dev/null 2>&1; then
                print_info "$tool has been installed successfully."
            else
                print_error "There was a problem installing $tool. Please try again."
            fi
        fi
    done
}

figlet -ct " Archbox Setup Script" 
if [ -t 0 ]; then
    # Script is being run interactively
    echo "Please enter your GitHub username:"
    read -r USERNAME
else
    # Script is being run non-interactively
    echo "Please enter your GitHub username:"
    read -r USERNAME </dev/tty
fi

check_and_install ansible chezmoi figlet cowsay

# Run chezmoi init
print_info "Running chezmoi init..."
chezmoi init --apply "$USERNAME"

# Clone the git repository
print_info "Cloning 'device-setup' repository..."
if [ -d ~/.config/device-setup ]; then
    rm -rf ~/.config/device-setup
fi

git clone "https://github.com/$USERNAME/device-setup.git" ~/.config/device-setup

cd ~/.config/device-setup
# Run ansible playbook
print_info "Running ansible playbook..."
ansible-galaxy install -r requirements.yml
ansible-playbook -v playbook.yml --ask-become-pass

# Change the remote URL to SSH based URL
print_info "Changing the remote URL to SSH based URL..."
git remote set-url origin "git@github.com:$USERNAME/device-setup.git"

# Return to home directory
cd ~

# Finishing messages
print_info "Setup is complete. Don't forget to set up SSH!"

