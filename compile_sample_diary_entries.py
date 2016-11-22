#!/bin/usr/python
# 20161121

import os
import subprocess
import sys
import time


"""Compile LaTeX diary, including table of contents, from selected sections."""

def assemble_whole(threshold, filename='diary_excerpts_{}_sections.tex'):
    """Combine file_start.tex and file_end.tex, w/all content between them"""

    # Start output file.
    with open(os.path.join('head_and_tail_matter', 'preamble.tex'), 'r') as f:
        whole = [f.read()]

    # Get all sections from `sections` directory.
    sections = os.listdir('sections')
    current_time = time.time()
    earliest_time = current_time - threshold
    mtimes = [(os.stat(os.path.join('sections', section)).st_mtime, section)
            for section in sections]
    mtimes = [item for item in mtimes if item[0] > earliest_time]
    print('items: {}'.format(len(mtimes)))
    for item in mtimes:
        if item[1] == '.DS_Store':
            continue
        else:#if item[0] > earliest_time:
            print(item)
            whole.append('\input{{\inputpath {}}}\n'.format(item[1]))

    # Finish file with `file_end.tex`
    with open(os.path.join('head_and_tail_matter', 'file_end.tex'), 'r') as f:
        whole.append(f.read())
    whole = '\n\n'.join(whole)

    # Write finished file.
    with open(filename.format(str(len(mtimes))), 'w') as f:
        f.write(whole)
    return len(mtimes)

def compile_latex(filename='diary_excerpts_{}_sections.tex'):
    threshold = 24
    if len(sys.argv) > 1:
        threshold = float(sys.argv[1])
    print('Time threshold is {} hours ago.'.format(threshold))
    threshold = threshold * 60 * 60 # We need it in seconds.
    mtimes = assemble_whole(threshold)
    print('File assembled, with {} sections.'.format(mtimes))
    filename = filename.format(str(mtimes))
    print('Filename: {}'.format(filename))
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
