from cx_Freeze import setup, Executable

setup(
    name = "Wordifyery",
    version = "1.0",
    description = "Simple terminal game for two players in guessing the word",
    executables = [Executable( "main.py" )]
)