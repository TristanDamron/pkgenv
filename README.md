# Package Env 0.2.0
Package Env (abbreviated as pkgenv) is a better way to do package management for Linux systems. Package Env allows you to create user space package environments by isolating system packages on a variety of Linux distributions.

Originally hacked together by Tristan Damron over Labor Day Weekend 2022

## Use Cases

- Creating isolated development environments using packages that are already on your system, (alternative to pyenv, Docker and other similar tools).
- Creating simulated environments for educational/training purposes.
- Switching between multiple versions of a software package with a single command.

## (Officially) Supported Distros
Package Env supports the following Linux distributions using Bash:
- Ubuntu
- Debian
- openSUSE
- Alpine Linux
- Arch Linux

## Supported Package Managers
Package Env supports the following package managers:
- apt-get
- zypper
- apk
- pacman
- pip
- gem 

Note that installing a package with `pkgenv add --package {your package}` will only perform a simple installation. For more complex use cases, stick to installing stuff with your system's package managers rather than installing through pkgenv.

# User Guide

## Dependencies

Package Env is written in Python and requires that you have Python 3.5 (or better) installed on your system. Additionally, Package Env depends on GNU system utils such as `which`, `readlink`, and `dirname` to function. Because of this, Package Env does not support BSD based systems. Vim and/or Nano are also strongly recommended to properly configure your Package Env config.yaml file.

## Installation

1. Clone this repository somewhere on your hard drive.
1. `cd` into the cloned repo and execute `sh install.sh`. 
1. The install script will take the pkgenv command and symlink it to /usr/local/bin/pkgenv

## Creating Your First Package Environment

1. Execute `pkgenv create`. Optionally, provide the `--name` flag to give your new package environment a custom name. Otherwise, an autogenerated name will be used for the new package environment.
1. Read the logs that appear on the screen. You'll notice that pkgenv added `pkgenv`, `which`, `readlink`, and `dirname` to the environment. These commands are required for pkgenv to work. If you have a preferred editor set in ~/.pkgenv/config.yaml, that will also be added to the new package environment.

## Package Env Configuration

1. Execute `pkgenv config`. 
1. If you haven't set a preferred text editor, you'll be asked to do so in the terminal. By default, you can choose between Vim and Nano, but you're welcome to change this to your favorite editor afterwards.
1. The ~/.pkgenv/config.yaml file opens in your preferred text editor.
1. There are several values to note in this configuration file:
- active_package_environment: The current, active package environment for your system.
- custom_environment_paths: A list of all known package environments on your system.
- default_environment_path: The system's default $PATH. It is recommended that you do not change this value to preserve your system's default PATH as you switch between package environments.
- preferred_editor: Your preferred text editor for opening the pkgenv config file.
- system_package_managers: All known package managers on your system.

## Adding Packages To A Package Environment

1. Execute `pkgenv add --package {your package} --name {your custom package environment}`. Optionally, include the `--manager {your package manager}` flag to install the package with a known package manager if it is not found on the system's default PATH.
1. If the package is not on the system's PATH and you did not set the `--manager` flag, you will be prompted to install (or not) the package to your system.
1. After finding the package on the system's PATH, pkgenv creates a symlink between the package's location on disk to your chosen custom package environment.

## Switching To A Package Environment

1. Execute `pkgenv switch --name {your package environment}`.
1. If the package environment is known by pkgenv (meaning that it is in custom_package_enviroments in the config.yaml file), your system's PATH will be switched to location on disk of the custom package environment _after you refresh your Bash session_.
1. You can switch back to your default package environment (using your system's default path) with `pkgenv switch --name default`.

## Removing Packages From A Package Environment

1. Execute `pkgenv remove --package {your package} --name {your custom package environment}`. 
1. The package is removed from your custom package environment, but stays installed on disk.

## Purging A Package Environment From Disk

1. Execute `pkgenv purge --name {your custom package environment}`. 
1. You will be prompted to decide if you really want to purge the chosen custom package environment (this action is not reversible!)
1. The chosen package environment is destroyed and all of the environment's packages stay installed on disk.

## Updating The default_environment_path Automatically

1. Execute `pkgenv path`. 
1. The default_environment_path in config.yaml is updated with the system's current PATH. It is recommended that you only run this command in your systems default package environment.

## Getting The Current Active Package Environment

There are two options...

Option 1:
1. Execute `pkgenv config`.
1. Check the value under active_package_environment.

Option 2:
1. Execute `pkgenv which`
1. The current active package environment is printed to the terminal.

## Using Multiple Package Managers

1. Execute `pkgenv config`.
1. Under system_package_managers, add the name of the package managers you want to add as a list item. Note that only the following package managers are currently supported:
- apt-get
- zypper
- apk
- pacman
- pip
- gem 
1. Save the config.yaml file.

# FAQs

## Is Package Env a package manager?
No. Package Env uses your system's package manager to install packages to your isolated package environment. You can use additional package managers (such as pip and gem) by adding them to Package Env's configuration file (~/.pkgenv/config.yaml). Please note that not all package managers are currently supported!

## Why would I use this over something like Docker?
Docker is a fine tool for containerizing applications, but Docker is not the end-all for creating user space development environments. Package Env allows you to isolate the packages you already have on your machine into a single environment. You can have multiple environments and switch between them using `pkgenv switch --name {your environment}`. For example, you could have a Package Env environment for creating Python 3.8 applications and then switch to a Package Env environment for developing Ruby 2.5.9 applications.

## Why would I use this over something like pyenv?
pyenv is a great tool for preventing conflicts across Python installations. Often, though, developers will find that their issues extend far passed that; as a tech stack becomes more and more complicated, the benefits of completely isolating all of your dependencies is invaluable.