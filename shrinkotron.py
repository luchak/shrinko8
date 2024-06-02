#!/usr/bin/env python3
from shrinko8 import create_main
from pico_defs import Language
import sys

main = create_main(Language.picotron)

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
