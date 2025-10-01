import psrcelmerpy
class SurveyData:
    def __init__(self, survey_year=2023):
        self.survey_year = survey_year
        self.conn = psrcelmerpy.ElmerConn()
        self.persons = self.get_persons()
        self.households = self.get_households() 
        self.trips = self.get_trips()
        
    def get_persons(self):
        survey_year = self.survey_year
        qry = f"""SELECT * FROM HHSurvey.v_persons_labels WHERE survey_year = {survey_year}"""
        persons = self.conn.get_query(qry)
        return persons

    def get_households(self):
        survey_year = 2023
        qry = f"""SELECT * FROM HHSurvey.v_households_labels WHERE survey_year = {survey_year}"""
        households = self.conn.get_query(qry)
        return households
    
    def get_trips(self):
        survey_year = 2023
        qry = f"""SELECT * FROM HHSurvey.v_trips_labels WHERE survey_year = {survey_year}"""
        trips = self.conn.get_query(qry)
        return trips