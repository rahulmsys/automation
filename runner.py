import os
import sys
from datetime import datetime
import argparse

from utility.email_reports import SendReportEmail
from utility.take_report_screenshot import TestReportScreenshot


def convert_time(elapsed_time):
    hours = elapsed_time // 3600
    minutes = (elapsed_time % 3600) // 60
    seconds = elapsed_time % 60
    if hours > 0:
        return f'{hours} hours {minutes} minutes {round(seconds, 2)} seconds'
    if minutes > 0:
        return f'{minutes} minutes {round(seconds, 2)} seconds'
    return f'{round(seconds, 2)} seconds'


if __name__ == '__main__':
    argparser = argparse.ArgumentParser()
    argparser.add_argument('--tags', dest='tags', help='Tag name separated by space', nargs='+', required=False)
    argparser.add_argument('--name', dest='name', type=str, help='Scenario name separated by space', nargs='+',
                           required=False)
    argparser.add_argument('-f', dest='features', type=str, help='Specify feature file path', nargs='+')
    argparser.add_argument('--mail', dest='mail', type=bool, help='Send email report', default=False)

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

    report_dir = str(datetime.now().strftime("%d-%b-%Y-%H-%M-%S-%p"))
    feature_path = './features'
    allure_script = "-f allure_behave.formatter:AllureFormatter -o reports/{} ".format(report_dir)
    # html_report = "--format html -o reports/{}/report.html ".format(report_dir)
    # log_script = " --logging-level DEBUG --logcapture -o reports/{}/debug.txt ".format(
    #     report_dir)
    # capture_log = '--logging-level DEBUG --logcapture --outfile tmp/debug.txt '

    # script = 'features/orangehrm_login.feature'
    if not len(sys.argv) > 1:
        # script = feature_path
        runner_script = "behave" + ' ' + allure_script + ' ' + script
        print(f'Executing test script: {runner_script}')
        start_time = datetime.now()
        time_now = start_time.strftime('%I:%M:%S %p')
        os.system(runner_script)
        print('Test execution completed. Generating allure report')
        end_time = datetime.now()
        e_time = end_time.strftime('%I:%M:%S %p')
        total_time = (end_time - start_time).total_seconds()
        time_elapsed = convert_time(total_time)
        print(f'Test started at {time_now} and ended at {e_time}. Total time taken: {time_elapsed}')
    else:
        runner_script = "behave" + ' ' + allure_script + ' ' + script
        print(f'Executing test script: {runner_script}')
        start_time = datetime.now()
        time_now = start_time.strftime('%I:%M:%S %p')
        os.system(runner_script)
        print('Test execution completed. Generating allure report')
        end_time = datetime.now()
        e_time = end_time.strftime('%I:%M:%S %p')
        total_time = (end_time - start_time).total_seconds()
        time_elapsed = convert_time(total_time)
        print(f'Test started at {time_now} and ended at {e_time}. Total time taken: {time_elapsed}')
        os.system("allure generate -c reports/{} -o allure-report/{}".format(report_dir, report_dir))

    if args.mail:
        print('Taking screenshot of the report')
        sc = TestReportScreenshot(os.path.abspath('allure-report/{}/index.html'.format(report_dir)),
                                  image_path='reports/{}/report.png'.format(report_dir))
        sc.save_image()
        print('Sending email report')
        report_email = SendReportEmail(template_path='resources/email_reports_template.html',
                                       attachment_dir='reports/{}'.format(report_dir),
                                       report_screenshot_path='reports/{}/report.png'.format(report_dir),
                                       start_time=time_now, end_time=e_time, time_elapsed=time_elapsed)
        report_email.send_email()

    os.system("allure open allure-report/{}".format(report_dir))
