import os
from collections import defaultdict

def find_duplicate_png_files(folder):
    png_files = defaultdict(list)
    duplicate_sets = []
    short_filenames = []

    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.lower().endswith('.png'):
                file_path = os.path.join(root, file)
                png_files[file].append(file_path)
                
                # Check for filenames with fewer than 37 characters
                if len(file) < 37:
                    short_filenames.append(file_path)
    
    # Find duplicates
    for file_name, paths in png_files.items():
        if len(paths) > 1:
            duplicate_sets.append(paths)
    
    return duplicate_sets, short_filenames

folder_to_check = '.'
duplicate_sets, short_filenames = find_duplicate_png_files(folder_to_check)

print()
print("Checking recursively to ensure all filenames are unique...")
print()

if duplicate_sets:
    print()
    print("******  WARNING: Duplicate texture names found  *******")
    print("*                                                      *")
    print("*  Must fix it. No two files can have the same name.   *")
    print("*                                                      *")
    for idx, duplicate_set in enumerate(duplicate_sets, start=1):
        count = len(duplicate_set)
        print(f"\nDuplicate Set {idx} ({count} item{'s' if count > 1 else ''}):")
        for duplicate in duplicate_set:
            print(duplicate)
    print()
    print("******  WARNING: Duplicate texture names found  *******")
    print("*                                                      *")
    print("*  Must fix it. No two files can have the same name.   *")
    print("*                                                      *")
    print("***  PLEASE REMOVE ALL DUPLICATES BEFORE SUBMITTING  ***")
    print()
else:
    print()
    print("Success. No duplicate PNG files found.")
    print()

# Output for PNG filenames with fewer than 37 characters
if short_filenames:
    print()
    print("Possible non-texture PNG files: ")
    for file_path in short_filenames:
        print(file_path)

print()
print("Press Enter or close this window to exit.")
input()
