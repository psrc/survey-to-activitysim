import psrcelmerpy

class SurveyData:
    def __init__(self, survey_year=2023):
        self.survey_year = survey_year
        self.conn = psrcelmerpy.ElmerConn()
        self.persons = self.get_persons()
        self.households = self.get_households() 

    def get_persons(self):

        e_conn = self.conn
        survey_year = self.survey_year
        qry = f"SELECT * FROM HHSurvey.v_persons_labels WHERE survey_year = {survey_year}"
        persons = e_conn.get_query(qry)

        return persons

    def get_households(self):
        
        e_conn = psrcelmerpy.ElmerConn()
        survey_year = 2023
        qry = f"SELECT * FROM HHSurvey.v_households_labels WHERE survey_year = {survey_year}"
        households = e_conn.get_query(qry)

        return households
