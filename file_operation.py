# myfile = open("test.txt", "w")
# myfile.write("My first file written from Python\n")
# myfile.write("---------------------------------\n")
# myfile.write("Hello, world!\n")
# myfile.close

# mynewhandle = open("test.txt", "r")
# while True:
#     theline = mynewhandle.readline()
#     if len(theline) == 0:
#         break
#     print(theline, end = "")

# mynewhandle.close()

# import urllib.request

# url = "http://xml.resource.org/public/rfc/txt/rfc793.txt"
# destination_filename = "rfc793.txt"

# urllib.request.urlretrieve(url, destination_filename)

def filter(oldfile, newfile):
    infile = open(oldfile, "r")
    outfile = open(newfile, "w")
    while True:
        text = infile.readline()
        if len(text) == 0:
            break
        if text[0] == "#":
            continue

        outfile.write(text)
    infile.close()
    outfile.close()

#filter(test.txt, test1.txt)

def reverse_line_file(oldfile, newfile):
    f = open(oldfile, "r")
    xs = f.readlines()
    f.close()
    xss = []
    length = len(xs)
    for i in range(0, length):
        xss += xs[length - 1 - i]
    g = open(newfile, "w")
    for v in xss:
        g.write(v)
    g.close()
#reverse_line_file("test.txt", "test1.txt")

def print_line_contain_substring(oldfile, substring):
    f = open(oldfile, "r")
    while True:
        text = f.readline()
        if len(text) == 0:
            break
        if substring in text:
            print(text, end = "")
    f.close()
#print_line_contain_substring("test.txt", "snake")


def copy_with_line_number(oldfile, newfile):
    f = open(oldfile, "r")
    outfile = open(newfile, "w")
    num = 0
    while True:
        text = f.readline()
        num += 1
        if len(text) == 0:
            break
        outfile.write("{0:04d}".format(num) + " " + text)
    f.close()
    outfile.close()

#copy_with_line_number("test.txt", "test1.txt")

def remove_line_number(oldfile, newfile):
    f = open(oldfile, "r")
    outfile = open(newfile, "w")
    while True:
        text = f.readline()
        if len(text) == 0:
            break
        text1 = text[5:]
        outfile.write(text1)
    f.close()
    outfile.close()

remove_line_number("test1.txt", "test2.txt")

























