import argparse
import yaml
from pathlib import Path
import pandas as pd
import sys

# Add project root to Python path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

def add_run_args(parser, multiprocess=True):
    """
    Run command args
    """
    parser.add_argument(
        "-c",
        "--configs_dir",
        type=str,
        metavar="PATH",
        help="path to configs dir",
    )
def run(args):
    """
    Implements the 'run' sub-command, which
    runs network builder using the specified
    configs.
    """

    pd.options.display.float_format = "{:.4f}".format
    #mp.freeze_support()
    run_pipeline(args.configs_dir)
    sys.exit()

def run_pipeline(configs_dir):
    """
    Run command
    """

    from survey_to_activitysim.utils.survey_data import SurveyData
    from survey_to_activitysim.steps.preprocess_persons import process_persons
    
    config = yaml.safe_load(open(Path(f"{configs_dir}/config.yaml")))

    survey_data = SurveyData(config["survey_year"])
    survey_data.persons = process_persons(survey_data.persons)

    print('done')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    add_run_args(parser)
    args = parser.parse_args()
    sys.exit(run(args))