#!/usr/bin/python

import re
import sys
#so we will need 4 classes (they could be sub classes actually.)

# Parent class would be "Files":

# Every entity has the following properties:
# Type – The type of the entity (one of the 4 type above).
# Name - An alphanumeric string. Two entities with the same parent cannot have the same name. Similarly, two drives cannot have the same name.
# Path – The concatenation of the names of the containing entities, from the drive down to and including the entity. The names are separated by ‘\’.

# A text file has a property called Content which is a string. 

# Size – an integer defined as follows:
# For a text file – it is the length of its content. 
# For a drive or a folder, it is the sum of all sizes of the entities it contains.
# For a zip file, it is one half of the sum of all sizes of the entities it contains

# 1) Create – Creates a new entity.
# Arguments: Type, Name, Path of parent.
# Exceptions: Path not found; Path already exists; Illegal File System Operation (if any of the rules a-d above is violated).

# 2)  Delete – Deletes an existing entity (and all the entities it contains).
# Arguments: Path
# Exceptions: Path not found.

# 3)  Move – Changing the parent of an entity.
# Arguments: Source Path, Destination Path. 
# Exceptions: Path not found; Path already exists, Illegal File System Operation.

# 4)  WriteToFile – Changes the content of a text file.
# Arguments: Path, Content
# Exceptions: Path not found; Not a text file.

# https://stackoverflow.com/questions/805066/how-do-i-call-a-parent-classs-method-from-a-child-class-in-python

# Well, do i even need to use Classes?
#HOW DO WE ENSURE THAT IF FOLDERS IS UPDATED THAT THE PATH FOR THE FILES AND ZIP FILES WILL UPDATE TOO?

class globalITEMS():

    options = ["Create a Folder", "Create a File", "Read a File", "Update a File", "Move a folder", "Move a file", "Delete a File or Folder", "Show all Current Paths", "Zip a file or Folder", "Unzip a File or Folder", "Show all Files, Folders, and their Attributes", "Exit"]


    #------------------------------------------------------------------------------
    #Here is the list for all the paths. This is like the most important piece...
    #------------------------------------------------------------------------------

    paths = ["Drive","Drive/Folder","Drive/Folder1", "Drive/Folder/File.txt", "Drive/File.txt", "Drive/File2.txt"]

    #------------------------------------------------------------------------------

    #------------------------------------------------------------------------------
    #Here is the list for hidden paths for storing paths for zipping and unzipping
    #------------------------------------------------------------------------------

    hiddenpaths = ["Test"]

    #------------------------------------------------------------------------------


    #------------------------------------------------------------------------------
    #THIS IS WHERE THE FILE CONTENT IS STORED!!! VERY IMPORTANT, DO NOT ACCIDENTALLY DELETE!!
    #------------------------------------------------------------------------------
    fileContentDict = {"Drive/Folder/File.txt":"test", "Drive/File.txt":"words", "Drive/File2.txt":"Does this work"}

    #------------------------------------------------------------------------------


    #------------------------------------------------------------------------------
    #THIS IS WHERE THE ZIPPED FILE CONTENT IS STORED!!! VERY IMPORTANT, DO NOT ACCIDENTALLY DELETE!!
    #------------------------------------------------------------------------------

    ZippedFileDict = {"Test/test":"test"}

    #------------------------------------------------------------------------------

    ZippedFileDictTEMP = {}

    test = []

#------------------------------------------------------------------------------
#CREATE A NEW FOLDER
#------------------------------------------------------------------------------

def CreateFolder(): #1. Create a Folder

    Show_All_Paths()

    # can't create it in a zip file or a txt file.

    while True:

        try:

            number = input("\nWhich Folder would you like to create a new Folder in?\n\n(A Folder is anything that does NOT end with .zip or .txt.)\n\n")

            selectedPath = globalITEMS.paths[int(number) -1]

            while ".txt" in selectedPath or ".zip" in selectedPath:
                print("\n!!!ILLEGAL FILE SYSTEM ERROR: That is not a Folder.!!!\n")
                number = input("\nWhich Folder would you like to create a new Folder in?\n\n(A Folder is anything that does NOT end with .zip or .txt.)\n\n")
                selectedPath = globalITEMS.paths[int(number) -1]


            name = input("\nWhat would you like to call this new folder?:\n\n")

            # if selectedpath + "/" + name in path throw error
            # else
            Newfoldername = selectedPath + "/" + name.title()

            while Newfoldername in globalITEMS.paths:
                print("\n!!!ERROR: Folder already exists in this Path. Please name it something else.!!!\n")

                name = input("\nWhat would you like to call this new folder?:\n\n")

                Newfoldername = selectedPath + "/" + name.title()

            globalITEMS.paths.append(Newfoldername)

            print("\n")

            Show_All_Paths()
            break

    # if selected path not in path, error.
        except IndexError:
                print("\n\n!!!ERROR: Path not found, please select from one of the existing Paths.!!!\n\n")

        except ValueError:
                print("\n\n!!!ERROR: Path not found, please select from one of the existing Paths.!!!\n\n")

        except KeyboardInterrupt:
            print("\n\nExiting...\n\n")
            sys.exit(0)

            # break
            #else:

    #1) Create – Creates a new entity.
    # Arguments: Type, Name, Path of parent.
    # Exceptions: Path not found; Path already exists; Illegal File System Operation (if any of the rules a-d above is violated).
            
    # Select from Existing Path
    # if Path does not Exist, Create path - path must have /Drive at the beginning though
    # Include a back button

#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
#CREATE A FILE
#------------------------------------------------------------------------------

def CreateFile(): #2 Create a File
    Show_All_Paths()

    while True:
        try:
            number = input("\nSelect a Folder to create the file in:\n\n(A Folder is anything that does NOT end with .zip or .txt.)\n\n")

            selectedPath = globalITEMS.paths[int(number) -1]

            while ".txt" in selectedPath or ".zip" in selectedPath:
                print("\n!!!ILLEGAL FILE SYSTEM ERROR: That is not a Folder.!!!\n")
                number = input("\nWhich Folder would you like to create a new Folder in?\n\n(A Folder is anything that does NOT end with .zip or .txt.)\n\n")
                selectedPath = globalITEMS.paths[int(number) -1]


            name = input("\nWhat would you like to name this file?:\n\n")

            newInnerFileName = name.title(),".txt"

            NewFilename = str(selectedPath) + "/" + str(newInnerFileName).replace("'","").replace(",","").replace("(","").replace(")","").replace(" ","")

            while NewFilename in globalITEMS.paths:
                print("\n!!!ERROR: File already exists in this Path. Please name it something else.!!!\n")
                name = input("\nWhat would you like to name this file?:\n\n")

                newInnerFileName = name.title(),".txt"

                NewFilename = str(selectedPath) + "/" + str(newInnerFileName).replace("'","").replace(",","").replace("(","").replace(")","").replace(" ","")


            globalITEMS.paths.append(NewFilename)

            fileContent = input("\n\nType some stuff to put in this file.\n\n")

            globalITEMS.fileContentDict[globalITEMS.paths[-1]] = fileContent

            print ("\nHere is the content you wrote:\n\n", str(list(globalITEMS.fileContentDict.values())[-1]).replace("'","").replace("]","").replace("[",""), "\n")

            #1) Create – Creates a new entity.
            # Arguments: Type, Name, Path of parent.
            # Exceptions: Path not found; Path already exists; Illegal File System Operation (if any of the rules a-d above is violated).
            # Select from Existing Path
            # Include a back button
            # Ask if user wants to write something to put in the file whilst creating it. if not then it is just a blank txt file that they can append to.
            # for path not found error, show that if the user puts in a non valid option like if there are only 8 paths and they pick #10        
            Show_All_Paths()
            break


        except IndexError:
            print("\n\n!!!ERROR: Path not found, please select from one of the existing Paths.!!!\n\n")

        except ValueError:
            print("\n\n!!!ERROR: Path not found, please select from one of the existing Paths.!!!\n\n")

        except KeyboardInterrupt:
            print("\n\nExiting...\n\n")
            sys.exit(0)

#------------------------------------------------------------------------------


#------------------------------------------------------------------------------
#READ A FILE
#------------------------------------------------------------------------------

def ReadFile(): #3. Read a File

    Show_All_Paths()

    while True:
        try:

            number = input("\nWhich File would you like to read?:\n\n(Text Files End with .txt)\n\n")

            selectedPath = globalITEMS.paths[int(number)-1]

            while ".txt" not in selectedPath:
                print("\n!!!ERROR: That is not a Text File.!!!\n")
                
                number = input("\nWhich File would you like to read?:\n\n(Text Files End with .txt)\n\n")
                
                selectedPath = globalITEMS.paths[int(number) -1]

            print ("\nHere are the contents of the file:\n\n", str(globalITEMS.fileContentDict[selectedPath]).replace("'","").replace("]","").replace("[",""), "\n")

        # Include a back button
        # If file is blank, show a new line and below that note "FYI That blank line you just saw means there's nothing in this file."
        # CANNOT READ A ZIP FILE!

            break

        except IndexError:
            print("\n\n!!!ERROR: Path not found, please select from one of the existing Paths.!!!\n\n")

        except ValueError:
            print("\n\n!!!ERROR: Path not found, please select from one of the existing Paths.!!!\n\n")
        
        except KeyboardInterrupt:
            print("\n\nExiting...\n\n")
            sys.exit(0)

#------------------------------------------------------------------------------


#------------------------------------------------------------------------------
#APPEND TO A FILE
#------------------------------------------------------------------------------

