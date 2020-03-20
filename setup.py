from setuptools import setup, setuptools

setup(name='FHIR Patient Summary',
      version='0.9.3',
      install_requires=['datetime', 'FHIR-Parser==0.1.5', "docxtpl", "flask"],
      description='Create a FHIR patient summary document in docx or pdf format.',
      url='https://github.com/nicford/FhirToPatientDocument',
      author='Nicolas Ford',
      author_email='zcabnjf@ucl.ac.uk',
      license='MIT',
      packages=setuptools.find_packages(),
      zip_safe=False)