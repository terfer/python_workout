def run_timing(*arg):
    run_time = input('Enter 10 km run time: ')
    n_call = arg[1] + 1
    if not run_time:
        return (arg[0]/ arg[1]), (arg[1])
    return run_timing(float(run_time) + arg[0], n_call)
        
   
avg_time, n_runs = run_timing(0,0)

print(f"Average of {avg_time}, over {n_runs} runs")