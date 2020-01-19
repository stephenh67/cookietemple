import click

from cookietemple.create.create_config import (TEMPLATE_STRUCT)


def common_python_options():
    """
    TODO
    """
    TEMPLATE_STRUCT['pypi_username'] = click.prompt('Please enter your pipy username (if you have one)',
                                                    type=str,
                                                    default='homersimpson')
    TEMPLATE_STRUCT['command_line_interface'] = click.prompt('Choose a command line library',
                                                             type=click.Choice(['Click', 'Argparse', 'No command-line interface']),
                                                             default='Click')
    testing_library = click.prompt('Please choose whether pytest or unittest should be used as the testing library [pytest, unittest]',
                                   type=click.Choice(['pytest', 'unittest']),
                                   default='pytest')
    if testing_library == 'pytest':
        TEMPLATE_STRUCT['use_pytest'] = 'y'
    else:
        TEMPLATE_STRUCT['use_pytest'] = 'n'
    use_pypi_deployment_with_travis = click.prompt('Please choose whether or not your project should be automatically deployed on pypi via travis [y, n]',
                                                   type=bool,
                                                   default='Yes')
    if use_pypi_deployment_with_travis:
        TEMPLATE_STRUCT['use_pypi_deployment_with_travis'] = 'y'
    else:
        TEMPLATE_STRUCT['use_pypi_deployment_with_travis'] = 'n'