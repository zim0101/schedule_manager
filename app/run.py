from app.scheduler import Scheduler


if __name__ == "__main__":
    python_location = '/home/trex/Development/PYTHON_PROJECTS/' \
                      'python_cron_job/bin/python3'
    file = '/worker.py'
    cron_job_command = python_location + " " + file

    # Execute job
    scheduler = Scheduler(cron_job_command)
    scheduler.execute_after_reboot()
    scheduler.hourly_execution()

