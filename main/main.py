from os import system, name
from sys import argv, exit
from random import randint


def has_uppercase( word ) -> bool:
    """
    Checks if the word has uppercase;
    Returns true if it has uppercase
    """
    return any( char.isupper() for char in word )

def clear() -> None:
    """
    Clears the shell
    """
    if name == "nt":
        system( "cls" )
    else:
        system( "clear" )

def arg_analysis() -> None:
    """
    Gets the number of arguments and their values;
    Sets values to global variables
    """
    global linesCnt, tipsCnt

    # Handle --help case
    if argc == 2 and argv[1] == "--help":
        print( "Usage:\n"
               "  --help      - list of valid arguments\n"
               "  -L {number} - set number of lines (attempts) (default=5)\n"
               "  -T {number} - set number of tips (default=0)" )
        exit()

    # Valid argument combinations: -L num, -T num, -L num -T num, -T num -L num
    if argc not in [3, 5]:
        print( "\x1b[31mERROR:\x1b[0m Invalid number of arguments. Use --help for more info." )
        exit()

    # Process arguments
    i = 1
    while i < argc:
        if argv[i] == "-L":
            if i + 1 >= argc:
                print( "\x1b[31mERROR:\x1b[0m Missing value for -L argument." )
                exit()

            try:
                value = int( argv[i + 1] )
                if 2 <= value <= 12:
                    linesCnt = value
                else:
                    print( "\x1b[31mERROR:\x1b[0m Number of lines must be between 2 and 12." )
                    exit()
            except ValueError:
                print( "\x1b[31mERROR:\x1b[0m -L argument requires an integer value." )
                exit()

            i += 2

        elif argv[i] == "-T":
            if i + 1 >= argc:
                print( "\x1b[31mERROR:\x1b[0m Missing value for -T argument." )
                exit()

            try:
                value = int( argv[i + 1] )
                if 0 <= value <= 10:
                    tipsCnt = value
                else:
                    print( "\x1b[31mERROR:\x1b[0m Number of tips must be between 0 and 10." )
                    exit()
            except ValueError:
                print( "\x1b[31mERROR:\x1b[0m -T argument requires an integer value." )
                exit()

            i += 2

        else:
            print( f"\x1b[31mERROR:\x1b[0m Unknown argument: { argv[i] }. Use --help for more info." )
            exit()


def main() -> int:
    """
    Main function;
    Returns exit code
    """
    global tipsCnt
    if argc != 1:
        arg_analysis()
    clear()
    while True:
        set_word = input( "\x1b[34mSetter#\x1b[0m Set the word: " )
        if set_word == "!q" or set_word == "!exit":
            clear()
            return 1
        if not set_word.isalpha():
            print( "\x1b[31mERROR:\x1b[0m Word couldn't contain special characters." )
            return 1
        else:
            if len( set_word ) > 12 or len( set_word ) < 2:
                print( "\x1b[31mERROR:\x1b[0m Word can't be longer than 12 characters and lower than 2." )
                return 1
            elif has_uppercase( set_word ):
                print( "\x1b[31mERROR:\x1b[0m All characters should be lowercase." )
                return 1
            else:
                frame = [ f"{ "? "*len( set_word ) }",
                                f"{ "_ "*len( set_word ) }" ]
                for line in range( linesCnt ):
                    frame.append( f"{ "* "*len( set_word ) }" )

                cnt = -1
                while cnt < linesCnt-1:
                    clear()
                    for s in frame:
                        print( s )

                    word = input( '\n\x1b[34mGuesser#\x1b[0m Enter a word: ' )
                    used_tips = 0

                    if word == "!q" or word == "!exit":
                        clear()
                        exit()
                    elif word == "!giveup":
                        break


                    elif word == "!tip":
                        if tipsCnt > 0:
                            hidden = [i for i in range( 0, len( set_word )) if frame[0][i * 2] == "?"]
                            if len( hidden ) > 0:
                                if ( len( set_word ) - used_tips ) >= 2:
                                    tipsCnt -= 1
                                    used_tips += 1
                                    rnd_i = hidden[randint( 0, len( hidden ) - 1 )]
                                    frame0 = list( frame[0] )
                                    frame0[rnd_i * 2] = set_word[rnd_i]
                                    frame[0] = "".join( frame0 )

                    elif len( word ) != len( set_word ) or has_uppercase( word ) or not word.isalpha():
                        pass

                    else:
                        cnt += 1
                        obj = ""
                        iteration = 0
                        for c in word:
                            if c == set_word[iteration]:
                                obj += f"\x1b[32m{ c }\x1b[0m "
                            elif c in set_word:
                                obj += f"\x1b[33m{ c }\x1b[0m "
                            else:
                                obj += f"\x1b[31m{ c }\x1b[0m "
                            iteration += 1

                        if word == set_word:
                            clear()
                            frame0 = ""
                            for c in set_word:
                                frame0 += f"{ c } "
                            frame[0] = frame0
                            frame[2 + cnt] = obj
                            for s in frame:
                                print( s )
                            print( f"\nGuesser win! The word was: { set_word }" )
                            break

                        frame[2+cnt] = obj

                if word != set_word:
                    clear()
                    frame0 = ""
                    for c in set_word:
                        frame0 += f"{ c } "
                    frame[0] = frame0
                    for s in frame:
                        print( s )
                    print( f"\nSetter win! The word was: { set_word }" )


if __name__ == "__main__":
    argc = len( argv )  # Count of arguments

    # Global vars
    linesCnt = 5
    tipsCnt = 0

    main()
