import subprocess


def convertDocxToPDF(source: str, destination: str):
    subprocess.run(["/Applications/LibreOffice.app/Contents/MacOS/soffice", "--headless", "--convert-to", "pdf", source, "--outdir", destination])