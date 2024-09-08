import argparse
import os


def main(folder: str, character: str):
    src = os.path.expanduser(folder)

    for file in os.listdir(src):
        if file.endswith(".png") or file.endswith(".jpg") or file.endswith(".jpeg"):
            dest = f"{src}/{file.replace('.png', '').replace('.jpg', '').replace('.jpeg', '')}.gt.txt"

            with open(dest, "w") as f:
                f.write(character)

            print(f"Transcription file created for {file}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Create a transcription file <image_file_name.gt.txt> with the ground-truth content of the image"
    )
    parser.add_argument(
        "--folder",
        "-f",
        type=str,
        action="store",
        help="Folder with images to transcribe",
        required=True,
    )
    parser.add_argument(
        "--character",
        "-c",
        type=str,
        action="store",
        help="Text content of the images in eac file",
        required=True,
    )
    args = parser.parse_args()

    main(args.folder, args.character)
