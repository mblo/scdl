#!/usr/bin/env python3

from scdl import scdl
import glob, os

"""
simple tests and maintenance scripts
"""

def fileNameTest():
    names = ["das ist ein test", "mit Leerzeichen am Ende   ",
    "mit falschen zeichen #+ä-.,?=? im Namen", "mit --_-- erlaubten zeichen",
    "mit Punkten", " mit Leerzeichen Vorne und Hinten . ", "  ", "mit Umlauten äüö ÄÜÖ ß"]

    for n in names:
        print("org: \"{0}\"\tchecked: \"{1}\"".format(n, scdl.strToFilename(n)))

    print("test longest filename: {0} chars".format(len(scdl.strToFilename("a"*4000))))
#fileNameTest()


def migrateFilesInFolder(folder):
    print("## migrateFilesInFolder '{0}'".format(folder))
    mapping = dict()
    for f in glob.glob(os.path.join(folder, "*.mp3")):
        filename = os.path.splitext(os.path.basename(f))
        converted = scdl.strToFilename(filename[0])
        mapping[filename] = converted
        #print("{0} -> {1}".format(f, converted + filename[1]))
    newNames = set()
    for k in mapping:
        assert(mapping[k] not in newNames)
        if (k[0] != mapping[k]):
            if os.path.exists(os.path.join(folder, mapping[k]+k[1])):
                print("FAILED - path exists \"{0}\"".format(mapping[k]))
                return
        else:
            #print("filename does not change for \"{0}\"".format(k[0]))
            pass
        newNames.add(mapping[k])
    # apply the mapping
    changed = 0
    notChanged = 0
    for k in mapping:
        if (k[0] != mapping[k]):
            print("#### you have to activate the file renameing")
            #os.rename(os.path.join(folder, k[0]+k[1]), os.path.join(folder, mapping[k]+k[1]))
            changed += 1
        else:
            notChanged += 1
    print("changed/ok {0}/{1}".format(changed, notChanged))

#migrateFilesInFolder("path to you old filenames")
