import os
import sys
from datetime import datetime
import argparse
import subprocess

"""
1. Run all features file inside the features folder
2. Run test by tags
3. Run test by tags and features file
4. Run test by features file
5. Run test by scenario name
6. Generate allure report and debug file
7. Generate allure report and debug file and send email
"""

if __name__ == '__main__':
    pass
argparser = argparse.ArgumentParser()
argparser.add_argument('--tags', dest='tags', help='Tag name separated by space', nargs='+', required=False)
argparser.add_argument('--name', dest='name', type=str, help='Scenario name separated by space', nargs='+',
                       required=False)
argparser.add_argument('-f', dest='features', type=str, help='Specify feature file path', nargs='+')

args = argparser.parse_args()
script = ''
if args.tags is not None:
    tags = args.tags
    script = '--tags ' + ','.join(tags)

if args.name is not None:
    name = args.name
    name_args = []
    for n in name:
        name_args.append('--name ' + '"' + n + '"')  # --name "name1" --name "name2"
    script = ' '.join(name_args)
    print(f'Script: {script}')

if args.features is not None:
    features = args.features
    feature_args = []
    for f in features:
        feature_args.append(f)
    script = ' '.join(feature_args)

if not len(sys.argv) > 1:
    test_dir = 'features/'

# os.system('cls')
report_dir = str(datetime.now().strftime("%d-%b-%Y-%H-%M-%S-%p"))
feature_path = 'features/ '
allure_script = "-f allure_behave.formatter:AllureFormatter -o reports/{} ".format(report_dir)

capture_logs = " --logging-level DEBUG --logcapture -o reports/{}/debug.txt ".format(
    report_dir)
capture_log = '--logging-level DEBUG --logcapture --outfile tmp/debug.txt '
test_script = "behave" + ' ' + allure_script + ' ' + script
print(f'Test Script: {test_script}')

# Running scripts
os.system(test_script)

# Generating reports
os.system("allure generate -c reports/{} -o allure-report/{}".format(report_dir, report_dir))
os.system("allure open allure-report/{}".format(report_dir))


# behave features/login.feature --tags demo,validation
# behave --tags demo,validation
