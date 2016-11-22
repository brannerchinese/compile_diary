## Python code for assembling and compiling LaTeX diary

### Actual diary

My actual diary is not found in a public repository. It was originally a single, long LaTeX file. I wrote a script to break it into sections, each section one diary entry, in the interest of the recognized good of modularity. Then I wrote the code in the present repository to compile either just the newest sections (because things sometimes go wrong in LaTeX and you would like to see what you've done) or to reassemble the parts into a whole diary.

### Organization and set-up

This program runs in both Python 2 and 3, though there are no dependencies and hence no `requirements.txt` file. 

Directory `head_and_tail_matter` contain two necessary files: `preamble.tex` and `file_end.tex`; `head_text_matter_can_be_edited.tex` can be empty.

Directory `sections` contains individual diary entries, whose filenames will be loaded in the order they are returned by Python's `os.listdir` (dictionary order on my system).

Directory `diary_graphics` is the "graphicspath"; it contains any graphics files needed in the text. To include an image, use the macro `\gr{filename}{n}` where `filename` is the name of the image file in `diary_graphics` and `n` is the `stylebox` ratio. There are also other graphics macros `grw` and `grh`, and still other macros for my own purposes — don't worry about them.

### Compilation of whole diary

To compile and view the whole diary:

```bash
python compile_latex_diary.py
```

The filename `diary_composite.tex` is used, and prior versions are overwritten. The file must be compiled twice in order to produce a table of contents.

### Compilation of individual sections alone

To compile and view only a selection of those sections modified in the past `n` hours, use:

```bash
python compile_sample_diary_entries.py n
```

where `n` is the maximum age in hours that is to be included. This second program is useful for examining the typesetting of individual entries without having to compile the whole diary. The filename `diary_excerpts_5_sections.tex` is used, where `5` here indicates that five sections were included.


[end]
