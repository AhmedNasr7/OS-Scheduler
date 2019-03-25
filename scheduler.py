import numpy as np

def FCFS(Processes):
    Processes = Processes[Processes[:,2].argsort()]
    OrderedProcesses = {}
    AvgWaitingTime = 0
    Time = 0
    NumOfProcesses = Processes.shape[0]

    for i in range(0, NumOfProcesses):
        AvgWaitingTime += (Time - Processes[i,2]) / NumOfProcesses
        OrderedProcesses[Processes[i,0]] = Time
        Time += Processes[i,1]

    return OrderedProcesses, AvgWaitingTime


def SJF(Processes):
    pass

def Priority(self, Processes, preemptive = False):

    OrderedProcesses = {}
    AvgWaitingTime = 0
    NumOfProcesses = Processes.shape[0]

    Processes = Processes[Processes[:,3].argsort()]
    count = 0
    for i in range(0, NumOfProcesses-1):
        if(Processes[i,3] == Processes[i+1,3]):
            count += 1
            if(count == NumOfProcesses-1):
                Processes = Processes[Processes[:,2].argsort()]
            continue
        else:
            Processes[i-count:i+1,] = Processes[Processes[i-count:i+1,2].argsort()]
            break

    if (preemptive):
        pass

    else:
        Time = 0
        # Every finished process recalculates the arranging of the rest of the processes 
        # based on Priority and time of Arrival
        while(True):
            # Average time is the time every process spent in the queue meaned across all processes
            # Avg = Start time of this process - Arrival Time / Num of Processes
            AvgWaitingTime += (Time - Processes[0,3]) / NumOfProcesses
            
            # Time Reashed after the present process finished
            Time += Processes[0,1]
            
            # Poping finished processes from the queue
            OrderedProcesses[Processes[0,0]] = Time
            Processes = np.delete(Processes,0,0)
            
            if(Processes.size == 0):
                break

            # Rearranging the rest of the processes if they arrived before the popped process finish By priority
            count = 0
            for i in range(0, Processes.shape[0]):
                if(Processes[i,3] <= Time):
                    count += 1
                    if(count == Processes.shape[0]):
                        Processes = Processes[Processes[:,2].argsort()]        
                    continue
            
                Processes[i-count:i+1,] = Processes[Processes[i-count:i+1,2].argsort()]
                        
        return OrderedProcesses, AvgWaitingTime

def round_robin():
    pass

def main():
    print(FCFS(np.array([1,5,1,2,5,0,3,5,0]).reshape(-1,3)))

if __name__ == '__main__':
    main()
