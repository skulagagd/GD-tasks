
def get_extension(filename: str) -> str:
    if "." not in filename:
        raise Exception("The file has no extension")
    ext = filename.split(".")[-1]
    print(ext)

get_extension("testpliktxt")