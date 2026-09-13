class simple_env:
    def __init__(self):
        self.grid_size = 100
        self.agent_pos = [0,0]
        self.target_pos = [10,10]

    def reset(self):
        self.agent_pos[0,0]
        observation=[
        self.agent_pos[0],
        self.agent_pos[1],
        self.target_pos[0],
        self.target_pos[1]
        ]

        return observation
    def step(self,action):
        if action==1:  #move up
            self.agent_pos[1]+=1
        if action==2:  #move down
            self.agent_pos[1]-=1
        if  action==3:  #move right
            self.agent_pos[0]+=1
        if action==4:  #move left
            self.agent_pos[0]-=1

        reward=-1
        success=False
        if self.agent_pos==self.target_pos:
            reward=100 
            success=True
            observation = [
            self.agent_pos[0],
            self.agent_pos[1],
            self.target_pos[0],
            self.target_pos[1]
        ]
        return observation,self.agent_pos,reward,success
    def render(self):
        for x in range(self.grid_size):
            row=""
            for y in range(self.grid_size):
                if [x,y]==self.agent_pos:
                    row+="⬤"
                elif [x,y]==self.target_pos:
                    row+="⭕"
                else:
                    row+="•"
        print(row)                
                