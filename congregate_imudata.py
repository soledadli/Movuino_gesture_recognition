import pandas as pd
import os.path
#from config import *

GESTURES = ["random0","random5","test0","test1"] #different names
MAIN_GESTURE= ["random","test"] # e.g walk
clean_dir = '/Users/soledqdli/Desktop/Internship/movuino_data/clean_data/test_data'
merge_dir = '/Users/soledqdli/Desktop/Internship/movuino_data/congregate_data/complete'
gesture = "r"
file_holder = []

# Merge the separate recordings into a complete file
def merge_data(gesture_name):
  dfs = pd.DataFrame()
  for path, currentDirectory, files in os.walk(clean_dir):
  # Find all the files same with the gesture name in the directory
    for file in files:
      if file.startswith(gesture_name):
        file_holder.append(file)
    # Concat the separate files (recordings) into a merged one
    for i in range(len(file_holder)):
      dir = os.path.join(path, str(file_holder[i]))
      df = pd.read_csv(dir, index_col=[0])
      dfs = dfs.append(df).reset_index(drop=True)
    # Save the separate files from one recording into one file
    mergeName = os.path.join(merge_dir, gesture_name + ".csv")
    dfs.to_csv(mergeName)

    # return the path of the merged data file
    return mergeName


if __name__ == "__main__":
 lst = merge_data("random")
 df = pd.read_csv(lst)
 print(len(df))

