import numpy as np

# Calculate Turn around time and substract from it the burst time
def AvgWaitingTime(Processes, OrderedProcesses):

    AvgWaitingTime = 0
    NumOfProcesses = Processes.shape[0] 
    for i in range(NumOfProcesses):
        AvgWaitingTime += OrderedProcesses[i,1] - Processes[i,3]
    
    return AvgWaitingTime

def FCFS(Processes):
    Processes = np.insert(Processes, 2, Processes[:,2], axis=1)
    return Priority(Processes, False)


def SJF(Processes, preemptive = False):
    Processes = np.insert(Processes, 2, Processes[:,1], axis=1)
    return Priority(Processes, preemptive)


def Priority(Processes, preemptive = False):

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
        Time = Processes[0,3]
        # Every finished process recalculates the arranging of the rest of the processes 
        # based on Priority and time of Arrival
        while(True):
            # Average time is the time every process spent in the queue meaned across all processes
            # Avg = Start time of this process - Arrival Time / Num of Processes
            AvgWaitingTime += float(Time - Processes[0,3]) / NumOfProcesses

            Flag = False

            for i in range(1, Processes.shape[0]):
                
                if (Processes[i,2] < Processes[0,2]):

                    Flag = True
                    
                    if(Processes[i,3] > (Time + Processes[0,1])):
                            
                        Time += Processes[0,1]
                        OrderedProcesses.append([Processes[0,0], Time])
                        Processes = np.delete(Processes,0,0)
                        break

                    elif (Processes[i,3] == (Time + Processes[0,1])):
                        
                        Time += Processes[0,1]
                        OrderedProcesses.append([Processes[0,0], Time])
                        Processes = np.delete(Processes,0,0)
                        Processes = np.insert(Processes,0,Processes[i-1,]).reshape(-1,4)
                        Processes = np.delete(Processes,i+1,0)
                        break

                    else:
                        print(Processes)
                        if (Processes[i,3] > Time):
                            Processes[0,1] -= Processes[i,3] - Time
                            Time = Processes[i,3]
                            OrderedProcesses.append([Processes[0,0], Time])
                            Processes = np.insert(Processes,0,Processes[i,]).reshape(-1,4)
                            Processes = np.delete(Processes,i+1,0)
                            break
                        
                        else:
                            Processes = np.insert(Processes,0,Processes[i,]).reshape(-1,4)
                            Processes = np.delete(Processes,i+1,0)
                            break
            
            if(Flag and Processes.shape[0] != 0):
                continue
            
            else:
                
                Time += Processes[0,1]
                OrderedProcesses.append([Processes[0,0], Time])
                Processes = np.delete(Processes,0,0)

            if(Processes.shape[0] == 0):
                break

            
                                    
        return OrderedProcesses, AvgWaitingTime


    else:
        Time = Processes[0,3]
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
    

def RoundRobin(Processes, q):

    OrderedProcesses = []
    AvgWaitingTime = 0
    NumOfProcesses = Processes.shape[0]

    Processes = Processes[Processes[:,2].argsort()]
    Time = Processes[0,2]
    AvgWaitingTime = sum(Processes[:,1]) / q
    
    i = 0
    while(True):
<<<<<<< HEAD

=======
        
>>>>>>> c1ea5bb47ee80b1bbd3e5354d0365b5d8c718acc
        if(Processes[i,1] > q):
            Processes[i,1] -= q
            Time += q
            OrderedProcesses.append([Processes[i,0], Time])

        else:
            Time += Processes[i,1]
            OrderedProcesses.append([Processes[i,0], Time])
            Processes = np.delete(Processes,i,0)
<<<<<<< HEAD
            i -= 1
=======
>>>>>>> c1ea5bb47ee80b1bbd3e5354d0365b5d8c718acc
            

        if(Processes.shape[0] == 0):
            break
        
        i = (i + 1) % (Processes.shape[0])

    return OrderedProcesses, AvgWaitingTime



def main():
    #print(FCFS(np.array([1,5,1,2,5,0,3,5,0]).reshape(-1,3)))
<<<<<<< HEAD
    processes = [[0, 6, 0], [1, 5, 0], [2, 8, 0]]
=======
    processes = [[1, 1, 0], [2, 6, 0], [3, 3, 0], [4, 20, 0]]
>>>>>>> c1ea5bb47ee80b1bbd3e5354d0365b5d8c718acc
    print(RoundRobin(np.array(processes), 4))
    # print(Priority(np.array([1,5,1,0,2,5,1,2,3,5,1,3,4,4,1,4,5,5,0,20]).reshape(-1,4), True))
    

if __name__ == '__main__':
    main()
