import os
from datetime import datetime
import argparse

# os.system('clear')
report_dir = str(datetime.now().strftime("%d-%b-%Y-%H-%M-%S-%p"))
feature_path = 'features/'
runner_script = "behave -f allure_behave.formatter:AllureFormatter -o reports/{} {}".format(report_dir, feature_path)

# Running scripts
os.system(runner_script)

# Generating reports
os.system("allure serve reports/{}".format(report_dir))

