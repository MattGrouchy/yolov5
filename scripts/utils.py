def choose_option(files):
    ''' print options and choose one. returns index or None '''
    print("Path options:")
    for index, filepath in enumerate(files):
        print(f"  {index}: {filepath}")

    print()
    unpack_index = int(input("Enter the index of the option:"))

    exists = _check_index(unpack_index, files)
    return unpack_index if exists else None


def _check_index(index, file_list):
    exists = False
    if index < len(file_list):
        print(f"  index: {index}", 'exists in the list')
        exists = True
    else:
        print(f"  index: {index}", "doesn't exist in the list \n", "  Exiting...")
    return exists