def AppendToFile(): #4. Update a File (Should have BOTH Append and OVERWRITE Options)

    Show_All_Paths()

    while True:
        try:

            number = input("\nWhich File would you like to append to?\n\n(Text Files End with .txt)\n\n")
            
            selectedPath = globalITEMS.paths[int(number)-1]

            while ".txt" not in selectedPath:
                print("\n!!!ERROR: That is not a Text File.!!!\n")

                number = input("\nWhich File would you like to append to?\n\n(Text Files End with .txt)\n\n")
                
                selectedPath = globalITEMS.paths[int(number)-1]

            print("\nHere's what's in the file currently:\n\n", globalITEMS.fileContentDict[selectedPath])
            appendText = input("\n\nWhat would you like to append to the file?\n\n")

            # AppendToThisFile = globalITEMS.paths[int(number)-1] # removed that and put it within the line below

            # globalITEMS.fileContentDict[selectedPath].append(appendText)

            # print ("\nHere is the updated content in the file:\n\n", str(list(globalITEMS.fileContentDict.values())[-1]).replace("'","").replace("]","").replace("[","").replace(",",""), "\n")
            # break

            globalITEMS.fileContentDict[selectedPath]= {globalITEMS.fileContentDict[selectedPath] + " " + appendText}

            print ("\nHere is the updated content in the file:\n\n", str(list(globalITEMS.fileContentDict[selectedPath])).replace("'","").replace("]","").replace("[","").replace(",",""), "\n")
            Show_All_Paths()
            break
    
        except IndexError:
            print("\n\n!!!ERROR: Path not found, please select from one of the existing Paths.!!!\n\n")

        except ValueError:
            print("\n\n!!!ERROR: Path not found, please select from one of the existing Paths.!!!\n\n")

        except KeyboardInterrupt:
            print("\n\nExiting...\n\n")
            sys.exit(0)

#------------------------------------------------------------------------------
    

#------------------------------------------------------------------------------
#OVERWRITE A FILE
#------------------------------------------------------------------------------

def OverwriteFile():#4. Update a File (Should have BOTH Append and OVERWRITE Options)

    Show_All_Paths()

    while True:
        try:

            number = input("\nWhich File would you like to Overwrite?\n\n(Files End with .txt or .zip)\n\n")

            selectedPath = globalITEMS.paths[int(number)-1]

            while ".txt" not in selectedPath:

                print("\n!!!ERROR: That is not a Text File.!!!\n")

                number = input("\nWhich File would you like to Overwrite?\n\n(Files End with .txt or .zip)\n\n")

                selectedPath = globalITEMS.paths[int(number)-1]

            print("\nThis is the File's Current Content:\n\n",str(list(globalITEMS.fileContentDict[selectedPath])).replace("'","").replace("]","").replace("[",""), "\n")

            overwriteContent = input("\nWhat would you like to overwrite the file with?\n\n")

            globalITEMS.fileContentDict[selectedPath] = {str(overwriteContent)}

            print ("\nHere is what the File looks like now:\n\n", str(list(globalITEMS.fileContentDict[selectedPath])).replace("'","").replace("]","").replace("[",""), "\n")

            Show_All_Paths()

            break
    
        except IndexError:
            print("\n\n!!!ERROR: Path not found, please select from one of the existing Paths.!!!\n\n")

        except ValueError:
            print("\n\n!!!ERROR: Path not found, please select from one of the existing Paths.!!!\n\n")

        except KeyboardInterrupt:
            print("\n\nExiting...\n\n")
            sys.exit(0)


    # Include a back button
 #------------------------------------------------------------------------------   

#def MoveFolder(): #5. Move a folder
    # 3)  Move – Changing the parent of an entity.
    # Arguments: Source Path, Destination Path. 
    # Exceptions: Path not found; Path already exists, Illegal File System Operation.
    # 
    # Display current list of Folders and their paths (anything ending with .txt or .zip)
    # Include a back button
    #pass


#------------------------------------------------------------------------------   
    

#------------------------------------------------------------------------------
#MOVE A FILE
#------------------------------------------------------------------------------

# would need to update both paths and globalITEMS.filecontentdict for THAT FILE.

# i should create a def for checking if a path exists but thats a bit hard when each input path name is called a different variable. perhaps i can hse {} in the def and then feed the name of that variable into each one when i call it for say creating a file, creating a folder, etc.

# Moving a FILE is easy. jsut replace everything before the last / with the FOLDER that is selected. if the selectd item is not a folder, then 

def MoveFile(): #6. Move a file
    # 3)  Move – Changing the parent of an entity.
    # Arguments: Source Path, Destination Path. 
    # Exceptions: Path not found; Path already exists, Illegal File System Operation.
    # Display current list of files and their paths (anything ending with .txt or .zip)
    # Include a back button
    # 

    Show_All_Paths()
    
    # print(globalITEMS.ZippedFileDict)

    while True:

        try:
    
            number = input("\n\nWhich File Would you like to move? \n\n(Files End with .txt or .zip)\n\n")

            selectedPath = globalITEMS.paths[int(number)-1]

            # if selected path contains .zip then do this, if it contans .txt then do that

            # should be either a zip file of a txt file.


            while ".txt" not in selectedPath and ".zip" not in selectedPath:
                
                print("\n!!!ERROR: That is not a File. Files End with .txt or .zip!!!\n")

                number = input("\n\nWhich File Would you like to move? \n\n(Files End with .txt or .zip)\n\n")

                selectedPath = globalITEMS.paths[int(number)-1]


            otherNumber = input("Where would you like the File to be moved to?\n\n")

            newPath = globalITEMS.paths[int(otherNumber)-1]

            updatedPath = re.split("/", selectedPath)
            updatedPath = updatedPath[-1]
            updatedPath =  newPath + "/" + str(updatedPath)


            while updatedPath in selectedPath:

                print("\n!!!ERROR - PATH ALREADY EXISTS - Please Select a Different location to move this file to!!!")
                otherNumber = input("Where would you like the File to be moved to?\n\n")

                newPath = globalITEMS.paths[int(otherNumber)-1]

                updatedPath = re.split("/", selectedPath)
                updatedPath = updatedPath[-1]
                updatedPath =  newPath + "/" + str(updatedPath)

            while ".txt" in selectedPath:

                print("\n!!!ERROR - ILLEGAL FILE OPERATION - Cannot move item into a file, Please Select a FOLDER (Folders do NOT End with .txt or .zip)!!!")
                otherNumber = input("Where would you like the File to be moved to?\n\n")

                newPath = globalITEMS.paths[int(otherNumber)-1]

                updatedPath = re.split("/", selectedPath)
                updatedPath = updatedPath[-1]
                updatedPath =  newPath + "/" + str(updatedPath)

            globalITEMS.paths.append(updatedPath) # this piece is GOOD.

            # ziptxtfiles = selectedPath.replace("_txt.zip", ".txt")

            pathtoPop = selectedPath.split("/")
            pathtoPopEND = pathtoPop[-1]
            del pathtoPop[-1]
            pathtoPop = "/".join(pathtoPop)

            pathtoPoPFILE = pathtoPop + "/" + pathtoPopEND

            pathtoPoPFILE = pathtoPoPFILE.replace("_txt.zip","_unzipped.txt")

            pathtoPop = pathtoPop + "_Unzipped/" + pathtoPopEND
            pathtoPop = pathtoPop.replace("_txt.zip",".txt")



            # print("zippefiledict : ",globalITEMS.ZippedFileDict)
            # print("Filecontentdict: ", globalITEMS.fileContentDict)
             # OLD = Drive/Folder_Unzipped/File_unzipped.txt but it is selecting Drive/Folder_Unzipped/File.txt

            # print(selectedPath)
            # print(updatedPath)

            # NEW = Drive/Folder1_Unzipped/File_unzipped.txt but pathtopop is this: Drive/Folder_Unzipped/File.txt

            # selected path is: Drive/Folder/File_txt.zip
            # updatedpath = Drive/Folder1/File_txt.zip

            ZIPpathtopop = pathtoPop.replace("_txt.zip", "_unzipped.txt")

            zipPathtoUpdate = updatedPath.split("/")
            zipPathtoUpdateEND = zipPathtoUpdate[-1]
            del zipPathtoUpdate[-1]
            zipPathtoUpdate = "/".join(zipPathtoUpdate)

            zipPathtoUpdate.replace(zipPathtoUpdate, pathtoPop)

            zipPathtoUpdateFOLDER = zipPathtoUpdate + "_Unzipped/" + zipPathtoUpdateEND

            # print(zipPathtoUpdateFOLDER)

            zipPathtoUpdateFILE = zipPathtoUpdate + "/" + zipPathtoUpdateEND
            # print(zipPathtoUpdateFILE)

            zipPathtoUpdateFILE = zipPathtoUpdateFILE.replace("_txt.zip", "_unzipped.txt")
            print(zipPathtoUpdateFOLDER)
            print(ZIPpathtopop)

            #Need to replace Drive/Folder_Unzipped/File.txt with Drive/Folder1_Unzipped/File.txt
            




            txtfile = ".txt"
            zipfile = "_txt.zip"

            if txtfile in selectedPath:

                    globalITEMS.fileContentDict[updatedPath] = globalITEMS.fileContentDict.pop(selectedPath)

                    # globalITEMS.paths.remove(selectedPath)

                    Show_All_Paths()
                
                # now i need to replace selected path in filecontent dict with updated path.

            if zipfile in selectedPath:
                for zipfile in selectedPath:
                #     # need to change it from _txt.zip to .txt
                #     # need to move it from zippedfiledict anc change it from .txt to _unzipped.txt

                #     # zipSelectedPath = selectedPath.replace("_txt.zip",".txt") # locate this
                #     # replace it with replacezipselectpath

                    # replaceZipSelectPath = selectedPath.replace("_txt.zip","_unzipped.txt")

                #     # print(zipSelectedPath, "\n\n", replaceZipSelectPath, "\n\n", globalITEMS.fileContentDict, "\n\n", globalITEMS.ZippedFileDict, "\n\n")

                #         # fileContentDictTEMP = {k:v for k, v in globalITEMS.}

                #     globalITEMS.fileContentDict[updatedPath] = globalITEMS.fileContentDict.pop(selectedPath)

                #     globalITEMS.ZippedFileDict[updatedPath] = globalITEMS.ZippedFileDict.pop(selectedPath)


                    # probably needs a temp thing here... 

                    # globalITEMS.ZippedFileDict[updatedPath] = globalITEMS.ZippedFileDict.pop(pathtoPop)

                    globalITEMS.ZippedFileDict.update({key.replace(pathtoPoPFILE, zipPathtoUpdateFILE): value for key, value in globalITEMS.ZippedFileDict.items()})

                    
                    # globalITEMS.ZippedFileDict.pop(updatedPath)

                    # move the file if updatedpath in k from zipped file dict to filecontent dict

                    # globalITEMS.paths.remove(selectedPath)


            #     # print(globalITEMS.ZippedFileDict)
            # elif ".zip" in selectedPath:

            #     zipFile = [item for item in selectedPath if ".zip" in item]
            #     txtFile = [item for item in selectedPath if ".txt" in item]


            #     for i in zipFile:
            #         # if zip in path, update zippedfilecontent dict ()
            #         globalITEMS.ZippedFileDict.update({key.replace(selectedPath, updatedPath).replace("_txt.zip", "_unzipped.txt"): value for key, value in globalITEMS.ZippedFileDict.items()})


            #     for i in txtFile:
            #          # for txt in path, need to update file content dict.

            #         globalITEMS.fileContentDict[updatedPath] = globalITEMS.fileContentDict.pop(selectedPath)


            #     globalITEMS.paths.remove(selectedPath)

            if zipfile not in selectedPath and ".zip" in selectedPath:
                for i in selectedPath:
                    globalITEMS.ZippedFileDict.update({key.replace(ZIPpathtopop, zipPathtoUpdateFOLDER): value for key, value in globalITEMS.ZippedFileDict.items()})

            globalITEMS.paths.remove(selectedPath)
            
            Show_All_Paths()
            
            break

        except IndexError:
                print("\n\n!!!ERROR: Path not found, please select from one of the existing Paths.!!!\n\n")

        except ValueError:
                print("\n\n!!!ERROR: Path not found, please select from one of the existing Paths.!!!\n\n")

        except KeyboardInterrupt:
            print("\n\nExiting...\n\n")
            sys.exit(0)
    # else:
    #     pass # it should go back and ask for a file.

