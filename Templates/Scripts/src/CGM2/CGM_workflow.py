import os
import sys

from pyCGM2.Utils import files
from pathlib2 import Path
import logging
import argparse

def delete_c3d_files_in(folder_path):
    folder_path = Path(folder_path)
    for c3d_file_path in folder_path.glob("*.c3d"):
        c3d_file_path.unlink()

parser = argparse.ArgumentParser(description='CGM workflow')
parser.add_argument('--working-directory', required=True, help='Working directory with qtm exported c3d files')

args = parser.parse_args()
os.chdir(args.working_directory)

session_xml_filename="session.xml"
session_xml = files.readXml(os.getcwd()+"\\",session_xml_filename)
CGM2_Model = session_xml.Subsession.CGM2_Model.text

delete_c3d_files_in(Path(args.working_directory, "processed"))

logging.info("PROCESSING TYPE " + CGM2_Model)
if CGM2_Model == "CGM1.0":
    from pyCGM2.Apps.QtmApps.CGMi import CGM1_workflow
    CGM1_workflow.main(session_xml_filename)
elif CGM2_Model == "CGM1.1":
    from pyCGM2.Apps.QtmApps.CGMi import CGM11_workflow
    CGM11_workflow.main(session_xml_filename)
elif CGM2_Model == "CGM2.1-HJC":
    from pyCGM2.Apps.QtmApps.CGMi import CGM21_workflow
    CGM21_workflow.main(session_xml_filename)
elif CGM2_Model == "CGM2.2-IK":
    from pyCGM2.Apps.QtmApps.CGMi import CGM22_workflow
    CGM22_workflow.main(session_xml_filename)
elif CGM2_Model == "CGM2.3-skinClusters":
    from pyCGM2.Apps.QtmApps.CGMi import CGM23_workflow
    CGM23_workflow.main(session_xml_filename)
elif CGM2_Model == "CGM2.4-ForeFoot":
    from pyCGM2.Apps.QtmApps.CGMi import CGM24_workflow
    CGM24_workflow.main(session_xml_filename)
elif CGM2_Model == "CGM2.5-UpperLimb":
    from pyCGM2.Apps.QtmApps.CGMi import CGM25_workflow
    CGM25_workflow.main(session_xml_filename)
elif CGM2_Model == "CGM2.6-Knee Calibration":
    from pyCGM2.Apps.QtmApps.CGMi import CGM26_workflow
    CGM26_workflow.main(session_xml_filename)
else:
    raise Exception(
        "The pyCMG processing type is not implemented, you selected %s" % CGM2_Model)
