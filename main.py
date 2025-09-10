from os import system, name
from sys import argv, exit
from random import randint


# Global vars
ERR = 0
linesCnt = 5
tipsCnt = 0

def clear():
    """
    Clears the shell
    """
    if name == "nt":
        system( "cls" )
    else:
        system( "clear" )

def has_uppercase( word ):
    """
    Checks if the word has uppercase;
    Returns true if it has uppercase
    """
    return any( char.isupper() for char in word )

def arg_analysis( argc, argv ):
    """
    Gets the number of arguments and their values;
    Sets values to global variables;
    Returns 1 on error
    """
    global linesCnt, tipsCnt, ERR
    if argc == 2 or argc == 4:
        if argv[1] != "--help":
            print( "\x1b[31mERROR:\x1b[0m Something wrong with arguments. Use --help for more info." )
            exit()
        else:
            print( "Usage:\n"
                   "  --help      - list of valid arguments\n"
                   "  -L {number} - set number of lines (attempts) (default=5)\n"
                   "  -T {number} - set number of tips (default=0)" )
            exit()

    elif argc == 3 or argc == 5:
        if argv[1] == "-L":
            try: argv[2] = int( argv[2] )
            finally: pass
            if isinstance( argv[2], int ):
                if 2 <= int( argv[2] ) <= 12:
                    linesCnt = int( argv[2] )
                else:
                    print( "\x1b[31mERROR:\x1b[0m Number of lines can't be higher than 12 and lower than 2." )
                    exit()
            else:
                print( "\x1b[31mERROR:\x1b[0m Something wrong with arguments. Use --help for more info." )
                exit()
        elif argv[1] == "-T":
            try: argv[2] = int( argv[2] )
            finally: pass
            if isinstance( argv[2], int ):
                if 0 <= int( argv[2] ) <= 10:
                    tipsCnt = int( argv[2] )
                else:
                    print( "\x1b[31mERROR:\x1b[0m Number of tips can't be higher than 10 and lower than 0." )
                    exit()
            else:
                print( "\x1b[31mERROR:\x1b[0m Something wrong with arguments. Use --help for more info." )
                exit()
        if argv[3] == "-L":
            try: argv[4] = int( argv[4] )
            finally: pass
            if isinstance( argv[4], int ):
                if 2 <= int( argv[4] ) <= 12:
                    linesCnt = int( argv[4] )
                else:
                    print( "\x1b[31mERROR:\x1b[0m Number of lines can't be higher than 12 and lower than 2." )
                    exit()
            else:
                print( "\x1b[31mERROR:\x1b[0m Something wrong with arguments. Use --help for more info." )
                exit()
        elif argv[3] == "-T":
            try: argv[4] = int( argv[4] )
            finally: pass
            if isinstance( argv[4], int ):
                if 0 <= int( argv[4] ) <= 10:
                    tipsCnt = int( argv[4] )
                else:
                    print( "\x1b[31mERROR:\x1b[0m Number of tips can't be higher than 10 and lower than 0." )
                    exit()
            else:
                print( "\x1b[31mERROR:\x1b[0m Something wrong with arguments. Use --help for more info." )
                exit()

    else:
        print("\x1b[31mERROR:\x1b[0m Something wrong with arguments. Use --help for more info.")
        exit()


def main( argc, argv ):
    """
    Main function
    """
    global tipsCnt
    arg_analysis( argc, argv )
    clear()
    while True:
        settedWord = input( "\x1b[34mSetter#\x1b[0m Set the word: " )
        if settedWord == "!q" or settedWord == "!exit":
            clear()
            exit()
        if not settedWord.isalpha():
            print( "\x1b[31mERROR:\x1b[0m Word couldn't contain special characters." )
            return 1
        else:
            if 13 < len( settedWord ) < 2:
                print( "\x1b[31mERROR:\x1b[0m Word can't be longer than 12 characters and lower than 2." )
                return 1
            elif has_uppercase( settedWord ):
                print( "\x1b[31mERROR:\x1b[0m All characters should be lowercase." )
                return 1
            else:
                frame = [ f"{ "? "*len( settedWord ) }",
                          f"{ "_ "*len( settedWord ) }" ]
                for line in range( linesCnt ):
                    frame.append( f"{ "* "*len( settedWord ) }" )

                cnt = -1
                while cnt < linesCnt-1:
                    clear()
                    for s in frame:
                        print( s )

                    word = input( '\n\x1b[34mGuesser#\x1b[0m Enter a word: ' )
                    usedTips = 0

                    if word == "!q" or word == "!exit":
                        clear()
                        exit()
                    elif word == "!giveup":
                        break


                    elif word == "!tip":
                        if tipsCnt > 0:
                            hidden = [i for i in range( 0, len( settedWord )) if frame[0][i * 2] == "?"]
                            if len( hidden ) > 0:
                                if ( len( settedWord ) - usedTips ) >= 2:
                                    tipsCnt -= 1
                                    usedTips += 1
                                    rnd_i = hidden[randint( 0, len( hidden ) - 1 )]
                                    frame0 = list( frame[0] )
                                    frame0[rnd_i * 2] = settedWord[rnd_i]
                                    frame[0] = "".join( frame0 )

                    elif len( word ) != len( settedWord ) or has_uppercase( word ) or not word.isalpha():
                        pass

                    else:
                        cnt += 1
                        obj = ""
                        iteration = 0
                        for c in word:
                            if c == settedWord[iteration]:
                                obj += f"\x1b[32m{ c }\x1b[0m "
                            elif c in settedWord:
                                obj += f"\x1b[33m{ c }\x1b[0m "
                            else:
                                obj += f"\x1b[31m{ c }\x1b[0m "
                            iteration += 1

                        if word == settedWord:
                            clear()
                            frame0 = ""
                            for c in settedWord:
                                frame0 += f"{ c } "
                            frame[0] = frame0
                            frame[2 + cnt] = obj
                            for s in frame:
                                print( s )
                            print( f"\nGuesser win! The word was: { settedWord }" )
                            break

                        frame[2+cnt] = obj

                if word != settedWord:
                    clear()
                    frame0 = ""
                    for c in settedWord:
                        frame0 += f"{ c } "
                    frame[0] = frame0
                    for s in frame:
                        print( s )
                    print( f"\nSetter win! The word was: { settedWord }" )


if __name__ == "__main__":
   main( len( argv ), argv )