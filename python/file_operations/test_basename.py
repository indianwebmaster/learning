import os


class CUtilityFuncs:
    @staticmethod
    def get_basename(input_filepath):
        """
        :param input_filepath:
        :return:
        """
        if "\\" in input_filepath:
            delim = "\\"
        elif "/" in input_filepath:
            delim = "/"
        else:
            # No delimiter, must be just the filepath
            return (".", input_filepath)

        f_splitpath = input_filepath.split(delim)

        tail = f_splitpath.pop(-1)
        if not tail:
            tail = f_splitpath.pop(-1)

        if f_splitpath[0] == "":
            parent_path = ""
        else:
            parent_path = "."

        i=0
        for f in f_splitpath:
            if f != "":
                parent_path += (delim + f)
            i += 1

        return (parent_path,tail)

fpaths = ['a/b/c/', 'a/b/c', '\\a\\b\\c', '\\a\\b\\c\\', 'a\\b\\c', 'a/b/../../a/b/c/', 'a/b/../../a/b/c']
fpaths = ['c', '/a/b/c', 'a/b/c', '\\a\\b\\c', 'a\\b\\c']
for fpath in fpaths:
    print (fpath,CUtilityFuncs.get_basename(fpath))
