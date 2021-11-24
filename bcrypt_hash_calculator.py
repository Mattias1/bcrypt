import argparse
import bcrypt
import getpass


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--version', action='version',
        version='A quick n\' dirty bcrypt hash calculator, version 1.0')
    parser.add_argument('password', type=str, nargs='?', help='The password to hash')
    parser.add_argument('--cost', type=int, nargs='?', default=10, help='The cost factor')
    args = parser.parse_args()

    if args.password is None:
        args.password = getpass.getpass('Enter a password: ')

    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(args.password.encode('utf-8'), salt)
    print("The bcrypt hash for '{}' is: {}".format(args.password, hashed))


main()
