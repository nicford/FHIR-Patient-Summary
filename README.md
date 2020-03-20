# FHIR-Patient-Summary
Python package that creates patient summary documents in docx or pdf from FHIR records

# Prerequisites

The following dotnet application must be running for the library to work.

https://github.com/goshdrive/FHIRworks_2020


# Usage

```python
from fhir_patient_summary import createPatientSummaryDocument, createPatientSummaryDocumentFromPatientIDList

outputDir = ""  # desired output directory of created documents
patientID = ""  # patient ID for which a summary document should be created
patientIDs = [] # list of patient IDs for which summary documents should be created

# single patient docx format
createPatientSummaryDocument(patientID, "docx", outputDir)

# single patient pdf format
createPatientSummaryDocument(patientID, "pdf", outputDir)

# multiple patient docx format
createPatientSummaryDocumentFromPatientIDList(patientIDs, "docx", outputDir)

# multiple patient pdf format
createPatientSummaryDocumentFromPatientIDList(patientIDs, "pdf", outputDir)

```
