import getpass
import FFT
import converter


if __name__ == "__main__":
    inputFile = input("Enter the name of file: ")
    extension = inputFile.split(".")[-1]

    if extension == "jpg" or extension == "jpeg" or extension == "enj": rgba = True
    elif extension == "png" or extension == "enp": rgba = False
    else: raise Exception("Invalid File Name")

    if extension in ["jpg", "jpeg", "png"]: encrypt = True
    else: encrypt = False

    password = getpass.getpass("Password: ")
    key = converter.getKeyFromPassword(password)

    if extension == "jpg" or extension == "jpeg": outputFile = inputFile.replace("jpg", "enj")
    elif extension == "png": outputFile = inputFile.replace("png", "enp")
    elif extension == "enj": outputFile = inputFile.replace("enj", "jpg")
    elif extension == "enp": outputFile = inputFile.replace("enp", "png")

    if encrypt:
        width, height, array = converter.getComplexArrayFromImage(inputFile, extension)
        FFT.FFT(array, False)
        array = [converter.encryptComplex(x, key) for x in array]
        converter.dumpComplexArray(array, width, height, outputFile)
    else:
        array, width, height = converter.getComplexArrayFromDumpFile(inputFile)
        array = [converter.decryptComplex(x, key) for x in array]
        FFT.FFT(array, True)
        converter.outputImageFromComplexArray(array, width, height, outputFile, "png" if extension == "enp" else "jpg")