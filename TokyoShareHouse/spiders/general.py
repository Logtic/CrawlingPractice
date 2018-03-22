import os


#createProjectDir(directory) : make Directory
#createDataFiles(projectName, url) : make projectfile.txt
#   and add url
#fileToList(fileName) : get fileName and lists urls
#listToFiles(links, file) : lists file's urls and append links
#appendToFile(path, data) : open path and append data in path file


def createProjectDir(directory):
    if not os.path.exists(directory):
        print('Creating project : ' + directory)
        os.makedirs(directory)

def createDataFiles(projectName, url):
    getUrlList = projectName + '/urlList.txt'
    if not os.path.isfile(getUrlList):
        writeFile(getUrlList, url)

def writeFile(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()

def appendToFile(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')

def deleteFileContents(path):
    with open(path, 'w'):
        pass

def fileToList(fileName):
    results = list()
    with open(fileName, 'rt') as f:
        for line in f:
            results.append(line.replace('\n', ''))
    return results

def listToFile(links, file):
    deleteFileContents(file)
    for link in sorted(links):
        appendToFile(file, link)