#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
#MOVE A FOLDER
#------------------------------------------------------------------------------

# would need to update both globalITEMS.paths and globalITEMS.filecontentdict for all folders in the selected Folder AND all files in the path of the selected path.
# could we say for everything that has .txt or .zip call movefile()?

def MoveFolder(): #5. Move a folder
    # 3)  Move – Changing the parent of an entity.
    # Arguments: Source Path, Destination Path. 
    # Exceptions: Path not found; Path already exists, Illegal File System Operation.
    # 
    # Display current list of Folders and their paths (anything ending with .txt or .zip)
    # Include a back button
    Show_All_Paths()

    while True:

        try:
    
            number = input("\n\nWhich Folder would you like to move?\n\n(A Folder is anything that does NOT end with .zip or .txt.)\n\n")

            selectedPath = globalITEMS.paths[int(number)-1]

            while "Drive/" not in selectedPath:
                print("\n!!!ERROR: ILLEGAL FILE SYSTEM OPERATION - A Drive cannot be contained in any other Entity. Do not Attempt to Move the DRIVE - Please Choose a Folder Instead. A Folder is anything that does NOT end with .zip or .txt.)!!!")
                
                number = input("\n\nWhich Folder would you like to move?\n\n(A Folder is anything that does NOT end with .zip or .txt.)\n\n")

                selectedPath = globalITEMS.paths[int(number)-1]

            while ".txt" in selectedPath or ".zip" in selectedPath:
                print("\n!!!ERROR: That is not a Folder!!!")

                number = input("\n\nWhich Folder would you like to move?\n\n(A Folder is anything that does NOT end with .zip or .txt.)\n\n")

                selectedPath = globalITEMS.paths[int(number)-1]

            otherNumber = input("\n\nWhere would you like to move the folder?\n\n(A Folder is anything that does NOT end with .zip or .txt.)\n\n")

            newPath = globalITEMS.paths[int(otherNumber)-1]

            selectedPathSlash = selectedPath + "/" 

            # this splits out the path by delimiter

            updatedPath = re.split("/", selectedPath)

            updatedNewPath = re.split("/", newPath)
            updatedNewPath = updatedNewPath[-1]

            updatedPath = updatedPath[-1]
            # print(updatedPath)

            updatedPath = newPath + "/" + updatedPath
            # print(updatedPath)

            # so we need to take into account updated path and select path. the inner while loop should go here.

            while updatedPath in globalITEMS.paths:

                print("\n!!!ERROR - PATH ALREADY EXISTS - Please Select a Different location to move this folder to!!!")

                otherNumber = input("\n\nWhere would you like to move the folder?\n\n(A Folder is anything that does NOT end with .zip or .txt.)\n\n")

                newPath = globalITEMS.paths[int(otherNumber)-1]

                selectedPathSlash = selectedPath + "/" 

                # this splits out the path by delimiter

                updatedPath = re.split("/", selectedPath)

                updatedNewPath = re.split("/", newPath)
                updatedNewPath = updatedNewPath[-1]

                updatedPath = updatedPath[-1]
                # print(updatedPath)

                updatedPath = newPath + "/" + updatedPath


            globalITEMS.paths.append(updatedPath)
            globalITEMS.paths.remove(selectedPath)

            updatedpathSlash = updatedPath + "/"


            #1. update the paths with the new path on surface level - DONE
            #2. Remove old path on surface level - DONE
            
            #3. For All paths containing Selected Path, update their paths - DONE
            #3.5 remove old paths... - DONE
            #4. For all TXT files update fileContentDict's keys to new path
            #5. for all ZIP files, update zipFileContentDict's keys to new path

            SECONDhiddenpaths = [item for item in globalITEMS.paths if selectedPathSlash in item]

            # for all items in hidden paths, split everything by / and take -1 then replace everything before that with new path.
            # print("SECONDhiddenpaths: ", SECONDhiddenpaths)
            # print(SECONDhiddenpaths) 

            for i in SECONDhiddenpaths:
                # test = [i.split('/', updatedNewPath)] # how do we keep the folder it came in??
                
                globalITEMS.test = [i.replace(selectedPath, updatedPath) for i in SECONDhiddenpaths]

                                # i_OLD = re.split("/", i)
                # i_end = i_OLD[-1]
                # del i_OLD[-1]

                # i_OLD = "/".join(i_OLD)

                # i_UPDATED = i_OLD + "_Unzipped/" + i_end

                #hmm so for selected string, the last word is the one we want to keep so that we can figure out where that word shows up.. but what if that word is the same word like Drive/folder/folder/folder/test.txt??? how do we know where to cut?

                # so lets see Example: move Drive/Folder/Folder > Drive/Folder1/Folder

                # we would select the folder to move as being Drive/Folder.

                # is there a way to remvoe the selected path from the thing?


            # globalITEMS.paths = [item for item in globalITEMS.paths if selectedPathSlash not in item]

            # ISSUE is how do we remove the old paths without accidentally removing the new ones

            # print("UPDATED SECONDhiddenpaths - IE test: ", test)

            globalITEMS.paths.extend(globalITEMS.test)




            # print("FilecontentDict: ", globalITEMS.fileContentDict) # replace(selectedPath, updatedPath)

            files = [".txt",".zip"]

            txt_zip = [item for item in SECONDhiddenpaths if ".txt" in item] # takes all the files with .txt in second hidden paths

            # print(txt_zip)

            # test2 = [item for item in test if ".txt" in item]

            # print(test2)


            fileContentDictTEMP = {k:v for k,v in globalITEMS.fileContentDict.items() for txt_zip in k} # creates a temp dict that only takes the txt files

            globalITEMS.fileContentDict.update({key.replace(selectedPathSlash,updatedpathSlash): value for key, value in fileContentDictTEMP.items()}) # updates keys by taking them from dict temp and replacing the - then adds updated keys to dict

            # globalITEMS.fileContentDict = {key: val for key, val in globalITEMS.fileContentDict.items() if key not in txt_zip} # removes old key values from dict

            globalITEMS.ZippedFileDict.update({key.replace(selectedPathSlash,updatedpathSlash): value for key, value in globalITEMS.ZippedFileDict.items()}) # updates keys by taking them from dict temp and replacing the - then adds updated keys to dict


            # print("ZippedFilecontentDict: ", globalITEMS.ZippedFileDict)


            
            # so for this, i need to create a new variable - split secondhiddenpaths and take out -1, then merge all the others before that, then add _Unzipped, then merge them back together to be able to call that to THEN be able to replace that with test BUT for test i also need to split the string by /, take out -1 and then merge the rest then add _Unzipped then join that back with the -1.

            # then i need to say, k:v for k:v in zippedfiledict if zippedhiddenpaths in key

           

            #Drive/Folder/File.txt is what is in fiilecontent dict. for everythuing in secondhiddenpaths

            # print(globalITEMS.hiddenpaths) # no need for this one, will not run into this

            # i should be able to replace the old names with the new names similar to this: i.replace(selectedPath, updatedPath)

            # globalITEMS.paths = [item for item in globalITEMS.paths if selectedPathSlash not in item]

            SECONDhiddenpaths.clear()

            globalITEMS.paths = [item for item in globalITEMS.paths if selectedPathSlash not in item]

            # print("SECOND HIDDEN PATHS",SECONDhiddenpaths,"TEST" ,test)

            Show_All_Paths()

            break


        except IndexError:
            print("\n\n!!!ERROR: Path not found, please select from one of the existing Paths.!!!\n\n")

        except ValueError:
            print("\n\n!!!ERROR: Path not found, please select from one of the existing Paths.!!!\n\n")

        except KeyboardInterrupt:
            print("\n\nExiting...\n\n")
            sys.exit(0)


    # This needs to move all zip files and folders within the thing too. 
    # Ok so it moves zip files.... does it move zip folders within a folder tho? It can if you are not directly selecting the zip folder itself.

