from pkgenv import create_package_environment, open_config_yaml_file, switch_to_package_environment, add_package, purge_package_environment, get_active_package_environment, update_default_environment_path_to_current_PATH
from argparse import ArgumentParser

if __name__ == "__main__":
    parser = ArgumentParser(description='pkgenv <command> <flags>')
    parser.add_argument('command', help='`create`: Initilizes a new package environment.\n' +
                                        '`config`: Opens the pkgenv yaml config file in Vim or Nano.\n' +
                                        '`add`: Install or add an existing package. Defaults to the active package environment.\n' +
                                        '`remove`: Uninstalls or removes a package. Defaults to the active package environment.\n' +
                                        '`purge`: Destroy a package environment (moves all packages back to the default environment).\n' +
                                        '`switch`: Change the active package environment.\n' +
                                        '`which`: Get the name of the active package environment.\n' +
                                        '`path`: Update the default_environment_path to equal the system\'s $PATH.')
    parser.add_argument('--manager', help='The package manager you want to use to install packages to ' + 
                                        'the package environment. Defaults to the system\'s package ' + 
                                        'manager. Use with the add/remove commands.' )
    parser.add_argument('-m', help='Shorthand for --manager.')
    parser.add_argument('--save', help='Preserves the package by removing it from the package environment' +
                                        'and not uninstalling it from the system. Use with the remove command.',
                                        action='store_true')
    parser.add_argument('-s', help='Shorthand for --save.', action='store_true')
    parser.add_argument('--name', help='The name of the package environment. Use with the add/remove/purge/switch commands.')
    parser.add_argument('-n', help='Shorthand for --name')
    parser.add_argument('--package', help='The package name or path to a package on disk. Use with the add/remove commands')
    parser.add_argument('-p', help='Shorthand for --package.')

    args = parser.parse_args()
    success = False

    if args.command == 'add':
        package = args.package if args.package else args.p
        manager = args.manager if args.manager else args.m
        name = args.name if args.name else args.n 

        success = add_package(package, name, manager)
    elif args.command == 'remove':
        package = args.package if args.package else args.p
        manager = args.manager if args.manager else args.m
        name = args.name if args.name else args.n 
        save = args.save if args.save else args.s

        print(package)
        print(manager)
        print(name)
        print(save)
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
    else:
        print('ERROR: \'{}\' is not a valid command'.format(args.command))
        success = False

    if not success: 
        exit(1)

exit(0)