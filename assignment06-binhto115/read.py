from typing import List, Optional

def readPPM(path: str) -> Optional[List[List[List[int]]]]:
    '''Attempts to read the .ppm file at the given path and return it as a list'''

    # Open the file
    try:
        f = open(path, 'r')

    except FileNotFoundError:
        print("readPPM could not find the file!")
        return None
    except:
        print("readPPM had an unexpected error!")
        return None
    else:

        f.readline() # Skip "P3" line

        # Read the header information
        width, height, max_color = None, None, None
        while (width == None and height == None):
            header = f.readline()
            if header[0] == "#": # Encountered a comment
                continue
            else: # Encountered the values
                try:
                    fields = header.strip().split()
                    width = int(fields[0])
                    height = int(fields[1])

                    # Get the maximum value from the next line
                    header = f.readline()
                    header = header.strip()

                    max_color = int(header)
                except:
                    print("readPPM failed to read header")
                    return None

        # Read in the pixel data
        data = []
        for h in range(height):
            row = []
            for w in range(width):
                pixel_data = []
                for i in range(3):
                    try:
                        value = int(float(f.readline().strip()))
                    except:
                        print("readPPM failed to read pixel data")
                    else:
                        pixel_data.append(value)
                row.append(pixel_data)
            data.append(row)
        f.close()

        return data
