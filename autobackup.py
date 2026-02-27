import os
import shutil
import argparse
import time
from datetime import datetime

def main() -> None:

    args = init_args()

    interval = 24 * 3600
    
    while True:
        backup_folder = create_backup_folder(args.destination)
        create_backup_files(args.source, backup_folder)
        print(f"Backup finished.")
        
        time.sleep(interval)


def create_backup_folder(folder_url : str) -> str :
    
    """ 
        Creates a backup folder.

        Returns:
            Target (backup) folder : String
    """
    timestamp = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
    target = os.path.join(folder_url, timestamp)

    if not (os.path.exists(folder_url)):
        os.makedirs(folder_url)


    return target


def create_backup_files(source: str, destination: str) -> None :
    
    """ 
        Creates a backup files with timestamp.

        Returns:
            Target (backup) folder : String
    """
        
    try: 
        shutil.copytree(source, destination)
        print(f"Backup created in {destination}")
    
    except Exception as error:
        print(f"Backup error: {error}")


def init_args() -> argparse.Namespace:

    """ 
        Initialize arguments.
        
        Returns:
            None
    """

    parser = argparse.ArgumentParser(
        description="Backs up a folder after a specified set time."
    )

    parser.add_argument(
    "-s", "--source", metavar="DIR", required=True,
    help="Copies a directory as a backup."
    )

    parser.add_argument(
        "-d", "--destination", metavar="DIR", required=False,
        default="backups", help="Copies a directory as a backup."
    )

    parser.add_argument(
        "-t", "--time", metavar="TIME", required=True,
        help="Set a time when a backup has to be created."
    )

    return parser.parse_args()



if (__name__ == "__main__"):
    main()