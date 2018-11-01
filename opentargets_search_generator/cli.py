import sys
import argparse
from opentargets_search_generator.version import __pkgname__ as prog_name


def main():
    parser = argparse.ArgumentParser(prog = prog_name)


if __name__ == '__main__':
    sys.exit(main())
