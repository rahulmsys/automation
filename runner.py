import os
import sys
from datetime import datetime
import argparse

argparser = argparse.ArgumentParser(description='Runs the specified test')
argparser.add_argument('-t', dest='tags', help='Specify tags separated by space', nargs='+')
argparser.add_argument('-n', dest='name', type=str, help='Specify scenario name separated by space', nargs='+')
argparser.add_argument('-f', dest='features', type=str, help='Specify feature file path', nargs='+')

args = argparser.parse_args()
script = ''
if args.tags is not None:
    tags = args.tags
    script = '--tags ' + ', '.join(tags)

if args.name is not None:
    name = args.name
    name_args = []
    for n in name:
        name_args.append('--name ' + '"' + n + '"')
    script = ' '.join(name_args)

if args.features is not None:
    features = args.features
    feature_args = []
    for f in features:
        feature_args.append(f)
    script = ' '.join(feature_args)

if not len(sys.argv) > 1:
    script = 'features/'

# os.system('cls')
report_dir = str(datetime.now().strftime("%d-%b-%Y-%H-%M-%S-%p"))
feature_path = 'features/ '
allure_script = "-f allure_behave.formatter:AllureFormatter -o reports/{} ".format(report_dir)

runner_script = "behave " + allure_script + '--logcapture ' + script
print(runner_script)

# Running scripts
os.system(runner_script)

# Generating reports
os.system("allure generate -c reports/{} -o allure-report/{}".format(report_dir, report_dir))
os.system("allure open allure-report/{}".format(report_dir))
