class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        temps = []
        for ind, temp in enumerate(temperatures):
            while temps and temp > temps[-1][0]:
                temps_temp, temps_id = temps.pop()
                result[temps_id] = ind - temps_id
            
            temps.append((temp, ind))

        return result