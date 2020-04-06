import os
import sys
import CGM1_workflow
import CGM11_workflow
import CGM21_workflow
import CGM22_workflow
import CGM23_workflow
import CGM24_workflow

from pyCGM2.Utils import files
import logging
import argparse

parser = argparse.ArgumentParser(description='CGM workflow')
parser.add_argument('--working-directory', required=True, help='Working directory with qtm exported c3d files')

args = parser.parse_args()
os.chdir(args.working_directory)

session_xml_filename="session.xml"
session_xml = files.readXml(os.getcwd()+"\\",session_xml_filename)
CGM2_Model = session_xml.Subsession.CGM2_Model.text

logging.info("PROCESSING TYPE " + CGM2_Model)
if CGM2_Model == "CGM1.0":
    CGM1_workflow.main()
elif CGM2_Model == "CGM1.1":
    CGM11_workflow.main()
elif CGM2_Model == "CGM2.1-HJC":
    CGM21_workflow.main()
elif CGM2_Model == "CGM2.2-IK":
    CGM22_workflow.main()
elif CGM2_Model == "CGM2.3-skinClusters":
    CGM23_workflow.main()
elif CGM2_Model == "CGM2.4-ForeFoot":
    CGM24_workflow.main()
else:
    raise Exception(
        "The pyCMG processing type is not implemented, you selected %s" % CGM2_Model)