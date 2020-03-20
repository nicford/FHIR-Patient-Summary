from fhir_parser import FHIR, observation

class observationDetails:
    def __init__(self, component, date):
        self.component = component
        self.date = date

def getObservationDate(observationDetails: observationDetails):
    return observationDetails.date


def createObservationDictionary(observations):

    observationDictionary = {}

    for observation in observations:
        observationDate = observation.effective_datetime

        for component in observation.components:
            componentCode = component.code
            if componentCode == "85354-9" or componentCode == "72166-2":     # skip blood pressure readings as they contain no useful information. Blood pressure is split into two readings: Diastolic and Systolic Blood Pressure, also skip tobacco readings since they are also meaningless
                continue
            if componentCode == "72514-3":
                component.unit = ""
            if component.code not in observationDictionary:
                observationDictionary[component.code] = []
            observationDictionary[component.code].append(observationDetails(component, observationDate))
    
    # sort dictionary lists
    for key in observationDictionary:
        currentList = observationDictionary[key]
        currentList.sort(key=getObservationDate)
    
    return observationDictionary