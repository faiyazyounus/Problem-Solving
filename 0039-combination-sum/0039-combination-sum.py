class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        
        def backtrack(start, target, path):
            if target == 0:
                result.append(path)
            if target < 0:
                return
            
            for i in range(start, len(candidates)):
                backtrack(i, target - candidates[i], path + [candidates[i]])
        
        backtrack(0, target, [])
        
        return result