# Example: Drive/Folder/Test.Zip. if you select test.zip to move it will not work. if you select Drive/Folder and move it to Drive/Folder1, it will indeed move it so the path looks like this: Drive/Folder1/Test.zip.

# so on the surface level, yes it does its thing. now we just need to update filecontent dict and zippedfilecontent dict and that's pretty much it.

# HOWEVER we need to make it so that we CANNOT SELECT anything with .zip or .txt directly otherwise it will fail. if the .zip or .txt is in the folder that you selected that is fine but do NOT select them directly!


#------------------------------------------------------------------------------


#------------------------------------------------------------------------------
#DELETE A FILE FROM THE PATHS LIST (AS WELL AS ITS CORROSPONDING DICTIONARY CONTENT)!
#------------------------------------------------------------------------------

def DeleteAFILE(): #7. Delete a File or Folder

    Show_All_Paths()
    
    while True:

        try:
            number = input("\nWhich file would you like to delete?\n\n(Files End with .txt or .zip)\n\n")

            selectedPath = (globalITEMS.paths[int(number)-1]) # this needs to be here. if it was lower than the del, it would not have captured the name of the file as the file would have been deleted by then.

            while ".txt" not in selectedPath and ".zip" not in selectedPath:

                print("\n!!!ERROR: That is not a File. Files End with .txt or .zip!!!\n")

                number = input("\nWhich file would you like to delete?\n\n(Files End with .txt or .zip)\n\n")

                selectedPath = (globalITEMS.paths[int(number)-1])


            del globalITEMS.paths[int(number)-1]

            globalITEMS.fileContentDict = {k:v for k,v in globalITEMS.fileContentDict.items() if not selectedPath in k}

            # copy this to delete a folder under for all dictdeletefolder that contains .zip, do this:

            zipSelectedPath = selectedPath.replace(".zip", "_Unzipped/")

            if ".zip" in selectedPath:
                # remove things continaing selected "path (remove.zip) + _Unzipped/" from zipped file dict
                # remove things continaing selected "path (remove.zip) + _Unzipped/" from hiddenpath
                #basically for i in hiddenpaths that contains zipselected path, remove that item or hidden paths = everything that does not contain zelected paths might be an easier way to do it. same thing with zippedfiledict.
                globalITEMS.ZippedFileDict = {k:v for k,v in globalITEMS.fileContentDict.items() if not zipSelectedPath in k}
                globalITEMS.hiddenpaths = [item for item in globalITEMS.hiddenpaths if zipSelectedPath not in item]

            Show_All_Paths()

            break

        except IndexError:
            print("\n\n!!!ERROR: Path not found, please select from one of the existing Paths.!!!\n\n")

        except ValueError:
            print("\n\n!!!ERROR: Path not found, please select from one of the existing Paths.!!!\n\n")       

        except KeyboardInterrupt:
            print("\n\nExiting...\n\n")
            sys.exit(0)

    # ok deleting a FILE works.
    # Deleting the file will also now delete the Dictionary Content of the file! YAY!!!

    # 2)  Delete – Deletes an existing entity (and all the entities it contains).
    # Arguments: Path
    # Exceptions: Path not found.
    # Include a back button
    # 
#------------------------------------------------------------------------------


def DeleteAFolder():

    # take the whole path and delete the thing after the last /. Example: /Drive/Folder1/test.txt <<< this would delete test.txt.

    Show_All_Paths()

    while True:

        try:

            number = input("\nWhich folder would you like to delete?\n\n(A Folder is anything that does NOT end with .zip or .txt.)\n\n")

            selectedPath = globalITEMS.paths[int(number)-1]

            while ".txt" in selectedPath or "zip" in selectedPath:
                print("\n!!!ERROR: That is not a Folder!!!\n")
                
                number = input("\nWhich folder would you like to delete?\n\n(A Folder is anything that does NOT end with .zip or .txt.)\n\n")

                selectedPath = globalITEMS.paths[int(number)-1]               

            DictDeleteFolder = selectedPath + "/" # this will be used to remove everything containing Drive/Folder/ in the Dictionary as well as in the list because if we want to remove 

            if "Drive/" in selectedPath:

                globalITEMS.paths.remove(selectedPath) # this deletes the folder but does not delete things in the folder.

            # for x in paths:
            #     if DictDeleteFolder in x:
            #         paths.remove(x) # Works BUT ONLY REMOVES THE FIRST INSTANCE OF THE ITEM!! IT NEEDS TO REMOVE EVERYTHING CONTAINING THAT ITEM, NOT JUST THE FIRST ITEM.
            
            #-------------
            # THIS PIECE REMOVES ANYTHING IN THE DELETED FOLDER'S PATH THAT CONTAINS ZIP BUT ALSO IT REMOVES THE UNDERLYING DICTIONARY AND HIDDENPATHS THAT GO ALONG WITH THE DELETED ZIP FILE.

            # print(globalITEMS.fileContentDict)

            filecontentdictZIPPED = {k:v for k,v in globalITEMS.ZippedFileDict.items() if DictDeleteFolder in k}
            # print(filecontentdictZIPPED)

            # print(globalITEMS.ZippedFileDict)

            globalITEMS.ZippedFileDict = {k: v for k, v in globalITEMS.ZippedFileDict.items() if k not in filecontentdictZIPPED}

            # print(globalITEMS.ZippedFileDict)
            # print("hiddenpaths: ", globalITEMS.hiddenpaths)
            #-------------

            globalITEMS.paths = [item for item in globalITEMS.paths if DictDeleteFolder not in item]

            globalITEMS.fileContentDict = {k:v for k,v in globalITEMS.fileContentDict.items() if not DictDeleteFolder in k} # cool this removes the dictionary associated with the txt file. There needs to be ADDITIONAL CODE here that says IF removed contains a .txt, then do this.



            # del globalITEMS.fileContentDict[DeleteFolder]

            #if list item deleted contains.txt, then remove the corrosponding dictionary content instance with that name...

            Show_All_Paths()
            break

        except IndexError:
                print("\n\n!!!ERROR: Path not found, please select from one of the existing Paths.!!!\n\n")

        except ValueError:
                print("\n\n!!!ERROR: Path not found, please select from one of the existing Paths.!!!\n\n")

        except KeyboardInterrupt:
            print("\n\nExiting...\n\n")
            sys.exit(0)


#------------------------------------------------------------------------------
#SHOW ALL PATHS
#------------------------------------------------------------------------------

def Show_All_Paths(): #8. Show all Current Paths 
    print('''

\n-------------------------------------
Here are all of your current Paths:
-------------------------------------\n
''')
    # show all current Paths.
    count = 1
    for path in globalITEMS.paths:
        print(count,"-",path)
        count +=1

#------------------------------------------------------------------------------


#------------------------------------------------------------------------------
#ZIPS A FILE - DONE
#------------------------------------------------------------------------------

def Zip_File(): #9 Zip a file or Folder

    # list all the paths and select a folder or file to zip.
    # Create a new item with the same name but with .zip and size being half the size of the original
    # When zipping a file, make a copy of it but store it in some other dictionary so that when you unzip it, it will take this copied version and put it back.
    
    Show_All_Paths()

    while True:

        try:

            number = input("\nWhich File would you like to Zip?\n\n(Text Files End with .txt)\n\n")

            selectedPath = globalITEMS.paths[int(number)-1]

            while ".txt" not in selectedPath:

                print("\n!!!ERROR: That is not a Text File!!!")

                number = input("\nWhich File would you like to Zip?\n\n(Text Files End with .txt)\n\n")

                selectedPath = globalITEMS.paths[int(number)-1]

            ZippedFile = selectedPath.replace(".txt","_txt.zip") # filter out the .txt then + ".zip"

            UnzippedFile = selectedPath.replace(".txt","_unzipped.txt")

            # this should ONLY Take .txt files. nothing else.

            globalITEMS.paths.append(ZippedFile) # Append it cuz we want to make a copy. Then when unzipping, simply duplicate the dictionary corrosponding with that filetozip, remove the .zip.. but what if i change the file after i zipped it and now want to unzip it?

            #perhaps i should make a Zipped Dictionary as well... then copy the zipped filename and content from the original dictionary to the zipped dictionary. then when i unzip, i will then move it back and append this to the original dictionary

            globalITEMS.ZippedFileDictTEMP = {k:v for k,v in globalITEMS.fileContentDict.items() if selectedPath in k}
            # need to replace selected path with the filename + _unzipped.txt

            globalITEMS.ZippedFileDict.update({key.replace(selectedPath, UnzippedFile): value for key, value in globalITEMS.ZippedFileDictTEMP.items()}) # takes from the temp dict and adds _unzipped for each of the txt file's paths.

            globalITEMS.ZippedFileDictTEMP.clear() # clears the temp dict. there should not be a need to use this temp dict outside of this def. so leaving it within the def.

            # globalITEMS.paths.remove(selectedPath)

            Show_All_Paths()

            break

        except IndexError:
            print("\n\n!!!ERROR: Path not found, please select from one of the existing Paths.!!!\n\n")

        except ValueError:
            print("\n\n!!!ERROR: Path not found, please select from one of the existing Paths.!!!\n\n")

        except KeyboardInterrupt:
            print("\n\nExiting...\n\n")
            sys.exit(0)

    #Size would be filetozip size / 2

