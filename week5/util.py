import csv
import library

def read_csv(filename):
    """
    Given the name of a file with data from the Hawaii State Library
    system, load the data into a list of instances of the Library
    class.

    Args:
        filename (str): the name of the file

    Returns (List[Library]): a list of instances of the Library
    class, one per branch.
    """    
    libs = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            libs.append(library.Library(row["Island"], 
                                        row["LIBRARY"], 
                                        int(row["REFERENCE"]), 
                                        int(row["BOOK"]),
                                        int(row["MICROFORM"])))
    return libs

# The data set to use for testing.
HI_LCS_2011 = read_csv("data/libraries-collection-statistics-2011-csv.csv")

