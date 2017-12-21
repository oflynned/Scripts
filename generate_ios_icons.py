import os

deletion_exceptions = ["svg", "py"]
generation_exceptions = ["py"]
px_dimensions = [40, 80, 120]


def main():
    clean_dir(deletion_exceptions)
    generate_ios_images(generation_exceptions)


def generate_ios_images(exceptions):
    svg_files = get_file_names()
    print("Generating new icons for", str(len(svg_files)), "files...")

    for file in svg_files:
        filename = file[0]
        extension = file[1]
        if extension not in exceptions:
            # os.system("mkdir " + filename)
            for px in px_dimensions:
                generate_image(filename, extension, px)

    print("Generation complete!")


def generate_image(filename, extension, px):
    os.system("inkscape -z -e " + get_output_name(filename, px) + \
        " -w " + str(px) + " -h " + str(px) + " " + filename + "." + extension)


def get_output_name(filename, dimension):
    return filename + "_x" + str(px_dimensions.index(dimension) + 1) + ".png"


def clean_dir(exceptions):
    print("Cleaning folder...")
    files = get_file_names()
    start_file_count = len(files)

    for item in files:
        is_folder = item[1] == ""
        if is_folder:
            print(is_folder)
            os.system("rm -rf " + item[0])
        else:
            extension = item[1]
            if extension not in exceptions:
                deletion_item = item[0] + "." + item[1]
                os.system("rm -rf " + deletion_item)

    end_file_count = len(get_file_names())

    print(str(start_file_count - end_file_count), "files deleted!")


def get_file_names():
    output = []
    files = os.listdir(".")
    for file in files:
        print(file)
        is_folder = len(file.split(".")) == 1

        filename = file.split(".")[0]
        extension = "" if is_folder else file.split(".")[1]
        if extension is not generation_exceptions:
            output.append((filename, extension))

    return output


if __name__ == "__main__":
    main()
