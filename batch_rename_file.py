import os

def batch_rename_files(folder_path, new_name_pattern, start_number, file_extension):
    """
        batch_rename_files
        参数:
            folder_path: folder_path
            new_name_pattern: 10101.jpg -> new_name_pattern_x.jpg
            start_number: start index
            file_extension: Specify the file extension, otherwise None.
            simply: folder_path.file_extension -> {new_name_pattern}_{start_num}.{file_extension}
    """
    if not os.path.exists(folder_path):
        print(f"Path {folder_path} unexists")
        return

    if not os.path.isdir(folder_path):
        print(f"Path {folder_path} not dir")
        return

    try:
        files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path,f))]
    except OSError as e:
        print(f"Failed read dir {e}")
        return

    files.sort()
    count = start_number

    for filename in files:
        # get extension -> build new filename -> check old filename
        if file_extension is None:
            ext = os.path.splitext(filename)[1] # a.txt -> .txt
        else:
            ext = file_extension if file_extension.startswith(".") else "." + file_extension

        new_filename = f"{filename}_{start_number}{ext}"

        old_path = os.path.join(folder_path, filename)
        new_path = os.path.join(folder_path, new_filename)

        if os.path.exists(new_path):
            print(f"{new_path} is exit, will skip")
            count += 1
            continue

        try:
            os.rename(old_path, new_path)
            print(f"rename file: {old_path} -> {new_path}")
            count += 1
        except FileExistsError:
            print(f"New file {filename} is exit")
        except PermissionError:
            print(f"No Permission to {filename}")
        except OSError:
            print(f"rename failed {filename}, count = {count}")

if __name__ == "__main__":
    # set param
    folder = input("Please enter the folder path:").strip()
    pattern = input("Please enter the new file name format:").strip()

    try:
        start_num = int(input("start index(default:1):") or "1")
    except ValueError:
        print("Please provide valid figures!")
        exit(1)

    ext_input = input("Please enter the file extension(keep as is if none):")
    file_ext = ext_input if ext_input else None

    # confirm
    print(f"\nPreparing to rename the files in {folder}")
    print(f"Pattern: {pattern}_index")
    print(f"Start: {start_num}")
    if file_ext:
        print(f"Extension: {file_ext}")

    confirm = input("\nConfirm execution?(y/n):")

    if confirm == 'y':
        batch_rename_files(folder, pattern, start_num, file_ext)
        print("Finished!")
    else:
        print("Operation has been cancelled.")