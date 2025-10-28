import pandera.pandas as pa
from survey_to_activitysim.utils.data_models import PersonSchema

def convert_person_age(df):
    age_map = {
        "Under 5 years old": 2,
        "5-11 years": 8,
        "12-15 years": 14,
        "16-17 years": 17,
        "18-24 years": 21,
        "25-34 years": 30,
        "35-44 years": 40,
        "45-54 years": 50,
        "55-64 years": 60,
        "65-74 years": 70,
        "75-84 years": 80,
        "85 years or older": 85,
    }
    df["age"] = df["age"].replace(age_map).astype(int)
    return df


def create_student_column(df):
    student_map = {
        "No, not a student": 0,
        "Part-time student": 2,
        "Full-time student": 1,
        "Part-time student, currently attending some or all classes in-person": 2,
        "Part-time student, ONLY online classes": 0,
        "Full-time student, currently attending some or all classes in-person": 1,
        "Full-time student, ONLY online classes": 0,
        "Missing Response": 0,
    }

    df["student"] = df["adult_student"].map(student_map).astype(int)
    return df

def convert_gender_column(df):
    gender_map = {
        "Boy/Man (cisgender or transgender)": 1,
        "Girl/Woman (cisgender or transgender)": 2,
        "Non-binary/Something else fits better": 9,
        "Non-Binary": 9,
        "Another": 9,
        "Missing Response": 9,
        "Prefer not to answer": 9,
    }

    df["sex"] = df["gender"].map(gender_map).astype(int)
    return df

def create_race_column(df):
    race_map = {
        "White Only": 1,
        "African American": 2,
        "Asian": 3,
        "Other": 4,
        "Hispanic": 6,
        "Child": 8,
        "Missing": 0,
    }

    df["race"] = df["race_category"].map(race_map).astype(int)
    return df

person_schema = PersonSchema.to_schema()

@pa.check_output(person_schema)
def preprocessor(df):
    # Convert age to numeric:
    df = convert_person_age(df)

    # Create student column:
    df = create_student_column(df)

    # Convert to sex column:
    df = convert_gender_column(df)

    #df = create_race_column(df)

    # ptype: 1 if employed full time, 0 otherwise
    df.loc[df["employment"] == "Employed full time (35+ hours/week, paid)", "ptype"] = 1

    # ptype: 2 if employed part time or self-employed, 0 otherwise
    df.loc[
        df["employment"].isin(
            ["Employed part time (fewer than 35 hours/week, paid)", "Self-employed"]
        ),
        "ptype",
    ] = 2

    # ptype: 4 Non working adult age < 65
    df.loc[
        (df["jobs_count"] == "Missing: Skip Logic")
        & (df["age"] < 65)
        & (df["student"] == 0),
        "ptype",
    ] = 4

    df["ptype"] = df["ptype"].fillna(0).astype(int)

    return df[list(person_schema.columns.keys())]
    
def process_persons(df):
    """
    Process survey data through preprocessing pipeline
    
    Args:
        df: DataFrame containing raw survey data
    
    Returns:
        Processed DataFrame
    """
    return preprocessor(df)