"""
pdflib.make allows pretty printing of PDFs from Jupyter notebooks

"""

import os


def make(notebook_name, classname="article"):
    """

    converts a notebook to a nicely formatted PDF for distribution

    Args:
        notebook_name (string): full path to location of notebook
        classname (str, optional): latex class.
    """

    original_dir = os.getcwd()

    notebook_dir, notebook_name = os.path.split(notebook_name)
    if not ".ipynb" in notebook_name:
        notebook_name = notebook_name + ".ipynb"
    notebook_name = os.path.join(notebook_dir, notebook_name)

    pdf_dir = os.path.join(os.path.dirname(notebook_dir), 'pdfs')

    # convert to latex using jupyter notebook
    # subprocess doesn't work for inscrutable reasons and
    # I can't figure out why

    eval_str = 'jupyter nbconvert --to latex --no-input --output-dir '
    eval_str = eval_str + pdf_dir
    eval_str = eval_str + ' ' + notebook_name
    stderr = os.system(eval_str)

    # clean up title
    in_file = os.path.join(
        pdf_dir, os.path.basename(notebook_name).replace('ipynb', 'tex')
    )
    out_file = in_file + ".temp"
    out_file = open(out_file, 'a+')

    lines = tuple(open(in_file, 'r'))
    for line in lines:

        if r"\title" in line:
            line = line.replace("\_", " ")
            line = line.replace('}', '{')
            strings = line.split('{')
            line = strings[0] + "{" + strings[1].title() + " }"

        if "autoreload" in line:
            line = "\n"

        if r"{ \hspace*{\fill} \\}" in line:
            line = "\n"

        # use includegraphics to display graphics objects
        if "adjustimage{" in line:
            line = line.replace(
                r"\adjustimage{max size={0.9\linewidth}{0.9\paperheight}}",
                r"\hspace*{-1.5cm}\includegraphics[width=1.1\textwidth]",
            )

        # switch to inscopix cls
        if "documentclass" in line:
            line = line.replace('article', classname)

        if "NbConvertApp" in line:
            break

        out_file.write(line)

    # need to insert some extra things in here
    out_file.write('\n \end{Verbatim} \n')  # because this has been started already

    out_file.write("\subsection{Reproducibility information}\n")
    out_file.write(
        "This section contains information on how to reproduce this document."
        " This document is generated from a Jupyter notebook that lives in this"
        " repository:\n"
    )

    out_file.write('\n')
    out_file.write(r'\begin{Verbatim}[commandchars=\\\{\}]')
    out_file.write('\n')

    txt = os.popen('git remote -v').read()
    txt = txt.split('\n')
    out_file.write(txt[0])

    out_file.write('\n \end{Verbatim} \n')

    out_file.write('check out this git hash:\n')

    txt = os.popen('git rev-parse HEAD').read()
    out_file.write('\n')
    out_file.write(r'\begin{Verbatim}[commandchars=\\\{\}]')
    out_file.write('\n')
    out_file.write(txt)
    out_file.write('\n \end{Verbatim} \n')
    out_file.write('\n \end{document} \n')

    out_file.close()

    # replace .tex with modified .tex
    os.remove(in_file)
    os.rename(in_file + '.temp', in_file)

    # convert to PDF
    os.chdir(pdf_dir)

    try:
        os.system('pdflatex ' + in_file)
    except:
        os.chdir(original_dir)

    # clean up
    _clean(pdf_dir)


def _clean(folder_name):
    """
    Small utlity function that cleans up the intermediate products
    generated by tex during PDF construction

    Args:
        folder_name (string): location of folder with files to be deleted
    """
    files = os.listdir(folder_name)

    for item in files:
        if item.endswith(".aux"):
            os.remove(os.path.join(folder_name, item))
        if item.endswith(".log"):
            os.remove(os.path.join(folder_name, item))
        if item.endswith(".out"):
            os.remove(os.path.join(folder_name, item))
