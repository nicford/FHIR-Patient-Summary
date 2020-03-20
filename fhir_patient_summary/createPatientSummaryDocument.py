from fhir_parser import FHIR
from docxtpl import DocxTemplate
from fhir_patient_summary.renderTemplate import *
from fhir_patient_summary.createObservationDictionary import *
from fhir_patient_summary.convertDocxToPDF import convertDocxToPDF
import shutil
import tempfile

fhir = FHIR()

def createPatientSummaryDocumentFromPatientIDList(patientIDList, format: str, destinationDir: str, zipFile=False):
    if zipFile is True:
        with tempfile.TemporaryDirectory() as dirpath:
            createDocuments(patientIDList, format, dirpath)
            shutil.make_archive(destinationDir + "/patientSummaryDocuments", 'zip', dirpath)
            return destinationDir + "/patientSummaryDocuments.zip"
    else:
        createDocuments(patientIDList, format, destinationDir)
        return destinationDir


def createDocuments(patientIDList, format: str, destinationDir: str):
    for counter, patientID in enumerate(patientIDList):
        if counter > 100:       # limit number of patients to 100
            break
        createPatientSummaryDocument(patientID, format, destinationDir)


def createPatientSummaryDocument(patientID, format, destinationDir):
    patient = fhir.get_patient(patientID)
    patientObservations = fhir.get_patient_observations(patientID)

    observationDictionary = createObservationDictionary(patientObservations)
    newDoc = createDocument(patient, observationDictionary)

    return saveFile(patientID, newDoc, format, destinationDir)


def saveFile(patientID, doc: DocxTemplate, format: str, destinationDir: str):
    outputPrefix = destinationDir + "/patientSummary_"
    outputPath = outputPrefix + patientID + ".docx"
    doc.save(outputPath)

    if format == "pdf":
        convertDocxToPDF(outputPath, destinationDir)
        outputPath = outputPrefix + patientID + ".pdf"
        
    return outputPath