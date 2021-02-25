import cx_Freeze

cx_Freeze.setup(
    name = "Talbot",
    version = "0.1",
    description = "Model of Talbot Carpet",
    executables = [cx_Freeze.Executable("main.py")]
)
