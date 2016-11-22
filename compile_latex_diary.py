#!/bin/usr/python
# 20161121

import os
import subprocess

"""Compile LaTeX diary, including table of contents, from discrete sections."""

def assemble_whole():
    """Combine file_start.tex and file_end.tex, w/all content between them"""

    # Start output file.
    with open(os.path.join('head_and_tail_matter', 'preamble.tex'), 'r') as f:
        whole = [f.read()]

    # Add "head text matter" (post-preamble).
    with open(os.path.join('head_and_tail_matter',
            'head_text_matter_can_be_edited.tex'), 'r') as f:
        whole.append(f.read())

    # Get all sections from `sections` directory.
    sections = os.listdir('sections')
    for section in sections:
        if section == '.DS_Store':
            continue
        else:
            whole.append('\input{{\inputpath {}}}\n'.format(section))

    # Finish file with `file_end.tex`
    with open(os.path.join('head_and_tail_matter', 'file_end.tex'), 'r') as f:
        whole.append(f.read())
    whole = '\n\n'.join(whole)

    # Write finished file.
    with open('diary_composite.tex', 'w') as f:
        f.write(whole)
    return len(sections) - 1

def compile_latex():
    filename = 'diary_composite.tex'
    sections = assemble_whole()
    print('File assembled, with {} sections.'.format(sections))
    print('There will now be two compilation passes.')
    subprocess.check_output(['xelatex', filename])
    print('First run completed.')
    subprocess.check_output(['xelatex', filename])
    print('Second run completed.')
    print('Now opening finished file.')
    subprocess.check_output(['open', filename.replace('.tex', '.pdf')])


def main():
    compile_latex()

if __name__ == '__main__':
    main()