#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
#UNZIPS A FILE - DONE
#------------------------------------------------------------------------------
def UNZIP_File(): #10 Unzip a File or Folder
    # When unzipping, add logic - if name.txt already exists, throw error - File has already been unzipped. Cannot create file with duplicate name OR if file name already exists, add a index after it.

    #USERS SHOULD NOT BE ABLE TO SELECT FOLDERS HERE!!
    
    Show_All_Paths()

    # print(globalITEMS.fileContentDict)
    # print(ZippedFileDict)
    while True:
        try:

            number = input("\nWhich Zip File would you like to Unzip?\n\n(ZIP Files End with _txt.zip)\n\n")
            selectedPath = globalITEMS.paths[int(number)-1]
         #    # note this should only work on FILES ending with _txt.zip..
            while "_txt.zip" not in selectedPath:
                
                print("\n!!!ERROR: That is not a ZIP FILE (Please select a ZIP FILE, not a ZIP Folder, or anything else)!!!")

                number = input("\nWhich File would you like to Unzip?\n\n(ZIP Files End with _txt.zip)\n\n")
                selectedPath = globalITEMS.paths[int(number)-1]



            UnzippedFile = selectedPath.replace("_txt.zip","_unzipped.txt")

         # # this takes Drive/File_txt.zip and turns it into Drive/File_unzipped.txt

         #    # OrigFileName = selectedPath.replace("_txt.zip",".txt") #this takes Drive/File_txt.zip to Drive/File.txt (which is what is in ZippedFileDict.) Issue is we need this to say Drive/File_unzipped.txt after moving it out of 

            globalITEMS.paths.append(UnzippedFile)

         #    #1. In ZippedFileDict, rename selectedPath and remove .txt and replace it with _unzipped.txt.
         #    #2. Rename affected KEY from orig file name to unzipped file name
         #    #3. Append the renamed key value pair to globalITEMS.fileContentDict
         #    #4. Delete renamed key (UnzippedFile) from from ZippedFileDict
         #    # if OrigFileName in globalITEMS.ZippedFileDict:
         #    #     globalITEMS.ZippedFileDict[UnzippedFile] = globalITEMS.ZippedFileDict.pop(OrigFileName) # Wow this worked!! now i just need to append this to globalITEMS.filecontentDict and delete it from zippedfiledict

            globalITEMS.fileContentDict.update({k:v for k,v in globalITEMS.ZippedFileDict.items() if UnzippedFile in k}) # PERFECT! IT WORKSS!!!!

            if UnzippedFile in globalITEMS.ZippedFileDict:
                del globalITEMS.ZippedFileDict[UnzippedFile]

         #    # print(globalITEMS.fileContentDict) 
         #    # print(ZippedFileDict)
            globalITEMS.paths.remove(selectedPath)
            Show_All_Paths()

         #    #size would be length of the file.
            break

        except IndexError:
            print("\n\n!!!ERROR: Path not found, please select from one of the existing Paths.!!!\n\n")

        except ValueError:
            print("\n\n!!!ERROR: Path not found, please select from one of the existing Paths.!!!\n\n")

        except KeyboardInterrupt:
            print("\n\nExiting...\n\n")
            sys.exit(0)

            #------------------------------------------------------------------------------


#------------------------------------------------------------------------------
#ZIP A FOLDER - DONE
#------------------------------------------------------------------------------
def Zip_Folder(): #9 Zip a file or Folder

    # list all the paths and select a folder or file to zip.

    # so when a folder is zipped, all .txt files in its path needs to undego the filezip process.

    #thinking out loud here... but suppose the folder was something like Drive/Folder/test/test.txt and we are zipping Drive/Folder. 

    #it should take Drive/Folder and put a .zip after it

    #HOWEVER it will also need to take EVERY PATH that has Drive/Folder/ in it and IF it is a .txt then do the Zip process for those files but do NOT append them into the path as they are supposed to be "hidden" that's just going to be used for the unzipping logic later so that the txt files will be the same but also, I should rename the txt files _unzipped.txt and put it in the ZippedFileDict.

    # then when it comes time to unzip the folder, simply call the ones that contain "_unzipped.txt" and move it from ZippedFileDict to globalITEMS.fileContentDict and delete the corrosponding key value in ZippedFileDict and voila!

    #0. Action is to Zip a folder and everything inside the folder.

    #1. Folder should be renamed to folder.zip.
    #2. Folders inside the folder (list comprehension) should also be renamed with a .zip after it.
    #3. For any and all text files inside there (list comprehension) rename it to end with _txt.zip
    #4. for all txt files it needs to copy those specific entries from the globalITEMS.fileContentDict dictionary (list comprehension) to ZippedFileDict
    # Show_All_Paths() # for testing

    Show_All_Paths()

    while True:

        try:

            number = input("\n\nWhich Folder would you like to Zip?\n\n(A Folder is anything that does NOT end with .zip or .txt.)\n\n")

            selectedPath = globalITEMS.paths[int(number)-1]

            while ".zip" in selectedPath or ".txt" in selectedPath:

                print("\n!!!ERROR: That is not a Folder!!!\n")

                number = input("\n\nWhich Folder would you like to Zip?\n\n(A Folder is anything that does NOT end with .zip or .txt.)\n\n")

                selectedPath = globalITEMS.paths[int(number)-1] #Drive/Folder

            ZippedFolder = selectedPath + ".zip" # appends.zip to the folder like Folder.zip

            targetFolders = selectedPath + "/" #Drive/Folder/

            unzippedFolder = selectedPath + "_Unzipped" #Drive/Folder_Unzipped

            # we need to also .zip anything that has the same path as selectedPath.perhaps we need to put it in a hidden list called HiddenPaths so that when the time comes we can move those back later when they're unzipped..

            foldername = re.split("/", selectedPath) # Drive, Folder
            foldername = foldername[-1] #Folder

            newfoldername =  foldername + "_Unzipped" # Folder_Unzipped

            globalITEMS.paths.append(ZippedFolder) #Drive/Folder.Zip

            globalITEMS.hiddenpaths = globalITEMS.hiddenpaths + [item for item in globalITEMS.paths if targetFolders in item]
            # i need to split out unzipped folder, take -1 which would be like test.txt then replace .txt with _unzipped.txt then i need to somehow port that bak in gobalitems.zippedfiledict.

            
                    # question is how do we get unzipped into the path of the zippedfile dictionary??


            globalITEMS.hiddenpaths = [i.replace(selectedPath, unzippedFolder) for i in globalITEMS.hiddenpaths] #(Drive/Folder > Drive/Folder_Unzipped)

            # print(globalITEMS.hiddenpaths)

            # no need to add .zip after them as later i will be adding _unzipped after them when i unzip and this is literally only here for it to be used for unzipping later. (though for unzipping i'd need to first say "for the ones WITHOUT TXT" rename that to _unzipped. for the ones WITH TXT, rename that to _unzipped.txt)

            # print(globalITEMS.hiddenpaths) # for testing

            # so for any paths with the targetfolder and with .txt, copy their dictionary keys to zippedFileDict. change .txt to be called _unzipped.txt if possible to do so now so its easier to move back when we unzip.

            globalITEMS.ZippedFileDictTEMP = {k:v for k,v in globalITEMS.fileContentDict.items() if selectedPath in k} # takes the selected path's folders and puts it in a temp dict


            # print(globalITEMS.ZippedFileDictTEMP)

            # for i in globalITEMS.ZippedFileDict:
            #     txt = ".txt"
            #     if txt in i:
            #         unzipped = i.replace(".txt","_unzipped.txt")

            txt = ".txt"
            zipfile = ".zip"

            for i in globalITEMS.ZippedFileDictTEMP:
                
                for txt in i:


                    globalITEMS.ZippedFileDict.update({key.replace(foldername, newfoldername): value for key, value in globalITEMS.ZippedFileDictTEMP.items()})


            # IF path contains .txt then do the following.
            for i in selectedPath: 
                for zipfile in i:

                    
                    globalITEMS.ZippedFileDict.update({key.replace(selectedPath, unzippedFolder).replace(".txt", "_unzipped.txt"): value for key, value in globalITEMS.ZippedFileDictTEMP.items()})

                     # takes from the temp dict and adds _unzipped for each of the txt file's paths.


            #globalITEMS.ZippedFileDict.update({key.replace(selectedPath, unzippedFolder).replace(selectedPath, unzippedFolder): value for key, value in globalITEMS.ZippedFileDictTEMP.items()}) 


            # globalITEMS.ZippedFileDictTEMP = {k:v for k,v in globalITEMS.ZippedFileDictTEMP if unzippedFolder not in k} # clears the temp dict. there should not be a need to use this temp dict outside of this def. so leaving it within the def.

            # print(globalITEMS.ZippedFileDictTEMP)

            # instead of selected path it is replace .txt with _unzipped.txt

            Show_All_Paths()

            break

        except IndexError:
            print("\n\n!!!ERROR: Path not found, please select from one of the existing Paths.!!!\n\n")

        except ValueError:
            print("\n\n!!!ERROR: Path not found, please select from one of the existing Paths.!!!\n\n")

        except KeyboardInterrupt:
            print("\n\nExiting...\n\n")
            sys.exit(0)

    #------------------------------------------------------------------------------



