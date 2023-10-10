import os
import sys
from PIL import Image
import face_recognition


def main():
    check_args(sys.argv)
    reference = sys.argv[1]
    image_folder = os.listdir(sys.argv[2])
    check_input_validity(image_folder, reference)
    narcissist = make_new_folder()
    save_images(image_folder)
    print(check_matches(narcissist))


def check_input_validity(image_folder, reference):
    image_endings = [
        "apng",
        "avif",
        "gif",
        "jpg",
        "jpeg",
        "jfif",
        "pjpeg",
        "pjp",
        "png",
        "svg",
        "webp",
        "bmp",
        "ico",
        "cur",
        "tif",
        "tiff",
    ]

    # Check if reference input is an image
    try:
        ref_end = reference.split('.')[1]
    except IndexError:
        raise ValueError("Reference input is not an image")

    if ref_end not in image_endings:
        raise ValueError("Reference input is not an image")
    
    # Check if image folder is empty
    if len(image_folder) == 0:
        sys.exit("Image folder input is empty")

    # Check if every file in folder input is an image
    for image in image_folder:
        try:
            ending = image.split(".")[1]
        except IndexError:
            raise ValueError(f"One or more files in <{sys.argv[1]}> are not an image file")
        
        if ending not in image_endings:
            raise ValueError(f"One or more files in <{sys.argv[1]}> are not an image file")
    
    return 0


def check_args(input):
    if len(input) != 3:
        sys.exit("usage: <reference_file_path> <image_folder_file_path>")
    elif os.path.isdir(input[2]) != True:
        sys.exit("Error: Image folder does not exist")
    elif os.path.isfile(input[1]) != True:
        sys.exit("Error: Reference image does not exist")
    else:
        return 0
    

def make_new_folder():
    os.chdir(sys.argv[2])
    os.mkdir("Narcissist")
    os.chdir(f"{sys.argv[2]}/Narcissist")
    return f"{sys.argv[2]}/Narcissist"


def save_images(image_folder):
    user = face_recognition.load_image_file(sys.argv[1])
    user_face = face_recognition.face_encodings(user, model="cnn")[0]
    i = 0
    for image in image_folder:
        test = face_recognition.load_image_file(f"{sys.argv[2]}/{image}")
        test_faces = face_recognition.face_encodings(test, model="cnn")
        result = face_recognition.compare_faces(test_faces, user_face)

        if True in result:
            with Image.open(f"{sys.argv[2]}/{image}") as img:
                img.save(f"{i}.png")
                i += 1


def check_matches(folder):
    files = os.listdir(folder)
    if len(files) == 0:
        os.rmdir(folder)
        return "No matches found"
    else:
        return "Done!"


if __name__ == "__main__":
    main()
