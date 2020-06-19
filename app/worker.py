from datetime import datetime


def worker(file_path: str):
    """
    This worker could be anything. Any work you desire to be executed
    :param file_path: path of the file we wanna write
    """
    with open(file_path, "a") as file:
        file.write('\nWorker1 executed at ' + str(datetime.now()))
        file.close()


if __name__ == "__main__":
    path = '/home/trex/Development/PYTHON_PROJECTS/python_cron_job/' \
           'schedule_manager/test.txt'

    worker(path)

