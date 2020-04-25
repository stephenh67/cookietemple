import os

from cookietemple.lint.TemplateLinter import TemplateLinter, files_exist_linting

CWD = os.getcwd()


class PubLatexLint(TemplateLinter):
    def __init__(self, path):
        super().__init__(path)

    def lint(self, label):
        methods = ['latex_template_files_exist']
        super().lint_project(self, methods, label=label)

    def latex_template_files_exist(self) -> None:
        """
        Checks a given pipeline directory for required files.
        Iterates through the templates's directory content and checkmarks files for presence.
        Files that **must** be present::
            'Dockerfile',
            'Makefile',
            'thesis.tex',
            'thesis-info.tex',
            'cookietemple.cfg',
            '.cookietemple.yml'
        Files that *should* be present::
            'References/references.bib',
            'Variables.ini',
            'glyphtounicode.tex',
        Files that *must not* be present::
            none
        Files that *should not* be present::
            '.travis.yml'
        """

        # NB: Should all be files, not directories
        # List of lists. Passes if any of the files in the sublist are found.
        files_fail = [
            ['Dockerfile'],
            ['Makefile'],
            ['thesis.tex'],
            ['thesis-info.tex'],
            ['cookietemple.cfg'],
            ['.cookietemple.yml'],
        ]
        files_warn = [
            [os.path.join('References', 'references.bib')],
            ['Variables.ini'],
            ['glyphtounicode.tex'],
        ]

        # List of strings. Fails / warns if any of the strings exist.
        files_fail_ifexists = [
        ]
        files_warn_ifexists = [
            '.travis.yml'
        ]

        files_exist_linting(self, files_fail, files_fail_ifexists, files_warn, files_warn_ifexists)