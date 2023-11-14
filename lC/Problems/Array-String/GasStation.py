
def canCompleteCircuit(self, gas, cost) -> int:
        tank = 0
        idx = 0
        #must find a gas stations s.t. you can make a full revolution back to it.
        #could use a double for loop or the following: the gas station to return is at the last index that is unreachable
        if sum(gas) < sum(cost):
            return -1
        tank = idx = 0

        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            if tank < 0:
                tank = 0
                idx = i+ 1
        return idx