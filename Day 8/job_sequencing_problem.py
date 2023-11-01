
class job:
    def __init__(self, start, end, profit):
        self.start = start
        self.end = end
        self.profit = profit


class JobSequencing:
    def job_sequencing(self, job_arr, n):
        job_arr.sort(key=lambda x: x.profit, reverse=True)
        max_profit = 0
        for i in range(n):
            if job_arr[i].end >= max_profit:
                max_profit = job_arr[i].end
        result = [-1] * (max_profit + 1)
        count_job, job_profit = 0, 0
        for i in range(n):
            for j in range(job_arr[i].end, 0, -1):
                if result[j] == -1:
                    result[j] = i
                    count_job += 1
                    job_profit += job_arr[i].profit
                    break

        return [count_job, job_profit] 



if __name__ == "__main__":
    jobs = [job(1, 4, 20), job(2, 1, 10), job(3, 2, 40), job(4, 2, 30)]
    count, profit = JobSequencing().job_sequencing(jobs)
    print(count, profit)