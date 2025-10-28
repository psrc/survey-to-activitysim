import sys

from survey_to_activitysim import __version__, __doc__


def main():
    
    from survey_to_activitysim.cli import CLI, run

    run_pipeline = CLI(version=__version__, description=__doc__)
    run.add_subcommand(
        name="run",
        args_func=run.add_run_args,
        exec_func=run.run,
        description=run.run.__doc__,
    )

    sys.exit(run_pipeline.execute())