#------------------------------------------------------------------------------
#UNZIP A FOLDER
#------------------------------------------------------------------------------
def UNZIP_Folder():

    #0. Action is to unzip a folder and everything inside the folder.

    #1. Folder should be renamed from folder.zip to folder_unzipped - DONE

    #2. Folders inside the folder (list comprehension) should also be renamed with a _unzipped after it. (so for everything in hiddenpaths, add _unzipped after it) - DONE

    #3. for all txt files it needs to copy those specific entries from the ZippedFileDict dictionary (list comprehension) to globalITEMS.fileContentDict (but for every file its folder should be _unzipped.)
        
        #Drive/Folder/test3.txt': ['test3'] < how would we later parse out Drive/Folder, add _unzipped like so? Drive/Folder_unzipped/test3.txt'

        #use this https://note.nkmk.me/en/python-list-str-select-replace/

    #4. then we need to Delete the renamed keys from from ZippedFileDict

     # it's said that if you need to use Global, you should be using a CLASS - now that would fulfill the OO part of the OO File system and is probably easier to implement.

    Show_All_Paths()

    while True:
        try:

            number = input("\n\nWhich Zip Folder would you like to Unzip?\n\n(A ZIP Folder is any ZIP file that does not contain '_txt.zip' in it.)\n\n")

            # has to be a .zip folder - does not end with _txt.zip or includes ".zip"

            selectedPath = globalITEMS.paths[int(number)-1] 

            #Drive/Folder.zip
            while ".zip" not in selectedPath or "_txt.zip" in selectedPath:

                print("\n!!!ERROR: That is not a ZIP FOLDER!!! A ZIP Folder is any ZIP FILE that does not contain '_txt.zip' in it.")

                number = input("\n\nWhich Zip Folder would you like to Unzip?\n\n(A ZIP Folder is any ZIP file that does not contain '_txt.zip' in it.)\n\n")

                # has to be a .zip folder - does not end with _txt.zip or includes ".zip"

                selectedPath = globalITEMS.paths[int(number)-1]                 


            folderZIPtoUnzip = selectedPath.replace(".zip","_Unzipped")

            globalITEMS.paths.append(folderZIPtoUnzip) # ok this works fine, easy. onto the fancy stuff.

            #Example selected path is: Drive/Folder/Test.Zip and it has a zip file within it called Drive/Folder/Test/File.Zip

            ## this should be for ZIP FOLDERS only... what about ZIP Files within the ZIP folders??

            selectedPath_zip = selectedPath.replace(".zip", "")

            appendTOpath = [item for item in globalITEMS.test if selectedPath_zip in item]

            #for Folders:

            for i in appendTOpath:

                i_OLD = re.split("/", i)
                i_end = i_OLD[-1]
                del i_OLD[-1]

                i_OLD = "/".join(i_OLD)

                i_UPDATED = i_OLD + "_Unzipped/" + i_end

                globalITEMS.paths.append(i_UPDATED)

            foldertoUnzip_folderonly = selectedPath + "/"

            globalITEMS.paths.extend([item for item in globalITEMS.hiddenpaths if folderZIPtoUnzip in item]) # This Line ALMOST WORKS. it lumps everything from the hiddenpaths together instead of creates an individual item per item. Ok so changing .append to .extend works perfectly!!!

            globalITEMS.hiddenpaths = [item for item in globalITEMS.hiddenpaths if folderZIPtoUnzip not in item]

            globalITEMS.paths = [ele for ele in globalITEMS.paths if ele != []] # removes any blank items from the list.


            globalITEMS.fileContentDict.update({k:v for k,v in globalITEMS.ZippedFileDict.items() if folderZIPtoUnzip in k})

            globalITEMS.ZippedFileDict = ({k:v for k,v in globalITEMS.ZippedFileDict.items() if folderZIPtoUnzip not in k})

            #for i in paths that contain selected path, make a list of all the paths that have txt.zip. 
            # for all the ones that have txt.zip, update zippedfiledict - for those to zippedfiledict.replace (selectedpath, selectedpath + "_Unzipped")





            globalITEMS.paths.remove(selectedPath)
            
            Show_All_Paths()

            break

        except IndexError:
            print("\n\n!!!ERROR: Path not found, please select from one of the existing Paths.!!!\n\n")

        except ValueError:
            print("\n\n!!!ERROR: Path not found, please select from one of the existing Paths.!!!\n\n")

        except KeyboardInterrupt:
            print("\n\nExiting...\n\n")
            sys.exit(0)

    #[item for item in hiddenpaths if folderZIPtoUnzip in item] need to move this from zippedfile dict to filecontent dict

    # then we need to remove those items from zippedfiledict


#------------------------------------------------------------------------------


def ShowAttributes(): #11 Show all Files, Folders, and their Attributes
    
    #11 Show all Files, Folders, and their Attributes
    # this would show the attributes of all .txt files, .zip files, 
    #  showing all of the below:

    #Type – The type of the entity (one of the 4 type above).
    #Name - An alphanumeric string. Two entities with the same parent cannot have the same name. Similarly, two drives cannot have the same name.
    #Path – The concatenation of the names of the containing entities, from the drive down to and including the entity. The names are separated by ‘\’.
    #A text file has a property called Content which is a string. 
    #Size – an integer defined as follows:
    #For a text file – it is the length of its content.
    #For a drive or a folder, it is the sum of all sizes of the entities it contains.
    #For a zip file, it is one half of the sum of all sizes of the entities it contains.

    try:
        #------------------------------------------------------------------------------
        #this can be used for easier sorting of attributes probably.
        #------------------------------------------------------------------------------

        excludeTXTandZip = [".txt",".zip"]

        folders = [x for x in globalITEMS.paths if all(y not in x for y in excludeTXTandZip)]
        # Drive = [x for x in folders if "/" in x] # remove anything without /
        files = [x for x in globalITEMS.paths if ".txt" in x]
        zipFiles = [x for x in globalITEMS.paths if ".zip" in x]
        #------------------------------------------------------------------------------


        print("Here are all the ITEMS in your Drive:\n")

        # print("-----------------------------------------------------------")
        # Drive = [x for x in globalITEMS.paths if x == "Drive"]
        

        # print("Here is a list of your Drives:\n\nDrive")

        # # INSERT DRIVE SIZE INFO HERE.


        print("\nHere's the list of Attributes for your Folders (And your Drive):\n")

        for i in folders:
            # match folder names with names in filecontentdict to get txt files.
            # but what if folders have zip files and zip folders? hmmmm.......
            # Split out the drive but basically drive just adds up all the folders

            # take all folders and add a / after it.
            # ok it looks like zip file and zip folders need to be treated differently

            FileAndZipFileContent = i + "/" # For Zip FOLDERS and normal files this will work... but for Zip Files This will not.
            ZipFoldercontent = i + "_Unzipped/"

            FileWORDS = {k:v for k,v in globalITEMS.fileContentDict.items() if FileAndZipFileContent in k}
            ZIPFileWords = {k:v for k,v in globalITEMS.ZippedFileDict.items() if FileAndZipFileContent in k}
            ZipFoldercontent = {k:v for k,v in globalITEMS.ZippedFileDict.items() if ZipFoldercontent in k}
            
            # zip file words and zip folder content need to be /2
            # file words can be a direct len - after extracting the values only

            FileWORDScount = (list(FileWORDS.values()))
            ZIPFileWORDScount = (list(ZIPFileWords.values()))
            ZipFolderWORDcount = (list(ZipFoldercontent.values()))

            ALLZIPContent = ZIPFileWORDScount + ZipFolderWORDcount

            FileWORDScount2 = ",".join(FileWORDScount)

            ALLZIPContent = ",".join(ALLZIPContent)
            ALLZIPContent = ALLZIPContent.replace(",","")

            ALLFILECONTENTWORDCOUNT = (len(FileWORDScount2))

            ALLZIPContentWORDCOUNT = (int(len(ALLZIPContent))/2)

            TOTAL_FOLDER_SIZE = ALLFILECONTENTWORDCOUNT + ALLZIPContentWORDCOUNT

            FileName =  re.split("/", i)
            FileName = FileName[-1]

            if "Drive/" not in i:
                print("TYPE: DRIVE")
            else:
                print("TYPE: FOLDER")


            print("NAME:", FileName, "\nPATH:", i)


            if "Drive/" not in i:
                print("DRIVE SIZE:", TOTAL_FOLDER_SIZE ,"Characters", "\n\n")
            else:
                print("FOLDER SIZE:", TOTAL_FOLDER_SIZE ,"Characters", "\n\n")        

            # "\nFILE CONTENT:", FileWORDS,"\nWORDS:", FileWORDScount, "MERGED TEXT:", FileWORDScount2 ,"\nFile Content Count:" ,ALLFILECONTENTWORDCOUNT ,"Characters", "\n\nZIP FILE/FOLDER CONTENT:" , "\nKEY/VALUE: ",ZIPFileWords, "\nWORDS:", ZIPFileWORDScount, ZipFoldercontent, "\nMERGED ZIP CONTENT:", ALLZIPContent, "\nZippedFILE/FOLDER Count:" , ALLZIPContentWORDCOUNT ,"Characters" ,"\nTOTAL FOLDER SIZE:", 
                # what do we do when there is nothing in the folder? well it should show 0 characters if that is the case.


            # print("File Content Dict", globalITEMS.fileContentDict, "\n\nZipped File Dict", globalITEMS.ZippedFileDict)


        print("-------------------------------------------------")


        if len(files) == 0:
            print("\nHere's the list of Attributes for your Files:\n\nThere are No Files In This Drive.")
            print("\n-------------------------------------------------")
        else:
            print("\nHere's the list of Attributes for your Files:\n")
            for i in files:
                # i = path
                # updatedPath = re.split("/", selectedPath)
                FileContent = {k:v for k,v in globalITEMS.fileContentDict.items() if i in k}
                FileContent = str(list(FileContent.values())).replace("[","").replace("]","").replace("'","")

                FileSize = len(FileContent)

                FileName =  re.split("/", i)
                FileName = FileName[-1]

                # for i in files, pick out the correlating files from file content zip

                print("\nTYPE: File ", "\nNAME:", FileName, "\nPATH:", i, "\nFILE SIZE:", FileSize,"Characters", "\nFILE CONTENT:", FileContent ,"\n")
                # File Content Dict
            print("-------------------------------------------------")
        
        if len(zipFiles) == 0:
            print("\nHere's the list of Attributes for your Zip Files:\n\nThere are No Zip Files In This Drive.")
            print("\n-------------------------------------------------")

        else:
            print("\nHere's the list of Attributes for your Zip Files:\n")
            
            zfiles = [x for x in zipFiles if "_txt.zip" in x ]
            
            for i in zfiles:
                zfiledict = i.replace("_txt.zip", "_unzipped.txt")
                # print(i)
                # print(zfiledict)

                zfilecontent = {k:v for k,v in globalITEMS.ZippedFileDict.items() if zfiledict in k}

                zfilewords = (list(zfilecontent.values()))
                zfilewords = ",".join(zfilewords)
                zfilewords = zfilewords.replace(",","")

                zipfilewordcount = (int(len(zfilewords))/2)

                zFileName = i.split("/")

                zFileName = zFileName[-1]

                # print(zfilewords)

                # print(zipfilewordcount)

                print("\nTYPE: Zip File ", "\nNAME:", zFileName, "\nPATH:", i, "\nFILE SIZE:", zipfilewordcount, "Characters", "\nZIP FILE CONTENT:", zfilewords ,"\n")

            zfolders = [x for x in zipFiles if "_txt.zip" not in x]     
            
            zfolders = [x for x in zfolders if "unzipped" not in x]  

            zfolders = [x for x in zfolders if "Unzipped" not in x]  

            print(zfolders)

            for i in zfolders:

                zfolderdict = i.replace(".zip", "_Unzipped")

                zfoldercontent = {k:v for k,v in globalITEMS.ZippedFileDict.items() if zfolderdict in k}

                words = (list(zfoldercontent.values()))

                words = ",".join(words)

                words = words.replace(",","")

                # print(words)


                zipfolderwordcount = (int(len(words))/2)
                # print(i)
                # print(zipfolderwordcount=

                zFolderName = i.split("/")

                zFolderName = zFolderName[-1]

                print("\n\nTYPE: Zip File ", "\nNAME:", zFolderName, "\nPATH:", i, "\nFILE SIZE:", zipfolderwordcount, "Characters","\nZIP FOLDER CONTENT:",words ,"\n")
                

                # print(zfolderdict, zfoldercontent, str(zfoldercontent.values()))

                # >>> words = ["alpha","omega","up","down","over","under","purple","red","blue","green"]
                # >>> [len(i) for i in words]
                # [5, 5, 2, 4, 4, 5, 6, 3, 4, 5]

                # Then simply sum using a generator expression

                # >>> sum(len(i) for i in words)
                # 43


                # i represents each zip file or folder. so i's with _unzipped.txt will have to be treated like files

                # the idea here is to take the list of zip files, and for all the zip files, if it contains _txt.zip then it needs to replace _txt.zip with _unzipped.txt for the files then count the characters for that key value pair's values and then divides it by 2.

                # file = i.replace("_txt.zip", "_unzipped.txt")

                # folder = i.replace(".zip", "_Unzipped") so for folders, it should be ones that contain both _Unzipped and _unzipped.txt
                
                #for the folders, it should take the folders, replace.zip with _Unzipped then it should take everything in the zippedfiledict that contains that name - might need to make a separate list to call that out tho -  then it takes the length of the values of the key value pair and then divides it by 2.

            # print("ZippedFileDict:\n\n", globalITEMS.ZippedFileDict)

            print("\n-------------------------------------------------")

    except TypeError:
        print("\nHmmm.. looks like there's a special character somewhere in one of the dictionaries that is causing an issue... RIP... Try playing with the program again but don't use special characters as file/folder names or as content in files....\n\nExiting...")
        sys.exit(0)

