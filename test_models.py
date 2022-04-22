""" Module for iteratively testing models to help save time """

import os 
import scripts.utils
import scripts.get_files

def get_sub_folders(path_dir):
  subfolders = [ f.path for f in os.scandir(path_dir) if f.is_dir() ]
  return subfolders


def main(path_dir):
  """ Method to select a directory and run a test on each model within it """
  

  sub_folders = get_sub_folders(path_dir)

  directory_index = scripts.utils.choose_option(sub_folders)

  if directory_index is False:
    return

  # get files and parse for .pt
  model_dir = sub_folders[directory_index]
  files = scripts.get_files.main(model_dir)
  model_paths = []
  for file_path in files:
      if file_path.endswith(".pt") and not file_path.endswith("last.pt"):
          model_paths.append(file_path)

  get_dataset(sub_folders, model_paths)

  


def get_dataset(sub_folders, model_paths):
  print("Choose the dataset directory:")
  sub_folders = get_sub_folders(path_dir)
  directory_index = scripts.utils.choose_option(sub_folders)

  if directory_index is not False:
    dataset_dir = sub_folders[directory_index]

    check_and_test(dataset_dir, model_paths)
    pass

def check_and_test(dataset_dir, model_paths):
  ''' function to confirm the users wants to run testing before executing '''
  ensure = input(f"Test models on the dataset [y/n]?")
  if ensure != "y":
    return
  
  # run testing
  for model in model_paths:
    test_model(dataset_dir, model)


def test_model(dataset_dir, model_path):
  ''' function to run the yolo validation testing with cli '''
  # !python val.py --weights $path_to_best_renamed --data $data_yaml_path --img $imgsz --half --task test
  data = os.path.join(dataset_dir, "data.yaml")
  os.system(f"python val.py --weights {model_path} --data {data}  --img 640 --half --task test")



if __name__ == "__main__":
  path_dir = os.getcwd()
  print(path_dir)
  main(path_dir)  # run in current directory
