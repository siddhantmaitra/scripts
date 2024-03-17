#!/bin/sh
set -eu

check_and_install() {
    for tool in "$@"; do
        if command -v $tool >/dev/null 2>&1; then
            echo "[INFO] $tool is already installed."
        else
            echo "[WARN] $tool is not installed. Would you like to install it? (y/n)"
            read answer
            if [ "$answer" != "${answer#[Yy]}" ]; then
                sudo pacman -Sy $tool --noconfirm
                if command -v $tool >/dev/null 2>&1; then
                    echo "[INFO] $tool has been installed successfully."
                else
                    echo "[ERROR] There was a problem installing $tool. Please try again."
                fi
            fi
        fi
    done
}

echo "Please enter your GitHub username:"
read USERNAME

check_and_install ansible chezmoi

# Run chezmoi init
echo "[INFO] Running chezmoi init..."
chezmoi init --apply $USERNAME

# Clone the git repository
echo "[INFO] Cloning 'device-setup' repository..."
if [ -d ~/.config/device-setup ]; then
	rm -rf ~/.config/device-setup
fi

git clone https://github.com/$USERNAME/device-setup.git ~/.config/device-setup

cd ~/.config/device-setup
echo "[INFO] Running ansible playbook..."
ansible-playbook -v playbook.yml --ask-become-pass

# Change the remote URL to SSH based URL
echo "[INFO] Changing the remote URL to SSH based URL..."
git remote set-url origin git@github.com:$USERNAME/device-setup.git
# Dir is home now!
cd ~
# Finishing messages
echo "[INFO] Setup is complete. Don't forget to setup SSH!"