#------------------------------------------------------------------------------

def MENU():

    while True:
        try:
            print('''
\n-------------------------------------------------
\nHere are all your options. 
\nWhat would you like to do (Please select a number):

-------------------------------------------------\n\n''')
            index = 1
            options_dup = globalITEMS.options.copy()
            for options_dup in options_dup:
                print(index,"-",options_dup)
                index +=1
            choice = input("\n\n")

            print("\nYou Selected: ",globalITEMS.options[int(choice)-1].upper(), "\n")

            while globalITEMS.options[int(choice)-1] not in globalITEMS.options:
                print("\n\n!!!ERROR: Option not found, please select from one of the existing Options!!!\n\n")


        except IndexError:
            print("\n\n!!!ERROR: Option not found, please select from one of the existing Options!!!\n\n")

        except ValueError:
            print("\n\n!!!ERROR: Option not found, please select from one of the existing Options!!!\n\n")

        except KeyboardInterrupt:
            print("\n\nExiting...\n\n")
            sys.exit(0)



        if choice == "1":
            CreateFolder()

        elif choice == "2":
            CreateFile()

        elif choice == "3":
            ReadFile()

        elif choice == "4":
            # override or append?
            while True:
                UserInput = input("\nSelect 1 to Append to a File. Select 2 to OVERWRITE a File.\n\n")


                if UserInput == "1":
                    AppendToFile()
                    break

                elif UserInput == "2":
                    OverwriteFile()
                    break

                else:
                    print("\n\n!!!ERROR: Option not found, please select from one of the existing Options!!!\n\n")
                    UserInput = input("\nSelect 1 to Append to a File. Select 2 to OVERWRITE a File.\n\n")



        elif choice == "5":
            MoveFolder()

        elif choice == "6":
            MoveFile()

        elif choice == "7":
            
            while True:
                UserInput = input("\nSelect 1 to DELETE a File. Select 2 to DELETE a Folder.\n\n")


                if UserInput == "1":
                    DeleteAFILE()
                    break

                elif UserInput == "2":
                    DeleteAFolder()
                    break

                else:
                    print("\n\n!!!ERROR: Option not found, please select from one of the existing Options!!!\n\n")
                    UserInput = input("\nSelect 1 to DELETE a File. Select 2 to DELETE a Folder.\n\n")


        elif choice == "8":
            Show_All_Paths()

        elif choice == "9":
            while True:
                UserInput = input("\nSelect 1 to Zip a FILE. Select 2 to Zip a FOLDER.\n\n")


                if UserInput == "1":
                    Zip_File()
                    break

                elif UserInput == "2":
                    Zip_Folder()
                    break

                else:
                    print("\n\n!!!ERROR: Option not found, please select from one of the existing Options!!!\n\n")
                    UserInput = input("\nSelect 1 to Zip a FILE. Select 2 to Zip a FOLDER.\n\n")

        elif choice == "10":
            
            while True:
                UserInput = input("\nSelect 1 to Unip a FILE. Select 2 to Unip a FOLDER.\n\n")


                if UserInput == "1":
                    UNZIP_File()
                    break

                elif UserInput == "2":
                    UNZIP_Folder()
                    break

                else:
                    print("\n\n!!!ERROR: Option not found, please select from one of the existing Options!!!\n\n")
                    UserInput = input("\nSelect 1 to Unzip a FILE. Select 2 to Unzip a FOLDER.\n\n")

        elif choice == "11":
            ShowAttributes()

        elif choice == "12":
            print("\n\nExiting...\n\n")
            sys.exit(0)




#------------------------------------------------------------------------------

def Bugs():
    print('''

\n---------------------------------------------
!!!NOTE:
---------------------------------------------

Here are the list of Bugs/Issues that I could not resolve with the time I had left due to time restrictions and/or technical debt - the Main functions all work fine though - especially individually:


1. Zip Files within Zip Folders show up with a size of 0.

2. Sporadic issue where if I zip a File then Zip a Folder that the Zip File is in then move the folder that this zip folder resides in, then unzip the folder, then unzip the file, sometimes the name gets messed up because I worked on this over the course of 2-3 months but when I first started, I forgot to write down exactly how the naming convention worked and by the time I noticed the wonkiness in the name I already had too much tech debt to fix it and learned a lot more along the way compared to when I first started and I didn't want to redo the whole thing.

3. Originally I left the Zip files there in the list of paths so you can unzip multiple times but then an issue arose where - because of how I had this oriented - (when Zip files get unzipped, the content moves from the ZippedFileContent dictionary to the FileContentDict Dictionary) it was making it show up on the Show Attributes List as 0.0. Another side issue would have been I had nothing in place to make sure that if a folder or file is unzipped, they can't be unzipped again in the same folder otherwise there'd be duplicates with the same name and with the issue with the show attributes I figured it'd be easier to just make it so once you unzip it, the zip folder disappears after all the instructions don't say you have to keep the zip folder (actually it doesnt even say you need to implement the zip folder but I figured I'd do it for completeness)

4. Yes, I noticed the instructions said "The names are separated by ‘\\’." but I forgot about that when I first started so I used / instead and didn't really want to change it.. since it is more about the concept than how it looks, I hope you don't mind.

5. I made it so there is only ever one Drive in this program at all times so you can't create another drive - as the instructions says full implementation is not required, I did not create the capability for multiple Drives.

With that aside, Let's begin!

---------------------------------------------\n\n

        ''')


# we will have a default path that goes: /Drive/Test_Folder/Test_file.txt
# User can add a Path after /Drive
# can add a folder after /Drive
# ok so the idea is to take user input on the path - must contain /Drive at bare minimum if it doesn't, then throw an error

#------------------------------------------------------------------------------
#MENU - probs should get its own def? just in case i need to call it again. but i shouldnt need to tho.. i should use a while loop for that.

