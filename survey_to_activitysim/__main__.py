import sys
import os

 
def main():
    # clean up message formatting
    if sys.argv and sys.argv[0].endswith("__main__.py"):
        sys.argv[0] = "survey_to_activitysim"

    print("Running survey-to-activitysim...")

    from .cli.main import main

    main()


if __name__ == "__main__":
    main()