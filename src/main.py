from pkgenv import create_package_environment, open_config_yaml_file, switch_to_package_environment, add_package, purge_package_environment, get_active_package_environment, update_default_environment_path_to_current_PATH, remove_package_from_package_environment, show_envs, register_env
from argparse import ArgumentParser

if __name__ == "__main__":
    parser = ArgumentParser(description='pkgenv <command> <flags>')
    parser.add_argument('command', help='`create`: Initilizes a new package environment.\n' +
                                        '`config`: Opens the pkgenv yaml config file in Vim or Nano.\n' +
                                        '`add`: Install or add an existing package. Defaults to the active package environment.\n' +
                                        '`remove`: Removes a package from a custom package environment.\n' +
                                        '`purge`: Destroy a package environment (moves all packages back to the default environment).\n' +
                                        '`switch`: Change the active package environment.\n' +
                                        '`which`: Get the name of the active package environment.\n' +
                                        '`path`: Update the default_environment_path to equal the system\'s $PATH.\n' +
                                        '`envs`: List all package environments in ~/.pkgenv/envs.\n' + 
                                        '`register`: Registers an existing directory as a known package environment by copying the contents of the directory to a new directory in ~/.pkgenv/envs.')
    parser.add_argument('--manager', help='The package manager you want to use to install packages to ' + 
                                        'the package environment. Defaults to the system\'s package ' + 
                                        'manager. Use with the add commands.' )
    parser.add_argument('-m', help='Shorthand for --manager.')
    parser.add_argument('--name', help='The name of the package environment. Use with the add/remove/purge/switch commands.')
    parser.add_argument('-n', help='Shorthand for --name')
    parser.add_argument('--package', help='The package name or path to a package on disk. Use with the add/remove commands')
    parser.add_argument('-p', help='Shorthand for --package.')
    parser.add_argument('--path', help='The path to a file or directory on disk. Use with the register command.')
    parser.add_argument('-ph', help='Shorthand for --path.')


    args = parser.parse_args()
    success = False

    if args.command == 'add':
        package = args.package if args.package else args.p
        manager = args.manager if args.manager else args.m
        name = args.name if args.name else args.n 
        success = add_package(package, name, manager)
    elif args.command == 'remove':
        package = args.package if args.package else args.p
        name = args.name if args.name else args.n 
        success = remove_package_from_package_environment(package, name)
    elif args.command == 'purge':
        name = args.name if args.name else args.n 
        success = purge_package_environment(name)
    elif args.command == 'switch':
        name = args.name if args.name else args.n 
        success = switch_to_package_environment(name)
    elif args.command == 'create':
        name = args.name if args.name else args.n 
        success = create_package_environment(name)
    elif args.command == 'config':
        success = open_config_yaml_file()
    elif args.command == 'which':
        active_package_environment = get_active_package_environment()
        print(active_package_environment)
        success = True if active_package_environment else False 
    elif args.command == 'path':
        updated_path = update_default_environment_path_to_current_PATH()
        success = True if updated_path else False
    elif args.command == 'envs':
        success = show_envs()
    elif args.command == 'register':
        pth = args.path if args.path else args.ph 
        success = register_env(pth)
    else:
        print('ERROR: \'{}\' is not a valid command'.format(args.command))
        success = False

    if not success: 
        exit(1)

exit(0)