#------------------------------------------------------------------------------
Bugs()
print("""
-----------------------------------------------------------


 \\-\\ \\-\\ /-/ /----|  |-|    /---]  /---\\  |--\\/--| /----]
  \\ \\-\\ \\ /  | =|    | |   | |     | | |  | /\\/\\ | |--]
   \\_/ \\_/   \\----|  |___|  \\---]  \\___/  |_|  |_| \\----]


 ...to your Drive!

-----------------------------------------------------------
    """)

# Show_All_Paths()



MENU()




#----------------------------------------------------------------------------------------------------------------------------

# For Testing:

# Zip_File()
# print("fileContentdict: ", globalITEMS.fileContentDict,"\n\n", "ZippedFileDict: ", globalITEMS.ZippedFileDict)
# UNZIP_File()
# print("fileContentdict: ", globalITEMS.fileContentDict,"\n\n", "ZippedFileDict: ", globalITEMS.ZippedFileDict)
# ReadFile()

#------------------------------------------------------------------------------

# Default options "Welcome to your Drive!"
# Here are all of your current Paths:
# <Show all current Paths>
# What would you like to do?

#------------------------------------------------------------------------------
#1. Create a Folder - Conceptually DONE
#------------------------------------------------------------------------------
    # Select from Existing Path
    # if Path does not Exist, Create path - path must have /Drive at the beginning though
    # Include a back button


#------------------------------------------------------------------------------
#2 Create a File - Conceptually DONE
#------------------------------------------------------------------------------

    # Select from Existing Path
    # if Path does not Exist, Create path - path must have /Drive at the beginning though
    # Include a back button
    # Ask if user wants to write something to put in the file whilst creating it. if not then it is just a blank txt file that they can append to.


#------------------------------------------------------------------------------
#3. Read a File - Conceptually DONE
#------------------------------------------------------------------------------
    # Include a back button
    # If file is blank, show a new line and below that note "There's nothing in this file."


#------------------------------------------------------------------------------
#4. Update a File - Conceptually DONE
#------------------------------------------------------------------------------

    #1.Append to File

        #-Take user input

    #2.Overwrite File

        #-Take user input
        #-Include a back button
        

#------------------------------------------------------------------------------
#5. Move a folder
#------------------------------------------------------------------------------

    # Display current list of Folders and their paths (simply throw an error unless user selects anything that does NOT include .txt or .zip)
    # 

#This below will probably be used for moving files and folders and deleting folders and all things in the folder cus we wil have to pick out the folder and everything that contains the path UP TO that folder. cus you could have multiple Folder1's but there will only ever be ONE Drive/Folder1 or Drive/Folder/Folder1. you could have a bunch of stuff after it but the fact remains that each of these file's paths will contain Drive/Folder/Folder1 at bare minimum so we need to call that out and delete it or move it.

    #For more advanced problems, use the dicionary method items(). For example to retrieve all
    #keys whose value is a vowel:
    #d = {0:'a', 1:'b', 2:'c', 3:'d', 4:'e'}
    #vowels = [key for key, item in d.items() if item in 'aeiou'] 

    # ^ https://blog.finxter.com/how-to-get-specific-elements-from-a-list/

#------------------------------------------------------------------------------
#6. Move a file
#------------------------------------------------------------------------------
    # Display current list of files and their paths (simply throw an error unless user selects anything with a .txt or .zip after it)
    # Include a back button
    # 


#------------------------------------------------------------------------------
#7. Delete a File or Folder  - Conceptually DONE
#------------------------------------------------------------------------------
    # IF It is a folder take the whole path and delete the thing after the last /. Example: /Drive/Folder1/test.txt <<< this would delete test.txt.
    # Include a back button
    # 
    #for folder ie deleting a path, use some kind of loop to figure out which ones have they folder (example: Drive/folder OR Drive/Folder1/Folder) in its string somewhere and if so delete that.


#------------------------------------------------------------------------------
#8. Show all Current Paths  - Conceptually DONE
#------------------------------------------------------------------------------
    # this shows all paths including ones that were created after the program starts. Since this is "in memory" if you close the program and come back it will only show the default.
    # Include a back button
    # 


#------------------------------------------------------------------------------
#9 Zip a file or Folder  - Conceptually DONE
#------------------------------------------------------------------------------
    # list all the paths and select a folder or file to zip.
    # Create a new item with the same name but with .zip and size being half the size of the original
    # When zipping a file, make a copy of it but store it in some other dictionary so that when you unzip it, it will take this copied version and put it back.
    # 


#------------------------------------------------------------------------------
#10 Unzip a File or Folder  - Conceptually DONE
#------------------------------------------------------------------------------
    # When unzipping, add logic - if name.txt already exists, throw error - File has already been unzipped. Cannot create file with duplicate name.
    #        


#------------------------------------------------------------------------------
#11 Show all Files, Folders, and their Attributes
#------------------------------------------------------------------------------
    # this would show the attributes of all .txt files, .zip files, 
    #showing all of the below:

    #Type – The type of the entity (one of the 4 type above).
        # If it contains .txt type = text File
        # If it contains .Zip type = Zip File
        # If it contains only Drive (no /'s') and nothing else, type = Drive
        # If it does NOT contain .txt and does NOT .zip AND contains Drive/ << The Drive/ is the differentiator between a Drive and a Folder cus a drive will not have Drive/ while a folder always will.

    #Name - An alphanumeric string. Two entities with the same parent cannot have the same name. Similarly, two drives cannot have the same name.
    #Path – The concatenation of the names of the containing entities, from the drive down to and including the entity. The names are separated by ‘\’.
    #A text file has a property called Content which is a string. 
    #Size – an integer defined as follows:
    #For a text file – it is the length of its content. - This should be the length of the characters!!!
    #For a drive or a folder, it is the sum of all sizes of the entities it contains. This should be the length of all the characters within the folder. (if fileA = 5 and FileB = 10 the Folder's length is 15 Characters)
    #For a zip file, it is one half of the sum of all sizes of the entities it contains.


#------------------------------------------------------------------------------
#12. Exit - Conceptually DONE
#------------------------------------------------------------------------------

    #breaks out of the program. to be implemented after the while loops are set up.



#------------------------------------------------------------------------------
# VERSIONS:
#------------------------------------------------------------------------------

# Version 1.0 - Make the program work...
# Version 2.0 - Add a GUI - shouldnt be TOOOO hard... after all, i have the defs so i can bind them to the keys easily.
# Version 3.0 - Revise the code based on Paul/Landon's Input (NOTE TO SELF - when doing OOP, the thing you are looking for that you didn't know how to make is probably a Factory Object.)

#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
#PROGRESS - Version 1.0
#------------------------------------------------------------------------------

# Finish the 12 key functionalities (Currenly done with 12/12 of them)
# Add in Exceptions and Errors
# Put all the pieces of the Program in while loop and add back buttons, etc.
# Test the program

    #------------------------------------------------------------------------------
    # Version 1.0 TESTING:
    #------------------------------------------------------------------------------

    #1. Create a Folder
        # make sure all the errors that are supposed to be thrown are thrown.

    #2 Create a File
        # make sure all the errors that are supposed to be thrown are thrown.

    #3. Read a File 
        # make sure all the errors that are supposed to be thrown are thrown.

    #4. Update a File
        # Append to a file
        # Overwrite a File
        # make sure all the errors that are supposed to be thrown are thrown.

    #5. Move a folder
        # make sure all the errors that are supposed to be thrown are thrown.

    #6. Move a file
        # make sure all the errors that are supposed to be thrown are thrown.

    #7. Delete a File or Folder
        # Delete a File
        # Delete a Folder
        # make sure all the errors that are supposed to be thrown are thrown.

    #8. Show all Current Paths- Conceptually DONE
        # make sure all the errors that are supposed to be thrown are thrown.

    #9 Zip a file or Folder
        # Zip a File
        # Zip a Folder 
        # make sure all the errors that are supposed to be thrown are thrown.

    #10 Unzip a File or Folder
        # Unzip a File
        # Unzip a Folder
        # make sure all the errors that are supposed to be thrown are thrown.

    #11 Show all Files, Folders, and their Attributes
        # make sure all the errors that are supposed to be thrown are thrown.

    #12. Exit
        # make sure all the errors that are supposed to be thrown are thrown.


#------------------------------------------------------------------------------
#PROGRESS - Version 2.0
#------------------------------------------------------------------------------

# Create GUI for the 12 key functionalities (Currenly done with 0/12 of them)
# Create GUI Exceptions and Errors
# Make sure all the back buttons, etc work as intended.
# Test the program

    #------------------------------------------------------------------------------
    # Version 2.0 TESTING:
    #------------------------------------------------------------------------------

    #1. Create a Folder
        # make sure all the errors that are supposed to be thrown are thrown.

    #2 Create a File
        # make sure all the errors that are supposed to be thrown are thrown.

    #3. Read a File 
        # make sure all the errors that are supposed to be thrown are thrown.

    #4. Update a File
        # Append to a file
        # Overwrite a File
        # make sure all the errors that are supposed to be thrown are thrown.

    #5. Move a folder
        # make sure all the errors that are supposed to be thrown are thrown.

    #6. Move a file
        # make sure all the errors that are supposed to be thrown are thrown.

    #7. Delete a File or Folder
        # Delete a File
        # Delete a Folder
        # make sure all the errors that are supposed to be thrown are thrown.

    #8. Show all Current Paths- Conceptually DONE
        # make sure all the errors that are supposed to be thrown are thrown.

    #9 Zip a file or Folder
        # Zip a File
        # Zip a Folder 
        # make sure all the errors that are supposed to be thrown are thrown.

    #10 Unzip a File or Folder
        # Unzip a File
        # Unzip a Folder
        # make sure all the errors that are supposed to be thrown are thrown.

    #11 Show all Files, Folders, and their Attributes
        # make sure all the errors that are supposed to be thrown are thrown.

    #12. Exit
        # make sure all the errors that are supposed to be thrown are thrown.

