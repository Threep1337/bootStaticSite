import os
import shutil

def copy_files_recursive(source,dest):
    if not os.path.exists(source):
        raise Exception("No source path exists!")
    if not os.path.exists(source):
        raise Exception("No destination path exists!")
    
    #print(f"copying {source} to {dest}")

    shutil.rmtree(dest)
    os.mkdir(dest)
    #shutil.copy(source,dest)
    #shutil.copy('/home/threep/bootdev/bootStaticSite/static/*',dest)
    filesToCopy = os.listdir(source)
    for file in filesToCopy:
        #print(file)
        fullSourcepath = os.path.join(source,file)
        fullDestpath = os.path.join(dest,file)
        if os.path.isfile(fullSourcepath):
            #print(f"{file} is a file")
            print(f"copying {fullSourcepath} to {fullDestpath}")
            shutil.copy(fullSourcepath,fullDestpath)
        else:
            print(f"creating directory {fullDestpath}")
            os.mkdir(fullDestpath)
            copy_files_recursive(fullSourcepath,fullDestpath)