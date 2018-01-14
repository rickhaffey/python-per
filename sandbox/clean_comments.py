line = "# Return the number of non-overlapping occurrences of substring sub in the range [start, end]. Optional arguments start and end are interpreted as in slice notation."  # noqa


def reformat_line(line):
    if line.startswith("#"):
        return reformat_comment(line)
    else:
        return [line]


def reformat_comment(comment):
    if len(comment) < 80:
        return [comment]
    else:
        words = comment.split(' ')
        line = ""
        result = []

        for word in words:
            if len(line + " " + word) < 80:
                line += " " + word
            else:
                result.append(line)
                line = "# " + word

        # add on the last line generated
        result.append(line.lstrip())
        return result


def main():
    for line in open('../chapter03.strings.py', 'r'):
        for l in reformat_line(line.rstrip()):
            print(l)


if __name__ == '__main__':
    main()
