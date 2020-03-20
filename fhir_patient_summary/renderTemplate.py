from docxtpl import DocxTemplate, Document
from fhir_parser import patient


def createDocument(patient: patient, observationDictionary) -> Document:
    doc = DocxTemplate("./templates/patientInformationTemplate.docx")
    context = { 'patient': patient, "homeNumbers": getPatientHomePhoneNumbers(patient), "mobileNumbers": getPatientMobilePhoneNumbers(patient), "addresses": getPatientAddresses(patient), 
                 "knownLanguages": getPatientKnownLanguages(patient), "observations": observationDictionary }
    doc.render(context)
    return doc

def getPatientAddresses(patient: patient):
    return "\n".join([(address.full_address if address.full_address.strip() != "" else "Not known") for address in patient.addresses])

def getPatientHomePhoneNumbers(patient: patient):
    numbers = ",".join([telecom.number for telecom in patient.telecoms if telecom.use.strip() == "home"])
    if numbers.strip() != "":
        return numbers
    else:
        return "Not known"

def getPatientMobilePhoneNumbers(patient: patient):
    numbers = ",".join([telecom.number for telecom in patient.telecoms if telecom.use == "mobile"])
    if numbers.strip() != "":
        return numbers
    else:
        return "Not known"

def getPatientKnownLanguages(patient: patient):
    return patient.communications