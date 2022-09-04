import pkgenv
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='pkgenv <command> <flags>')
    parser.add_argument('command', help='`create`: Initilizes a new package environment.\n' +
                                        '`config`: Opens the pkgenv yaml config file in Vim or Nano.\n' +
                                        '`add`: Install or add an existing package. Defaults to the active package environment.\n' +
                                        '`remove`: Uninstalls or removes a package. Defaults to the active package environment.\n' +
                                        '`purge`: Destroy a package environment (moves all packages back to the default environment).\n' +
                                        '`switch`: Change the active package environment.\n' +
                                        '`which`: Get the name of the active package environment.')
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

    if args.command == 'add':
        package = args.package if args.package else args.p
        manager = args.manager if args.manager else args.m
        name = args.name if args.name else args.n 

        print(package)
        print(manager)
        print(name)
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

        print(name)
    elif args.command == 'switch':
        name = args.name if args.name else args.n 
        
        print(name)
    elif args.command == 'create':
        name = args.name if args.name else args.n 

        print(name)
    elif args.command == 'config':
        print('config')
    elif args.command == 'which':
        print('which')
    else:
        print('ERROR: \'{}\' is not a valid command'.format(args.command))
        exit(1)

exit(0)