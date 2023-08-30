def optimalFreelancing(jobs):
    jobs = sorted(jobs, key=lambda x: x["payment"], reverse=True)
    print(jobs)


if __name__ == "__main__":
    jobs = [
        {"deadline": 1, "payment": 1},
        {"deadline": 2, "payment": 2},
        {"deadline": 2, "payment": 3},
        {"deadline": 7, "payment": 4},
    ]
    optimalFreelancing(jobs)
