
def WaitingTime(processes, n, wt):
    wt[0] = 0; 
    for i in range(1,n): 
        wt[i] = processes[i-1][1]+ wt[i-1] ;
        
def TurnAroundTime(processes, n, wt, tat):   
    for i in range(n): 
        tat[i] = processes[i][1] + wt[i]

def AverageTime(processes, n):  
    wt = [0] * n 
    tat = [0] * n  
    WaitingTime(processes, n, wt)  
    TurnAroundTime(processes, n, wt, tat)  
    print("Processes    Duration Time     Waiting",   "Time     Turn-Around Time") 
    total_wt = 0
    total_tat = 0
    for i in range(n): 
        total_wt = total_wt + wt[i]  
        total_tat = total_tat + tat[i]  
        print(" ", processes[i][0], "\t\t",  processes[i][1], "\t\t",  wt[i], "\t\t", tat[i]) 
    print("\nAverage waiting time = %.6f "%(total_wt /n) ) 
    print("Average turn around time = ", (total_tat) / n)  
  


if __name__ =="__main__":
    
    proc = [[1,10], [2,4], [3, 2], [4, 8]] 
    n = len(proc)
    proc.sort(key=lambda x: x[1])
    print("Order in which process gets executed :")
    for i in range (n):
         print(proc[i][0],end=' ' )
    print()
    AverageTime(proc, n)
    
