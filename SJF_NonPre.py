"""witout arrival time"""
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
    total_wt = 0
    total_tat = 0
    for i in range(n): 
        total_wt = total_wt + wt[i]  
        total_tat = total_tat + tat[i]  
    return(total_wt /n)  
  


if __name__ =="__main__":
    
    proc = [[1,6], [2,8], [3, 7], [4, 3]] 
    n = len(proc)
    proc.sort(key=lambda x: x[1])
    AverageTime(proc, n)
