
def cal_cutting_num(workers, jobs):
    job_stack = list()

    job_stack.append(int(jobs/2))
    job_stack.append(int(jobs/2))

    top_job = job_stack[-1]
    cut_count = 1

    while top_job !=1:
        job_cnt = len(job_stack)
        for i in range(min(workers, job_cnt)):
            curr_job = job_stack.pop()
            new_job = int(curr_job/2)
            rem_job = curr_job - new_job
            job_stack.append(new_job)
            if rem_job:
                job_stack.append(rem_job)
            # ascending
            job_stack.sort()
        top_job = job_stack[-1]
        cut_count +=1
    return cut_count

if __name__ == '__main__':
    workers = 5
    jobs = 100
    print(cal_cutting_num(workers, jobs))