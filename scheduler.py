import numpy as np

def FCFS(Processes):
    Processes = np.insert(Processes, 2, Processes[:,2], axis=1)
    return Priority(Processes)


def SJF(Processes, preemptive = False):
    Processes = np.insert(Processes, 2, Processes[:,1], axis=1)
    return Priority(Processes, preemptive)


def Priority(self, Processes, preemptive = False):

    OrderedProcesses = []
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
        Time = 0
        # Every finished process recalculates the arranging of the rest of the processes 
        # based on Priority and time of Arrival
        while(True):
            # Average time is the time every process spent in the queue meaned across all processes
            # Avg = Start time of this process - Arrival Time / Num of Processes
            AvgWaitingTime += float(Time - Processes[0,3]) / NumOfProcesses


            for i in range(0, Processes.shape[0] - 2):

                if (Processes[i, 3] > Processes[0,3] and Processes[i, 2] > Processes[0,2] and Processes[0,1] >= Processes[i, 3]):
                    if (Processes[0,1] - Processes[i, 3]):
                        # Time taken after the present process finished
                        Time += Processes[0,1] - Processes[i, 3]
                        OrderedProcesses.append([Processes[0,0], Time])
                        Processes[0,1] = Processes[0,1] - (Processes[i,3] - Processes[0,3])
                        Processes = np.insert(Processes,0,Processes[i,]).reshape(-1,4)
                    else:
                        Time += Processes[0,1]
                        # Poping finished processes from the queue
                        OrderedProcesses.append([Processes[0,0], Time])
                        Processes = np.delete(Processes,0,0)
                        i -= 1
                
                else: 
                    Time += Processes[0,1]
                    # Poping finished processes from the queue
                    OrderedProcesses.append([Processes[0,0], Time])
                    Processes = np.delete(Processes,0,0)
                    i -= 1
                
                
                if(Processes.shape[0] == 0):
                    break

            
            if(Processes.shape[0] == 0):
                break

                                    
        return OrderedProcesses, AvgWaitingTime


    else:
        Time = 0
        # Every finished process recalculates the arranging of the rest of the processes 
        # based on Priority and time of Arrival
        while(True):
            # Average time is the time every process spent in the queue meaned across all processes
            # Avg = Start time of this process - Arrival Time / Num of Processes
            AvgWaitingTime += float(Time - Processes[0,3]) / NumOfProcesses
            
            # Time Reashed after the present process finished
            Time += Processes[0,1]
            
            # Poping finished processes from the queue
            OrderedProcesses.append([Processes[0,0], Time])
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
    

def roundRobin(processes, q):
    output = []
    processes.sort(key=lambda x: x[1]) # sorting processes by its arrival time.
    processes_cpy = processes
    t = 0
    while(len(processes_cpy) > 0):
       
        i = 0
        for p in processes:
            l = []
            if p[2] < q and p[2] > 0:
                t += p[2]
                l = [p[0], t]
            elif p[2] <= 0:
                processes_cpy.pop(i)
            else:
                t += q
                l = [p[0], t]

            p[2] = p[2] - q
            if len(l) > 0:
                output.append(l)
            
            i += 1
            
    return output    

def main():
    #print(FCFS(np.array([1,5,1,2,5,0,3,5,0]).reshape(-1,3)))
    processes = [[0, 1, 5], [1, 2, 3], [2, 3, 10], [7, 0, 7]]
    print(roundRobin(processes, 4))
    #print(Priority(np.array([1,5,1,0,2,5,0,1,3,5,0,2,4,4,0,3]).reshape(-1,4), True))
    

if __name__ == '__main__':
    main()
