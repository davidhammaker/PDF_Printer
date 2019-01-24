# PDF Printer

A simple Python script for printing multiple PDF files at once.

## About

This tool will search for PDF files within a modifiable list of directories, print out the files on a standard paper-and-ink printer, then isolate all printed files in a new directory.

## Limitations

This tool currently only works on Windows.

## Usage

Clone this repository. Open "paths.txt" and add the full paths to all directories containing PDF files you want to print. The format of these paths should resemble the following:

```
C:/Path/to/Directory/
```

* At this time, the trailing `/` at the end of the path is required.

Once you have added all directory paths to "paths.txt", you may run the code from a shell prompt (like [GitBash](https://git-scm.com/downloads)):

```
$ python pdf_printer.py <path_to_'paths.txt'>
```
* The direct path to "paths.txt" is required.

All PDF files will print. For each directory listed in "paths.txt", a new directory called "printed_<today's date>" will be created, and PDF files within the current directory will be moved from the current directory to the working directory. There is a 10 second delay between printing the files and moving the files, so that the files are not moved before they are printed. This 10 second delay occurs once for each path listed in "paths.txt" that contains PDFs, so keep that in mind when adding paths.

## Copyright
© David J. Hammaker 2019
