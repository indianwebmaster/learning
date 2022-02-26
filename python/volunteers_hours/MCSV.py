class MCSV:
    csvFilename = ""
    csvFileLoaded = False
    csvFileContent = []
    """
    :string filename
    :boolean skip_heading. If True, returned content will not contain any heading lines
    """

    def load_file(self, filename, skip_heading=False):
        if not self.csvFileLoaded:
            self.csvFilename = filename
            with open(filename) as f:
                self.csvFileContent = f.readlines()
            f.close()

            # Strip any whitespace line \n from the end of each line
            self.csvFileContent = [x.strip() for x in self.csvFileContent]
            if skip_heading:
                content_copy = []
                for one_line in self.csvFileContent:
                    if one_line[0] != "#":
                        content_copy.append(one_line)
                self.csvFileContent = content_copy

            self.csvFileLoaded = True

        return self.csvFileContent


if __name__ == "__main__":
    import Defines

    mcsv = MCSV()
    content = mcsv.load_file(Defines.Defines.volunteers_hours_filepath)
    for aline in content:
        print(aline)
