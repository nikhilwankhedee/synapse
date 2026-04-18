import os


def find_entrypoints(directory):

    entrypoints = []

    for root, _, files in os.walk(directory):

        for file in files:

            if file == "__main__.py":

                entrypoints.append(os.path.join(root, file))

            if file.endswith(".py"):

                path = os.path.join(root, file)

                try:

                    with open(path, errors="ignore") as f:

                        text = f.read()

                        if "if __name__ == '__main__'" in text:

                            entrypoints.append(path)

                except:
                    pass

    return entrypoints
