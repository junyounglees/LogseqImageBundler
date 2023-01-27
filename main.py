import os
import shutil
import pandas as pd

# make a dataFrame with the lines with jpg files only.
# return dataFrame with the name of the files.


def makeDataFrame(searchFile):
    with open(searchFile, 'r') as f:
        df = pd.DataFrame(f)
        isContainJPG = df[0].str.contains('jpg')
        df = df[isContainJPG]
        df = df[0].str.split('\[').str[1]
        df = df.str.split('.jpg').str[0]
        df.reset_index(drop=True, inplace=True)
        df = df.str.replace(' ', '_')
        print(df)
        return df

# search jpg files with the names in searchDirectory/searchFile  and copy the files to /copyDir/. Make sure your copyDir exists.


def searchAndCopy(searchFile, searchDir, copyDir):
    import os
    import shutil
    df = makeDataFrame(searchFile)
    print(df.shape)
    j = 0
    for i in range(len(df)):
        for root, dirs, files in os.walk(searchDir):
            for file in files:
                if file.startswith(df[i]):
                    j += 1
                    print(str(j) + ". " + file + " is copied.")
                    shutil.copy(os.path.join(root, file),
                                copyDir)


if __name__ == '__main__':

    # Your file to search, directory to search, directory to copy
    searchAndCopy('searchFile.txt or md', 'searchDir', 'copyDir')
