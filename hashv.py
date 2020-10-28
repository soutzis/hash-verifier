import sys
import os
import colorama
import hashlib

# Coloured stdout
USAGE_COLORED = colorama.Fore.BLUE + "USAGE" + colorama.Style.RESET_ALL
HELP_COLORED = colorama.Fore.BLUE + "HELP" + colorama.Style.RESET_ALL
VERSION_COLORED = colorama.Fore.BLUE + "VERSION" + colorama.Style.RESET_ALL
FILE_NOT_FOUND = colorama.Fore.RED + "FILE NOT FOUND!" + colorama.Style.RESET_ALL
HELP_EX = colorama.Fore.YELLOW + "hashv help" + colorama.Style.RESET_ALL
INV_CMD = colorama.Fore.RED + "INVALID COMMAND\n" + colorama.Style.RESET_ALL + f"To see program usage, type: {HELP_EX}"
INV_HASH = colorama.Fore.RED + "INVALID HASH" + colorama.Style.RESET_ALL

# Algorithms
SHA512 = "SHA-512"
SHA256 = "SHA-256"
MD5 = "MD5"

# Algo lengths (in digits, not bits)
SHA512_LEN = 128
SHA256_LEN = 64
MD5_LEN = 32

VERSION = "0.0.1"
AUTHOR = "psoutzis, 27/10/2020"
HELP = f"{USAGE_COLORED}:\t1. hashv <file> <hash> -> Will compute " \
       f"and compare the hash digest of the provided file against the provided hash digest. " \
       f"The provided hash digest type is automatically detected " \
       f"(supported: MD5, SHA-256 and SHA-512).\n\t2. hashv <file> -> Will compute the md5, sha256 and sha512 hash" \
       f"digests for the provided file.\n" \
       f"{HELP_COLORED}:\thashv <h | help>\n" \
       f"{VERSION_COLORED}:hashv <v | version>"


def print_result(hash_type, match: bool):
    hash_ok = colorama.Fore.GREEN + f"{hash_type} OK" + colorama.Style.RESET_ALL
    hash_mismatch = colorama.Fore.RED + f"{hash_type} NO MATCH"
    if match:
        print(hash_ok)
    else:
        print(hash_mismatch)


def print_inv_cmd():
    print(INV_CMD)


def print_inv_hash(hash_chars):
    print(INV_HASH)
    print(f"It seems that the hash digest you provided has {hash_chars} digits.")
    print(f"[MD5: {MD5_LEN} digits, SHA-256: {SHA256_LEN} digits, SHA-512: {SHA512_LEN} digits].")


def print_help():
    print(HELP)


def print_fnfe():
    file_not_found_err_msg = f"{FILE_NOT_FOUND}\n{HELP}"
    print(file_not_found_err_msg)


def get_hash_algo(algo):
    if algo == MD5:
        hash_algo = hashlib.md5()
    elif algo == SHA256:
        hash_algo = hashlib.sha256()
    else:
        hash_algo = hashlib.sha512()

    return hash_algo


def get_hash_type(hash_dig):
    hash_type = None
    hash_chars_count = char_count(hash_dig)

    if hash_chars_count == MD5_LEN:
        hash_type = MD5
    elif hash_chars_count == SHA256_LEN:
        hash_type = SHA256
    elif hash_chars_count == SHA512_LEN:
        hash_type = SHA512
    else:
        print_inv_hash(hash_chars_count)

    return hash_type


def compute_hash_digest(fname, hash_algo: hashlib):
    with open(fname, "rb") as f:
        # # Reads chunks of file
        for chunk in iter(lambda: f.read(8192), b""):
            hash_algo.update(chunk)
        # # Reads whole file into memory
        # hash_algo.update(f.read())
    return hash_algo.hexdigest()


def path_check(path):
    return os.path.exists(path)


def run(argv):
    version_flags = ["v", "version", "-v", "-Version", "--v", "--version"]
    help_flags = ["h", "help", "-h", "-help", "--h", "--help"]

    # if only parameter is provided, then check flags and if parameter is a file, then check if it exists
    if len(argv) == 2:
        if argv[1].casefold() in version_flags:
            print(colorama.Fore.GREEN + f"version {VERSION} by {AUTHOR}")
        elif argv[1].casefold() in help_flags:
            print_help()
        # if file exists, calculate hash digests
        elif path_check(argv[1]):
            res = colorama.Fore.YELLOW + \
                  f"MD5: {compute_hash_digest(argv[1], get_hash_algo(MD5))}\n" \
                  f"SHA-256: {compute_hash_digest(argv[1], get_hash_algo(SHA256))}\n" \
                  f"SHA-512: {compute_hash_digest(argv[1], get_hash_algo(SHA512))}" + \
                  colorama.Style.RESET_ALL
            print(res)
        # if file doesn't exist print error
        elif not path_check(argv[1]):
            print_fnfe()
        # in other cases, command is invalid
        else:
            print_inv_cmd()

    # check if file and hash are provided, if yes then return true.
    elif len(argv) == 3:
        if path_check(argv[1]):
            # file exists, so compute digest and print result
            correct_digest = argv[2]
            hash_type = get_hash_type(correct_digest)
            if hash_type is not None:
                algo = get_hash_algo(hash_type)
                computed_digest = compute_hash_digest(argv[1], algo)
                res = (correct_digest == computed_digest)
                print_result(hash_type, match=res)
        elif not path_check(argv[1]):
            print_fnfe()
        else:
            print_inv_cmd()
    else:
        print_inv_cmd()
        print("It looks like you entered zero, or more parameters than necessary.")


def char_count(string):
    count = 0
    for _ in string:
        count += 1

    return count


if __name__ == '__main__':
    colorama.init()
    run(sys.argv)
    colorama.deinit()
