import os
import shutil

allure_report_path = os.path.abspath('../allure-report/')
reports_path = os.path.abspath('../reports/')


def remove_files_from_dir(dir_path):
    if os.path.exists(dir_path):
        for file in os.listdir(dir_path):
            file_path = os.path.join(dir_path, file)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
                print("Removed dir: {}".format(file_path))
            except Exception as e:
                print(e)
                print("Failed to remove {}".format(file_path))
    else:
        print("Dir {} does not exist".format(dir_path))


remove_files_from_dir(dir_path=allure_report_path)
